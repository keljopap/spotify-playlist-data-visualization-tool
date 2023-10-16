# Background

## Prerequisites

1. Follow the steps [here](https://developer.spotify.com/documentation/web-api/tutorials/getting-started) to create an access token.
2. Run `cp .env.dist .env`
3. Set the CLIENT_ID and CLIENT_SECRET values in the .env file

## Feature Ideas

Playlist analysis:

- [x] give playlists rankings based on danceability, tempo, metrics
- [ ] actually paginate through more than the page limit of 50 and rank entire list (may hit api limits at certain playlist sizes, need to throttle)
- [ ] compare most similar playlists
- [ ] rank your friends' public playlists based on these too
- [ ] combine any two playlists
- [ ] identify "outlier" songs
- [ ] identify most homogeneous and least homogeneous playlists

Playlist analysis visualization:

- [ ] use a plugin to automatically do some of the data visualizations
- [ ] create a session for an arbitrary user who authenticates and show them their data

Playlist management:

- [ ] find playlists by a particular song
- [ ] find repeat songs across different playlists

Artists' songs analysis:

- [ ] rank a favorite artists' songs by audio features
- [ ] identify outlier songs
- [ ] compare homogeneity of two artists' songs across a certain category

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
