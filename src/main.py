import defaults
import genre_recs
import playlists
import recently_played
import saved_tracks

for sort_key in defaults.POSSIBLE_SORT_KEYS:
    saved_tracks.print_saved_tracks_rankings(10, sort_key, True)

playlists.print_playlists_rankings()

genre_recs.print_recs_based_on_genres()
recently_played.print_recently_played()