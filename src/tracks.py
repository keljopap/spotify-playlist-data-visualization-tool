import defaults

# Get track metadata
def get_tracks_from_ids(
    sp = defaults.SP_CLIENT,
    track_ids = []
):
    tracks_by_ids = {}
    tracks = sp.tracks(track_ids)
    for track in tracks['tracks']:
        tracks_by_ids[track['id']] = {
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'album': track['album']['name'],
            'popularity': track['popularity']/100
        }
    return tracks_by_ids

# Takes a list of track ids, returns a map of them to their audio features
def get_tracks_by_features(
    sp = defaults.SP_CLIENT,
    track_ids = [],
    limit=5
):
    audio_features_by_track = sp.audio_features(track_ids)
    ids_to_features = {}
    for tfs in audio_features_by_track:
        ids_to_features[tfs['id']] = {}
        for fk in defaults.FEATURE_KEYS:
            ids_to_features[tfs['id']][fk] = tfs[fk]
    return ids_to_features

def get_sorted_tracks_by_feature(
    tracks_to_features = {},
    selected_feature_key="energy",
    descending=True
):
    sorted_tracks = sorted(
        tracks_to_features.values(),
        key=lambda x: x['audio_features'][selected_feature_key],
        reverse=descending
    )
    return sorted_tracks

# Print the sorted list with song names and their artists
def print_list_of_tracks_sorted_by_feature(
    sorted_tracks,
    selected_feature_key,
    desc=True
):
    print("Your first", len(sorted_tracks), "tracks sorted by", selected_feature_key, "(desc)" if desc == True else "(asc)")
    for idx, track in enumerate(sorted_tracks, start=1):
        if selected_feature_key not in defaults.FEATURE_KEYS:
            print(f"Invalid feature key \"{selected_feature_key}\", must be one of \"{defaults.FEATURE_KEYS}\"")
            break

        measure = track['audio_features'][selected_feature_key]
        if selected_feature_key == "key":
            measure = defaults.KEY_MAPPINGS[measure]
        elif selected_feature_key == "duration_ms":
            minutes, seconds = defaults.ms_to_min_sec(measure)
            measure = f"{minutes}:{seconds}"

        print(f"{idx}. [{measure}] {track['name']} - {track['artist']}    (Popularity: {track['popularity']})")
