import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import defaults
import playlists
import time

PLAYLIST_LIMIT = 50
TRACK_LIMIT = 50
print(f"Loading first {TRACK_LIMIT} tracks of first {PLAYLIST_LIMIT} user playlists")
start_time = time.time()  # get the current time before running the function
USER_PLAYLISTS = playlists.get_current_user_playlists_to_track_ids(
    defaults.SP_CLIENT,
    PLAYLIST_LIMIT,
    TRACK_LIMIT
)

end_time = time.time()  # get the current time after running the function
elapsed_time = end_time - start_time  # compute the difference
print(f"Loading user playlist data took {elapsed_time:.4f} seconds to run.")

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
            {'label': 'Default Playlist Order', 'value': 'default'},
            {'label': 'Ascending', 'value': 'asc'},
            {'label': 'Descending', 'value': 'desc'}
        ],
        value='default',
        clearable=False
    ),
    dcc.Graph(id='bar-plot', figure=fig),
    dcc.Checklist(
        id='toggle-charts',
        options=[
            {'label': 'Show Bar Chart', 'value': 'bar'},
            {'label': 'Show Trend Line', 'value': 'trend'}
        ],
        value=['bar', 'trend'],  # default to showing both
        inline=True
    ),
    dcc.Store(id='store-toggle-state', storage_type='session'),
])

@app.callback(
    Output('bar-plot', 'figure'),
    [
        Input('playlist-dropdown', 'value'),
        Input('feature-dropdown', 'value'),
        Input('sort-order-dropdown', 'value'),
        Input('toggle-charts', 'value')
    ]
)
def update_figure(playlist_id, selected_feature, sort_order, toggled_charts):
    global USER_PLAYLISTS
    tracks_data = USER_PLAYLISTS[playlist_id]['tracks'].values()
    if USER_PLAYLISTS[playlist_id]['features_loaded']:
        tracks_data = USER_PLAYLISTS[playlist_id]['tracks'].values()
    else:
        USER_PLAYLISTS = playlists.populate_audio_features_by_playlist(
            playlist_id,
            USER_PLAYLISTS
        )
        USER_PLAYLISTS[playlist_id]['features_loaded'] = True

    if sort_order == 'default':
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

    if 'bar' in toggled_charts:
        fig.add_trace(
            go.Bar(
                x=shortened_names,
                y=values,
                hovertext=hover_info_names,
                hoverinfo='text+y',
                name=selected_feature,
            )
        )
    if 'trend' in toggled_charts:
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
