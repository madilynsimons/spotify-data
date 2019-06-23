import json
from random import randint

class Song:
    def __init__(self):
        self.endTime = None
        self.artistName = None
        self.trackName = None
        self.msPlayed = None

def get_songs():
    filename = "001-1245272821/StreamingHistory.json"

    with open(filename, "r") as f:
        datastore = json.load(f)

    songs = []
    for s in datastore:
        song = Song()
        song.endTime = str(s["endTime"])
        song.artistName = str(s["artistName"])
        song.trackName = str(s["trackName"])
        song.msPlayed = int(s["msPlayed"])
        songs.append(song)
    return songs

def ms_to_time(millis):
    seconds=(millis/1000)%60
    seconds = int(seconds)
    minutes=(millis/(1000*60))%60
    minutes = int(minutes)
    hours=(millis/(1000*60*60))%24

    ret = "%d:%d:%d" % (hours, minutes, seconds)
    return ret

def time_listened(songs, artist):
    millis = 0
    for song in songs:
        if song.artistName == artist:
            millis += song.msPlayed

    return ms_to_time(millis)

def get_time_by_artist(songs):
    ret = {}
    for song in songs:
        if not song.artistName in ret:
            ret[song.artistName] = song.msPlayed
        else:
            ret[song.artistName] += song.msPlayed
    return ret;

def add_to_list(artist, top_ten):
    msPlayed = artist[1]
    i = 0
    while i < 10:
        if msPlayed > top_ten[i][1]:
            top_ten.insert(i, artist)
            top_ten.remove(top_ten[10])
            return
        i += 1

def sort_by_time(artists):
    n = len(artists)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if artists[j][1] > artists[j+1][1] :
                artists[j], artists[j+1] = artists[j+1], artists[j]
    return artists

def top_ten(artist_time):
    top_ten = []
    i = 0

    artists = []
    podcasts = ['Sleep With Me', 'Tmsoft’s White Noise Sleep Sounds', 'Chapo Trap House', "And That's Why We Drink", "Natural Sound Selections", "Granular"]
    for artist, time in artist_time.items():
        artists.append([artist, time])

    artists = sort_by_time(artists)

    while i < 10:
        top_ten.append(artists[i])
        i += 1

    while i < len(artists):
        if artists[i][0] in podcasts:
            i+=1
            continue
        if artists[i][1] > top_ten[9][1]:
            add_to_list(artists[i], top_ten)
        i += 1
    return top_ten

def main():
    songs = get_songs()
    t = get_time_by_artist(songs)
    print(top_ten(t))


if __name__ == "__main__":
    main()
