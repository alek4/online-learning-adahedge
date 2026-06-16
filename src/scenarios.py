import numpy as np

SWAP_EVERY = 200


def generate_stochastic(K, T, seed):
    rng = np.random.default_rng(seed)
    losses = rng.binomial(1, 0.5, size=(T, K)).astype(float)
    losses[:, 0] = rng.binomial(1, 0.3, size=T)
    return losses


def generate_adversarial(K, T, seed, swap_every=SWAP_EVERY):
    rng = np.random.default_rng(seed)
    losses = rng.binomial(1, 0.5, size=(T, K)).astype(float)
    for t in range(T):
        best = (t // swap_every) % K
        losses[t, best] = rng.binomial(1, 0.1)
    return losses


def generate_low_gap(K, T, seed):
    rng = np.random.default_rng(seed)
    losses = rng.binomial(1, 0.5, size=(T, K)).astype(float)
    losses[:, 0] = rng.binomial(1, 0.49, size=T)
    return losses
