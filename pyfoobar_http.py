import configset
import os
import time

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

