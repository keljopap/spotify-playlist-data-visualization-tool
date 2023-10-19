import defaults
import json
import tracks

# Raw response from API - shared by preemptive load and lazy load methods
def get_current_user_playlists(
    sp = defaults.SP_CLIENT,
    limit=5
):
    return sp.user_playlists(
        limit=limit,
        user=sp.current_user()['id']
    )['items']

# Used for lazy loading the tracks in favor of showing all the playlist metadata first
def get_current_user_playlists_no_tracks(
    sp = defaults.SP_CLIENT,
    playlist_limit=5
):
    playlists_info_no_tracks = {}
    user_playlists = get_current_user_playlists(sp, playlist_limit)
    for playlist in user_playlists:
        pid=playlist['id']
        playlists_info_no_tracks[pid] = {
            'name': playlist['name'],
            'description': playlist['description'],
            'tracks': {},
            'tracks_loaded': False,
            'features_loaded': False
        }
    return playlists_info_no_tracks

# Used to get the tracks from a single playlist on demand - the graphing UI can cache it in memory if needed
def get_tracks_from_playlist(
    playlist_id,
    sp = defaults.SP_CLIENT,
    limit=defaults.TRACK_LIMIT
):
    tracks_from_this_playlist = sp.user_playlist_tracks(
        user=sp.current_user()['id'],
        playlist_id=playlist_id,
        limit=limit
    )['items']
    track_ids = [t['track']['id'] for t in tracks_from_this_playlist]
    return tracks.get_tracks_from_ids(sp, track_ids)

def get_current_user_playlists_to_track_ids(
    sp = defaults.SP_CLIENT,
    playlist_limit=5,
    track_limit=5
):
    playlists_to_track_ids = {}
    user_playlists = get_current_user_playlists(sp, playlist_limit)
    for playlist in user_playlists:
        pid=playlist['id']
        playlists_to_track_ids[pid] = {
            'name': playlist['name'],
            'description': playlist['description'],
            'tracks': {},
            'tracks_loaded': False,
            'features_loaded': False
        }
        print(f"Loading tracks' metadata for playlist {playlist['name']}")
        playlists_to_track_ids[pid]['tracks'] = get_tracks_from_playlist(pid, sp, track_limit)
        playlists_to_track_ids[pid]['tracks_loaded'] = True

    return playlists_to_track_ids

def get_tracks_with_audio_features(
    track_ids,
    sp = defaults.SP_CLIENT
):
    tracks_with_audio_features = {}
    tbf = tracks.get_tracks_by_features(sp, track_ids)
    for track_id, features in tbf.items():
        tracks_with_audio_features[track_id] = {}
        tracks_with_audio_features[track_id]['audio_features'] = features
    return tracks_with_audio_features

# Only really to be used after calling get_current_user_playlists_to_track_ids,
# but can be used to load audio features lazily since it is one API call per track 
# therefore by far the slowest call that be delayed until the playlist is selected
def populate_audio_features_by_playlist(
    playlist_id,
    playlists_with_tracks = {},
    sp = defaults.SP_CLIENT
):
    #print(json.dumps(playlists_with_tracks[playlist_id]['tracks'], indent=2))
    track_ids = playlists_with_tracks[playlist_id]['tracks'].keys()
    tracks_with_audio_features = get_tracks_with_audio_features(track_ids, sp)
    for tid in track_ids:
        if tid in tracks_with_audio_features and 'audio_features' in tracks_with_audio_features[tid]:
            playlists_with_tracks[playlist_id]['tracks'][tid]['audio_features'] = tracks_with_audio_features[tid]['audio_features']
    #print("\n\n\n", playlist_id, "\n\nplaylists with tracks with audio features:", json.dumps(playlists_with_tracks))
    return playlists_with_tracks

def get_current_user_playlists_to_track_ids_with_audio_features(
    sp = defaults.SP_CLIENT,
    playlist_limit = defaults.PLAYLIST_LIMIT,
    track_limit = defaults.TRACK_LIMIT
):
    playlists_with_tracks = get_current_user_playlists_to_track_ids(sp, playlist_limit, track_limit)
    for pid in playlists_with_tracks:
        print(f"Loading tracks' audio features for playlist {playlists_with_tracks[pid]['name']}")
        playlists_with_tracks = populate_audio_features_by_playlist(pid, playlists_with_tracks)
        playlists_with_tracks[pid]['features_loaded'] = True
    print("Done loading track data - check http://127.0.0.1:8050/")
    return playlists_with_tracks

## Gets first x sorted tracks by the selected audio feature for each of the first y user playlists found
def get_playlists_rankings(
    selected_feature_key = defaults.SELECTED_FEATURE_KEY,
    descending_order = defaults.DESCENDING,
    playlist_limit = defaults.PLAYLIST_LIMIT,
    track_limit = defaults.TRACK_LIMIT
):
    playlists_with_ratings = get_current_user_playlists_to_track_ids_with_audio_features(
        defaults.SP_CLIENT,
        playlist_limit,
        track_limit
    )
    sorted_playlists = {}
    for pid in playlists_with_ratings:
        playlist = playlists_with_ratings[pid]
        sorted_playlists[pid] = {}
        sorted_playlists[pid]['name'] = playlist['name']
        sorted_playlists[pid]['description'] = playlist['description']
        sorted_playlists[pid]['tracks'] = tracks.get_sorted_tracks_by_feature(
            playlist['tracks'],
            selected_feature_key,
            descending_order
        )
    return sorted_playlists

## Prints first x sorted tracks by the selected audio feature for each of the first y user playlists found
def print_playlists_rankings(
    selected_feature_key = defaults.SELECTED_FEATURE_KEY,
    descending_order = defaults.DESCENDING,
    playlist_limit = defaults.PLAYLIST_LIMIT,
    track_limit = defaults.TRACK_LIMIT
):
    playlists_with_ratings = get_playlists_rankings(selected_feature_key, descending_order, playlist_limit, track_limit)
    for pid in playlists_with_ratings:
        print("\n\nFor playlist \"" + playlists_with_ratings[pid]['name'] + "\"")
        tracks.print_list_of_tracks_sorted_by_feature(
            playlists_with_ratings[pid]['tracks'],
            selected_feature_key,
            descending_order
        )