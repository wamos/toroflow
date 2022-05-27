from typing import List
from numpy.random import default_rng
from component import Component
import numpy as np

class Source(Component):
    @property
    def output_names(self) -> List[str]:
        return ["tensors"]

    def initialize(self):
        pass

    def execute(self, tensors):
        t = default_rng(42).random((720,720,3))
        t1 = np.float32(t)
        tensors.push(t1, t1.shape)

class Sink(Component):
    @property
    def input_names(self) -> List[str]:
        return ["tensors"]

    def initialize(self):
        pass

    def execute(self, tensors):
        t1 = tensors.pop()