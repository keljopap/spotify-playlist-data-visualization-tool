import plotly.graph_objects as go

tracks = [
   {
      "name": "Hunnybee",
      "artist": "Unknown Mortal Orchestra",
      "album": "Sex & Food",
      "popularity": 0.0,
      "custom_order_idx": 46,
      "audio_features": {
         "acousticness": 0.569,
         "danceability": 0.956,
         "duration_ms": 268333,
         "energy": 0.373,
         "instrumentalness": 0.394,
         "key": 6,
         "liveness": 0.314,
         "loudness": -7.963,
         "speechiness": 0.0773,
         "tempo": 119.994,
         "time_signature": 4,
         "valence": 0.568
      }
   },
   {
      "name": "Cool It Now",
      "artist": "New Edition",
      "album": "New Edition",
      "popularity": 0.55,
      "custom_order_idx": 9,
      "audio_features": {
         "acousticness": 0.126,
         "danceability": 0.871,
         "duration_ms": 347667,
         "energy": 0.532,
         "instrumentalness": 0.00819,
         "key": 10,
         "liveness": 0.321,
         "loudness": -13.335,
         "speechiness": 0.0677,
         "tempo": 116.574,
         "time_signature": 4,
         "valence": 0.74
      }
   },
   {
      "name": "Eye In The Sky",
      "artist": "The Alan Parsons Project",
      "album": "Eye In The Sky (Expanded Edition)",
      "popularity": 0.74,
      "custom_order_idx": 24,
      "audio_features": {
         "acousticness": 0.562,
         "danceability": 0.823,
         "duration_ms": 276280,
         "energy": 0.417,
         "instrumentalness": 0.00098,
         "key": 2,
         "liveness": 0.0765,
         "loudness": -12.643,
         "speechiness": 0.032,
         "tempo": 111.928,
         "time_signature": 4,
         "valence": 0.522
      }
   },
   {
      "name": "Tired of Being Alone",
      "artist": "Al Green",
      "album": "Gets Next to You",
      "popularity": 0.72,
      "custom_order_idx": 10,
      "audio_features": {
         "acousticness": 0.339,
         "danceability": 0.772,
         "duration_ms": 172320,
         "energy": 0.397,
         "instrumentalness": 0.00541,
         "key": 7,
         "liveness": 0.0753,
         "loudness": -8.585,
         "speechiness": 0.0391,
         "tempo": 97.964,
         "time_signature": 4,
         "valence": 0.617
      }
   },
   {
      "name": "Home",
      "artist": "LCD Soundsystem",
      "album": "This Is Happening",
      "popularity": 0.54,
      "custom_order_idx": 2,
      "audio_features": {
         "acousticness": 0.0462,
         "danceability": 0.752,
         "duration_ms": 473333,
         "energy": 0.844,
         "instrumentalness": 0.131,
         "key": 9,
         "liveness": 0.0782,
         "loudness": -8.705,
         "speechiness": 0.0398,
         "tempo": 124.013,
         "time_signature": 4,
         "valence": 0.78
      }
   },
   {
      "name": "Bright Star",
      "artist": "Ana\u00efs Mitchell",
      "album": "Ana\u00efs Mitchell",
      "popularity": 0.55,
      "custom_order_idx": 30,
      "audio_features": {
         "acousticness": 0.618,
         "danceability": 0.712,
         "duration_ms": 190587,
         "energy": 0.348,
         "instrumentalness": 0.000206,
         "key": 1,
         "liveness": 0.107,
         "loudness": -8.808,
         "speechiness": 0.0402,
         "tempo": 99.144,
         "time_signature": 4,
         "valence": 0.321
      }
   },
   {
      "name": "Everybody Everybody",
      "artist": "Black Box",
      "album": "Dreamland",
      "popularity": 0.6,
      "custom_order_idx": 33,
      "audio_features": {
         "acousticness": 0.00363,
         "danceability": 0.712,
         "duration_ms": 247002,
         "energy": 0.785,
         "instrumentalness": 6.95e-06,
         "key": 5,
         "liveness": 0.0878,
         "loudness": -6.418,
         "speechiness": 0.0386,
         "tempo": 117.643,
         "time_signature": 4,
         "valence": 0.975
      }
   },
   {
      "name": "Love You For A Long Time",
      "artist": "Maggie Rogers",
      "album": "Love You For A Long Time",
      "popularity": 0.7,
      "custom_order_idx": 48,
      "audio_features": {
         "acousticness": 0.164,
         "danceability": 0.707,
         "duration_ms": 223120,
         "energy": 0.67,
         "instrumentalness": 0.00283,
         "key": 9,
         "liveness": 0.109,
         "loudness": -6.137,
         "speechiness": 0.0323,
         "tempo": 112.993,
         "time_signature": 4,
         "valence": 0.822
      }
   },
   {
      "name": "Here (In Your Arms)",
      "artist": "Hellogoodbye",
      "album": "Zombies! Aliens! Vampires! Dinosaurs!",
      "popularity": 0.0,
      "custom_order_idx": 34,
      "audio_features": {
         "acousticness": 0.206,
         "danceability": 0.701,
         "duration_ms": 240547,
         "energy": 0.608,
         "instrumentalness": 0.0041,
         "key": 5,
         "liveness": 0.273,
         "loudness": -6.819,
         "speechiness": 0.0374,
         "tempo": 126.044,
         "time_signature": 4,
         "valence": 0.794
      }
   },
   {
      "name": "Another Way",
      "artist": "Ten F\u00e9",
      "album": "Hit the Light",
      "popularity": 0.37,
      "custom_order_idx": 7,
      "audio_features": {
         "acousticness": 0.118,
         "danceability": 0.7,
         "duration_ms": 254410,
         "energy": 0.362,
         "instrumentalness": 0.128,
         "key": 5,
         "liveness": 0.118,
         "loudness": -6.979,
         "speechiness": 0.0302,
         "tempo": 97.999,
         "time_signature": 4,
         "valence": 0.446
      }
   },
   {
      "name": "Out Loud",
      "artist": "Remember Sports",
      "album": "Like a Stone",
      "popularity": 0.38,
      "custom_order_idx": 41,
      "audio_features": {
         "acousticness": 0.284,
         "danceability": 0.696,
         "duration_ms": 409283,
         "energy": 0.699,
         "instrumentalness": 0.0029,
         "key": 11,
         "liveness": 0.336,
         "loudness": -8.676,
         "speechiness": 0.0399,
         "tempo": 100.796,
         "time_signature": 4,
         "valence": 0.57
      }
   },
   {
      "name": "Forever (feat. Joseph Chilliams & Ravyn Lenae)",
      "artist": "Noname",
      "album": "Telefone",
      "popularity": 0.0,
      "custom_order_idx": 40,
      "audio_features": {
         "acousticness": 0.571,
         "danceability": 0.672,
         "duration_ms": 218627,
         "energy": 0.655,
         "instrumentalness": 0,
         "key": 6,
         "liveness": 0.188,
         "loudness": -9.768,
         "speechiness": 0.469,
         "tempo": 113.74,
         "time_signature": 5,
         "valence": 0.906
      }
   },
   {
      "name": "Moon (And It Went Like)",
      "artist": "Kid Francescoli",
      "album": "Play Me Again",
      "popularity": 0.66,
      "custom_order_idx": 1,
      "audio_features": {
         "acousticness": 0.289,
         "danceability": 0.662,
         "duration_ms": 390639,
         "energy": 0.657,
         "instrumentalness": 0.868,
         "key": 7,
         "liveness": 0.103,
         "loudness": -10.002,
         "speechiness": 0.0345,
         "tempo": 117.986,
         "time_signature": 4,
         "valence": 0.0563
      }
   },
   {
      "name": "Best to You",
      "artist": "Blood Orange",
      "album": "Freetown Sound",
      "popularity": 0.55,
      "custom_order_idx": 29,
      "audio_features": {
         "acousticness": 0.181,
         "danceability": 0.658,
         "duration_ms": 225748,
         "energy": 0.785,
         "instrumentalness": 0.00223,
         "key": 0,
         "liveness": 0.724,
         "loudness": -8.513,
         "speechiness": 0.036,
         "tempo": 125.015,
         "time_signature": 4,
         "valence": 0.345
      }
   },
   {
      "name": "I Know There's Gonna Be (Good Times)",
      "artist": "Jamie xx",
      "album": "In Colour",
      "popularity": 0.55,
      "custom_order_idx": 28,
      "audio_features": {
         "acousticness": 0.12,
         "danceability": 0.657,
         "duration_ms": 213622,
         "energy": 0.597,
         "instrumentalness": 0,
         "key": 11,
         "liveness": 0.477,
         "loudness": -9.919,
         "speechiness": 0.168,
         "tempo": 89.606,
         "time_signature": 4,
         "valence": 0.486
      }
   },
   {
      "name": "Comin' Home",
      "artist": "City and Colour",
      "album": "Sometimes",
      "popularity": 0.55,
      "custom_order_idx": 37,
      "audio_features": {
         "acousticness": 0.792,
         "danceability": 0.654,
         "duration_ms": 305413,
         "energy": 0.539,
         "instrumentalness": 0,
         "key": 6,
         "liveness": 0.12,
         "loudness": -5.828,
         "speechiness": 0.0309,
         "tempo": 122.923,
         "time_signature": 4,
         "valence": 0.392
      }
   },
   {
      "name": "golden arm",
      "artist": "Sadurn",
      "album": "Radiator",
      "popularity": 0.34,
      "custom_order_idx": 3,
      "audio_features": {
         "acousticness": 0.843,
         "danceability": 0.61,
         "duration_ms": 244989,
         "energy": 0.18,
         "instrumentalness": 0.00913,
         "key": 2,
         "liveness": 0.0872,
         "loudness": -14.843,
         "speechiness": 0.0307,
         "tempo": 130.16,
         "time_signature": 4,
         "valence": 0.23
      }
   },
   {
      "name": "We Will Become Silhouettes - Remastered",
      "artist": "The Postal Service",
      "album": "Give Up (Deluxe 10th Anniversary Edition)",
      "popularity": 0.54,
      "custom_order_idx": 18,
      "audio_features": {
         "acousticness": 0.0798,
         "danceability": 0.606,
         "duration_ms": 300547,
         "energy": 0.555,
         "instrumentalness": 0.0712,
         "key": 2,
         "liveness": 0.12,
         "loudness": -8.418,
         "speechiness": 0.0319,
         "tempo": 155.031,
         "time_signature": 4,
         "valence": 0.155
      }
   },
   {
      "name": "Portland, Maine",
      "artist": "Donovan Woods",
      "album": "Hard Settle, Ain't Troubled",
      "popularity": 0.66,
      "custom_order_idx": 19,
      "audio_features": {
         "acousticness": 0.764,
         "danceability": 0.606,
         "duration_ms": 203870,
         "energy": 0.349,
         "instrumentalness": 0.306,
         "key": 4,
         "liveness": 0.112,
         "loudness": -13.967,
         "speechiness": 0.0319,
         "tempo": 80.071,
         "time_signature": 4,
         "valence": 0.156
      }
   },
   {
      "name": "Here You Come Again",
      "artist": "Dolly Parton",
      "album": "Here You Come Again",
      "popularity": 0.67,
      "custom_order_idx": 35,
      "audio_features": {
         "acousticness": 0.647,
         "danceability": 0.585,
         "duration_ms": 179491,
         "energy": 0.511,
         "instrumentalness": 0.007,
         "key": 1,
         "liveness": 0.0392,
         "loudness": -9.37,
         "speechiness": 0.0391,
         "tempo": 105.898,
         "time_signature": 4,
         "valence": 0.552
      }
   },
   {
      "name": "Hometown",
      "artist": "Sarah Jarosz",
      "album": "World On The Ground",
      "popularity": 0.45,
      "custom_order_idx": 8,
      "audio_features": {
         "acousticness": 0.853,
         "danceability": 0.584,
         "duration_ms": 180240,
         "energy": 0.273,
         "instrumentalness": 0.000109,
         "key": 9,
         "liveness": 0.102,
         "loudness": -12.806,
         "speechiness": 0.0357,
         "tempo": 149.757,
         "time_signature": 4,
         "valence": 0.47
      }
   },
   {
      "name": "If It Means A Lot To You",
      "artist": "A Day To Remember",
      "album": "Homesick",
      "popularity": 0.71,
      "custom_order_idx": 45,
      "audio_features": {
         "acousticness": 0.112,
         "danceability": 0.584,
         "duration_ms": 243227,
         "energy": 0.536,
         "instrumentalness": 0,
         "key": 10,
         "liveness": 0.456,
         "loudness": -8.158,
         "speechiness": 0.0279,
         "tempo": 127.001,
         "time_signature": 4,
         "valence": 0.441
      }
   },
   {
      "name": "good 4 u",
      "artist": "Olivia Rodrigo",
      "album": "SOUR",
      "popularity": 0.87,
      "custom_order_idx": 36,
      "audio_features": {
         "acousticness": 0.335,
         "danceability": 0.563,
         "duration_ms": 178147,
         "energy": 0.664,
         "instrumentalness": 0,
         "key": 9,
         "liveness": 0.0849,
         "loudness": -5.044,
         "speechiness": 0.154,
         "tempo": 166.928,
         "time_signature": 4,
         "valence": 0.688
      }
   },
   {
      "name": "Love And Affection",
      "artist": "Joan Armatrading",
      "album": "Joan Armatrading",
      "popularity": 0.47,
      "custom_order_idx": 22,
      "audio_features": {
         "acousticness": 0.724,
         "danceability": 0.559,
         "duration_ms": 272333,
         "energy": 0.276,
         "instrumentalness": 5.29e-05,
         "key": 4,
         "liveness": 0.0977,
         "loudness": -13.862,
         "speechiness": 0.0286,
         "tempo": 93.525,
         "time_signature": 4,
         "valence": 0.4
      }
   },
   {
      "name": "Wake Up",
      "artist": "Coheed and Cambria",
      "album": "Good Apollo I'm Burning Star IV Volume One: From Fear Through The Eyes Of Madness",
      "popularity": 0.5,
      "custom_order_idx": 44,
      "audio_features": {
         "acousticness": 0.593,
         "danceability": 0.559,
         "duration_ms": 215947,
         "energy": 0.44,
         "instrumentalness": 3.81e-06,
         "key": 11,
         "liveness": 0.402,
         "loudness": -9.273,
         "speechiness": 0.0312,
         "tempo": 72.015,
         "time_signature": 4,
         "valence": 0.483
      }
   },
   {
      "name": "That Funny Feeling",
      "artist": "Bo Burnham",
      "album": "Inside (The Songs)",
      "popularity": 0.0,
      "custom_order_idx": 50,
      "audio_features": {
         "acousticness": 0.764,
         "danceability": 0.545,
         "duration_ms": 301111,
         "energy": 0.277,
         "instrumentalness": 0,
         "key": 4,
         "liveness": 0.372,
         "loudness": -11.7,
         "speechiness": 0.0392,
         "tempo": 75.763,
         "time_signature": 4,
         "valence": 0.389
      }
   },
   {
      "name": "IOWA",
      "artist": "Aoife O'Donovan",
      "album": "The Apathy Sessions",
      "popularity": 0.0,
      "custom_order_idx": 20,
      "audio_features": {
         "acousticness": 0.761,
         "danceability": 0.528,
         "duration_ms": 275171,
         "energy": 0.287,
         "instrumentalness": 0.000406,
         "key": 1,
         "liveness": 0.206,
         "loudness": -10.812,
         "speechiness": 0.0308,
         "tempo": 96.035,
         "time_signature": 4,
         "valence": 0.224
      }
   },
   {
      "name": "Here and Heaven",
      "artist": "Stuart Duncan",
      "album": "The Goat Rodeo Sessions",
      "popularity": 0.36,
      "custom_order_idx": 27,
      "audio_features": {
         "acousticness": 0.93,
         "danceability": 0.525,
         "duration_ms": 233413,
         "energy": 0.233,
         "instrumentalness": 0.0205,
         "key": 2,
         "liveness": 0.138,
         "loudness": -12.789,
         "speechiness": 0.0347,
         "tempo": 123.655,
         "time_signature": 4,
         "valence": 0.424
      }
   },
   {
      "name": "Eighteen",
      "artist": "Joyce Manor",
      "album": "Cody",
      "popularity": 0.48,
      "custom_order_idx": 43,
      "audio_features": {
         "acousticness": 0.0032,
         "danceability": 0.524,
         "duration_ms": 125467,
         "energy": 0.947,
         "instrumentalness": 0,
         "key": 9,
         "liveness": 0.0804,
         "loudness": -1.331,
         "speechiness": 0.0536,
         "tempo": 97.576,
         "time_signature": 4,
         "valence": 0.415
      }
   },
   {
      "name": "ceilings",
      "artist": "Lizzy McAlpine",
      "album": "five seconds flat",
      "popularity": 0.86,
      "custom_order_idx": 21,
      "audio_features": {
         "acousticness": 0.473,
         "danceability": 0.516,
         "duration_ms": 182888,
         "energy": 0.322,
         "instrumentalness": 0.00194,
         "key": 9,
         "liveness": 0.215,
         "loudness": -11.762,
         "speechiness": 0.0292,
         "tempo": 148.005,
         "time_signature": 3,
         "valence": 0.261
      }
   },
   {
      "name": "Not Strong Enough",
      "artist": "boygenius",
      "album": "the record",
      "popularity": 0.77,
      "custom_order_idx": 14,
      "audio_features": {
         "acousticness": 0.00261,
         "danceability": 0.508,
         "duration_ms": 234933,
         "energy": 0.797,
         "instrumentalness": 7.56e-06,
         "key": 1,
         "liveness": 0.0916,
         "loudness": -5.854,
         "speechiness": 0.0411,
         "tempo": 126.982,
         "time_signature": 4,
         "valence": 0.361
      }
   },
   {
      "name": "The Remedy (I Won't Worry) - Live at the Charter One Pavilion, Chicago, IL, 8/13/2009",
      "artist": "Jason Mraz",
      "album": "Jason Mraz's Beautiful Mess: Live on Earth",
      "popularity": 0.29,
      "custom_order_idx": 26,
      "audio_features": {
         "acousticness": 0.0832,
         "danceability": 0.497,
         "duration_ms": 381640,
         "energy": 0.882,
         "instrumentalness": 0,
         "key": 7,
         "liveness": 0.929,
         "loudness": -4.047,
         "speechiness": 0.0658,
         "tempo": 87.27,
         "time_signature": 4,
         "valence": 0.737
      }
   },
   {
      "name": "Trying to Feel Alive",
      "artist": "Porter Robinson",
      "album": "Nurture",
      "popularity": 0.47,
      "custom_order_idx": 12,
      "audio_features": {
         "acousticness": 0.344,
         "danceability": 0.494,
         "duration_ms": 279693,
         "energy": 0.533,
         "instrumentalness": 0.00297,
         "key": 6,
         "liveness": 0.11,
         "loudness": -8.183,
         "speechiness": 0.0368,
         "tempo": 108.007,
         "time_signature": 4,
         "valence": 0.41
      }
   },
   {
      "name": "Enough Is Enough",
      "artist": "Post Malone",
      "album": "AUSTIN",
      "popularity": 0.81,
      "custom_order_idx": 5,
      "audio_features": {
         "acousticness": 0.014,
         "danceability": 0.483,
         "duration_ms": 165175,
         "energy": 0.768,
         "instrumentalness": 0,
         "key": 0,
         "liveness": 0.109,
         "loudness": -4.911,
         "speechiness": 0.0344,
         "tempo": 166.061,
         "time_signature": 4,
         "valence": 0.332
      }
   },
   {
      "name": "Something Comforting",
      "artist": "Porter Robinson",
      "album": "Nurture",
      "popularity": 0.57,
      "custom_order_idx": 11,
      "audio_features": {
         "acousticness": 0.0448,
         "danceability": 0.474,
         "duration_ms": 281974,
         "energy": 0.558,
         "instrumentalness": 3.79e-06,
         "key": 8,
         "liveness": 0.0806,
         "loudness": -9.688,
         "speechiness": 0.0298,
         "tempo": 143.992,
         "time_signature": 4,
         "valence": 0.291
      }
   },
   {
      "name": "Hands Down",
      "artist": "Dashboard Confessional",
      "album": "A Mark, A Mission, A Brand, A Scar",
      "popularity": 0.66,
      "custom_order_idx": 17,
      "audio_features": {
         "acousticness": 0.013,
         "danceability": 0.463,
         "duration_ms": 186867,
         "energy": 0.827,
         "instrumentalness": 2.41e-05,
         "key": 3,
         "liveness": 0.0964,
         "loudness": -4.085,
         "speechiness": 0.0437,
         "tempo": 94.035,
         "time_signature": 4,
         "valence": 0.26
      }
   },
   {
      "name": "Always",
      "artist": "blink-182",
      "album": "blink-182",
      "popularity": 0.67,
      "custom_order_idx": 39,
      "audio_features": {
         "acousticness": 0.0106,
         "danceability": 0.463,
         "duration_ms": 251867,
         "energy": 0.925,
         "instrumentalness": 0.027,
         "key": 11,
         "liveness": 0.189,
         "loudness": -5.74,
         "speechiness": 0.0747,
         "tempo": 158.337,
         "time_signature": 4,
         "valence": 0.59
      }
   },
   {
      "name": "Sweet Time",
      "artist": "Porter Robinson",
      "album": "Nurture",
      "popularity": 0.47,
      "custom_order_idx": 4,
      "audio_features": {
         "acousticness": 0.192,
         "danceability": 0.457,
         "duration_ms": 251510,
         "energy": 0.728,
         "instrumentalness": 0.0292,
         "key": 2,
         "liveness": 0.0944,
         "loudness": -8.625,
         "speechiness": 0.0497,
         "tempo": 84.976,
         "time_signature": 4,
         "valence": 0.439
      }
   },
   {
      "name": "Flowers Never Bend with the Rainfall",
      "artist": "Simon & Garfunkel",
      "album": "Parsley, Sage, Rosemary And Thyme",
      "popularity": 0.54,
      "custom_order_idx": 6,
      "audio_features": {
         "acousticness": 0.656,
         "danceability": 0.425,
         "duration_ms": 131747,
         "energy": 0.34,
         "instrumentalness": 0,
         "key": 9,
         "liveness": 0.127,
         "loudness": -14.176,
         "speechiness": 0.0357,
         "tempo": 110.208,
         "time_signature": 4,
         "valence": 0.488
      }
   },
   {
      "name": "I Miss You",
      "artist": "blink-182",
      "album": "blink-182",
      "popularity": 0.79,
      "custom_order_idx": 25,
      "audio_features": {
         "acousticness": 0.00113,
         "danceability": 0.423,
         "duration_ms": 227250,
         "energy": 0.714,
         "instrumentalness": 6.28e-06,
         "key": 11,
         "liveness": 0.0855,
         "loudness": -8.295,
         "speechiness": 0.045,
         "tempo": 110.017,
         "time_signature": 4,
         "valence": 0.593
      }
   },
   {
      "name": "erase me",
      "artist": "Lizzy McAlpine",
      "album": "five seconds flat",
      "popularity": 0.6,
      "custom_order_idx": 15,
      "audio_features": {
         "acousticness": 0.578,
         "danceability": 0.415,
         "duration_ms": 214468,
         "energy": 0.45,
         "instrumentalness": 2.82e-05,
         "key": 6,
         "liveness": 0.155,
         "loudness": -8.529,
         "speechiness": 0.0599,
         "tempo": 93.17,
         "time_signature": 4,
         "valence": 0.305
      }
   },
   {
      "name": "doomsday",
      "artist": "Lizzy McAlpine",
      "album": "five seconds flat",
      "popularity": 0.69,
      "custom_order_idx": 13,
      "audio_features": {
         "acousticness": 0.583,
         "danceability": 0.404,
         "duration_ms": 268433,
         "energy": 0.268,
         "instrumentalness": 0,
         "key": 1,
         "liveness": 0.102,
         "loudness": -9.631,
         "speechiness": 0.0341,
         "tempo": 134.587,
         "time_signature": 3,
         "valence": 0.124
      }
   },
   {
      "name": "Good Thoughts, Bad Thoughts",
      "artist": "Funkadelic",
      "album": "Standing On The Verge Of Getting It On",
      "popularity": 0.43,
      "custom_order_idx": 32,
      "audio_features": {
         "acousticness": 0.934,
         "danceability": 0.398,
         "duration_ms": 737131,
         "energy": 0.306,
         "instrumentalness": 0.0121,
         "key": 4,
         "liveness": 0.215,
         "loudness": -17.293,
         "speechiness": 0.0363,
         "tempo": 108.145,
         "time_signature": 3,
         "valence": 0.293
      }
   },
   {
      "name": "Hallelujah",
      "artist": "Paramore",
      "album": "Riot!",
      "popularity": 0.51,
      "custom_order_idx": 38,
      "audio_features": {
         "acousticness": 0.000787,
         "danceability": 0.396,
         "duration_ms": 203640,
         "energy": 0.863,
         "instrumentalness": 1.95e-06,
         "key": 11,
         "liveness": 0.279,
         "loudness": -2.646,
         "speechiness": 0.0453,
         "tempo": 150.778,
         "time_signature": 4,
         "valence": 0.438
      }
   },
   {
      "name": "Constant Nothing",
      "artist": "Joyce Manor",
      "album": "S/T",
      "popularity": 0.37,
      "custom_order_idx": 42,
      "audio_features": {
         "acousticness": 0.000531,
         "danceability": 0.376,
         "duration_ms": 84653,
         "energy": 0.994,
         "instrumentalness": 0.00205,
         "key": 1,
         "liveness": 0.236,
         "loudness": -3.65,
         "speechiness": 0.124,
         "tempo": 108.794,
         "time_signature": 4,
         "valence": 0.0908
      }
   },
   {
      "name": "Keep on Raging",
      "artist": "Julie Byrne",
      "album": "Rooms With Walls and Windows",
      "popularity": 0.25,
      "custom_order_idx": 16,
      "audio_features": {
         "acousticness": 0.935,
         "danceability": 0.349,
         "duration_ms": 197893,
         "energy": 0.261,
         "instrumentalness": 0.151,
         "key": 11,
         "liveness": 0.113,
         "loudness": -15.422,
         "speechiness": 0.0301,
         "tempo": 132.489,
         "time_signature": 4,
         "valence": 0.26
      }
   },
   {
      "name": "Aphasia",
      "artist": "Pinegrove",
      "album": "Cardinal",
      "popularity": 0.0,
      "custom_order_idx": 49,
      "audio_features": {
         "acousticness": 0.77,
         "danceability": 0.309,
         "duration_ms": 270933,
         "energy": 0.482,
         "instrumentalness": 7.06e-06,
         "key": 6,
         "liveness": 0.235,
         "loudness": -7.991,
         "speechiness": 0.0422,
         "tempo": 66.749,
         "time_signature": 4,
         "valence": 0.349
      }
   },
   {
      "name": "A",
      "artist": "Cartel",
      "album": "Chroma",
      "popularity": 0.29,
      "custom_order_idx": 23,
      "audio_features": {
         "acousticness": 0.000624,
         "danceability": 0.278,
         "duration_ms": 585053,
         "energy": 0.931,
         "instrumentalness": 0.0204,
         "key": 8,
         "liveness": 0.0501,
         "loudness": -5.96,
         "speechiness": 0.0777,
         "tempo": 130.123,
         "time_signature": 4,
         "valence": 0.26
      }
   },
   {
      "name": "Brooklyn Bridge",
      "artist": "Ana\u00efs Mitchell",
      "album": "Ana\u00efs Mitchell",
      "popularity": 0.3,
      "custom_order_idx": 31,
      "audio_features": {
         "acousticness": 0.82,
         "danceability": 0.272,
         "duration_ms": 258760,
         "energy": 0.201,
         "instrumentalness": 0.203,
         "key": 8,
         "liveness": 0.209,
         "loudness": -15.293,
         "speechiness": 0.0399,
         "tempo": 165.508,
         "time_signature": 4,
         "valence": 0.0696
      }
   },
   {
      "name": "Saturday",
      "artist": "Remember Sports",
      "album": "All of Something",
      "popularity": 0.0,
      "custom_order_idx": 47,
      "audio_features": {
         "acousticness": 0.0066,
         "danceability": 0.202,
         "duration_ms": 73835,
         "energy": 0.945,
         "instrumentalness": 0.514,
         "key": 9,
         "liveness": 0.464,
         "loudness": -4.908,
         "speechiness": 0.251,
         "tempo": 193.252,
         "time_signature": 4,
         "valence": 0.719
      }
   }
]

