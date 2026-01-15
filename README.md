# PES-Learn
![Continuous Integration](https://github.com/CCQC/PES-Learn/actions/workflows/continuous_integration.yml/badge.svg)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

PES-Learn is a Python library designed to fit system-specific Born-Oppenheimer potential energy surfaces using modern machine learning models. PES-Learn assists in generating datasets, and features Gaussian process and neural network model optimization routines. The goal is to provide high-performance models for a given dataset without requiring user expertise in machine learning.

This project is young and under active development. It is recommended to take a look at the documentation. The [Tutorials](https://ccqc.github.io/PES-Learn/guides/tutorials.html), [FAQ page](https://ccqc.github.io/PES-Learn/guides/faq.html), and the list of [keyword options](https://ccqc.github.io/PES-Learn/reference/keywords.html) are particularly useful. Questions and comments are encouraged; please consider submitting an issue. 

## Features

* **Ease of Use**
  * PES-Learn can be run by writing an input file and running the code (much like most electronic structure theory packages)
  * PES-Learn also features a Python API for more advanced workflows
  * Once ML models are finished training, PES-Learn automatically writes a Python file containing a function for evaluating the energies at new geometries. 
  
* **Data Generation**
  * PES-Learn supports input file generation and output file parsing for arbitrary electronic structure theory packages such as Psi4, Molpro, Gaussian, NWChem, etc. 
  * Data is generated with user-defined internal coordinate displacements with support for:
    * Redundant geometry removal
    * Configuration space filtering

* **Automated Data Transformation**
  * Rotation, translation, and permutation invariant molecular geometry representations

* **Automated Machine Learning Model Generation**
  * Neural network models are built using PyTorch
  * Gaussian process models are built using GPy

* **Hyperparameter Optimization**


## Installation Instructions 
PES-Learn has been tested and developed on Linux, Mac, and Windows 10 through the Windows Subsystem for Linux (WSL). 
Recommended Installation:

First clone the repository:
`git clone https://github.com/CCQC/PES-Learn.git`
Change into top level directory:
`cd PES-Learn`
Create conda environment from peslearn.yml file:
`conda env create -f peslearn.yml`
This will create a conda environment called peslearn that contains all the dependencies needed to run peslearn. The next step is to activate the peslearn conda environment and install the `peslearn` package with pip:
`conda activate peslearn`
`pip install -e .`
PES-Learn should now be ready to use! For further/alternate installation instructions please checkout the [docs](https://ccqc.github.io/PES-Learn/started/installation.html).

To update PES-Learn in the future, run `git pull` while in the top-level directory `PES-Learn`.

To run the test suite, you need pytest: `pip install pytest-cov` 
To run tests, in the top-level directory called `PES-Learn`, run: `py.test -v tests/`

## Citing PES-Learn
[PES-Learn: An Open-Source Software Package for the Automated Generation of Machine Learning Models of Molecular Potential Energy Surfaces ](https://pubs.acs.org/doi/10.1021/acs.jctc.9b00312)

Bibtex:
```
@article{Abbott2019,
  title={PES-Learn: An open-source software package for the automated generation of machine learning models of molecular potential energy surfaces},
  author={Abbott, Adam S and Turney, Justin M and Zhang, Boyi and Smith, Daniel GA and Altarawy, Doaa and Schaefer III, Henry F},
  journal={Journal of chemical theory and computation},
  volume={15},
  number={8},
  pages={4386--4398},
  year={2019},
  publisher={ACS Publications}
}
```

```
@article{Beck2026,
  title={Methods in PES-Learn: Direct-Fit Machine Learning of Born-Oppenheimer Potential Energy Surfaces},
  author={Beck, Ian T and Turney, Justin M and Schaefer III, Henry F},
  journal={Molecules},
  volume={31},
  number={1},
  pages={100},
  year={2026},
  publisher={MDPI}
}
```


## Funding 
This project is a collaboration with the [Molecular Sciences Software Institute](http://molssi.org).
The author gratefully acknowledges MolSSI for funding the development of this software.

