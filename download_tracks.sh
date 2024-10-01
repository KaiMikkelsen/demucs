import musdb
mus = musdb.DB(download=True)

for track in mus:
    print(track.name)