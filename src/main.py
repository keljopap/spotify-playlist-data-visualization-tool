import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import rank_tracks_by_feature
import user_inputs

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-library-read"))

# 1. Ask the user how many tracks they'd like to list
# 2. Ask the user which trait they want to sort by
#selected_feature_key = user_inputs.select_feature_to_sort_by()
selected_feature_key = "tempo"
# 3. Ask the user if they want to sort in ascending or descending order
#descending = user_inputs.sort_by_descending()
descending = True
limit=50

saved_tracks = rank_tracks_by_feature.get_user_saved_tracks_with_audio_features(sp, limit)
#for audio_feature in user_inputs.FEATURE_KEYS:
sorted = rank_tracks_by_feature.get_sorted_tracks_by_feature(saved_tracks, selected_feature_key, descending)
#print(sorted)
rank_tracks_by_feature.print_list_of_tracks_sorted_by_feature(sorted, selected_feature_key)

#playlists_to_track_ids = rank_tracks_by_feature.get_current_user_playlists_to_track_ids(sp)

#print(json.dumps(playlists_to_track_ids, indent=2))
# for pid in playlists_to_track_ids:
#     playlist = playlists_to_track_ids[pid]
#     print("Most danceable songs from playlist ", playlist['name'])
#     ranked = rank_tracks_by_feature.get_sorted_tracks_by_feature_ids_only(
#         sp,
#         playlist['tracks'].keys(),
#         5,
#         selected_feature_key,
#         descending
#     )
#     #print(json.dumps(ranked))
#     rank_tracks_by_feature.print_list_of_playlist_tracks_sorted_by_feature(
#         ranked,
#         playlist['tracks'],
#         selected_feature_key,
#         descending
#     )
playlists_with_ratings = rank_tracks_by_feature.get_current_user_playlists_to_track_ids_with_audio_features(sp, limit)
for pid in playlists_with_ratings:
    playlist = playlists_with_ratings[pid]
    print("\n\nFor playlist \"" + playlist['name'] + "\"")
    new_sorted = rank_tracks_by_feature.get_sorted_tracks_by_feature(
        playlist['tracks'],
        selected_feature_key,
        descending
    )
    rank_tracks_by_feature.print_list_of_tracks_sorted_by_feature(
        new_sorted,
        selected_feature_key,
        descending
    )