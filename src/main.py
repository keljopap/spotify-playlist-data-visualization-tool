import defaults
import genre_recs
import json
import playlists
import recently_played
import saved_tracks

#saved_tracks.print_saved_tracks_rankings(10, defaults.TRAIT_POPULARITY, True)
#saved_tracks.print_saved_tracks_rankings(10, defaults.TRAIT_DANCEABILITY, True)

#playlists.print_playlists_rankings()

#genre_recs.print_recs_based_on_genres()
#recently_played.print_recently_played(50)

#print(json.dumps(playlists.get_current_user_playlists(defaults.SP_CLIENT, 5), indent=3))

#print(json.dumps(playlists.get_current_user_playlists_to_track_ids(defaults.SP_CLIENT, 5, 5), indent=3))

# Load playlist metadata first, then load it for all the tracks on it afterward
#playlists_no_tracks = playlists.get_current_user_playlists_no_tracks(defaults.SP_CLIENT, 50)
#print(json.dumps(playlists_no_tracks, indent=3))
#playlists.print_playlists_rankings(defaults.TRAIT_TEMPO, True, 50, 50)

#print(json.dumps(playlists.get_current_user_playlists_no_tracks(defaults.SP_CLIENT, 5), indent=2))
#print(json.dumps(playlists.get_current_user_playlists_to_track_ids(defaults.SP_CLIENT, 50, 50), indent=3))
#print(json.dumps(playlists.get_current_user_playlists_to_track_ids_with_audio_features(defaults.SP_CLIENT, 5, 5), indent=2))
playlists.get_current_user_playlists_to_track_ids_with_audio_features(defaults.SP_CLIENT, 5, 5)