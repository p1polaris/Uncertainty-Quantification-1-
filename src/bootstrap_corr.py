import numpy as np

def iid_bootstrap_corr(x, y, n_boot=1000, seed=None):
    rng = np.random.default_rng(seed)
    n = len(x)
    ests = np.empty(n_boot)
    for b in range(n_boot):
        idx = rng.integers(0, n, n)
        ests[b] = np.corrcoef(x[idx], y[idx])[0, 1]
    return ests

def spatial_block_bootstrap_corr(x, y, coords, block_size, n_boot=1000, seed=None):

    rng = np.random.default_rng(seed)
    bx = np.floor((coords[:, 0] - coords[:, 0].min()) / block_size).astype(int)
    by = np.floor((coords[:, 1] - coords[:, 1].min()) / block_size).astype(int)
    block_id = bx * (by.max() + 1) + by
    uniq = np.unique(block_id)
    ests = np.empty(n_boot)
    for b in range(n_boot):
        chosen = rng.choice(uniq, size=len(uniq), replace=True)
        idx = np.concatenate([np.where(block_id == c)[0] for c in chosen])
        ests[b] = np.corrcoef(x[idx], y[idx])[0, 1]
    return ests