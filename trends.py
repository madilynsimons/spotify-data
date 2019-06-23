from songs import *
from artists import *
from datetime import datetime

def save_trend(by_day, artist):
    filename = "trends/" + artist.replace(" ","") + ".csv"
    fp = open(filename, "w")
    for day in sorted(by_day.keys()):
        fp.write("%d,%d\n" % (day,by_day[day]))
    fp.close()

def get_trend_by_artist(songs, artist):
    by_day = {}
    for song in songs:
        if song.artistName == artist:
            date = song.endTime.split(" ")[0]
            y = date.split("-")[0]
            m = date.split("-")[1]
            d = date.split("-")[2]

            day = datetime(int(y), int(m), int(d)).timestamp()

            if not day in by_day:
                by_day[day] = song.msPlayed
            else:
                by_day[day] += song.msPlayed
    return by_day
