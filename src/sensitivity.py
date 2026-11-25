import numpy as np

def local_sensitivity(evaluate, p0, delta_frac, params):

    base = evaluate(p0)
    out = {}
    for p in params:
        p_pert = dict(p0)
        p_pert[p] = p0[p] * (1 + delta_frac)
        out[p] = ((evaluate(p_pert) - base) / base) / delta_frac
    return out

def sobol_indices(sampler, evaluate, n_samples, seed=None):

    # Placeholder: delegate to SALib.sobol.analyze for actual computation.
    raise NotImplementedError("Use SALib.sobol.analyze with a Saltelli sample matrix.")