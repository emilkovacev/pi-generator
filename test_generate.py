import plotly.express as px
from generate import generate_pi

ps, p, n = 0, 0, 0
pi = []
for _ in range(1000):
    retval = generate_pi(1000, 250)
    ps += retval[0]
    p += retval[1]
    n += 1
    pi.append(ps/n)

print(pi)
fig = px.line(x=[i for i in range(len(pi))], y=pi, title="pi calculated over time")
print(fig)
fig.show()
