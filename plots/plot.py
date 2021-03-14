import plotly.express as px
from generating_methods.statistics_generator import generate_pi


# the following plot takes a series of less accurate trials using
# the statistics generator method, and plots the average over time

ps, p, n = 0, 0, 0
pi = []
precision = []
for _ in range(1_000):
    retval = generate_pi(500, 250)
    ps += retval[0]
    p += retval[1]
    n += 1
    pi.append(ps/n)
    precision.append(p/n)

fig = px.line(x=[i+1 for i in range(len(pi))], y=pi)
fig.add_scatter(x=[i+1 for i in range(len(pi))], y=precision, mode='lines')
fig.show()
