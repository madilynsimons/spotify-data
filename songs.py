import json

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
