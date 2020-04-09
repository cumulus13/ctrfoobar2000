from __future__ import print_function
import configset
import re
import os
import sys
import time
from bs4 import BeautifulSoup as bs
if sys.version_info.major == 3:
    import urllib.parse
else:
    class urllib:
        def parse(self):
            pass
    import urlparse
    urllib.parse = urlparse
import platform
# from multiprocessing import ThreatPool

CONF_FILE = os.path.join(os.path.dirname(__file__), 'pyfoobar.ini')

class urlhandle:
    def __init__(self, handle=None):
        self.handle = handle
        if self.handle == None:
            self.handle = 'urllib2'

        self.module = __import__(handle)

    def isPlaying(self):
        return None

    def check_connection(self, url):
        if self.handle == 'requests':
            try:
                self.module.get(url)
                return True
            except:
                return False
        else:
            try:
                self.module.urlopen(url)        
                return True
            except:
                return False

    def close(self, url):
        get = self.module.get(url)
        return get.close()

    def play(self, url):
        #print "url =", url
        if self.handle == 'requests':
            return self.module.get(url)
        else:
            return self.module.urlopen(url)

    def playTrack(self, url):
        # print "url =", url
        if self.handle == 'requests':
            return self.module.get(url)
        else:
            return self.module.urlopen(url)
        
    def deltrack(self, url):
        if self.handle == 'requests':
            return self.module.get(url)
        else:
            return self.module.urlopen(url)    

    def stop(self, url):
        if self.handle == 'requests':
            return self.module.get(url)
        else:
            return self.module.urlopen(url)

    def pauseplay(self, url):
        if self.handle == 'requests':
            return self.module.get(url)
        else:
            return self.module.urlopen(url)

    def isPaused(self, url):
        if self.handle == 'requests':
            return self.module.get(url)
        else:
            return self.module.urlopen(url)

    def next(self, url):
        if self.handle == 'requests':
            return self.module.get(url)
        else:
            return self.module.urlopen(url)

    def previous(self, url):
        if self.handle == 'requests':
            return self.module.get(url)
        else:
            return self.module.urlopen(url)

    def playRandom(self, url):
        if self.handle == 'requests':
            return self.module.get(url)
        else:
            return self.module.urlopen(url)

    def seekPosition(self, url):
        if self.handle == 'requests':
            return self.module.get(url)
        else:
            return self.module.urlopen(url)

    def lengthOfTrack(self, url):
        if self.handle == 'requests':
            return self.module.get(url)
        else:
            return self.module.urlopen(url)

    def currentVolumeLevel(self, url):
        if self.handle == 'requests':
            return self.module.get(url)
        else:
            return self.module.urlopen(url)

    def mute(self, url):
        if self.handle == 'requests':
            return self.module.get(url)
        else:
            return self.module.urlopen(url)

    def setVolumeLevel(self, url):
        if self.handle == 'requests':
            return self.module.get(url)
        else:
            return self.module.urlopen(url)

    def currentActivePlaylist(self, url):
        if self.handle == 'requests':
            return self.module.get(url)
        else:
            return self.module.urlopen(url)

    def getCurrentTrack(self, url):
        if self.handle == 'requests':
            return self.module.get(url)
        else:
            return self.module.urlopen(url)


    def getCurrentArtist(self, url):
        if self.handle == 'requests':
            return self.module.get(url)
        else:
            return self.module.urlopen(url)


    def getCurrentAlbum(self, url):
        if self.handle == 'requests':
            return self.module.get(url)
        else:
            return self.module.urlopen(url)


    def isCurrentlyPlaying(self, url):
        if self.handle == 'requests':
            return self.module.get(url)
        else:
            return self.module.urlopen(url)

    def info(self, url):
        if self.handle == 'requests':
            return self.module.get(url)
        else:
            return self.module.urlopen(url)

    def playlist(self, url):
        if self.handle == 'requests':
            return self.module.get(url)
        else:
            return self.module.urlopen(url)

    def browser(self, url):
        if self.handle == 'requests':
            #print "URL =", url
            return self.module.get(url)
        else:
            return self.module.urlopen(url)

    def repeat(self, url):
        if self.handle == 'requests':
            return self.module.get(url)
        else:
            return self.module.urlopen(url)

try:
    import requests
    c_handle = urlhandle('requests')
except:
    import urllib.request, urllib.error, urllib.parse
    c_handle = urlhandle('urllib2')

