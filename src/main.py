import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import rank_tracks_by_feature
import user_inputs

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-library-read"))

# 1. Ask the user how many tracks they'd like to list
# 2. Ask the user which trait they want to sort by
#selected_feature_key = user_inputs.select_feature_to_sort_by()
SELECTED_FEATURE_KEY = "tempo"
# 3. Ask the user if they want to sort in ascending or descending order
#descending = user_inputs.sort_by_descending()
DESCENDING = True

PLAYLIST_LIMIT=10
TRACK_LIMIT=50

saved_tracks = rank_tracks_by_feature.get_user_saved_tracks_with_audio_features(sp, TRACK_LIMIT)
sorted = rank_tracks_by_feature.get_sorted_tracks_by_feature(saved_tracks, SELECTED_FEATURE_KEY, DESCENDING)
rank_tracks_by_feature.print_list_of_tracks_sorted_by_feature(sorted, SELECTED_FEATURE_KEY)

playlists_with_ratings = rank_tracks_by_feature.get_current_user_playlists_to_track_ids_with_audio_features(sp, PLAYLIST_LIMIT, TRACK_LIMIT)
for pid in playlists_with_ratings:
    playlist = playlists_with_ratings[pid]
    print("\n\nFor playlist \"" + playlist['name'] + "\"")
    new_sorted = rank_tracks_by_feature.get_sorted_tracks_by_feature(
        playlist['tracks'],
        SELECTED_FEATURE_KEY,
        DESCENDING
    )
    rank_tracks_by_feature.print_list_of_tracks_sorted_by_feature(
        new_sorted,
        SELECTED_FEATURE_KEY,
        DESCENDING
    )