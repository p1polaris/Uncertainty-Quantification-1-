import numpy as np
from src.error_propagation import total_uncertainty, contribution_ratio
from src.monte_carlo import sample_multivariate_normal, mc_interval

U = {"class": 0.04, "change": 0.05, "product": 0.06}
rho = {("class", "change"): 0.33, ("class", "product"): 0.13, ("change", "product"): 0.20}
print("U_total:", total_uncertainty(U, rho))
print("contributions:", contribution_ratio(U, rho))

mu = np.zeros(3); cov = np.array([[0.04**2, 0.33*0.04*0.05, 0.13*0.04*0.06],
                                  [0.33*0.04*0.05, 0.05**2, 0.20*0.05*0.06],
                                  [0.13*0.04*0.06, 0.20*0.05*0.06, 0.06**2]])
s = sample_multivariate_normal(mu, cov, 1000, seed=0)[:, 0]
print("95% interval:", mc_interval(s))