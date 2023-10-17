import defaults

def get_recently_played(limit = defaults.TRACK_LIMIT):
    return defaults.SP_CLIENT.current_user_recently_played(limit)

def print_recently_played(limit = defaults.TRACK_LIMIT):
    print("\n\nMost recently listened to songs:")
    recently_played_tracks = get_recently_played(limit)
    for idx, item in enumerate(recently_played_tracks['items'], start=1):
        defaults.print_track_info(idx, item['track'])