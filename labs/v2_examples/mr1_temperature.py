# Educational toy / unit-test illustration; not a full replication of the cited paper.
import numpy as np
z = np.array([4.0, 2.0, 0.0, -1.0])
def softmax(z):
    e = np.exp(z - np.max(z))
    return e / e.sum()
for temp in [1, 2, 4]:
    p = softmax(z / temp)
    entropy = -np.sum(p * np.log(p))
    print(f"T={temp}: p={p.round(3)}, entropy={entropy:.4f}")
assert np.isclose(softmax(z/2).sum(), 1)
