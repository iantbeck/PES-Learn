"""
Contains the TemplateProcessor class for handling template input file data
"""

from . import regex
import re

class TemplateProcessor(object):
    """
    A class for handling template input files for electronic structure theory codes
        Parameters
        ----------
        template : str
            A file string of a template input file  
    """

    def __init__(self, template):
        self.template = template

    def count_lines(self, string):
        """
`       Finds number of lines in a file string 
        Parameters
        ----------
        string: str
            A file string
        Returns
        -------
        line_count : int 
            The number of lines
        """
        line_count = len(string.splitlines())
        return line_count 

    def parse_xyz(self):
        """
        Locates the file positions of the xyz geometry.
        Returns
        -------
        bounds : tuple
            A tuple of size two: start and end string positions of the xyz geometry block 
        """ 
        iter_matches = re.finditer(regex.xyz_block_regex, self.template, re.MULTILINE)
        matches = [match for match in iter_matches]
        if matches is None:
            raise Exception("No XYZ geometry found in template input file")
        # only find last xyz if there are multiple
        # grab string positions of xyz coordinates
        start = matches[-1].start() 
        end   = matches[-1].end() 
        return start, end 

    def header_xyz(self):
        """
        The header of the xyz template input file (all text before the geometry) 

        Returns
        -------
        header : str
            All template input file text before xyz geometry specification 
        """
        start, end = self.parse_xyz()
        header = self.template[:start]
        return header 

    def footer_xyz(self):
        """
        The footer of the xyz template input file (all text after the geometry) 

        Returns
        -------
        header : str
            All template input file text after xyz geometry specification 
        """
        start, end = self.parse_xyz()
        footer = self.template[end:]
        return footer

    def extract_xyz(self):
        """
        Extracts an xyz-style geometry block from a template input file 

        Returns
        ------- 
        XYZ : str
            An xyz geometry of the form:
            atom_label  x_coord y_coord z_coord 
            atom_label  x_coord y_coord z_coord 
            ...
        """
        start, end = self.parse_xyz()
        xyz = self.template[start:end]
        return xyz

