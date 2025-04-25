import plotly.express as px

from die import Die

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(1, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "Rolling Two D6 1000 times"
labels = {'x': 'Results', 'y': 'Frequencies of result'}

fig = px.line(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()