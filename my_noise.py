import numpy as np

# Precomputed gradient vectors for improved performance
grad3 = np.array([
    [1, 1, 0], [-1, 1, 0], [1, -1, 0], [-1, -1, 0],
    [1, 0, 1], [-1, 0, 1], [1, 0, -1], [-1, 0, -1],
    [0, 1, 1], [0, -1, 1], [0, 1, -1], [0, -1, -1],
    [1, 1, 0], [-1, 1, 0], [0, -1, 1], [0, -1, -1],
])


def perlin(x, y, z, permutation):
    """Generate Perlin noise for coordinates x, y, z."""
    # Calculate unit cube coordinates and relative positions
    xi_float = np.floor(x)
    yi_float = np.floor(y)
    zi_float = np.floor(z)
    
    xi = int(xi_float) & 255
    yi = int(yi_float) & 255
    zi = int(zi_float) & 255
    
    xf = x - xi_float
    yf = y - yi_float
    zf = z - zi_float
    
    # Fade curves
    u = xf * xf * xf * (xf * (xf * 6 - 15) + 10)
    v = yf * yf * yf * (yf * (yf * 6 - 15) + 10)
    w = zf * zf * zf * (zf * (zf * 6 - 15) + 10)
    
    # Permutation table
    p = permutation
    
    # Hash coordinates of cube corners
    xi_plus1 = (xi + 1) & 255
    yi_plus1 = (yi + 1) & 255
    zi_plus1 = (zi + 1) & 255
    
    # Access permutations only once per unique index
    xi_p = p[xi]
    xi_plus1_p = p[xi_plus1]
    
    yi_p = p[xi_p + yi]
    yi_plus1_p = p[xi_p + yi_plus1]
    yi_p_plus1 = p[xi_plus1_p + yi]
    yi_plus1_p_plus1 = p[xi_plus1_p + yi_plus1]
    
    aaa = p[yi_p + zi]
    aba = p[yi_plus1_p + zi]
    aab = p[yi_p + zi_plus1]
    abb = p[yi_plus1_p + zi_plus1]
    baa = p[yi_p_plus1 + zi]
    bba = p[yi_plus1_p_plus1 + zi]
    bab = p[yi_p_plus1 + zi_plus1]
    bbb = p[yi_plus1_p_plus1 + zi_plus1]
    
    # Gradients
    def grad(hash_value, x, y, z):
        g = grad3[hash_value & 15]
        return g[0] * x + g[1] * y + g[2] * z
    
    # Gradient calculations
    x1 = (1 - v) * ((1 - u) * grad(aaa, xf, yf, zf) + u * grad(baa, xf - 1, yf, zf)) + \
         v * ((1 - u) * grad(aba, xf, yf - 1, zf) + u * grad(bba, xf - 1, yf - 1, zf))
    
    x2 = (1 - v) * ((1 - u) * grad(aab, xf, yf, zf - 1) + u * grad(bab, xf - 1, yf, zf - 1)) + \
         v * ((1 - u) * grad(abb, xf, yf - 1, zf - 1) + u * grad(bbb, xf - 1, yf - 1, zf - 1))
    
    # Final interpolation
    result = (1 - w) * x1 + w * x2
    
    return result  # Output is in the range -1 to 1

 
# Generate permutation table
np.random.seed(0)  # For reproducibility
permutation = np.arange(256, dtype=int)
np.random.shuffle(permutation)
permutation = np.concatenate([permutation, permutation])
