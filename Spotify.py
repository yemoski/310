import random
track_names = []
artist_names = []
index =0



def get_randindex():
    global index
    index= random.randint(0, 19)

def get_track():

    with open("tracknames.txt", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        track_names.append(line)

    print(track_names)
    return track_names[index]

def get_artist_name():
    with open("artistnames.txt", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        artist_names.append(line)

    print(artist_names)
    return artist_names[index]

get_randindex()
print(get_artist_name())
print(get_track())