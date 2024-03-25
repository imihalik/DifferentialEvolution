from __future__ import annotations
from typing import List, Callable
import numpy as np
from scipy.optimize import differential_evolution
from qiskit_algorithms.optimizers.optimizer import Optimizer, OptimizerSupportLevel, OptimizerResult, POINT


class DifferentialEvolution(Optimizer):
    _OPTIONS = ["maxiter", "disp", "tol", "strategy", "popsize"]

    def __init__(
        self,
        maxiter: int = 100,
        disp: bool = False,
        tol: float | None = 1e-4,
        strategy: str = "best1bin",
        popsize: int = 15,
        mutation: float = 0.7,
        recombination: float = 0.9,
        init: str = 'latinhypercube',
        bounds: list[tuple[float, float]] | None = None,  
        options: dict | None = None,
        **kwargs,) -> None:
        if options is None:
            options = {}
        for k, v in list(locals().items()):
            if k in self._OPTIONS:
                options[k] = v
        super().__init__(**kwargs)
        self._options = options
        self._bounds = bounds

    def minimize(self, fun: Callable, x0: List[float], bounds: list[tuple[float, float]] = None) -> np.ndarray:
        bounds = [(- 2 * np.pi, 2 * np.pi)] * len(x0)
        result = differential_evolution(
            fun, bounds=bounds, maxiter=self._options["maxiter"], disp=self._options["disp"],
            tol=self._options["tol"], strategy=self._options["strategy"], popsize=self._options["popsize"])

        return result
    
    def get_support_level(self):
        """Get the support level dictionary."""
        return {"gradient": OptimizerSupportLevel.ignored,
            "bounds": OptimizerSupportLevel.ignored,
            "initial_point": OptimizerSupportLevel.required,}

