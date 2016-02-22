import numpy as np
from matplotlib import pyplot
import plistlib

def plotStatS(filename):
    plist = plistlib.readPlist(filename)
    tracks = plist["Tracks"]

    size = []
    durations= []

    for trackId, track in tracks.items():
        try:
            size.append(track['Size'])
            durations.append(track['Total Time'])


        except:
            pass


    if size == [] or durations == []:
        print ("No valid data in %s." %filename)
        return

    x = np.array(durations,np.int32)

    x = x/60000.0
    y = np.array(size,np.int32)

    #the scatter plot
    #pyplot.subplot(1,1)
    pyplot.plot(x,y,'*')
    pyplot.axis([0,1.05*np.max(x),-1,110])
    pyplot.xlabel('Track duration')
    pyplot.ylabel('Track rating')

    pyplot.show()

