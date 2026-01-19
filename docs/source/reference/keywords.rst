
Input Keywords (alphabetical)
=============================

``energy``
    * Description: The method by which output energies are parsed into a ``PES.dat`` file.
    * Type: string
    * Default value: ``None``
    * Possible values: ``cclib``, ``regex``, ``schema``.
    * Ref: 

``energy_cclib``
    * Description: Tells cclib which energy to parse. Use when keyword ``energy`` is set to ``cclib``.
    * Type: string
    * Default value: ``None``
    * Possible values: ``scfenergies``, ``mpenergies``, ``ccenergies``.
    * Ref: 

``energy_regex``
    * Description: A regular expression string used for parsing energies in single or double quotes. Use when keyword ``energy`` is set to ``schema``.
    * Type: string
    * Default value: ``None``
    * Possible values: Any valid regular expression in single or double quotes.
    * Ref: 

``eq_geom``
    * Description: The minimum of the surface. It is suggested to set this as the true global minimum of the PES. This helps the generation of templates, schemas, and strucure based train/test set splitting.
    * Type: list
    * Default value: ``None``
    * Possible values: A 1D list of internal coordinate values in order they appear in. 
    * Ref: 

``gradient``
    * Description: The method by which output gradients are parsed into a ``PES.dat`` file.
    * Type: string
    * Default value: ``None``
    * Possible values: ``cclib``, ``regex``, ``schema``.
    * Ref: 

``gradient_header``
    * Description: A string of regular expressions which match unique text that is before and close to the gradient data.
    * Type: string
    * Default value: ``None``
    * Possible values: A unique and valid regular expression in single or double quotes.
    * Example: 
        | CARTESIAN GRADIENT:                 (header)
        | (optional extra text that does not match grad_line_regex)
        | Atom 1 O 0.00000 0.23410 0.32398         (grad_line_regex)
        | Atom 2 H 0.02101 0.09233 0.01342
        | Atom 3 N 0.01531 0.04813 0.06118
        | (optional extra text that does not match grad_line_regex)
        | (footer)
    * Ref: 

``gradient_footer``
    * Description: A string of regular expressions for text that comes close to after the gradient data. (Does not need to be unique)
    * Type: string
    * Default value: ``None``
    * Possible values: A valid regular expression in single or double quotes.
    * Example: 
        | CARTESIAN GRADIENT:                 (header)
        | (optional extra text that does not match grad_line_regex)
        | Atom 1 O 0.00000 0.23410 0.32398         (grad_line_regex)
        | Atom 2 H 0.02101 0.09233 0.01342
        | Atom 3 N 0.01531 0.04813 0.06118
        | (optional extra text that does not match grad_line_regex)
        | (footer)
    * Ref: 

``gradient_line``
    * Description: A string of regular expressions for one line of gradient data. The regex must be general enough for all lines of gradient data. Use capture groups () for the x, y, and z components.
    * Type: string
    * Default value: ``None``
    * Possible values: A valid regular expression in single or double quotes, containing threee capturing groups one each for x, y, and z components.
    * Example: 
        | CARTESIAN GRADIENT:                 (header)
        | (optional extra text that does not match grad_line_regex)
        | Atom 1 O 0.00000 0.23410 0.32398         (grad_line_regex)
        | Atom 2 H 0.02101 0.09233 0.01342
        | Atom 3 N 0.01531 0.04813 0.06118
        | (optional extra text that does not match grad_line_regex)
        | (footer)
        | 
        | A valid argument for grad_line_regex would be ``r"Atom\s+\d+\s+[A-Z,a-z]+\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)"``
    * Ref: 

``grid_generation``
    * Description: The method that internal coordinate displacements are generated along defined ranges. Either fixed intervals or uniform random distribution.
    * Type: string
    * Default value: ``fixed``
    * Possible values: ``fixed``, ``uniform``
    * Ref: 

