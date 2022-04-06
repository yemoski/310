import requests
import random
from random import randrange
import string
import urllib
CLIENT_SECRET = "d81e58a20a5c4e558c614a04aae40361"
CLIENT_ID = "a5f27ad6dc1a4acabff90a9475c715f4"

AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})


# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token(golden)
access_token = auth_response_data['access_token']


# getting a random song from spotify
def get_random_tracks():
    wildcard = f'%{random.choice(string.ascii_lowercase)}%' #a random character from a-z
    query = urllib.parse.quote(wildcard)
    offset = random.randint(0,2000)
    url = f'https://api.spotify.com/v1/search?q={query}&offset={offset}&type=track'
    response = requests.get(url,
                            headers={
                                "Content-Type":"application/json",
                                'Authorization': 'Bearer {token}'.format(token=access_token)
                            }
                            )

    response_json = response.json()
    print(response_json)
    tracks = [
        track for track in response_json['tracks']['items']
    ]
    print(f'Found {len(tracks)} from your search')
    return tracks


random_tracks = get_random_tracks()
#print(get_random_tracks())
track_names = [track['name'] for track in random_tracks]
artist_names = [track['artists'][0]['name'] for track in random_tracks]
print(track_names)
print(artist_names)







with open("tracknames.txt","w", encoding="utf-8") as f:
    for i in track_names:
        f.write(i+"\n")



with open("artistnames.txt","w", encoding="utf-8") as f:
    for i in artist_names:
        f.write(i+"\n")



#