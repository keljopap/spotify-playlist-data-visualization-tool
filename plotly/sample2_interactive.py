import plotly.graph_objects as go

FEATURE_ONE = 'Feature One'
FEATURE_TWO = 'Feature Two'
FEATURE_THREE = 'Feature Three'
SONG_NAME = 'Song Name'

songs = {
    FEATURE_ONE: [4, 1, 2, 5, 3],
    FEATURE_TWO: [5, 3, 2, 1, 4],
    FEATURE_THREE: [2, 3, 1, 4, 5],
    SONG_NAME: ['Song A', 'Song B', 'Song C', 'Song D', 'Song E']
}

fig = go.Figure(
    go.Bar(
        x=songs[SONG_NAME],
        y=songs[FEATURE_ONE],
        name=FEATURE_ONE
    )
)

feature_dropdown = [
    {
        "label": FEATURE_ONE,
        "method": "update",
        "args": [
            {
                "x": [songs[SONG_NAME]],
                "y": [songs[FEATURE_ONE]],
                "name": [FEATURE_ONE]
            },
            {
                "title": FEATURE_ONE
            }
        ]
    },
    {
        "label": FEATURE_TWO,
        "method": "update",
        "args": [
            {
                "x": [songs[SONG_NAME]],
                "y": [songs[FEATURE_TWO]],
                "name": [FEATURE_TWO]
            },
            {
                "title": FEATURE_TWO
            }
        ]
    },
    {
        "label": FEATURE_THREE,
        "method": "update",
        "args": [
            {
                "x": [songs[SONG_NAME]],
                "y": [songs[FEATURE_THREE]],
                "name": [FEATURE_THREE]
            },
            {
                "title": FEATURE_THREE
            }
        ]
    }
]

fig.update_layout(
    title=FEATURE_ONE,
    updatemenus=[
        {
            "buttons": feature_dropdown,
            "direction": "down",
            "pad": {"r": 10, "t": 10},
            "showactive": True,
            "x": 0.1,
            "xanchor": "left",
            "y": 1.15,
            "yanchor": "top"
        }
    ]
)

fig.show()