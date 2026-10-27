import torch
import torch.nn.functional as F

torch.manual_seed(17)
device = 'cuda' if torch.cuda.is_available() else 'cpu'
V, N = 5, 12
lengths = {0: 28, 1: 4}  # same prompt count, different response lengths
teacher = torch.tensor([[.70,.12,.08,.06,.04],
                        [.06,.06,.08,.10,.70]], device=device)

class Student(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.logits = torch.nn.Parameter(torch.zeros(2,V))
    def forward(self,domain):
        return torch.softmax(self.logits[domain],dim=-1)

def train(reduction):
    student = Student().to(device)
    optimizer = torch.optim.SGD(student.parameters(),lr=1.2)
    for step in range(35):
        response_losses, token_losses = [], []
        for domain in (0,1):
            probs = student(domain)
            # Draw the student's CURRENT on-policy tokens.
            samples = torch.multinomial(probs.expand(N,-1),lengths[domain],replacement=True)
            logp_student = torch.log(probs[samples].clamp_min(1e-12))
            logp_teacher = torch.log(teacher[domain,samples].clamp_min(1e-12))
            advantage = (logp_teacher - logp_student).detach()
            pg_loss = -advantage * logp_student  # sampled-token OPD gradient
            response_losses.append(pg_loss.mean())
            token_losses.append(pg_loss.reshape(-1))
        loss = (torch.cat(token_losses).mean() if reduction=='global-token'
                else torch.stack(response_losses).mean())
        optimizer.zero_grad(); loss.backward(); optimizer.step()
    with torch.no_grad():
        return [float(F.kl_div(student(d).log(),teacher[d],reduction='sum'))
                for d in (0,1)]  # teacher||student KL (diagnostic only)

for reduction in ('global-token','equal-domain'):
    print(reduction, 'teacher||student KL:',
          [round(k,4) for k in train(reduction)])
print('Toy MOPD; NOT a frontier-model reproduction.')