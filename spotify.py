from songs import *
from artists import *
from trends import *

def main():
    songs = get_songs()
    artists = get_top_artists(songs, 10)
    x_val = []
    trends = {}
    print(artists)
    for artist in artists:
        trend = get_trend_by_artist(songs, artist[0]) # dictionay where key is date, value is time listened
        trends[artist[0]] = trend
        for date in trend.keys():
            if not date in x_val:
                x_val.append(date)

    x_val.sort()

    fp = open("ms_listened.csv", "w")
    fp.write("date,")
    for artist in artists:
        fp.write("%s," % artist[0])
    fp.write("\n")

    for x in x_val:
        fp.write("%d," % x)
        for artist in artists:
            trend = trends[artist[0]]
            if x in trend:
                fp.write("%d," % trend[x])
            else:
                fp.write("0,")
        fp.write("\n")
    fp.close()





if __name__ == "__main__":
    main()
