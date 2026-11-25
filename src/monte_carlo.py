import numpy as np

def sample_multivariate_normal(mu, cov, n, seed=None):
    rng = np.random.default_rng(seed)
    return rng.multivariate_normal(mu, cov, size=n)

def paired_bootstrap(errors, n, seed=None):
    """errors: (N, k) array of paired error vectors; resample rows."""
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(errors), size=(n, len(errors)))
    return errors[idx]

def mc_interval(samples, level=0.95):

    from scipy.stats import norm
    z = norm.ppf(0.5 + level / 2)
    m, s = samples.mean(), samples.std(ddof=1)
    return m - z * s, m + z * s