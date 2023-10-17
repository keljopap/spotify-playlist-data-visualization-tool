import plotly.graph_objects as go

FEATURE_ONE = 'Feature One'
FEATURE_TWO = 'Feature Two'
FEATURE_THREE = 'Feature Three'
SONG_NAME = 'Song Name'

songs = {
    FEATURE_ONE: [4, 11, 12, 15, 3],
    FEATURE_TWO: [5, 3, 2, 7, 4],
    FEATURE_THREE: [2, 9, 1, 6, 5],
    SONG_NAME: ['Song A', 'Song B', 'Song C', 'Song D', 'Song E']
}

def sorted_songs_and_values_by_feature(feature):
    sorted_pairs = sorted(zip(songs[feature], songs[SONG_NAME]))
    sorted_values, sorted_songs = zip(*sorted_pairs)
    return sorted_songs, sorted_values

for feature in [FEATURE_ONE, FEATURE_TWO, FEATURE_THREE]:
    print("\nsongs sorted by feature:", feature)
    print(sorted_songs_and_values_by_feature(feature)[0])
    print(sorted_songs_and_values_by_feature(feature)[1])

fig = go.Figure(
    go.Bar(
        x=sorted_songs_and_values_by_feature(FEATURE_ONE)[0],
        y=sorted_songs_and_values_by_feature(FEATURE_ONE)[1],
        name=FEATURE_ONE
    )
)

feature_dropdown = [
    {
        "label": FEATURE_ONE,
        "method": "update",
        "args": [
            {
                "x": [sorted_songs_and_values_by_feature(FEATURE_ONE)[0]],
                "y": [sorted_songs_and_values_by_feature(FEATURE_ONE)[1]],
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
                "x": [sorted_songs_and_values_by_feature(FEATURE_TWO)[0]],
                "y": [sorted_songs_and_values_by_feature(FEATURE_TWO)[1]],
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
                "x": [sorted_songs_and_values_by_feature(FEATURE_THREE)[0]],
                "y": [sorted_songs_and_values_by_feature(FEATURE_THREE)[1]],
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