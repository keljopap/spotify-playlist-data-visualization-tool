import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import saved_tracks
import defaults
import playlists
import json

# TODO make a dropdown to select the playlist you'd like to display the rankings for, then load the data (display loading icon in Graph with "loading_state")
#USER_PLAYLISTS = playlists.get_current_user_playlists_no_tracks(defaults.SP_CLIENT, 50)
USER_PLAYLISTS = playlists.get_current_user_playlists_to_track_ids_with_audio_features(defaults.SP_CLIENT,50,50)
PLAYLIST_OPTIONS = [{'label': details['name'], 'value': playlist_id} for playlist_id, details in USER_PLAYLISTS.items()]

app = dash.Dash(__name__)

fig = make_subplots(rows=1, cols=1, shared_xaxes=True, vertical_spacing=0.05)

SORT_FEATURES_OPTIONS = [
    {'label': defaults.TRAIT_POPULARITY.capitalize(), 'value': defaults.TRAIT_POPULARITY}
]

for feature in defaults.AUDIO_FEATURE_KEYS:
    SORT_FEATURES_OPTIONS.append({
        'label': feature.replace('_', ' ').capitalize(),
        'value': feature
    })

app.layout = html.Div([
    dcc.Dropdown(
        id='playlist-dropdown',
        options=PLAYLIST_OPTIONS,
        value=PLAYLIST_OPTIONS[0]['value'] if PLAYLIST_OPTIONS else None,  # default to the first playlist if available
        clearable=False
    ),
    dcc.Dropdown(
        id='feature-dropdown',
        options=SORT_FEATURES_OPTIONS,
        value=defaults.TRAIT_POPULARITY,
        clearable=False
    ),
    dcc.Dropdown(
        id='sort-order-dropdown',
        options=[
            {'label': 'Ascending', 'value': 'asc'},
            {'label': 'Descending', 'value': 'desc'},
            {'label': 'None (Custom Order)', 'value': 'none'},
        ],
        value='desc',
        clearable=False
    ),
    dcc.Graph(id='bar-plot', figure=fig),
])


@app.callback(
    Output('bar-plot', 'figure'),
    [
        Input('playlist-dropdown', 'value'),
        Input('feature-dropdown', 'value'),
        Input('sort-order-dropdown', 'value')
    ]
)
def update_figure(playlist_id, selected_feature, sort_order):
    #print("\nplaylist id:", playlist_id)
    #print("selected feature:", selected_feature)
    #print("sort order:", sort_order)

    #print("USER_PLAYLISTS:", json.dumps(USER_PLAYLISTS))
    tracks_data = USER_PLAYLISTS[playlist_id]['tracks'].values()
    #print("tracks data for playlist:", tracks_data)

    if sort_order == 'none':
        tracks_sorted = sorted(tracks_data, key=lambda x: x[defaults.TRAIT_CUSTOM_ORDER])
    elif selected_feature == defaults.TRAIT_POPULARITY:
        tracks_sorted = sorted(tracks_data, key=lambda x: x[selected_feature], reverse=(sort_order == 'desc'))
    elif selected_feature in defaults.AUDIO_FEATURE_KEYS:
        tracks_sorted = sorted(tracks_data, key=lambda x: x['audio_features'][selected_feature], reverse=(sort_order == 'desc'))

    if selected_feature == defaults.TRAIT_POPULARITY:
        values = [track[selected_feature] for track in tracks_sorted]
    elif selected_feature in defaults.AUDIO_FEATURE_KEYS:
        values = [track['audio_features'][selected_feature] for track in tracks_sorted]

    hover_info_names = ["Name: " + track['name'] + "<br>Artist: " + track['artist'] + "<br>Album: " + track['album'] for track in tracks_sorted]
    shortened_names = [str(i) + ". " + track['name'][:25] for i, track in enumerate(tracks_sorted, start=1)]

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=shortened_names,
            y=values,
            hovertext=hover_info_names,
            hoverinfo='text+y',
            name=selected_feature,
        )
    )

    fig.add_trace(
        go.Scatter(
            x=shortened_names,
            y=values,
            hovertext=hover_info_names,
            hoverinfo='text+y',
            name=selected_feature,
        )
    )

    fig.update_layout(title_text=f"Songs by {selected_feature}")
    fig.update_xaxes(tickangle=30)
    fig.update_xaxes(title_text="Song Names")
    fig.update_xaxes
    fig.update_yaxes(title_text=selected_feature.capitalize())

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
