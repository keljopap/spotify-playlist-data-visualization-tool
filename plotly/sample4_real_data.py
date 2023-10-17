import plotly.graph_objects as go

data = {
    'Feature1': [1, 4, 2, 6, 3, 5],
    'Feature2': [5, 4, 3, 18, 2, 1],
    'Song Name': ['Song A', 'Song B', 'Song C', 'Song D', 'Song E', 'Song F']
}

tracks = [
   {
      "name": "Enough Is Enough",
      "artist": "Post Malone",
      "album": "AUSTIN",
      "popularity": 0.81,
      "audio_features": {
         "acousticness": 0.014,
         "danceability": 0.483,
         "duration_ms": 165175,
         "energy": 0.768,
         "instrumentalness": 0,
         "key": 0,
         "liveness": 0.109,
         "loudness": -4.911,
         "speechiness": 0.0344,
         "tempo": 166.061,
         "time_signature": 4,
         "valence": 0.332
      }
   },
   {
      "name": "Hometown",
      "artist": "Sarah Jarosz",
      "album": "World On The Ground",
      "popularity": 0.45,
      "audio_features": {
         "acousticness": 0.853,
         "danceability": 0.584,
         "duration_ms": 180240,
         "energy": 0.273,
         "instrumentalness": 0.000109,
         "key": 9,
         "liveness": 0.102,
         "loudness": -12.806,
         "speechiness": 0.0357,
         "tempo": 149.757,
         "time_signature": 4,
         "valence": 0.47
      }
   },
   {
      "name": "Welcome Home, Son",
      "artist": "Radical Face",
      "album": "Ghost",
      "popularity": 0.72,
      "audio_features": {
         "acousticness": 0.723,
         "danceability": 0.587,
         "duration_ms": 287634,
         "energy": 0.497,
         "instrumentalness": 0.782,
         "key": 6,
         "liveness": 0.142,
         "loudness": -10.757,
         "speechiness": 0.0307,
         "tempo": 144.972,
         "time_signature": 3,
         "valence": 0.401
      }
   },
   {
      "name": "golden arm",
      "artist": "Sadurn",
      "album": "Radiator",
      "popularity": 0.34,
      "audio_features": {
         "acousticness": 0.843,
         "danceability": 0.61,
         "duration_ms": 244989,
         "energy": 0.18,
         "instrumentalness": 0.00913,
         "key": 2,
         "liveness": 0.0872,
         "loudness": -14.843,
         "speechiness": 0.0307,
         "tempo": 130.16,
         "time_signature": 4,
         "valence": 0.23
      }
   },
   {
      "name": "Home",
      "artist": "LCD Soundsystem",
      "album": "This Is Happening",
      "popularity": 0.54,
      "audio_features": {
         "acousticness": 0.0462,
         "danceability": 0.752,
         "duration_ms": 473333,
         "energy": 0.844,
         "instrumentalness": 0.131,
         "key": 9,
         "liveness": 0.0782,
         "loudness": -8.705,
         "speechiness": 0.0398,
         "tempo": 124.013,
         "time_signature": 4,
         "valence": 0.78
      }
   },
   {
      "name": "Cool It Now",
      "artist": "New Edition",
      "album": "New Edition",
      "popularity": 0.55,
      "audio_features": {
         "acousticness": 0.126,
         "danceability": 0.871,
         "duration_ms": 347667,
         "energy": 0.532,
         "instrumentalness": 0.00819,
         "key": 10,
         "liveness": 0.321,
         "loudness": -13.335,
         "speechiness": 0.0677,
         "tempo": 116.574,
         "time_signature": 4,
         "valence": 0.74
      }
   },
   {
      "name": "Flowers Never Bend with the Rainfall",
      "artist": "Simon & Garfunkel",
      "album": "Parsley, Sage, Rosemary And Thyme",
      "popularity": 0.54,
      "audio_features": {
         "acousticness": 0.656,
         "danceability": 0.425,
         "duration_ms": 131747,
         "energy": 0.34,
         "instrumentalness": 0,
         "key": 9,
         "liveness": 0.127,
         "loudness": -14.176,
         "speechiness": 0.0357,
         "tempo": 110.208,
         "time_signature": 4,
         "valence": 0.488
      }
   },
   {
      "name": "Another Way",
      "artist": "Ten F\u00e9",
      "album": "Hit the Light",
      "popularity": 0.37,
      "audio_features": {
         "acousticness": 0.118,
         "danceability": 0.7,
         "duration_ms": 254410,
         "energy": 0.362,
         "instrumentalness": 0.128,
         "key": 5,
         "liveness": 0.118,
         "loudness": -6.979,
         "speechiness": 0.0302,
         "tempo": 97.999,
         "time_signature": 4,
         "valence": 0.446
      }
   },
   {
      "name": "Tired of Being Alone",
      "artist": "Al Green",
      "album": "Gets Next to You",
      "popularity": 0.72,
      "audio_features": {
         "acousticness": 0.339,
         "danceability": 0.772,
         "duration_ms": 172320,
         "energy": 0.397,
         "instrumentalness": 0.00541,
         "key": 7,
         "liveness": 0.0753,
         "loudness": -8.585,
         "speechiness": 0.0391,
         "tempo": 97.964,
         "time_signature": 4,
         "valence": 0.617
      }
   },
   {
      "name": "Sweet Time",
      "artist": "Porter Robinson",
      "album": "Nurture",
      "popularity": 0.47,
      "audio_features": {
         "acousticness": 0.192,
         "danceability": 0.457,
         "duration_ms": 251510,
         "energy": 0.728,
         "instrumentalness": 0.0292,
         "key": 2,
         "liveness": 0.0944,
         "loudness": -8.625,
         "speechiness": 0.0497,
         "tempo": 84.976,
         "time_signature": 4,
         "valence": 0.439
      }
   }
]

song_names = [track["name"] + " - " + track["artist"] for track in tracks]
popularity = [track["popularity"] for track in tracks]
audio_features = list(tracks[0]["audio_features"].keys())

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

for feature in audio_features:
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
