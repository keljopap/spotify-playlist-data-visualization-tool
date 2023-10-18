import plotly.graph_objects as go
import shared

# This function will return the y-values based on the chosen sort order and feature
def get_sorted_values(order, feature='popularity'):
    if order == 'asc':
        return sorted([(track[feature], track['name']) for track in shared.TRACKS_DATA])
    elif order == 'desc':
        return sorted([(track[feature], track['name']) for track in shared.TRACKS_DATA], reverse=True)
    else:  # custom
        return [(track[feature], track['name']) for track in shared.TRACKS_DATA]

POPULARITY = "popularity"
CUSTOM_ORDER_INDEX = "custom_order_idx"

song_names = [track["name"][:25] + " - " + track["artist"] for track in shared.TRACKS_DATA]
custom_order_indices = [track[CUSTOM_ORDER_INDEX] for track in shared.TRACKS_DATA]
popularity = [track[POPULARITY] for track in shared.TRACKS_DATA]
audio_features = list(shared.TRACKS_DATA[0]["audio_features"].keys())

fig = go.Figure(
    go.Bar(
        x=song_names,
        y=popularity,
        name="Popularity"
    )
)

feature_dropdown = [
    {
        "label": "Popularity",
        "method": "update",
        "args": [
            {"y": [popularity], "name": [POPULARITY]},
            {"title": "Popularity"}
        ]
    }
]

feature_dropdown.append(
   {
      "label": CUSTOM_ORDER_INDEX,
      "method": "update",
      "args": [
            {"y": [custom_order_indices], "name": [CUSTOM_ORDER_INDEX]},
            {"title": "Default Playlist Index"}
      ]
   }
)

for feature in audio_features:
    feature_values = [track["audio_features"][feature] for track in shared.TRACKS_DATA]
    feature_dropdown.append(
        {
            "label": feature,
            "method": "update",
            "args": [
                {"y": [feature_values], "name": [feature]},
                {"title": feature}
            ]
        }
    )

fig.update_layout(
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
