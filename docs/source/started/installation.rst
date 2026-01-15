
Installation
============

PES-Learn best works with Python > 3.8. 
There are a few options for installing the ``peslearn`` package. It is recommended to compile from source and use the provided ``peslearn.yml`` file to create a conda environment that contains the necessary dependencies. 
Alternate options for instatllation include via ``pip`` (largely untested) and installing from source with manual package installation.

**Compile from source and create conda environment automatically**

These instructions follow the instructions listed on the PES-Learn github page. 

First clone the repository:

.. code-block::

    git clone https://github.com/CCQC/PES-Learn.git

Change into top level directory:

.. code-block::
    
    cd PES-Learn

Create conda environment from peslearn.yml file:

.. code-block::
    
    conda env create -f peslearn.yml

This will create a conda environment called peslearn that contains all the dependencies needed to run peslearn. The next step is to activate the peslearn conda environment and install the `peslearn` package with pip:

.. code-block::
    
    conda activate peslearn

.. code-block::
    
    pip install .

PES-Learn should now be ready to use! 

**Installing With pip**

Make sure that you have Python and it is at least version 3.8 or greater. To check this you can run the following from a command line:

.. code-block::

    python --version

Now that you have ensured you have a working version Python you can install the ``peslearn`` application with ``pip``:

.. code-block::

    pip install peslearn

This should install the ``peslearn`` package and all its dependencies.

.. note::
    If you don't have ``pip`` in your environment checkout the `pip instalation guide <https://pip.pypa.io/en/latest/installation/>`_ .


**Compiling from source and installing dependencies manually**

Compiling from source can be done with pip to install dependencies or with an Anaconda package manager. It is strongly recommended to install dependencies using an Anaconda package manager, for performance and stability reasons. 
We recommend using Mamba as a package manager, because it is much faster and more efficient at resolving dependencies than Conda. More information can be found `here <https://mamba.readthedocs.io/en/latest/index.html>`_

*Install dependencies with Anaconda package manager:*

If you are utilizing Mamba, in the following commands you can substitute ``mamba`` wherever you see ``conda``.
It is recommended to start with a clean environment. After installing your prefered package manager create the environment and activate it. 

.. code-block::

    conda create -n peslearn
    conda activate peslearn

Then install the required dependencies into your environment.

.. code-block::

    conda install -c conda-forge -c pytorch numpy gpy scikit-learn pandas hyperopt cclib joblib qcelemental qcengine matplotlib pytorch

Then install the ``peslearn`` package from GitHub 

.. code-block::

    git clone https://github.com/CCQC/PES-Learn.git
    cd PES-Learn/
    pip install .    

Now you should be all setup and ready to use the ``peslearn`` package!
To update the ``peslearn`` package in the future, move to the top-level directory and run 

.. code-block::

    git pull


*Install dependencies with pip*:

To compile PES-Learn from source and install the dependencies with ``pip`` first check the python version you are using (Python 3.8 is recommended).

Then clone the repository from GitHub in your desired location and move to the top-level directory.

.. code-block:: 
    
    git clone https://github.com/CCQC/PES-Learn.git
    cd PES-Learn/

Then install the ``peslearn`` dependencies with pip

.. code-block:: bash

    pip install .

To update the ``peslearn`` package in the future, move to the top-level directory and run 

.. code-block::

    git pull

**Installing with conda**

*Coming Soon!*
