# Background

## Prerequisites

1. Follow the steps [here](https://developer.spotify.com/documentation/web-api/tutorials/getting-started) to create an access token.
2. Run `cp .env.dist .env`
3. Set the CLIENT_ID and CLIENT_SECRET values in the .env file

## Feature Ideas

- [ ] find playlists by a particular song
- [ ] find repeat songs across different playlists
- [ ] compare most similar playlists
- [x] give playlists rankings based on danceability, tempo, metrics
- [ ] rank your friends' public playlists based on these too
- [ ] combine any two playlists
- [ ] identify "outlier" songs
- [ ] identify most homogeneous and least homogeneous playlists
- [ ] report listening trends over time
- [ ] what time of day are you listening
- [ ] rank a favorite artists' songs by audio features
- [ ] use a plugin to automatically do some of the data visualizations
- [ ] create a session for an arbitrary user who authenticates and show them their data

## Sources and inspirations

- [Sort Your Music](http://sortyourmusic.playlistmachinery.com) ([Source code](https://github.com/plamere/SortYourMusic/tree/master))
- [Spotipy client documentation](https://spotipy.readthedocs.io/en/2.22.1/)
- [Spotify developer API documentation](https://developer.spotify.com/documentation/web-api)
- [Stats for Spotify](https://www.statsforspotify.com/) (Paid service - source code not linked)
