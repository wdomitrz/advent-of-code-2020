import numpy as np
from scipy.signal import fftconvolve as convolve


class Simulator:
    def __init__(self, data, dim, size):
        self.dim = dim
        self.size = size
        data_arr = np.array(
            list(map(lambda l: list(map(lambda x: x == '#', l)), data)))
        self.arr = np.zeros(list(np.array(data_arr.shape) +
                                 2 * size) + [2 * size + 1] * (dim - 2), dtype=int)
        self.arr[size:size + data_arr.shape[0], size:size + data_arr.shape[1]] = np.pad(np.expand_dims(
            data_arr, axis=list(range(2, dim))), [(0, 0), (0, 0)] + [(size, size)] * (dim - 2))

        self.rules = np.ones([3] * dim, dtype=int)

    def step(self):
        counted = convolve(self.arr, self.rules, mode='same')
        self.arr = (3 - 0.5 <= counted) * (counted <= 3.5) + \
            (((4 - 0.5 <= counted) * (counted <= 4 + 0.5) * (self.arr == 1)) >= 1)

    def size_steps(self):
        for _ in range(self.size):
            self.step()
        return self.arr


def main():
    with open("inputs/d17.txt") as f:
        data = f.read().splitlines()

    print(Simulator(data, dim=3, size=6).size_steps().sum())
    print(Simulator(data, dim=4, size=6).size_steps().sum())


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()
