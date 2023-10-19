# Background

I wanted a tool to visualize my playlists based on all the quantitative metrics the Spotify API provides for each track.  Sometimes I start throwing a bunch of songs I like in a playlist without having a good sense of the theme yet, then end up with a group of songs I like individually but they just don't quite flow well together.  This will use data to validate those feelings and tune your ears to the differences between your favorite songs.

## Prerequisites

This assumes you have Python 3 and Pip installed.

## Steps to run

1. Follow the steps [here](https://developer.spotify.com/documentation/web-api/tutorials/getting-started) to create an access token.
2. Create your .env file that Python will automatically look for environment variables in: `cp .env.dist .env`
3. Set the CLIENT_ID and CLIENT_SECRET values generated in step one in the .env file
4. Download the necessary libraries with `pip install -r requirements.txt`
5. Run `python src/main.py`
6. Note: when authenticating against your Spotify account for the first time, just paste the entire generated URL with all the appended params after allowing the application permissions to read your playlists' data in the terminal you ran the main script from.  (I've only tested this from my machine so far!)
7. Navigate to http://127.0.0.1:8050/ to see your playlist data come to life

## Feature Ideas

Playlist analysis:

- [x] give playlists rankings based on danceability, tempo, metrics
- [ ] actually paginate through more than the page limit of 50 and rank entire list (may hit api limits at certain playlist sizes, need to throttle)
- [ ] compare most similar playlists
- [ ] rank your friends' public playlists based on these too
- [ ] combine any two playlists
- [ ] identify "outlier" songs (plotly may do statistical significance reporting)
- [ ] identify most homogeneous and least homogeneous playlists
- [x] rank songs by popularity
- [ ] create new copies of the playlists based on custom ordering (or override in place)

Playlist analysis visualization:

- [x] data visualization plugin works using sample data
- [x] use a plugin to automatically do some of the data visualizations
- [x] visualize popularity and audio features for all the current user's playlists
- [x] sort by ascending, descending, or original order in the playlist to analyze where there transitions between songs could sound more seamless
- [ ] create a session for an arbitrary user who authenticates and show them their data

Playlist management:

- [ ] find playlists by a particular song
- [ ] find repeat songs across different playlists

Artists' songs analysis:

- [ ] rank a favorite artists' songs by audio features
- [ ] identify outlier songs
- [ ] compare homogeneity of two artists' songs across a certain category
- [ ] popularity ranking

Stretch goals with account data zip  (these can only be done with account data zip - must request download per user instead of using api)

- [ ] report listening trends over time
- [ ] what time of day are you listening

Recently listened to data:

- [x] Use a different scope to fetch most recently listened to songs
- [ ] Rate the "mood" of recent listens (perhaps against average moods of playlists)

## Sources and inspirations

- [Sort Your Music](http://sortyourmusic.playlistmachinery.com) ([Source code](https://github.com/plamere/SortYourMusic/tree/master))
- [Spotipy client documentation](https://spotipy.readthedocs.io/en/2.22.1/)
- [Spotify developer API documentation](https://developer.spotify.com/documentation/web-api)
- [Stats for Spotify](https://www.statsforspotify.com/) (Paid service - source code not linked)
- [Plotly](https://plotly.com/python/graph-objects/) Graphing library for plotting the data - see static examples in plotly folder
- [Dash](https://dash.plotly.com/) For dynamically plotting the data based on playlist, trait to sort by, sort order
