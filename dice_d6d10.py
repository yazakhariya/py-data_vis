import plotly.express as px

from die import Die

die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(1, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "Rolling D6 & D10 50.000 times"
labels = {'x': 'Results', 'y': 'Frequencies of result'}

fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.write_html('dice_visual_d6d10.html')