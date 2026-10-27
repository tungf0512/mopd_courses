# Educational toy / unit-test illustration; not a full replication of the cited paper.
import numpy as np
z_t = np.array([3., 1., -2.]); z_s = z_t + 17.0
sm = lambda z: np.exp(z - z.max()) / np.exp(z - z.max()).sum()
def dld(a,b): return np.mean((a-b)**2)
def csd_pairwise(a,b):
    e = (a[:,None] - a[None,:]) - (b[:,None] - b[None,:])
    return 0.5 * np.mean(e**2)
print('max |softmax diff|=', np.max(abs(sm(z_s)-sm(z_t))))
print('DLD=',dld(z_s,z_t),'toy CSD=',csd_pairwise(z_s,z_t))
assert np.allclose(sm(z_s),sm(z_t))
assert np.isclose(csd_pairwise(z_s,z_t),0)
assert dld(z_s,z_t)>0
z_bad=np.array([3., 0., -2.])
assert csd_pairwise(z_bad,z_t)>0
