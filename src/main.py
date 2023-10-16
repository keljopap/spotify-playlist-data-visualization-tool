import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import rank_tracks_by_feature
import user_inputs

scopes = "user-library-read user-read-recently-played"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scopes))

# TODO Ask the user how many tracks they'd like to list
# TODO Ask the user which trait they want to sort by
#selected_feature_key = user_inputs.select_feature_to_sort_by()
SELECTED_FEATURE_KEY = "tempo"
# TODO Ask the user if they want to sort in ascending or descending order
# descending = user_inputs.sort_by_descending()
DESCENDING = True

# PLAYLIST_LIMIT=1
TRACK_LIMIT=5

def print_saved_tracks_rankings():
    saved_tracks = rank_tracks_by_feature.get_user_saved_tracks_with_audio_features(sp, TRACK_LIMIT)
    sorted = rank_tracks_by_feature.get_sorted_tracks_by_feature(saved_tracks, SELECTED_FEATURE_KEY, DESCENDING)
    rank_tracks_by_feature.print_list_of_tracks_sorted_by_feature(sorted, SELECTED_FEATURE_KEY)

def print_playlists_rankings():
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

print_saved_tracks_rankings()

print("Most recently listened to songs...")
recently_played_tracks = sp.current_user_recently_played()
for idx, item in enumerate(recently_played_tracks['items'], start=1):
    track = item['track']
    print(idx, ".", track['id'], track['name'], "-", track['artists'][0]['name'], "-", track['album']['name'])