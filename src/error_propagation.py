import numpy as np

def total_uncertainty(U, rho):

    names = list(U.keys())
    var = sum(U[n] ** 2 for n in names)
    cov = 0.0
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            a, b = names[i], names[j]
            r = rho.get((a, b), rho.get((b, a), 0.0))
            cov += 2.0 * r * U[a] * U[b]
    return float(np.sqrt(var + cov))

def contribution_ratio(U, rho):
    ut = total_uncertainty(U, rho)
    out = {}
    for s in U:
        own = U[s] ** 2
        cross = 0.0
        for j in U:
            if j == s:
                continue
            r = rho.get((s, j), rho.get((j, s), 0.0))
            cross += r * U[s] * U[j]
        out[s] = (own + cross) / (ut ** 2) * 100.0
    return out