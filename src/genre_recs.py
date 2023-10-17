import defaults
import json

DEFAULT_GENRES = ['ska', 'anime']

def get_possible_genres():
    return defaults.SP_CLIENT.recommendation_genre_seeds()

def print_possible_genres():
    print("\n\nGenre recs:\n", json.dumps(get_possible_genres()))

def get_recs_based_on_genres(genres = DEFAULT_GENRES):
    return defaults.SP_CLIENT.recommendations(
        [],
        genres,
        [],
        limit=defaults.TRACK_LIMIT
    )

def print_recs_based_on_genres(genres = DEFAULT_GENRES):
    print(f"\n\nYour recommendations based on {DEFAULT_GENRES} are:")
    recs = get_recs_based_on_genres(genres)
    for idx, track in enumerate(recs['tracks'], start=1):
        defaults.print_track_info(idx, track)