class foobar(object):
    def __init__(self, host=None, port=None):
        super(foobar, self)
        self.THIS_PATH = ''
        self.host = host
        self.port = port
        if self.host == None:
            self.host = configset.read_config('HTTP', 'server', CONF_FILE)
        if self.port == None:
            self.port = configset.read_config('HTTP', 'port', CONF_FILE)

        self.data = {'url':self.host, 'port':self.port, 'cmd':'', 'param1':'', 'param2':''}
        self.redata = (self.data.get('url'), self.data.get('port'), self.data.get('cmd'), self.data.get('param1'), self.data.get('param2'))
        self.cdata = configset.read_config('CONTROL', 'type')
        self.url = "http://{0}:{1}/default/?cmd={2}&param1={3}&param2={4}".format(*self.redata)

    def setURL(self, data):
        self.data.update(data)
        redata = (self.data.get('url'), self.data.get('port'), self.data.get('cmd'), self.data.get('param1'), self.data.get('param2'))
        if isinstance(data, dict):
            url = "http://{0}:{1}/default/?cmd={2}&param1={3}&param2={4}".format(*redata)
            return url
        else:
            raise SyntaxError('Invalid data dictionary')

    def isPlaying(self):
        return None

    def check_connection(self):
        #import urllib.parse
        parse = urllib.parse.urlparse(self.url)
        url = parse.scheme + "://" + parse.netloc
        return c_handle.check_connection(url)

    def close(self):
        c_handle.close(self.url)

    def play(self):
        data = {'cmd':'Start'}
        url = self.setURL(data)
        return c_handle.play(url)

    def playTrack(self, track, page=None):
        if page:
            track = (30 * (int(page) - 1)) + int(track)
        
        data = {'cmd':'Start', 'param1':str(track)}
        url = self.setURL(data)
        #print "url =", url
        return c_handle.play(url)

    def seekSecond(self, seeks):
        # print "seeks =", seeks
        if seeks:
            data = {'cmd':'SeekSecond', 'param1':str(seeks), 'param3':'NoResponse'}
            url = self.setURL(data)
            return c_handle.play(url)
        return None
    
    def deltrack(self, track):
        if isinstance(track, list):
            sys.stdout.write("del track = ")
            for i in track:
                data = {'cmd':'Del', 'param1':str(int(i) - 1)}
                url = self.setURL(data)
                sys.stdout.write(str(int(i)) + ", ")
                # return c_handle.deltrack(url)                
                c_handle.deltrack(url)
        else:
            data = {'cmd':'Del', 'param1':str(track)}
            url = self.setURL(data)
            return c_handle.deltrack(url)

    def stop(self):
        data = {'cmd':'Stop'}
        url = self.setURL(data)
        return c_handle.play(url)

    def pauseplay(self):
        data = {'cmd':'PlayOrPause'}
        url = self.setURL(data)
        return c_handle.play(url)

    def isPaused(self):
        return None

    def next(self):
        data = {'cmd':'StartNext'}
        url = self.setURL(data)
        return c_handle.play(url)

    def previous(self):
        data = {'cmd':'StartPrevious'}
        url = self.setURL(data)
        return c_handle.play(url)

    def playRandom(self):
        data = {'cmd':'StartRandom'}
        url = self.setURL(data)
        return c_handle.play(url)

    def browser_pre(self, url=None, direct_path=None):
        data_urlx = {0:'',1:'', 2:'', 3:''}

        data = {'cmd':'Browse'}

        if url == None:
            print("def:browser_pre --> url == None")
            url = self.setURL(data)
        if direct_path != None:
            print("def:browser_pre --> str(url) =", url)
            url_edit1 = str(url).split("&param2")[0]
            print("def:browser_pre --> url_edit1 =", url_edit1)
            url = url_edit1 + direct_path
            print("def:browser_pre --> url =", url)

        data1 = c_handle.browser(url).text
        soup1 = bs(data1, 'lxml')
        data2 = soup1.find("table")
        data3 = soup1.find('div', {'class':'dir'})
        data5 = data3.find_all('a')
        data4 = []
        for i in data2.find_all('a'):
            data4.append(i.contents)
        for a in data5:
            b = a.get('href')
            data_urlx.update({data5.index(a):b})
            

        #print "url X           1 =", url
        #print "list_url_suffix 1 =", data_urlx
        #print "list_file/dir   1 =", data4
        #print "-"*120
        return data_urlx, data4, url

    def browser(self, num_suffix=None, direct_path=None, url=None):
        data_urlx = self.browser_pre()[0]
        if num_suffix != None:
            print("def:browser --> num_suffix ! = None")
            r_url = urllib.parse.urlparse(self.url)
            print("def:browser --> num_suffix ! --> r_url =", r_url)
            url = r_url.scheme + "://" + r_url.netloc + data_urlx.get(num_suffix)
            print("def:browser --> num_suffix ! --> url =", url)
            data_urlx = self.browser_pre(url)
            print("url X           2 =", data_urlx[2])
            print("list_url_suffix 2 =", data_urlx[1])
            print("list_file/dir   2 =", data_urlx[2])
            print("+"*120)
            return self.browser_pre(url)

        if direct_path != None:
            print("def:browser --> direct_path ! = None")
            data_urlx = self.browser_pre(url, direct_path=direct_path)
            return self.browser_pre(url, direct_path=direct_path)
        
        return self.browser_pre()


    def seekPosition(self):
        return None

    def lengthOfTrack(self):
        return None

    def currentVolumeLevel(self):
        return None

    def mute(self):
        data = {'cmd':'Volume', 'param1':'0'}
        url = self.setURL(data)
        return c_handle.play(url)

    def setVolumeLevel(self, value):
        data = {'cmd':'Volume', 'param1':value}
        url = self.setURL(data)
        return c_handle.play(url)

    def currentActivePlaylist(self):
        return None

    def getCurrentTrack(self):
        return None

    def getCurrentArtist(self):
        return None

    def getCurrentAlbum(self):
        return None

    def isCurrentlyPlaying(self):
        return None

    def info(self):
        data1 = c_handle.info(self.url).text
        soup1 = bs(data1, 'lxml')
        data2 = soup1.find(id = 'track_title')
        data3 = str(data2.text).encode('UTF-8')
        if "//" in data3:
            #print "AAA"
            data4 = data3.split("//")
            #print "data 4=", data4
            if not len(data4) > 1:
                print("Foobar2000 is stopped")
                return None            
            artist = str(data4[-1]).strip()
            data5 = re.split("\[|\]", data4[0])
            albumartist = data5[0]     
            data6 = re.split("CD", data5[1])
            #print "data6 =", data6
            album = data6[0]
            track = data6[1][3:]
            cd = "CD" + data6[1][0]
            song = data5[2]
        else:
            #print "BBB"
            #print "data3 =", data3
            data4 = re.split("\[|\]", data3)
            #print ("data4 =", data4)
            if len(data4) > 1:
                data5 = data4[1].split("#")
                #print ("data5 =", data5)
            else:
                print("Foobar2000 is stopped")
                return None
            
            artist = data4[0]
            #print "artist 2 =", artist
            album = data5[0]
            #print "album    =", album
            song = song = " ".join(data4[2:])
            track = data5[1][-2:]
            #print "track =", track
            albumartist = data4[0]
            cd = "CD" + data5[1][0]
            #print "cd    =", cd

        #print "-" * 120
        print("Artist          :", artist) #unicode(artist).encode('UTF-8')
        print("Song            :", song.strip())
        print("Track           :", track)
        print("CD              :", cd)
        print("Album           :", album)
        print("Album Artist    :", albumartist)

    def getPages(self, page=None):
        # print "self.urlopen =", self.url
        URL = self.url
        if page:
            url_data = {'url':self.host, 'port':self.port, 'cmd':'P', 'param1':str(page), 'param2':''}
            URL = self.setURL(url_data)
        # print 'URL =', URL
        url_parse = urllib.parse.urlparse(URL)
        # print "url_parse =", url_parse
        data1 = c_handle.playlist(URL).text
        # print "data1 =", data1
        soup1 = bs(data1, 'lxml')
        data2 = soup1.find_all('p')
        # print "data2 =", data2
        data3 = ""
        for i in data2:
            if "First Previous " in i or " Next Last" in i:
                data3 = i
                break
        pages = {}
        if data3:
            data4 = data3.find_all('a')
            # print "data4 =", data4
            for i in data4:
                pages.update({i.text: url_parse.scheme + "://" + url_parse.netloc + i.get('href')})
            # print "pages =", pages
        return pages

    def playlist(self, page=None):
        # print "self.url =", self.url
        URL = self.url
        if page:
            url_data = {'url':self.host, 'port':self.port, 'cmd':'P', 'param1':str(page), 'param2':''}
            URL = self.setURL(url_data)
        # print "URL =", URL
        data1 = c_handle.playlist(URL).text
        soup1 = bs(data1, 'lxml')
        data2 = soup1.find(id='pl')
        #data3 = data2.find_all('tr')
        #print "data3 =", data3
        data4 = []
        for i in data2.find_all('tr'):
            data4.append(i.td.contents)
            #print "i.td.contents =",i.td.contents
        return data4

    def clearPlaylist(self):
        data = {'cmd':'EmptyPlaylist'}
        url = self.setURL(data)
        return c_handle.play(url)

    def addFolder(self, folder,verbosity=None):
        if verbosity:
            print("FOLDER00    ::",folder)
        if platform.uname()[0] == 'Windows':
            folder = os.path.abspath(folder)
        else:
            folder = folder
        if verbosity:
            print("FOLDER0     ::",folder)
        if '/' in folder[3]:
            folder = str(folder).replace('/', '\\')
            #folder = folder[1:]
        if verbosity:
            print("FOLDER      ::",folder)
        if platform.uname()[0] == 'Windows':
            folder = os.path.abspath(folder)
            folder = str(folder).replace(':', '%3A')
            folder = str(folder).replace(' ', '%20')
            folder = str(folder).replace('&', '%26')
            folder = str(folder).replace('(', '%28')
            folder = str(folder).replace(')', '%29')
            folder = folder + "\\"
        else:
            folder = str(folder).replace(':', '%3A')
            folder = str(folder).replace(' ', '%20')
            folder = str(folder).replace('&', '%26')
            folder = str(folder).replace('(', '%28')
            folder = str(folder).replace(')', '%29')
            folder = folder + "\\"

        if verbosity:
            print("FOLDER1     ::",folder)
        data = {'param1':folder, 'param2':'EnqueueDir', 'cmd':'Browse'}
        #print("data [521] =", data)
        url = self.setURL(data)
        return c_handle.play(url)
        
    def playlistCount(self):
        pl = len(self.playlist()[0:-1])
        return pl

    def addFiles(self, files):
        if isinstance(files, list):
            for i in files:
                if platform.uname()[0] == 'Windows':
                    i = os.path.abspath(i)
                else:
                    i = i

                i = str(i).replace(':', '%3A')
                i = str(i).replace(' ', '%20')
                i = str(i).replace('&', '%26')
                i = str(i).replace('(', '%28')
                i = str(i).replace(')', '%29')

                data = {'param1':i, 'cmd':'Browse'}
                url = self.setURL(data)
                c_handle.play(url)
        else:
            if platform.uname()[0] == 'Windows':
                files = os.path.abspath(files)
            else:
                files = files

            files = str(files).replace(':', '%3A')
            files = str(files).replace(' ', '%20')
            files = str(files).replace('&', '%26')
            files = str(files).replace('(', '%28')
            files = str(files).replace(')', '%29')

            data = {'param1':files, 'cmd':'Browse'}
            url = self.setURL(data)
            c_handle.play(url)
        
        # return self.play()


    def playFolder(self, folder, verbosity=None, clear=True):
        if verbosity:
            print("FOLDER00::",folder)
        if platform.uname()[0] == 'Windows':
            folder = os.path.abspath(folder)
        else:
            folder = folder
        if verbosity:
            print("FOLDER0::",folder)
        if '/' in folder:
            folder = str(folder).replace('/', '\\')
            folder = folder[1:]
        if verbosity:
            print("FOLDER::",folder)
        
        if clear:
            self.stop()
            self.clearPlaylist()
        #http://192.168.10.10:8888/default/?cmd=Browse&param1=M%3A\INSTRUMENTAL\GUITAR\Acoustic%20Rock\Vol.%2006\&param2=EnqueueDir
        # http://127.0.0.1:8888/default/?cmd=Browse&param1=m%3A%5CWEST%5CDevil%20Shoots%20Devil%20%26%20What%20We%20Feel%20-%20Split%20%282007%29%5C
        # http://127.0.0.1:8888/default/?cmd=Browse&param1=m%3A\WEST\Devil Shoots Devil & What We Feel - Split (2007)\&param2=EnqueueDir
        folder = str(folder).replace(':', '%3A')
        folder = str(folder).replace(' ', '%20')
        folder = str(folder).replace('&', '%26')
        folder = str(folder).replace('(', '%28')
        folder = str(folder).replace(')', '%29')
        folder = folder + "\\"
        if verbosity:
            print("FOLDER1::",folder)
        data = {'param1':folder, 'param2':'EnqueueDir', 'cmd':'Browse'}
        #print("data [595] =", data)
        url = self.setURL(data)
        #print("url [597] =", url)
        c_handle.play(url)
        #self.close()
        # count = 0
        # while 1:
        #     if self.playlistCount() == 0:
        #         time.sleep(1)
        #         count += 1
        #         if count == 50:
        #             break
        #     else:
        #         break
        # self.stop()
        return self.play()

    def repeat(self, tnum):
        '''
            tnum: 0 = Default (repeat off)
                  1 = Repeat Playlist
                  2 = Repeat Track
                  3 = Random Play
                  4 = Shuffle Track
                  5 = Shuffle Album
                  6 = Shuffle Folders
        '''
        data = {'cmd':'PlaybackOrder', 'param1':str(tnum)}
        url = self.setURL(data)
        return c_handle.repeat(url)

if __name__ == "__main__":
    c = foobar()
    # c.browser(1)
    c.getPages()
