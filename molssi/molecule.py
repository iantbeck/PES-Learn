import constants
import re
import regex
import math
import numpy as np
from geometry_transform_helper import get_local_axes, get_bond_vector

"""
Contains Atom and Molecule classes for reading, saving and editing the geometry of a molecule 
"""

class Atom(object):
    """
    The Atom class holds information about the geometry of an atom
        Parameters
        ----------
        label : str
            The atomic symbol
        r_idx  : str
            The bond connectivity index, as represented in a Z-matrix
        a_idx  : str
            The angle connectivity index, as represented in a Z-matrix
        d_idx  : str
            The dihedral connectivity index, as represented in a Z-matrix
        r  : dict
            A dictionary of the bond label e.g. "R1" and the value 
        a  : dict
            A dictionary of the angle label e.g. "A1" and the value 
        d  : dict
            A dictionary of the dihedral label e.g. "D1" and the value 
    """
    def __init__(self, label, r_idx, a_idx, d_idx, r, a, d):
        self.label = label
        self.r_idx = r_idx
        self.a_idx = a_idx
        self.d_idx = d_idx
        self.r    = r
        self.a    = a
        self.d    = d
        rlist     = list(self.r.values())
        alist     = list(self.a.values())
        dlist     = list(self.d.values())
        self.rval = rlist[0]
        self.aval = alist[0] 
        self.dval = dlist[0]
        
        self.coords = np.array([None, None, None]) 

    

class Molecule(object):
    """
    The Molecule class holds geometry information about all the atoms in the molecule
    Requires initialization with a file string containing internal coordinates
    """
    def __init__(self, zmat_string):
        self.zmat_string = zmat_string
        self.extract_zmat(self.zmat_string)
         
    
    def extract_zmat(self, zmat_string):
        """
        This should maybe just be in the init method.
        Take the string which contains an isolated Z matrix definition block,
        and extract information and save the following attributes:
        self.n_atoms         - the number of atoms in the molecule
        self.atom_labels     - a list of element labels 'H', 'O', etc.
        self.geom_parameters - a list of geometry labels 'R3', 'A2', etc.
        self.atoms           - a list of Atom objects containing complete Z matrix information
        """
        # grab array like representation of zmatrix and count the number of atoms 
        zmat_array = [line.split() for line in zmat_string.splitlines()]
        self.n_atoms = len(zmat_array)

        # find geometry parameter labels 
        # atom labels will always be at index 0, 1, 3, 6, 6++4... 
        # and geometry parameters are all other matches
        tmp = re.findall(regex.coord_label, zmat_string)
        self.atom_labels = []
        for i, s in enumerate(tmp):
                if (i == 0) or (i == 1) or (i == 3):
                    self.atom_labels.append(tmp[i])
                if ((i >= 6) and ((i-6) % 4 == 0)):
                    self.atom_labels.append(tmp[i])
        self.geom_parameters = [x for x in tmp if x not in self.atom_labels]
        
        self.atoms = []
        for i in range(self.n_atoms):
            label = zmat_array[i][0]
            if (i >= 1):
                r_idx = int(zmat_array[i][1]) - 1
                r = {zmat_array[i][2]: None} 
            else:
                r_idx = None
                r = {None: None}
            if (i >= 2):
                a_idx = int(zmat_array[i][3]) - 1
                a = {zmat_array[i][4]: None}
            else:
                a_idx = None
                a = {None: None}
            if (i >= 3):
                d_idx = int(zmat_array[i][5]) - 1
                d = {zmat_array[i][6]: None}
            else:
                d_idx = None
                d = {None: None}
            self.atoms.append(Atom(label, r_idx, a_idx, d_idx, r, a, d))

    def zmat2xyz(self):
        """
        Convert Z-matrix representation to cartesian coordinates
        """
        if (self.n_atoms >= 1):
            self.atoms[0].coords = np.array([0.0, 0.0, 0.0])
        if (self.n_atoms >= 2):
            self.atoms[1].coords = np.array([0.0, 0.0, self.atoms[1].rval])
        if (self.n_atoms >= 3):
            r1,  r2  = self.atoms[1].rval, self.atoms[2].rval
            rn1, rn2 = self.atoms[1].r_idx, self.atoms[2].r_idx
            a1 = self.atoms[2].aval
            print(a1)
            print(r2)
            y = r2*math.sin(a1)
            z = self.atoms[rn2].coords[2] + (1-2*float(rn2==1))*r2*math.cos(a1)
            self.atoms[2].coords = np.array([0.0, y, z])
        for i in range(3, self.n_atoms):
            atom = self.atoms[i]
            coords1 = self.atoms[atom.r_idx].coords
            coords2 = self.atoms[atom.a_idx].coords
            coords3 = self.atoms[atom.d_idx].coords
            self.atoms[i].local_axes = get_local_axes(coords1, coords2, coords3)
            bond_vector = get_bond_vector(atom.rval, atom.aval, atom.dval)
            disp_vector = np.array(np.dot(bond_vector, self.atoms[i].local_axes))
            for p in range(3):
                atom.coords[p] = self.atoms[atom.r_idx].coords[p] + disp_vector[p]

        cartesian_coordinates = []
        for atom in self.atoms:
            cartesian_coordinates.append(atom.coords)
        return np.array(cartesian_coordinates)

 

#zmatstring = 'O\nH 1 R1\nH 1 R2 2 A1\nH 1 R3 2 A2 3 D1\n'
zmatstring = 'O\nH 1 R1\nH 1 R2 2 A1\nH 3 R3 1 A2 2 D1\n'
#zmatstring = 'O\nH 1 R1\nH 1 R2 2 A1\n'
print(zmatstring)
mol = Molecule(zmatstring)
#mol.atoms[1].r["R1"] = 1.2
mol.atoms[1].rval = 1.1
#mol.atoms[2].r["R2"] = 1.1
mol.atoms[2].rval = 1.1
#mol.atoms[2].a["A1"] = -109.1
mol.atoms[2].aval = 180.0 * constants.deg2rad
##mol.atoms[3].r["R3"] = 1.1
mol.atoms[3].rval = 1.1
##mol.atoms[3].a["A2"] = 90.0
mol.atoms[3].aval = 180.0* constants.deg2rad
##mol.atoms[3].d["D1"] = 180.1
mol.atoms[3].dval = 0.0* constants.deg2rad
a = mol.zmat2xyz()
print(a)
#for atom in mol.atoms:
#    print(atom.coords)
#    print(atom.rval)
#    print(atom.aval)
#    print(atom.dval)
#print(mol.geom_parameters)