POPULARITY = "popularity"
CUSTOM_ORDER_INDEX = "custom_order_idx"
song_names = [track["name"][:25] + " - " + track["artist"] for track in tracks]
custom_order_indices = [track[CUSTOM_ORDER_INDEX] for track in tracks]
popularity = [track[POPULARITY] for track in tracks]
audio_features = list(tracks[0]["audio_features"].keys())

fig = go.Figure(
    go.Bar(
        x=song_names,
        y=popularity,
        name="Popularity"
    )
)

feature_dropdown = [
    {
        "label": "Popularity",
        "method": "update",
        "args": [
            {"y": [popularity], "name": ["Popularity"]},
            {"title": "Popularity"}
        ]
    }
]

feature_dropdown.append(
   {
      "label": CUSTOM_ORDER_INDEX,
      "method": "update",
      "args": [
            {"y": [custom_order_indices], "name": [CUSTOM_ORDER_INDEX]},
            {"title": "Default Playlist Index"}
      ]
   }
)

for feature in audio_features:
    feature_values = [track["audio_features"][feature] for track in tracks]
    feature_dropdown.append(
        {
            "label": feature,
            "method": "update",
            "args": [
                {"y": [feature_values], "name": [feature]},
                {"title": feature}
            ]
        }
    )

fig.update_layout(
    updatemenus=[
        {
            "buttons": feature_dropdown,
            "direction": "down",
            "pad": {"r": 10, "t": 10},
            "showactive": True,
            "x": 0.1,
            "xanchor": "left",
            "y": 1.15,
            "yanchor": "top"
        }
    ]
)

fig.show()
