from dotenv import load_dotenv
import os
import spotipy
import time

load_dotenv()

# Define the custom behavior on rate limit
def rate_limited(response, *args, **kwargs):
    print("in the rate limit method with response status code", response.status_code)
    if response.status_code == 429:
        wait_time = int(response.headers.get('Retry-After', 1))
        print(f"Rate limited! Sleeping for {wait_time} seconds.")
        time.sleep(wait_time)

SCOPES = "user-library-read user-read-recently-played" # playlist-read-private"
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')

SP_CLIENT = spotipy.Spotify(
    auth_manager=spotipy.SpotifyOAuth(
        scope=SCOPES,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI
    )
)

# Attach the custom behavior to the Spotipy session
SP_CLIENT._session.hooks['response'].append(rate_limited)
print(SP_CLIENT._session.hooks['response'])

TRAIT_POPULARITY = "popularity"
TRAIT_CUSTOM_ORDER = "custom_order_idx"

SELECTED_FEATURE_KEY = TRAIT_CUSTOM_ORDER
DESCENDING = True

PLAYLIST_LIMIT=1
TRACK_LIMIT=20

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

TRAIT_ACOUSTICNESS, TRAIT_DANCEABILITY, TRAIT_DURATION_MS = "acousticness", "danceability", "duration_ms"
TRAIT_ENERGY, TRAIT_INSTRUMENTALNESS, TRAIT_KEY = "energy", "instrumentalness", "key"
TRAIT_LIVENESS, TRAIT_LOUDNESS, TRAIT_SPEECHINESS = "liveness", "loudness", "speechiness"
TRAIT_TEMPO, TRAIT_TIME_SIGNATURE, TRAIT_VALENCE = "tempo", "time_signature", "valence"

# Source: https://developer.spotify.com/documentation/web-api/reference/get-audio-features
AUDIO_FEATURES = {
    TRAIT_ACOUSTICNESS: "A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.",
    TRAIT_DANCEABILITY: "Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.",
    TRAIT_DURATION_MS: "The duration of the track in milliseconds.",
    TRAIT_ENERGY: "Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.",
    TRAIT_INSTRUMENTALNESS: "Predicts whether a track contains no vocals. \"Ooh\" and \"aah\" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly \"vocal\". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.",
    TRAIT_KEY: "The key the track is in. Integers map to pitches using standard Pitch Class notation. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1.",
    TRAIT_LIVENESS: "Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.",
    TRAIT_LOUDNESS: "The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typically range between -60 and 0 db.",
    TRAIT_SPEECHINESS: "Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.",
    TRAIT_TEMPO: "The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.",
    TRAIT_TIME_SIGNATURE: "An estimated time signature. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure). The time signature ranges from 3 to 7 indicating time signatures of \"3/4\", to \"7/4\".",
    TRAIT_VALENCE: "A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry)."
}

AUDIO_FEATURE_KEYS = AUDIO_FEATURES.keys()
POSSIBLE_SORT_KEYS = [
    TRAIT_CUSTOM_ORDER,
    TRAIT_POPULARITY,
    *AUDIO_FEATURE_KEYS
]

def select_feature_to_sort_by():
    print("Select a trait to sort by:")
    for idx, key in enumerate(AUDIO_FEATURE_KEYS, start=1):
        print(f"{idx}. {key}")

    selection = int(input())
    return AUDIO_FEATURE_KEYS[selection - 1]

def sort_by_descending():
    order = input("Sort in descending order (y/n)? ")
    return order.lower() == "y"

def print_track_info(idx, track):
    artist = track['artists'][0]['name']
    album = track['album']['name']
    print(f"{idx}. {track['name']} - {artist} - {album}")