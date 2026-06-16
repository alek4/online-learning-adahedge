import numpy as np


def hedge(losses, eta):
    T, K = losses.shape
    weights = np.ones(K) / K
    cum_loss = 0.0
    expert_loss = np.zeros(K)

    cum_losses_t = np.empty(T)
    regret_t = np.empty(T)

    for t in range(T):
        p_t = weights / weights.sum()
        l_t = losses[t]

        learner_loss = p_t @ l_t
        cum_loss += learner_loss
        expert_loss += l_t

        weights *= np.exp(-eta * l_t)

        cum_losses_t[t] = cum_loss
        regret_t[t] = cum_loss - expert_loss.min()

    return {
        'cumulative_loss': cum_losses_t,
        'regret': regret_t,
    }
