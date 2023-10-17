import plotly.express as px

data = {
    'Feature1': [1, 4, 2, 6, 3, 5],
    'Feature2': [5, 4, 3, 18, 2, 1],
    'Song Name': ['Song A', 'Song B', 'Song C', 'Song D', 'Song E', 'Song F']
}

fig = px.bar(data, x='Song Name', y='Feature1', title='Songs Visualization Based on Feature1')
fig.show()

fig2 = px.scatter(data, x='Feature1', y='Feature2', hover_name='Song Name', title='Songs Visualization')
fig2.show()