"""MR15 toy RLCR: 2 role-conditioned agents sharing one policy, same team reward.
Not Avalon implementation. Dependencies: NumPy only. Reproducible stochastic policy gradient.
"""
import numpy as np


def softmax(x):
    y = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return y / y.sum(axis=-1, keepdims=True)


def train(seed=42, steps=700, k=16, lr=0.15, verbose=False):
    assert k > 1
    rng = np.random.default_rng(seed)
    theta = np.zeros((2, 2), dtype=float)  # SAME policy parameter matrix, conditioned on role
    curve = []
    for step in range(steps):
        p = softmax(theta)
        actions = np.column_stack([rng.choice(2, size=k, p=p[j]) for j in range(2)])
        # Team succeeds only if both roles coordinate on their complementary subtask.
        rewards = ((actions[:, 0] == 0) & (actions[:, 1] == 1)).astype(float)
        # Leave-one-out reward baseline: excludes each rollout's own reward.
        # LOO advantage preserves unbiased REINFORCE for independent rollouts.
        advantage = rewards - (rewards.sum() - rewards) / (k - 1)
        # Every agent gets SAME organisation-level advantage within a rollout.
        grads = np.zeros_like(theta)
        for j in range(2):
            logp_grad = np.eye(2)[actions[:, j]] - p[j]  # ∇log π(a|role=j)
            grads[j] = np.mean(advantage[:, None] * logp_grad, axis=0)
        theta += lr * grads
        if step % 50 == 0 or step == steps - 1:
            success = float(softmax(theta)[0, 0] * softmax(theta)[1, 1])
            curve.append((step, success))
    if verbose:
        for step, success in curve:
            print(f"step={step:4d}  analytical P(team success)={success:.4f}")
    return theta, curve


def check_gradient(seed=8):
    rng = np.random.default_rng(seed)
    theta = rng.normal(size=(2, 2)) * 0.2
    p = softmax(theta)
    # Analytic objective J(θ) = P(action0=0, action1=1): exact gradient
    true_grad = np.zeros_like(theta)
    g0 = np.array([1., 0.]) - p[0]
    g1 = np.array([0., 1.]) - p[1]
    success_prob = p[0, 0] * p[1, 1]
    true_grad[0] = success_prob * g0
    true_grad[1] = success_prob * g1
    # Finite-difference derivative of J.
    eps = 1e-5
    fd = np.zeros_like(theta)
    for row in range(2):
        for col in range(2):
            plus, minus = theta.copy(), theta.copy()
            plus[row, col] += eps
            minus[row, col] -= eps
            jp = np.prod([softmax(plus)[0, 0], softmax(plus)[1, 1]])
            jm = np.prod([softmax(minus)[0, 0], softmax(minus)[1, 1]])
            fd[row, col] = (jp - jm) / (2 * eps)
    assert np.allclose(true_grad, fd, atol=1e-8), (true_grad, fd)
    return true_grad


if __name__ == '__main__':
    print('Gradient test:', check_gradient().round(5))
    _, curve = train(verbose=True)
    assert curve[0][1] >= 0.20
    assert curve[-1][1] > 0.85, curve[-1]
    print('PASS: collective return trains a shared role-conditioned policy.')
