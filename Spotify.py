import random
track_names = []
def get_track():
    with open("tracknames.txt", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        track_names.append(line)

    #print(track_names)
    return random.choice(track_names)