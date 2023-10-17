import defaults
import tracks
import json

# Returns a list of current user's saved tracks mapped by its id
# to some useful human-readable info (name, artist, album)
def get_user_saved_tracks(
    sp = defaults.SP_CLIENT,
    limit=5
):
    saved_tracks = sp.current_user_saved_tracks(limit=limit)
    user_saved_tracks = {}
    for idx, item in enumerate(saved_tracks['items'], start=1):
        track = item['track']
        user_saved_tracks[track['id']] = {
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'album': track['album']['name'],
            defaults.TRAIT_POPULARITY: track[defaults.TRAIT_POPULARITY]/100,
            defaults.TRAIT_CUSTOM_ORDER: idx
        }
    return user_saved_tracks

# Returns a list of current user's saved tracks mapped by its id
# to some useful human-readable info (name, artist, album),
# plus select audio feature statistics
def get_user_saved_tracks_with_audio_features(
    sp = defaults.SP_CLIENT,
    limit=5
):
    saved_tracks_by_features = get_user_saved_tracks(sp, limit)
    tbf = tracks.get_tracks_by_features(sp, saved_tracks_by_features.keys())
    for track_id, features in tbf.items():
        saved_tracks_by_features[track_id]['audio_features'] = features
    return saved_tracks_by_features

def get_sorted_saved_tracks(
    limit = defaults.TRACK_LIMIT,
    selected_feature_key = defaults.SELECTED_FEATURE_KEY,
    descending_order = defaults.DESCENDING
):
    saved = get_user_saved_tracks_with_audio_features(
        defaults.SP_CLIENT,
        limit
    )
    return tracks.get_sorted_tracks_by_feature(
        saved,
        selected_feature_key,
        descending_order
    )

## Prints first x sorted tracks by the selected audio feature from the user's saved tracks list
def print_saved_tracks_rankings(
    limit = defaults.TRACK_LIMIT,
    selected_feature_key = defaults.SELECTED_FEATURE_KEY,
    descending_order = defaults.DESCENDING
):
    print("\n\nFor your saved tracks")
    tracks.print_list_of_tracks_sorted_by_feature(
        get_sorted_saved_tracks(limit, selected_feature_key, descending_order),
        selected_feature_key,
        descending_order
    )