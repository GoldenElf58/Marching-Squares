# import numpy as np

# from opensimplex import OpenSimplex
# from perlin_noise import PerlinNoise

EDGE_TABLE: dict[int, list[tuple[int, int]]] = {
    0: [],                             # 0000: No corners inside
    1: [(3, 0)],                       # 0001: Corner 0 inside
    2: [(0, 1)],                       # 0010: Corner 1 inside
    3: [(3, 1)],                       # 0011: Corners 0 and 1 inside
    4: [(1, 2)],                       # 0100: Corner 2 inside
    5: [(3, 0), (1, 2)],               # 0101: Corners 0 and 2 inside
    6: [(0, 1), (1, 2)],               # 0110: Corners 1 and 2 inside
    7: [(3, 2)],                       # 0111: Corners 0, 1, and 2 inside
    8: [(2, 3)],                       # 1000: Corner 3 inside
    9: [(2, 0)],                       # 1001: Corners 0 and 3 inside
    10: [(0, 1), (2, 3)],              # 1010: Corners 1 and 3 inside
    11: [(2, 1)],                      # 1011: Corners 0, 1, and 3 inside
    12: [(1, 2), (2, 3)],              # 1100: Corners 2 and 3 inside
    13: [(0, 1)],                      # 1101: Corners 0, 2, and 3 inside
    14: [(3, 0)],                      # 1110: Corners 1, 2, and 3 inside
    15: [],                            # 1111: All corners inside
}

# noise = OpenSimplex(0)
# noise = PerlinNoise()

# # Generate permutation table
# np.random.seed(0)  # For reproducibility
# permutation = np.arange(256, dtype=int)
# np.random.shuffle(permutation)
# permutation = np.concatenate([permutation, permutation])
