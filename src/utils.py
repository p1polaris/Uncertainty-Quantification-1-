import numpy as np

def morans_i(x, w):
    x = np.asarray(x, float)
    xbar = x.mean()
    z = x - xbar
    n = len(x)
    W = w.sum()
    return (n / W) * (z @ w @ z) / (z @ z)

def empirical_coverage(lower, upper, ref):
    return float(np.mean((ref >= lower) & (ref <= upper)))

def crps_normal(mu, sigma, obs):
    from scipy.stats import norm
    z = (obs - mu) / sigma
    return float(sigma * (z * (2 * norm.cdf(z) - 1) + 2 * norm.pdf(z) - 1 / np.sqrt(np.pi)))