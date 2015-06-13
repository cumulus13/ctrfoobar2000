import configset
import os
import time
from bs4 import BeautifulSoup as bs
import urlparse

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
        #print "url =", url
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

try:
    import requests
    c_handle = urlhandle('requests')
except:
    import urllib2
    c_handle = urlhandle('urllib2')

class foobar(object):
    def __init__(self, host=None, port=None):
        super(foobar, self)
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
        import urlparse
        parse = urlparse.urlparse(self.url)
        url = parse.scheme + "://" + parse.netloc
        return c_handle.check_connection(url)

    def close(self):
        c_handle.close(self.url)

    def play(self):
        data = {'cmd':'Start'}
        url = self.setURL(data)
        return c_handle.play(url)

    def playTrack(self, track):
        #print "TRACK =", track
        data = {'cmd':'Start', 'param1':str(track)}
        url = self.setURL(data)
        #print "url =", url
        return c_handle.play(url)
    
    def deltrack(self, track):
        if isinstance(track, list):
            for i in track:
                data = {'cmd':'Del', 'param1':str(i)}
                url = self.setURL(data)
                return c_handle.deltrack(url)                
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
            print "def:browser_pre --> url == None"
            url = self.setURL(data)
        if direct_path != None:
            print "def:browser_pre --> str(url) =", url
            url_edit1 = str(url).split("&param2")[0]
            print "def:browser_pre --> url_edit1 =", url_edit1
            url = url_edit1 + direct_path
            print "def:browser_pre --> url =", url

        data1 = c_handle.browser(url).text
        soup1 = bs(data1)
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
            print "def:browser --> num_suffix ! = None"
            r_url = urlparse.urlparse(self.url)
            print "def:browser --> num_suffix ! --> r_url =", r_url
            url = r_url.scheme + "://" + r_url.netloc + data_urlx.get(num_suffix)
            print "def:browser --> num_suffix ! --> url =", url
            data_urlx = self.browser_pre(url)
            print "url X           2 =", data_urlx[2]
            print "list_url_suffix 2 =", data_urlx[1]
            print "list_file/dir   2 =", data_urlx[2]
            print "+"*120
            return self.browser_pre(url)

        if direct_path != None:
            print "def:browser --> direct_path ! = None"
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
        return None

    def playlist(self):
        data1 = c_handle.playlist(self.url).text
        soup1 = bs(data1)
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

    def addFolder(self, folder):
        #http://192.168.10.10:8888/default/?cmd=Browse&param1=M%3A\INSTRUMENTAL\GUITAR\Acoustic%20Rock\Vol.%2006\&param2=EnqueueDir
        folder = str(folder).replace(':', '%%3A')
        data = {'param1':folder, 'param2':'EnqueueDir'}
        url = self.setURL(data)
        return c_handle.play(url)

    def playFolder(self, folder):
        self.stop()
        self.clearPlaylist()
        #http://192.168.10.10:8888/default/?cmd=Browse&param1=M%3A\INSTRUMENTAL\GUITAR\Acoustic%20Rock\Vol.%2006\&param2=EnqueueDir
        folder = str(folder).replace(':', '%3A')
        folder = folder + "\\"
        data = {'param1':folder, 'param2':'EnqueueDir', 'cmd':'Browse'}
        url = self.setURL(data)
        c_handle.play(url)
        #self.close()
        time.sleep(5)
        self.play()
        return self.play()

if __name__ == "__main__":
    c = foobar()
    c.browser(1)