``grid_reduction``
    * Description: The number of geometries to reduce the generated grid of internal coordinate values to. 
    * Type: int
    * Default value: ``None``
    * Possible values: Any int.
    * Ref: 

``gp_ard``
    * Description: Set whether features in GP optimization are independent in kernel, or to set this as a hyperparameter.
    * Type: str
    * Default value: ``true``
    * Possible values: ``true``, ``false``, ``opt``
    * Ref: 

``hessian`` (not yet implemented)
    * Description: The method by which output Hessians are parsed into a ``PES.dat`` file.
    * Type: str
    * Default value: ``None``
    * Possible values: ``schema``
    * Ref: 

``hp_maxit``
    * Description: The max number of hyperparameter optimization steps.
    * Type: int
    * Default value: ``20``
    * Possible values: Any int.
    * Ref: 

``hp_opt`` (not yet implemented)
    * Description: Choose whether or not to optimize hyperparameters
    * Type: str
    * Default value: ``true``
    * Possible values: ``true``, ``false``
    * Ref: 

``input_name``
    * Description: The name for new imput files generated from templates.
    * Type: str
    * Default value: ``input.dat``
    * Possible values: A valid file name as a string in single or double quotes.
    * Ref: 

``kernel``
    * Description: Use a specific kernel (``precomputed``) or all possible kernel options (``verbose``) when optimizing with KRR models.
    * Type: str
    * Default value: ``None``
    * Possible values: ``verbose``, ``precomputed``
    * Ref: 

``ml_model``
    * Description: Which machine learning model to optimize.
    * Type: str
    * Default value: ``gp``
    * Possible values: ``gp``, ``nn``, ``krr``
    * Ref: 

``mode``
    * Description: Which mode to use PES-Learn in either generate data, parse data, or make ML models.
    * Type: str
    * Default value: ``None``
    * Possible values: ``generate``, ``parse``, ``learn``, ``g``, ``p``, ``l``
    * Ref: 

``n_low_energy_train``
    * Description: Force the training set to contain the first n lowest energy points.
    * Type: int 
    * Default value: ``0`` 
    * Possible values: Any int less than the training set size. 
    * Ref: 

``nas_trial_layers``
    * Description: Trial layers for neural network optimization as a list of tuples where each item in a tuple is the depth of a layer and the number of items in the tuple is the number of layers. Multiple tuples in a list means PES-Learn will try each of those tuples as possible architectures.
    * Type: list 
    * Default value: ``None``
    * Possible values: A list of tuples of trial layers.
    * Example: ``[(10,), (10,10,10), (50,50)]``
    * Ref: 

``nn_precision``
    * Description: Neural network floating point precision.
    * Type: int
    * Default value: ``32``
    * Possible values: ``32``, ``64``
    * Ref: 

``output_name``
    * Description: The name of electronic strucutre theory output files for use when generating schemas.
    * Type: str 
    * Default value: ``output.dat``
    * Possible values: A valid file name.
    * Ref: 

``pes_dir_name``
    * Description: Name for the directory that either template input files or schema inputs are written into.
    * Type: str
    * Default value: ``PES_data``
    * Possible values: A valid directory name.
    * Ref: 

``pes_format``
    * Description: The format that outputs are in for parsing.
    * Type: str 
    * Default value: ``interatomics``
    * Possible values: ``interatomics``, ``zmat``
    * Ref: 

``pes_name``
    * Description: File name for dataset that parsed outputs are compiled in.
    * Type: str 
    * Default value: ``PES.dat``
    * Possible values: A valid file name.
    * Ref: 

``pes_redundancy``
    * Description: Are redundant points allowed when parsing data from outputs.
    * Type: str
    * Default value: ``false``
    * Possible values: ``true``, ``false``
    * Ref: 

