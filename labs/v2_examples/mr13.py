# Educational toy / unit-test illustration; not a full replication of the cited paper.
import numpy as np
labels = np.array(['answer_A','answer_B','answer_C','other','tool'])
p_t = np.array([.60, .39, .005, .004, .001])
p_s = np.array([.20, .30, .04, .01, .45])
assert np.isclose(p_t.sum(),1) and np.isclose(p_s.sum(),1)
critical = 4
for k in [1, 2, 3, 4, 5]:
    t_idx = set(np.argsort(p_t)[-k:])
    s_idx = set(np.argsort(p_s)[-k:])
    union = t_idx | s_idx
    print('k=',k, 'teacher mass=',round(p_t[list(t_idx)].sum(),4),
          'tool in teacher=',critical in t_idx,'tool in union=',critical in union)
print('full forward-KL logit gradient on tool=',round(p_s[critical]-p_t[critical],3))
# NOTE: Đây KHÔNG phải restricted-JSD gradient của paper.
