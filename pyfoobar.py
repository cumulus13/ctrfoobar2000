#!/usr/bin/python
# coding=UTF-8

#Copyright (c) 2009, Ranveer Raghuwanshi
#All rights reserved.

import win32com.client
import win32gui
import datetime
import optparse
import sys

ProgID = "Foobar2000.Application.0.7"
foobar_COM_object = win32com.client.Dispatch(ProgID)
playback = foobar_COM_object.Playback

class foobar(object):
    def __init__(self):
        super(foobar, self)

    def isPlaying(self):
        return playback.IsPlaying

    def play(self):
        if self.isPaused():
            playback.Pause()
        else:
            playback.Start()

    def stop(self):
        playback.Stop()

    def pauseplay(self):
        playback.Pause()

    def isPaused(self):
        return playback.IsPaused

    def next(self):
        playback.Next()

    def previous(self):
        playback.Previous()

    def playRandom(self):
        playback.Random()

    def seekPosition(self):
        return playback.Position

    def lengthOfTrack(self):
        return str(playback.FormatTitle("[%length%]"))


    def currentVolumeLevel(self):
        return str(playback.Settings.Volume) + "dB"

    def mute(self):
        playback.Settings.Volume = -100

    def setVolumeLevel(self,value):
        '''Set volume level to given value
           0dB corresponds to MAX_VALUE and -100dB corresponds to MIN_VALUE
           So, -100 <= value <= 0'''
        playback.Settings.Volume = value

    def currentActivePlaylist(self):
        return str(foobar_COM_object.Playlists.ActivePlaylist.Name)

    def getCurrentTrack(self):
        if self.isPlaying():
            track = str(playback.FormatTitle("[%title%]"))
            if len(track) == 0:
                return "check metadata"
            else:
                return track
        else:
            return "Check foobar running or not"


    def getCurrentArtist(self):
        if self.isPlaying():
            artist = str(playback.FormatTitle("[%artist%]"))
            if len(artist) == 0:
                return "check metadata"
            else:
                return artist
        else:
            return "Check foobar running or not"


    def getCurrentAlbum(self):
        if self.isPlaying():
            album = str(playback.FormatTitle("[%album%]"))
            if len(album) == 0:
                return "check metadata"
            else:
                return album
        else:
            return "Check foobar running or not"


    def isCurrentlyPlaying(self):
        return 'Currently playing "{0}" by "{1}"'.format(self.getCurrentTrack(),self.getCurrentArtist())

    def info(self):
        try:
            print "\n"
            print "\t Track    :", self.getCurrentTrack()
            print "\t Artist   :", self.getCurrentArtist()
            print "\t Album    :", self.getCurrentAlbum()
            print "\t Playlist :", self.currentActivePlaylist()
            state_play = self.isPlaying()
            state_pause = self.isPaused()
            if state_play:
                print "\t State    : Playing"
            elif state_pause:
                print "\t State    : Pause"
            else:
                print "\t State    : Unknown"

        except:
            print "\t Error communication with Foobar2000 COM Server !"
            
    def check_connection(self, url=None):
        print "COM: NOT HTTP Control !"
    
    def usage(self, print_help=None):
        print "\n"
        # try:
        #   c = control(pyfoobar.foobar)
        # except:
            # print "\t Error communication with Foobar2000 COM Server !"
        parser = optparse.OptionParser()
        parser.add_option('-l', '--list', help='List type of foobar2000', action='store_true')
        parser.add_option('-p', '--play', help='Play Playback', action='store_true')
        parser.add_option('-s', '--stop', help='Stop Playback', action='store_true')
        parser.add_option('-P', '--pause', help='Pause Playback', action='store_true')
        parser.add_option('-n', '--next', help='Next Play', action='store_true')
        parser.add_option('-r', '--previous', help='Previous Play', action='store_true')
        parser.add_option('-R', '--random', help='Play Random', action='store_true')
        parser.add_option('-V', '--volume', help='Set Volume, range is -100 <= value <= 0', action='store')
        parser.add_option('-M', '--mute', help='Mute Volume', action='store_true')
        parser.add_option('-i', '--info', help='Get info current Playing', action="store_true")
        parser.add_option('-t', '--type', help='Set Type of Foobar2000', action='store', type=int)
        options, args = parser.parse_args()
        if len(sys.argv) == 1:
            parser.print_help()
        elif print_help:
            parser.print_help()
        else:
            if options.play:
                self.play()
            elif options.stop:
                self.stop()
            elif options.pause:
                self.pauseplay()
            elif options.previous:
                self.previous()
            elif options.next:
                self.next()
            elif options.random:
                self.playRandom()
            elif options.volume:
                self.setVolumeLevel()
            elif options.mute:
                self.mute()
            elif options.info:
                self.info()

if __name__ == "__main__":

    f = foobar()
    f.usage()
