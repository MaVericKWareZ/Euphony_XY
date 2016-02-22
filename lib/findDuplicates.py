import plistlib

def findDuplicates(fileName) :
    print("Searching for duplicates tracks in %s....." % fileName)

    plist = plistlib.readPlist(fileName)

    tracks = plist['Tracks']

    track_name = {}

    for trackId, track in tracks.items():
        try:
            name = track['Name']
            duration = track['Total time']
            if name in track_name:
                if duration//1000 == track_name[name][0]//1000:  #for millisecond conversion and comparision
                    count  = track_name[name][1]
                    track_name[name] = (duration,count+1)

                else:
                    track_name[name] = (duration,1)

        except:
            pass

    dups = []
    for i,v in track_name.items():
        if v[1] > 1 :
            dups.append(v[1],k)

        if len(dups) > 0:
            print("Found %d duplicates. Tracks saved to the text file generated.  " %len(dups))
        else :
            print("No duplicates found")

        f = open("duplicate.txt","w")

        for val in dups:
            f.write("[%d] %s\n" % (val[0],val[1]))
        f.close()

        




