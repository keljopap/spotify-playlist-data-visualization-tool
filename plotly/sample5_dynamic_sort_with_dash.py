import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import shared

app = dash.Dash(__name__)

# Initialize the figure layout
fig = make_subplots(rows=1, cols=1, shared_xaxes=True, vertical_spacing=0.04)

app.layout = html.Div([
    dcc.Graph(id='bar-plot', figure=fig),
    dcc.Dropdown(
        id='feature-dropdown',
        options=[
            {'label': 'Popularity', 'value': 'popularity'},
            {'label': 'Acousticness', 'value': 'acousticness'},
            # ... add other features here ...
        ],
        value='popularity',
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
])


@app.callback(
    Output('bar-plot', 'figure'),
    [Input('feature-dropdown', 'value'),
     Input('sort-order-dropdown', 'value')]
)
def update_figure(selected_feature, sort_order):
    print("\n\nselected feature:", selected_feature)
    print("sort order:", sort_order)
    if sort_order == 'none':
        tracks_sorted = sorted(shared.TRACKS_DATA, key=lambda x: x['custom_order_idx'])
        if selected_feature == "popularity":
            values = [track[selected_feature] for track in tracks_sorted]
        elif selected_feature == "acousticness":
            values = [track['audio_features'][selected_feature] for track in tracks_sorted]
    elif selected_feature == "popularity":
        tracks_sorted = sorted(shared.TRACKS_DATA, key=lambda x: x[selected_feature], reverse=(sort_order == 'desc'))
        values = [track[selected_feature] for track in tracks_sorted]
    elif selected_feature == "acousticness":
        tracks_sorted = sorted(shared.TRACKS_DATA, key=lambda x: x['audio_features'][selected_feature], reverse=(sort_order == 'desc'))
        values = [track['audio_features'][selected_feature] for track in tracks_sorted]

    names = [track['name'] for track in tracks_sorted]

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=names,
            y=values,
            text=names,
            name=selected_feature,
        )
    )

    fig.update_layout(title_text=f"Songs by {selected_feature}")
    fig.update_xaxes(title_text="Song")
    fig.update_yaxes(title_text=selected_feature)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
