def fade(t):
    """Fade function as defined by Ken Perlin. This eases coordinate values 
    so that they will "ease" towards integral values. This ends up smoothing 
    the final output."""
    return 6 * t ** 5 - 15 * t ** 4 + 10 * t ** 3


def lerp(a, b, x):
    """Linear interpolation function."""
    return a + x * (b - a)


def grad(hash, x, y):
    """Calculate gradient vector and return the dot product with (x, y)."""
    h = hash & 3
    u = x if h & 1 == 0 else -x
    v = y if h & 2 == 0 else -y
    return u + v


def perlin(x, y, permutation):
    """Generate Perlin noise for coordinates x, y."""
    xi = int(x) & 255
    yi = int(y) & 255
    xf = x - int(x)
    yf = y - int(y)

    u = fade(xf)
    v = fade(yf)

    aa = permutation[permutation[xi] + yi]
    ab = permutation[permutation[xi] + yi + 1]
    ba = permutation[permutation[xi + 1] + yi]
    bb = permutation[permutation[xi + 1] + yi + 1]

    x1 = lerp(grad(aa, xf, yf), grad(ba, xf - 1, yf), u)
    x2 = lerp(grad(ab, xf, yf - 1), grad(bb, xf - 1, yf - 1), u)

    return (lerp(x1, x2, v) + 1) / 2  # Normalize to 0 - 1
