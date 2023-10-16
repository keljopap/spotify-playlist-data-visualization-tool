import json
import spotipy
import user_inputs

SP_CLIENT= spotipy.Spotify(
    auth_manager=spotipy.SpotifyOAuth(
        scope="user-library-read"
    )
)

# Returns a list of current user's saved tracks mapped by its id
# to some useful human-readable info (name, artist, album)
def get_user_saved_tracks(
    sp = SP_CLIENT,
    limit=5
):
    saved_tracks = sp.current_user_saved_tracks(limit=limit)
    user_saved_tracks = {}
    for item in saved_tracks['items']:
        track = item['track']
        #print(json.dumps(track, indent=3))
        user_saved_tracks[track['id']] = {
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'album': track['album']['name']
        }
    return user_saved_tracks

def get_tracks_from_ids(
    sp = SP_CLIENT,
    track_ids = [],
    limit=5
):
    tracks_by_ids = {}
    tracks = sp.tracks(track_ids)
    for track in tracks['tracks']:
        tracks_by_ids[track['id']] = {
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'album': track['album']['name']
        }
    return tracks_by_ids

# Returns a list of current user's saved tracks mapped by its id
# to some useful human-readable info (name, artist, album),
# plus select audio feature statistics
def get_user_saved_tracks_with_audio_features(
    sp = SP_CLIENT,
    limit=5
):
    saved_tracks_by_features = get_user_saved_tracks(sp, limit)
    tbf = get_tracks_by_features(sp, saved_tracks_by_features.keys())
    for track_id, features in tbf.items():
        saved_tracks_by_features[track_id]['audio_features'] = features
    return saved_tracks_by_features

# Takes a list of track ids, returns a map of them to their audio features
def get_tracks_by_features(
    sp = SP_CLIENT,
    track_ids = [],
    limit=5
):
    audio_features_by_track = sp.audio_features(track_ids)
    ids_to_features = {}
    for tfs in audio_features_by_track:
        ids_to_features[tfs['id']] = {}
        for fk in user_inputs.FEATURE_KEYS:
            ids_to_features[tfs['id']][fk] = tfs[fk]
    return ids_to_features


def get_sorted_tracks_by_feature(
    tracks_to_features = {},
    selected_feature_key="energy",
    descending=True
):
    #print("About to sort tracks by feature key")
    #print(json.dumps(tracks_to_features, indent=2))
    # 4. Sort the saved_tracks_by_features dictionary by the selected feature key
    sorted_tracks = sorted(
        tracks_to_features.values(),
        key=lambda x: x['audio_features'][selected_feature_key],
        reverse=descending
    )
    return sorted_tracks

# This one takes ids only
# def get_sorted_tracks_by_feature_ids_only(
#     sp = SP_CLIENT,
#     track_ids = [],
#     limit=5,
#     selected_feature_key="energy",
#     descending=True
# ):
#     tracks_by_features = get_tracks_by_features(sp, track_ids, limit)
#     sorted_tracks = sorted(
#         tracks_by_features.values(),
#         key=lambda x: x[selected_feature_key],
#         reverse=descending
#     )
#     return sorted_tracks

KEY_MAPPINGS = {
    0: "C",
    1: "C♯/D♭",
    2: "D",
    3: "D♯/E♭",
    4: "E",
    5: "F",
    6: "F♯/G♭",
    7: "G",
    8: "G♯/A♭",
    9: "A",
    10: "A♯/B♭",
    11: "B"
}

def ms_to_min_sec(milliseconds):
    total_seconds = milliseconds // 1000
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return minutes, seconds

# Print the sorted list with song names and their artists
def print_list_of_tracks_sorted_by_feature(
    sorted_tracks,
    selected_feature_key,
    desc=True
):
    print("\nYour first", len(sorted_tracks), "tracks sorted by", selected_feature_key, "(desc)" if desc == True else "(asc)")
    for idx, track in enumerate(sorted_tracks, start=1):
        if selected_feature_key not in user_inputs.FEATURE_KEYS:
            print(f"Invalid feature key \"{selected_feature_key}\", must be one of \"{user_inputs.FEATURE_KEYS}\"")
            break

        measure = track['audio_features'][selected_feature_key]
        if selected_feature_key == "key":
            measure = KEY_MAPPINGS[measure]
        elif selected_feature_key == "duration_ms":
            minutes, seconds = ms_to_min_sec(measure)
            measure = f"{minutes}:{seconds}"

        print(f"{idx}. [{measure}] {track['name']} - {track['artist']}")

# Print the sorted list with song names and their artists
# def print_list_of_playlist_tracks_sorted_by_feature(
#     ranked,
#     playlist_tracks,
#     selected_feature_key,
#     desc=True
# ):
#     print("\nYour tracks sorted by", selected_feature_key, "(desc)" if desc == True else "(asc)")
#     print(playlist_tracks)
#     for idx, track in enumerate(ranked, start=1):
#         if selected_feature_key not in user_inputs.FEATURE_KEYS:
#             print(f"Invalid feature key \"{selected_feature_key}\", must be one of \"{user_inputs.FEATURE_KEYS}\"")
#             break

#         measure = track[selected_feature_key]
#         if selected_feature_key == "key":
#             measure = KEY_MAPPINGS[measure]
#         elif selected_feature_key == "duration_ms":
#             minutes, seconds = ms_to_min_sec(measure)
#             measure = f"{minutes}:{seconds}"
#         print(track)    
#         print(f"{idx}. [{measure}] for track {track}")
        #print(f"{idx}. [{measure}] {track['name']} - {track['artist']}")
            

def get_current_user_playlists(
    sp = SP_CLIENT,
    limit=5
):
    return sp.user_playlists(
        limit=limit,
        user=sp.current_user()['id']
    )['items']

def get_current_user_playlists_to_track_ids(
    sp = SP_CLIENT,
    limit=5
):
    playlists_to_track_ids = {}
    user_playlists = get_current_user_playlists(sp, limit)
    for playlist in user_playlists:
        pid=playlist['id']
        tracks_from_this_playlist = sp.user_playlist_tracks(
            user=sp.current_user()['id'],
            playlist_id=pid,
            limit=limit
        )
        playlists_to_track_ids[pid] = {
            'name': playlist['name'],
            'description': playlist['description'],
            'tracks': {}
        }
        track_ids = []
        for idx, list_track in enumerate(tracks_from_this_playlist['items'], start=1):
            #print(json.dumps(list_track, indent=1))
            tid = list_track['track']['id']
            track_ids.append(tid)
            playlists_to_track_ids[pid]['tracks'][tid] = {}
        track_data = get_tracks_from_ids(sp, track_ids)
        for tid in track_ids:
            playlists_to_track_ids[pid]['tracks'][tid] = track_data[tid]
    return playlists_to_track_ids

def get_current_user_playlists_to_track_ids_with_audio_features(
    sp = SP_CLIENT,
    limit=5
):
    playlists_to_track_ids = get_current_user_playlists_to_track_ids(sp, limit)
    for pid in playlists_to_track_ids:
        pl_track_ids = playlists_to_track_ids[pid]['tracks'].keys()
        tbf = get_tracks_by_features(sp, pl_track_ids)
        for tid in playlists_to_track_ids[pid]['tracks']:
            playlists_to_track_ids[pid]['tracks'][tid]['audio_features'] = tbf[tid]
    return playlists_to_track_ids    