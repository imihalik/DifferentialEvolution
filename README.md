## Overview

The implementation of the Differential Evolution (DE) method from SciPy has been adapted into a Qiskit Optimizer class: https://qiskit-community.github.io/qiskit-algorithms/stubs/qiskit_algorithms.optimizers.Optimizer.html#qiskit_algorithms.optimizers.Optimizer.
This adaptation enables the utilization of classical optimization algorithm within Qiskit's quantum computing framework.

### Parameters

- **fun** (callable): The objective function to be minimized. Must be in the form `f(x, *args)`, where `x` is the argument in the form of a 1-D array and `args` is a tuple of any additional fixed parameters needed to completely specify the function.

- **maxiter** (int, optional): The maximum number of iterations.

- **disp** (bool, optional): Prints the evaluated `fun` at every iteration.

- **tol** (float, optional): Relative tolerance for convergence.

- **strategy** ({str, callable}, optional): The differential evolution approach used to generate trial solutions for optimization. Should be one of: `best1bin`, `best1exp`, `rand1bin`, `rand1exp`, `rand2bin`, `rand2exp`, `randtobest1bin`, `randtobest1exp`, `currenttobest1bin`, `currenttobest1exp`, `best2exp`, `best2bin`.

- **popsize** (int, optional): A multiplier for setting the total population size.

- **mutation** (float or tuple(float, float), optional): The mutation constant.

- **recombination** (float, optional): The recombination constant.

- **init** (str or array-like, optional): Specify which type of population initialization is performed. Should be one of: 'latinhypercube', 'sobol', 'halton', 'random', or an array specifying the initial population.

- **bounds** (sequence or Bounds): Bounds for variables.

For more information about the SciPy implementation: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.differential_evolution.html
