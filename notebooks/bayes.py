import numpy as np
from scipy.special import betaln as logbeta


def prob_b_beats_a(wins_a: int, loses_a: int, wins_b: int, loses_b: int) -> float:
    alpha_a = wins_a + 1
    beta_a = loses_a + 1

    alpha_b = wins_b + 1
    beta_b = loses_b + 1

    total = 0.0
    for i in range(alpha_b):
        total += np.exp(
            logbeta(alpha_a + i, beta_b + beta_a)
            - np.log(beta_b + i)
            - logbeta(1 + i, beta_b)
            - logbeta(alpha_a, beta_a)
        )
    return total
