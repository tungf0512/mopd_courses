# Educational toy / unit-test illustration; not a full replication of the cited paper.
import numpy as np
student = {'science': np.array([0.55, .25, .20]), 'tool': np.array([.30,.55,.15])}
teacher = {'science': np.array([.72,.18,.10]), 'tool': np.array([.10,.80,.10])}
def kl(p, q):
    return np.sum(p * (np.log(p) - np.log(q)))
for task in student:
    gap = kl(student[task], teacher[task])
    wrong_task = 'tool' if task == 'science' else 'science'
    gap_wrong = kl(student[task], teacher[wrong_task])
    print(task, 'routed KL=', round(gap,4), 'wrong route KL=',round(gap_wrong,4))
    assert np.isfinite(gap) and gap >= -1e-10
# Trong LLM thực tế: cố định θ0 cho teacher, train Pk bằng gold labels,
# rồi train student θ trên self-rollouts và query teacher tại chính prefix đó.
