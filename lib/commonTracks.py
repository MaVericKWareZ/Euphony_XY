def Eq_tracks(fileN) :
    trackName = []
    for fileName in fileN :
        trackNames = set()
        plist = plist.readPlist(fileN)
        tracks = plist['Tracks']
        for trackId, track in tracks.items():
            try:
                trackNames.add(track['Name'])
            except:
                pass

        trackName.append(trackNames)

    commonTracks = set.intersection(*trackName)

    if len(commonTracks) > 0 :
        f = open("common.txt", "W")
        for val in commonTracks:
            s = "%s\n" %val
            f.write(s.encode("UTF-8"))

        f.close()

        print("%d common tracks found. Output written to common.txt" %len(commonTracks))
    else:
        print("No common tracks")




