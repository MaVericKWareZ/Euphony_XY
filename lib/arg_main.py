import re, argparse
import sys
import plistlib
from lib.findDuplicates import findDuplicates
from lib.commonTracks import Eq_tracks
from lib.histogram import plotStatH
from lib.scatter_plot import plotStatS



def main():
    descString = """
    Python module to analyze playlist files exported from iTunes and graph them.
    """
    parser = argparse.ArgumentParser(description=descString)
    group = parser.add_mutually_exclusive_group()


    group.add_argument('--common', nargs='*',dest='playlistFiles',required = False)
    group.add_argument('--statsS', dest='playlistScatter',required= False)
    group.add_argument('--statsH', dest='playlistHist',required= False)
    group.add_argument('--dup', dest='playlistDup',required= False)

    args = parser.parse_args()

    if args.playlistFiles:
        Eq_tracks(args.playlFiles)
    elif args.playlistScatter:
        plotStatS(args.playlistScatter)
    elif args.playlistHist:
        plotStatH(args.playlistHist)
    elif args.playlistDup:
        findDuplicates(args.playlistDup)
    else:
        print("Error : tracks not found")





