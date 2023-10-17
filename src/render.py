import plotly.graph_objects as go
import defaults
import saved_tracks

tracks = saved_tracks.get_sorted_saved_tracks(50, defaults.TRAIT_DANCEABILITY, True)

song_names = [track["name"][:25] + " - " + track["artist"] for track in tracks]
custom_order_indices = [track[defaults.TRAIT_CUSTOM_ORDER] for track in tracks]
popularity = [track[defaults.TRAIT_POPULARITY] for track in tracks]

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
            {"y": [popularity], "name": ["Popularity"]},
            {"title": "Popularity"}
        ]
    }
]

feature_dropdown.append(
   {
      "label": defaults.TRAIT_CUSTOM_ORDER,
      "method": "update",
      "args": [
            {"y": [custom_order_indices], "name": [defaults.TRAIT_CUSTOM_ORDER]},
            {"title": "Default Playlist Index"}
      ]
   }
)

for feature in defaults.AUDIO_FEATURE_KEYS:
    feature_values = [track["audio_features"][feature] for track in tracks]
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
