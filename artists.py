from songs import *

def get_artist_time(songs):
    time_by_artists = {}
    artists = []
    podcasts = ['Sleep With Me', 'Tmsoft’s White Noise Sleep Sounds', 'Chapo Trap House', "And That's Why We Drink", "Natural Sound Selections", "Granular", "Jensen and Holes: The Murder Squad"]

    for song in songs:
        if song.artistName in podcasts:
            continue

        artist = song.artistName
        if not artist in time_by_artists:
            time_by_artists[artist] = song.msPlayed
            artists.append(artist)
        else:
            time_by_artists[artist] += song.msPlayed

    return time_by_artists, artists

def get_top_artists(songs, num):

    top_artists = []
    time_by_artists, artists = get_artist_time(songs)

    n = len(artists)
    for i in range(n):
        for j in range(0, n-i-1):
            if time_by_artists[artists[j]] < time_by_artists[artists[j+1]]:
                artists[j], artists[j+1] = artists[j+1], artists[j]

    for i in range(num):
        artist = artists[i]
        top_artists.append([artist, time_by_artists[artist]])

    return top_artists