``precomputed_kernel``
    * Description: Kernel for use in optimizing KRR models.
    * Type: dict
    * Default value: ``None``
    * Possible values: A dictionary of kernel options. Keys in dict should be limited to 'kernel', 'degree', 'gamma', and 'alpha'.
    * Example: ``{'kernel': ['rbf', 'laplacian'], 'gamma': ['uniform']}``
    * Ref: 

``remember_redundancy`` (not fully implemented)
    * Description: Add symmetry redundant geometries back into dataset after removing them. (see remove_redundancy)
    * Type: str 
    * Default value: ``false``
    * Possible values: ``true``, ``false``
    * Ref: 

``remove_redundancy``
    * Description: Remove symmetry redundant geometries from dataset.
    * Type: str 
    * Default value: ``true``
    * Possible values: ``true``, ``false``
    * Ref: 

``rseed``
    * Description: Random seed to use for machine learning optimization.
    * Type: int 
    * Default value: ``None``
    * Possible values: Any int
    * Ref: 

``sampling``
    * Description: Which sampling method to use for training/test set splitting.
    * Type: str
    * Default value: ``structure_based``
    * Possible values: ``structure_based``, ``sobol``, ``smart_random``, ``random``
    * Ref: 

``schema_basis``
    * Description: A basis set interpretable by electronic structure theory code specified by schema_prog.
    * Type: str
    * Default value: ``None``
    * Possible values: A basis set interpretable by electronic structure theory code of choice.
    * Ref: 

``schema_driver``
    * Description: Tells electronic structure theory code what value to compute.
    * Type: str 
    * Default value: ``energy``
    * Possible values: ``energy``, ``gradient``, ``hessian``, ``properties`` 
    * Ref: 

``schema_generate``
    * Description: Choose whether or not to generate schemas with QCSchema.
    * Type: str 
    * Default value: ``false``
    * Possible values: ``true``, ``false``
    * Ref: 

``schema_keywords``
    * Description: Keywords to be passed to electronic structure theory code.
    * Type: dict in single quotes
    * Default value: ``None``
    * Possible values: A dict of keywords in quotes, interpretable by electronic structure theory code specified by schema_prog.
    * Ref: 

``schema_method``
    * Description: Tells electronic structure theory code what method to use.
    * Type: str
    * Default value: ``None``
    * Possible values: A string of a method to compute desired property.
    * Example: ``CCSD``
    * Ref: 

``schema_prog``
    * Description: The electronic structure theory code for use via QCEngine, must be compatible with QCEngine.
    * Type: str 
    * Default value: ``None``
    * Possible values: A program supported by QCEngine as a string.
    * Ref: 

``schema_units``
    * Description: Which units to use for QCSchema inputs. 
    * Type: str 
    * Default value: ``angstrom``
    * Possible values: ``angstrom``, ``bohr``
    * Ref: 

``sort_pes``
    * Description: Choose whether to sort parsed PES by energies or not.
    * Type: str 
    * Default value: ``true``
    * Possible values: ``true``, ``false``
    * Ref: 

``training_points``
    * Description: Number of points to include in the training set. Note that if the default value ``None`` is used, the number of training points will be set to 80% of the dataset.
    * Type: int 
    * Default value: ``None``
    * Possible values: Any int less than the size of the dataset.
    * Ref: 

``tooclose``
    * Description: Value by which to remove generated geometries where atoms are too close to each other. This value is the threshold that interatomic distances must be greater than in order to not be thrown out. This is to reduce errors from electronic structure theory codes.
    * Type: float
    * Default value: ``0.1``
    * Possible values: Any float
    * Ref: 

``use_pips``
    * Description: Choose whether to use permutationally invariant polynomials (PIPs). 
    * Type: str 
    * Default value: ``true``
    * Possible values: ``true``, ``false``
    * Ref: 

``validation_points``
    * Description: How many data points to use in validation for neural network models.
    * Type: int
    * Default value: ``None``
    * Possible values: Any int less than the number of points in the dataset.
    * Ref: 