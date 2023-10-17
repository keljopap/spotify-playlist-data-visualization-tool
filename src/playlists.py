import defaults
import tracks

def get_current_user_playlists(
    sp = defaults.SP_CLIENT,
    limit=5
):
    return sp.user_playlists(
        limit=limit,
        user=sp.current_user()['id']
    )['items']

def get_current_user_playlists_to_track_ids(
    sp = defaults.SP_CLIENT,
    playlist_limit=5,
    track_limit=5
):
    playlists_to_track_ids = {}
    user_playlists = get_current_user_playlists(sp, playlist_limit)
    for playlist in user_playlists:
        pid=playlist['id']
        tracks_from_this_playlist = sp.user_playlist_tracks(
            user=sp.current_user()['id'],
            playlist_id=pid,
            limit=track_limit
        )
        playlists_to_track_ids[pid] = {
            'name': playlist['name'],
            'description': playlist['description'],
            'tracks': {}
        }
        track_ids = []
        for list_track in tracks_from_this_playlist['items']:
            tid = list_track['track']['id']
            track_ids.append(tid)
            playlists_to_track_ids[pid]['tracks'][tid] = {}
        track_data = tracks.get_tracks_from_ids(sp, track_ids)
        for tid in track_ids:
            playlists_to_track_ids[pid]['tracks'][tid] = track_data[tid]
    return playlists_to_track_ids

def get_current_user_playlists_to_track_ids_with_audio_features(
    sp = defaults.SP_CLIENT,
    playlist_limit=5,
    track_limit=5
):
    playlists_to_track_ids = get_current_user_playlists_to_track_ids(sp, playlist_limit, track_limit)
    for pid in playlists_to_track_ids:
        pl_track_ids = playlists_to_track_ids[pid]['tracks'].keys()
        tbf = tracks.get_tracks_by_features(sp, pl_track_ids)
        for tid in playlists_to_track_ids[pid]['tracks']:
            playlists_to_track_ids[pid]['tracks'][tid]['audio_features'] = tbf[tid]
    return playlists_to_track_ids

## Prints first x sorted tracks by the selected audio feature for each of the first y user playlists found
def print_playlists_rankings():
    playlists_with_ratings = get_current_user_playlists_to_track_ids_with_audio_features(
        defaults.SP_CLIENT,
        defaults.PLAYLIST_LIMIT,
        defaults.TRACK_LIMIT
    )
    for pid in playlists_with_ratings:
        playlist = playlists_with_ratings[pid]
        new_sorted = tracks.get_sorted_tracks_by_feature(
            playlist['tracks'],
            defaults.SELECTED_FEATURE_KEY,
            defaults.DESCENDING
        )
        print("\n\nFor playlist \"" + playlist['name'] + "\"")
        tracks.print_list_of_tracks_sorted_by_feature(
            new_sorted,
            defaults.SELECTED_FEATURE_KEY,
            defaults.DESCENDING
        )