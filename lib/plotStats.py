def plotStatS(filename):
    plist = plistlib.readPlist(filename)
    tracks = plist["Tracks"]

    ratings = []
    durations= []

    for trackId, track in tracks.items():
        try:
            ratings.append(track['Album Ratings'])
            durations.append(track['Total Time'])


        except:
            pass


    if ratings == [] or durations == []:
        print ("No valid data in %s." %filename)
        return


