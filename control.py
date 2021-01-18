#!/usr/bin/env python2
from __future__ import print_function
from safeprint import print as sprint
from make_colors import make_colors
import traceback
from configset import configset# as cfgset
#configset = cfgset()
import argparse
import sys
import os
import subprocess
from pydebugger.debug import debug

if sys.version_info.major == 3:
    import urllib.parse
    from urllib.parse import unquote, quote
else:
    class urllib:
        def parse(self):
            pass
    import urlparse
    from urllib import unquote, quote
    urllib.parse = urlparse
    input = raw_input
import re
import platform
import time
try:
    from pause import pause
except:
    import inspect
    try:
        if sys.platform == 'win32':
            import msvcrt as getch
        else:
            from pygetch.getch import GETCH as getch
        try:
            from make_colors import make_colors
        except:
            def make_colors(data, fg=None, bg=None):
                print(data)
    except:
        input("Enter to Continue !")
    

    def pause(page=''):
        lineno = str(inspect.stack()[1][2])     
        if page:
            page = make_colors("[" + str(page) + "]", "lw", "bl")
        else:
            page = make_colors("[" + str(lineno) + "]", "lw", "bl")
        note = make_colors("Enter to Continue . ", "lw", "lr") + "[" + page + "] " + make_colors("x|q = exit|quit", "lw", "lr")
        print(note)
        q = getch.getch()
        if q == 'x' or q == 'q':
            sys.exit(make_colors("EXIT !", 'lw','lr'))
PAGE = 0

class control(object):
    def __init__(self, host=None, port=None):
        super(control, self)
        
        self.host = host
        self.port = port
        self.configname = os.path.join(os.path.dirname(__file__), 'pyfoobar.ini')
        
        cfg = configset(self.configname)
        self.cfg = cfg
        
        self.type_foobar = cfg.options('TYPE')
        self.error = ''
        self.nircmd = r"c:\EXE\nircmd.exe"
        if not os.path.isfile(self.nircmd):
            self.nircmd = r"nircmd.exe"
        self.ctype = cfg.read_config('CONTROL', 'type')
        self.foobar2000 = ''
        if not os.getenv('PROCESSOR_ARCHITECTURE') == 'x86':
            self.prog_path = os.getenv('ProgramFiles(x86)')
        else:
            self.prog_path = os.getenv('ProgramFiles')
        self.DATA = {}
        if self.host:
            self.DATA.update({'url':host})
        if self.port:
            self.DATA.update({'port':port})
            
    def write_config(self, data):
        if isinstance(data, list):
            for i in data:
                if "#" in i:
                    list_data = re.split("#", i)
                    section = list_data[0].strip()
                    option = list_data[1].strip()
                    value = list_data[2].strip()
                    self.cfg.write_config(section, option, value)

    def getModulePath(self):
        return configset.read_config('MODULE', 'path')

    def re_init(self):
        #print "self.ctype =", self.ctype
        if self.ctype == 'com':
            #print "COM SET"
            import pyfoobar
            self.foobar2000 = pyfoobar.foobar()
        elif self.ctype == 'http':
            #print "HTTP SET"
            import pyfoobar_http
            self.foobar2000 = pyfoobar_http.foobar(self.host, self.port)

    def play(self, stop=False):
        self.re_init()
        try:
            return self.foobar2000.play(self.DATA)
        except:
            print(traceback.format_exc(True))
            self.check_connection()
            print("\t Error communication with Foobar2000 [COM|HTTP] Server !")

    def playTrack(self, track, page=None):
        self.re_init()
        # print "TRACK 0 =", track
        try:
            return self.foobar2000.playTrack(track, page)
        except:
            self.check_connection()
            print("\t This only use with with Foobar2000 HTTP Server Controller Plugin !")

    def seekSecond(self, seeks):
        self.re_init()
        try:
            return self.foobar2000.seekSecond(seeks)
        except:
            import traceback
            traceback.format_exc()
            self.check_connection()
            print("\t This only use with with Foobar2000 HTTP Server Controller Plugin !")

    def stop(self):
        self.re_init()
        try:
            return self.foobar2000.stop(self.DATA)
        except:
            self.check_connection()
            print("\t Error communication with Foobar2000 [COM|HTTP] Server !")

    def pause(self):
        self.re_init()
        try:
            return self.foobar2000.pauseplay(self.DATA)
        except:
            self.check_connection()
            print("\t Error communication with Foobar2000 [COM|HTTP] Server !")

    def previous(self):
        self.re_init()
        try:
            return self.foobar2000.previous()
        except:
            self.check_connection()
            print("\t Error communication with Foobar2000 [COM|HTTP] Server !")

    def next(self):
        self.re_init()
        try:
            return self.foobar2000.next()
        except:
            traceback.format_exc()
            self.check_connection()
            print("\t Error communication with Foobar2000 [COM|HTTP] Server !")

    def random(self):
        self.re_init()
        try:
            return self.foobar2000.playRandom()
        except:
            self.check_connection()
            print("\t Error communication with Foobar2000 [COM|HTTP] Server !")

    def volume(self, vol):
        self.re_init()
        try:
            return self.foobar2000.setVolumeLevel(vol)
        except:
            self.check_connection()
            print("\t Error communication with Foobar2000 [COM|HTTP] Server !")

    def mute(self):
        self.re_init()
        try:
            return self.foobar2000.mute()
        except:
            self.check_connection()
            print("\t Error communication with Foobar2000 [COM|HTTP] Server !")

    def info(self, slim = False):
        if not slim:
            print("Current Playing : ")
        self.re_init()
        try:
            self.foobar2000.info(self.DATA, slim = slim)
        except:
            #traceback.format_exc(True)
            traceback.format_exc()
            self.check_connection()
            print("\t " + make_colors("Error communication with Foobar2000 [COM|HTTP] Server !", 'lw', 'r'))

    def clearPlaylist(self):
        self.re_init()
        return self.foobar2000.clearPlaylist()
    
    def deltrack(self, track):
        self.re_init()
        return self.foobar2000.deltrack(track)

    def addFolder(self, folder, verbosity=None):
        self.re_init()
        return self.foobar2000.addFolder(folder, verbosity)

    def addFiles(self, files):
        self.re_init()
        return self.foobar2000.addFiles(files)

    def playFolder(self, folder, verbosity=None, clear=True, play=True, host = None, port = None):
        if host:
            print("HOST:", host)
        if port:
            print("PORT:", port)
        self.re_init()
        return self.foobar2000.playFolder(folder, verbosity, clear, play, host, port)

    def kill(self, pid=None):
        import win32ts
        hand = win32ts.WTSOpenServer('localhost')
        process = win32ts.WTSEnumerateProcesses(hand, 1, 0)
        for i in process:
            # subprocess.Popen(self.nircmd + " closeprocess foobar2000.exe")
            if "foobar2000.exe" in i[2]:
                os.kill(i[1], i[1])
            if "COMServer2Helper.exe" in i[2]:
                os.kill(i[1], i[1])

    def close(self):
        # import win32ts
        # hand = win32ts.WTSOpenServer('localhost')
        # process = win32ts.WTSEnumerateProcesses(hand, 1, 0)
        # for i in process:
        subprocess.Popen(self.nircmd + " closeprocess foobar2000.exe")

    def clear(self):
        self.kill()
        if os.path.isdir(os.path.join(os.getenv('ProgramFiles(x86)'), 'foobar2000')):
            os.rmdir(os.path.join(os.getenv('ProgramFiles(x86)'), 'foobar2000'))
        elif os.path.isdir(os.path.join(os.getenv('ProgramFiles'), 'foobar2000')):
            os.rmdir(os.path.join(os.getenv('ProgramFiles'), 'foobar2000'))
        if os.path.isdir(os.path.join(os.getenv('appdata'), 'foobar2000')):
            os.rmdir(os.path.join(os.getenv('appdata'), 'foobar2000'))

    def open(self):
        import module002a
        data = ''
        del(sys.argv[1])
        if os.getenv('ProgramFiles(x86)') != None:
            if os.path.isdir(os.path.join(os.getenv('ProgramFiles(x86)'), 'foobar2000')):
                data = [os.getenv('ProgramFiles(x86)') + '\\foobar2000.exe']
        else:
            if os.path.isdir(os.path.join(os.getenv('ProgramFiles'), 'foobar2000')):
                data = [os.getenv('ProgramFiles') + '\\foobar2000\\foobar2000.exe']
        module002a.main(data)

    def config(self, num_type, verbosity=None):
        for i in self.type_foobar:
            if self.type_foobar.index(i) == num_type - 1:
                subprocess.Popen("taskkill /f /im foobar2000.exe")
                if os.path.isdir(os.path.join(self.prog_path, 'foobar2000')):
                    os.rmdir(os.path.join(self.prog_path, 'foobar2000'))
                if os.path.isdir(os.path.join(os.getenv('appdata'), 'foobar2000')):
                    os.rmdir(os.path.join(os.getenv('appdata'), 'foobar2000'))
                os.chdir(self.prog_path)
                os.system("mklink /d \"%s\\foobar2000\" \"%s\"" %(self.prog_path, configset.read_config('TYPE', i)))
                os.chdir(os.getenv('appdata'))
                if os.path.isdir(os.path.join(os.getenv('appdata'), i)):
                    os.system("mklink /d \"%s\\foobar2000\" \"%s\"" %(os.getenv('appdata'), os.path.join(os.getenv('appdata'), i)))
                else:
                    if os.path.isdir(os.path.join(os.getenv('appdata'), configset.read_config('APPDATA', i))):
                        os.system("mklink /d \"%s\\foobar2000\" \"%s\"" %(os.getenv('appdata'), configset.read_config('APPDATA', i)))
                    else:
                        self.error = "Please re-config your config file for section:APPDATA, option: %s" %(i)
                        return False
        return True	

    def setconfig(self, num_type, verbosity=None):
        # print "\n"
        if num_type > len(self.type_foobar):
            for l in self.type_foobar:
                l2 = str(l).split("_")
                print("\t " + str(self.type_foobar.index(l) + 1) + ".", str(l2[0]).title(), str(l2[1]).title())
            print("\n")
            q = input("Please Select your Type [use option -t for direct option]: ")
            if q == '':
                self.usage(True)
            else:
                q = int(q)
                self.config(q, verbosity)
        else:
            usage(True)

    def readConfig(self):
        #print("\n")
        print(self.cfg.read_all_config())
        #print("\n")

    def check_connection(self):
        self.re_init()
        if self.foobar2000.check_connection() != True:
            print("\t " + make_colors("Please re-config config file for server and host or use option -H and option -O [HTTP]", 'lw', 'r'))
            print("\n")          
        return self.foobar2000.check_connection()

    def printPages(self, pages):
        pages_print = ""
        for i in pages:
            pages_print += str(i) + " | "
        if pages_print:
            if pages_print[-3:] == " | ":
                pages_print = pages_print[:-3]

        # print pages_print
        return pages_print

    def format_number(self, number, length=99):
        return ("0" * (len(str(length)) - len(str(number)))) + str(number)

    def format_playlist(self, text="Blue Night [Blue Night CD01 #07] She's Leaving Home // Andy Timmons Band"):
        #Blue Night [Blue Night CD01 #07] She's Leaving Home // Andy Timmons Band
        # print("text:", text)
        title = re.findall("\] (.*?) //", text)
        if not title:
            title = re.findall("\] (.*?)$", text)
        # print("title =", title)
        album = re.findall("\[(.*?) CD", text)
        if not album:
            album = ['']
        # print("album =", album)
        album_artist = re.findall("^(.*?) \[", text)
        # print("album_artist =", album_artist)
        cd = re.findall("\[.*?(CD\d+) .*?\]", text)
        if not cd:
            cd = ["CD1"]
        # print("cd    =", cd)
        track = re.findall("(#\d+)", text)
        # print("track =", track)
        if not track:
            track = ["#0"]
        artist = re.findall("// (.*?)$", text)
        if not artist:
            artist = re.findall("^(.*?)\[", text)
        # print("artist=", artist)

        return make_colors(title[0], 'lw', 'r') + " - " + make_colors(artist[0], 'lw', 'bl') + " [" + make_colors(track[0], 'b', 'y') + "/" + make_colors(cd[0], 'lw', 'm') + ". " + make_colors(album[0], 'b', 'lg') + "] // " + make_colors(album_artist[0], 'b', 'lc')

    def playlist(self, page=None):
        self.re_init()
        global PAGE
        if page:
            PAGE = page
        if PAGE:
            page = PAGE
        try:
            pages = self.foobar2000.getPages(page, self.DATA)
        except:
            print(traceback.format_exc())
            sys.exit("Connection Error !")

        try:
            # print "self.foobar2000.playlist(page) =", self.foobar2000.playlist(page)
            # print "-"*200
            pl, last = self.foobar2000.playlist(page)[0:]

            if len(pl) > 9:
                for i in range(0, 9):
                    try:
                        print(self.format_number(str(i + 1), len(pl)) + '. ' + self.format_playlist(str(pl[i][0]).encode('UTF-8')) + "\n")
                    except:
                        sprint(self.format_number(str(i + 1), len(pl)) + '. ' + self.format_playlist(pl[i][0]) + "\n")
                    # try:
                    #     print("-"*len(str(pl[i][0]).encode('UTF-8')))
                    # except:
                    #     sprint("-"*len(pl[i][0]))
                for i in range(9, len(pl)):
                    try:
                        print(self.format_number(str(i + 1), len(pl)) +  '. ' + self.format_playlist(str(pl[i][0]).encode('UTF-8')) + "\n")
                    except:
                        print(self.format_number(str(i + 1), len(pl)) +  '. ' + self.format_playlist(unquote(pl[i][0])) + "\n")
                    # print("-"*len(unquote(pl[i][0])))
            else:
                for i in pl:
                    if i:
                        sprint(self.format_number(str(pl.index(i) + 1), len(pl)) + ". ", self.format_playlist(i[0].encode('utf-8')) + "\n")
                        # print("-"*len(str(i[0]).encode('UTF-8')))
            self.info(slim=True)
            # print("pages =", pages)
            print("\n")
            if pages:
                print("\t PAGE:", self.printPages(pages))
                print("\n")
            q = input("\t " + make_colors("Do you want to play Track No ", 'lw', 'bl') + "[" + make_colors("x = exit", 'lw', 'r') + ", " + make_colors("p[number] = page number", 'b', 'y') + "]: ")
            print("\n")
            if q:
                #print "PLAY TRACK", q
                if q == 'x':
                    try:
                        sys.exit()
                    except:
                        return None
                if q[0].lower() == 'p' and len(q) > 1:
                    return self.playlist(q[1])
                if q == 'Previous' or q == 'First' or q == 'Next' or q == 'Last':
                    try:
                        page_number = re.findall("param1=.*?$", pages.get(q))[0].split('param1=')[1]
                        return self.playlist(page_number)
                    except:
                        tp, vl, tr = sys.exc_info()
                        if vl.__class__.__name__ == 'TypeError':
                            pass
                        else:
                            traceback.format_exc()
                try:
                    self.playTrack(str(int(q) - 1), page)
                    return self.playlist()
                except:
                    pass
                return self.playlist()
        except:
            print("ERROR =", traceback.format_exc())
            self.check_connection()
            print("\t This only use with Foobar2000 HTTP Server Controller Plugin !")

    def playlistCount(self):
        self.re_init()
        pl, last = self.foobar2000.playlist()[0:-1]
        return len(pl)

    def browser(self, num_suffix=None, direct_path=None, url=None):
        self.re_init()
        try:
            #data_url, data4, url
            try:
                www = self.foobar2000.browser(num_suffix, direct_path, url)
            except:
                print("\n")
                print("\t Error Communication with server !")
                #return SystemExit
                return sys.exit()

            print("www              =", www)
            print("www[0] / dataurl =", www[0])
            print("www[1] / data4   =", www[1])
            print("www[2] / url     =", www[2])
            for i in www[1]:
                print(i)
            listdir = list(www[0].values())
            #print "listdir =", listdir
            #print "len(listdir) =", len(listdir)
            print("\n")
            q = input("\t GO To [up|back|(Folder/Path Name)]: ")
            if str(q).lower() == 'up':
                for i in range(1, len(listdir)):
                    if len(str(listdir[-i]).strip()) != 0:
                        return self.browser(i)

                return self.browser(0)
            elif str(q).isdigit():
                print("str(q).isdigit()")
                return self.browser(int(q))
            elif q == None:
                q = ''
            else:
                for i in range(1, len(listdir)):
                    if len(str(listdir[-i]).strip()) != 0:
                        r_url = urllib.parse.urlparse(www[2])
                        url = r_url.scheme + "://" + r_url.netloc
                        url1 = str(listdir[-i]).split('&param2=')[0]
                        url = url + "/" + url1 + direct_path
                        return self.browser(direct_path=q, url=url)
        except:
            print("ERROR:",traceback.format_exc())
            self.check_connection()
            print("\t This only use with Foobar2000 HTTP Server Controller Plugin !")

    def format_alias_dir(self, path, alias=None, level=0, verbosity=None):
        drive = ''
        if not level and alias:
            level = re.findall("\d+", alias)
            if level:
                level = level[0]
                debug(level = level)
                alias = list(filter(None, re.split(level, alias)))
                debug(alias = alias)
            else:
                level = 0
        debug(alias = alias)
        debug(level = level)
        
        if alias and level:
            if isinstance(alias, list):
                drive = alias[0]
            else:
                drive = alias
            if 'linux' in sys.platform:
                alias_split = path.split("/")
                alias_split = filter(None, alias_split)
                
            else:
                alias_split = path.split("\\")
                alias_split = filter(None, alias_split)
            alias = alias_split[abs(int(level)):]
            debug(alias = alias)
            alias.insert(0, drive)

            alias = "\\".join(alias)

            debug(alias = alias)
        elif alias and not level:
            debug(alias = alias)
            if isinstance(alias, list):
                drive = alias[0]
            else:
                drive = alias
            if 'linux' in sys.platform:
                alias_split = path.split("/")
                alias_split = filter(None, alias_split)
                
            else:
                alias_split = path.split("\\")
                alias_split = filter(None, alias_split)
            alias = alias_split
            debug(path = path)
            debug(drive = drive)
            debug(alias = alias)
            alias.insert(0, drive)

            alias = "\\".join(alias)

            debug(alias = alias)
            # sys.exit()
        elif not alias and level:
            if 'linux' in sys.platform:
                alias_split = path.split("/")
                alias_split = filter(None, alias_split)
                
            else:
                alias_split = path.split("\\")
                alias_split = filter(None, alias_split)
            alias = alias_split[abs(int(level)):]
            debug(alias = alias)
            alias = "\\".join(alias)
            debug(alias = alias)
        else:
            debug(path = path)
            if path[0] == "/":
                path = path[1:]
            debug(path = path)
            alias = re.sub("/", "\\\\", path)
            debug(alias = alias)
        verbosity = False
        debug(alias = alias)
        
        return alias
        
    def getVersion(self):
        import __version__, __test__
        print("\tVersion: " + str(__version__) + "." + str(__test__))
        sys.exit(0)

    def repeat(self, tnum):
        self.re_init()
        try:
            return self.foobar2000.repeat(tnum)
        except:
            print(traceback.format_exc())
            self.check_connection()
            print("\t Error communication with Foobar2000 [COM|HTTP] Server !")

    def add_resursive_folders(self, folders):
        exps = ['img', 'imgs', 'cover', 'platlist', 'covers']
        exps_files = ['.jpg', '.ini', '.pls', '.m3u', '.txt', '.md', '.rst', '.db', '.jpeg', '.png', '.bmp', '.gif', '.exe', '.py', '.php', '.pyc', '.db3', '.list', '.nfo', '.bif', '.lrc']
        incl_files = ['.mp3', '.flac', '.m4a', '.mp4', '.wav', '.egg', '.arm']
        list_dirs = []
        list_files = []
        for root, dirs, files in os.walk(folders):
            if len(dirs) > 0:
                # print "dirs =", dirs
                for i in dirs:
                    if not str(i).lower() in exps:
                        dirs_add = os.path.join(root, i)
                        # print "dirs_add =", dirs_add
                        list_dirs.append(dirs_add)
            if len(files) > 0:
                for i in files:
                    if os.path.splitext(str(i).lower())[1].lower() in incl_files:
                        list_files.append(os.path.join(root, i))
        return list_dirs, list_files

    def file_listing(self, folder):
        exps = ['img', 'imgs', 'cover', 'platlist', 'covers']
        exps_files = ['.jpg', '.ini', '.pls', '.m3u', '.txt', '.md', '.rst', '.db', '.jpeg', '.png', '.bmp', '.gif', '.exe', '.py', '.php', '.pyc', '.db3', '.list', '.nfo', '.bif', '.lrc']
        incl_files = ['.mp3', '.flac', '.m4a', '.mp4', '.wav', '.egg', '.arm']
        list_files = []
        if not os.path.isdir(folder):
            return []
        files = os.listdir(folder)
        # print("FILES =", files)
        for i in files:
            if os.path.splitext(str(i).lower())[1].lower() in incl_files:
                list_files.append(os.path.join(folder, i))
        return list_files

    def check_playlist(self, all_files, current_playlist):
        while 1:
            # print("len(all_files) 2 =", len(all_files))
            # print("len playlist   2 =", len(current_playlist))
            if len(all_files) == len(current_playlist):
                break
            else:
                # time.sleep(1)
                current_playlist, last = self.foobar2000.playlist()[0:]
                # print("last =", last)
                # print("len current_playlist 1 =", len(current_playlist))
                if last > 0:
                    current_playlist = []
                    for p in range(1, last+1):
                        cp, last = self.foobar2000.playlist(p)[0:]
                        # print("len(cp) =", len(cp))
                        current_playlist += cp
                # print("len current_playlist 2 =", len(current_playlist))
        return True

    def usage(self, print_help=None):
        print("\n")
        parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
        parser.add_argument('-l', '--list', help='List type of foobar2000 [com] or List Playlist [http]', action='store_true')
        parser.add_argument('-p', '--play', help='Play Playback', action='store_true')
        parser.add_argument('-s', '--stop', help='Stop Playback', action='store_true')
        parser.add_argument('-P', '--pause', help='Pause Playback', action='store_true')
        parser.add_argument('-n', '--next', help='Next Play', action='store_true')
        parser.add_argument('-r', '--previous', help='Previous Play', action='store_true')
        parser.add_argument('-R', '--random', help='Play Random', action='store_true')
        parser.add_argument('-V', '--volume', help='Set Volume, range is -100 <= value <= 0', action='store')
        parser.add_argument('-m', '--mute', help='Mute Volume', action='store_true')
        parser.add_argument('-i', '--info', help='Get info current Playing [com]', action="store_true")
        parser.add_argument('-t', '--type', help='Set Type of Foobar2000 [com]', action='store', type=int)
        parser.add_argument('-C', '--clear', help='Clear all Configuration [com]', action='store_true')
        parser.add_argument('-k', '--kill', help='Terminate Foobar2000 running [com]', action='store_true')
        parser.add_argument('-o', '--open', help='Just run Foobar2000 [com]', action='store_true')
        parser.add_argument('-q', '--close', help='Just close Foobar2000 [com]', action='store_true')
        parser.add_argument('-S', '--type-controller', help='Set Type Of Controller [com,http]', action='store')
        parser.add_argument('-x', '--change-config', help='Set Change config. format: section=option', action='store')
        #parser.add_argument('-x', '--store-config', help='Store Set Type Of Controller [com,http]', action='store_true')
        parser.add_argument('-f', '--addfolder', help='Add Remote Folder Queue [HTTP]', action='store', nargs='*')
        parser.add_argument('-fi', '--addfiles', help='Add Remote Files Queue [HTTP]', action='store', nargs='*')
        parser.add_argument('-F', '--addfolderplay', help='Add Remote Folder Queue & Play it [HTTP]', action='store', nargs='*')
        parser.add_argument('-Fi', '--addfilesplay', help='Add Remote Folder Queue & Play it [HTTP]', action='store', nargs='*')
        parser.add_argument('-c', '--clear-playlist', help='Clear Current Playlist [HTTP]', action='store_true')
        parser.add_argument('-H', '--host', help="Remote Host control Address [HTTP]", action='store')
        parser.add_argument('-O', '--port', help="Remote Port control Address [HTTP]", action='store')      
        parser.add_argument('-g', '--read-config', help="Read config file", action="store_true")
        parser.add_argument('-?', '--usage', help='Print All Help', action='store_true')
        parser.add_argument('-T', '--section', help="Set Section Config", action="store")
        parser.add_argument('-E', '--option', help="Set Option Config", action="store", nargs=2)   
        parser.add_argument('-a', '--dir-alias', help="Root of Directory Alias On Server [HTTP]", action="store")
        parser.add_argument('-v', '--version', help='-v = show version | -vv = verbosity process', action='count')

        subparser = parser.add_subparsers(title='TYPE CONTROLLER', dest='TYPE')

        args_com = subparser.add_parser('com', help='Type Controller "com"')
        args_com.add_argument('-l', '--list', help='List type of foobar2000', action='store_true')
        args_com.add_argument('-p', '--play', help='Play Playback', action='store_true')
        args_com.add_argument('-s', '--stop', help='Stop Playback', action='store_true')
        args_com.add_argument('-P', '--pause', help='Pause Playback', action='store_true')
        args_com.add_argument('-n', '--next', help='Next Play', action='store_true')
        args_com.add_argument('-r', '--previous', help='Previous Play', action='store_true')
        args_com.add_argument('-R', '--random', help='Play Random', action='store_true')
        args_com.add_argument('-V', '--volume', help='Set Volume, range is -100 <= value <= 0', action='store')
        args_com.add_argument('-m', '--mute', help='Mute Volume', action='store_true')
        args_com.add_argument('-i', '--info', help='Get info current Playing', action="store_true")
        args_com.add_argument('-t', '--type', help='Set Type of Foobar2000', action='store', type=int)
        args_com.add_argument('-C', '--clear', help='Clear all Configuration', action='store_true')
        args_com.add_argument('-k', '--kill', help='Terminate Foobar2000 running', action='store_true')
        args_com.add_argument('-o', '--open', help='Just run Foobar2000', action='store_true')
        args_com.add_argument('-S', '--type-controller', help='Set Type Of Controller [com,http]', action='store')
        args_com.add_argument('-x', '--change-config', help='Store Set Type Of Controller [com,http]', action='store_true')
        args_com.add_argument('-?', '--usage', help='Print All Help', action='store_true')
        args_com.add_argument('-g', '--read-config', help="Read config file", action="store_true")
        args_com.add_argument('-T', '--section', help="Set Section Config", action="store")
        args_com.add_argument('-E', '--option', help="Set Option Config", action="store", nargs=2)
        args_com.add_argument('-v', '--version', help='-v = show version | -vv = verbosity process', action='count')
        #FOOBAR2000 HTTP PLUGIN
        args_http = subparser.add_parser('http', help='Type Controller "http"')
        args_http.add_argument('-p', '--play', help='Play Playback', action='store_true')
        args_http.add_argument('-t', '--play-track', help="Play Playback Track No", action="store")
        args_http.add_argument('-s', '--stop', help='Stop Playback', action='store_true')
        args_http.add_argument('-P', '--pause', help='Pause Playback', action='store_true')
        args_http.add_argument('-n', '--next', help='Next Play', action='store_true')
        args_http.add_argument('-r', '--previous', help='Previous Play', action='store_true')
        args_http.add_argument('-R', '--random', help='Play Random', action='store_true')
        args_http.add_argument('-V', '--volume', help='Set Volume, range is -100 <= value <= 0', action='store')
        args_http.add_argument('-m', '--mute', help='Mute Volume', action='store_true')
        args_http.add_argument('-i', '--info', help='Get info current Playing', action="store_true")
        args_http.add_argument('-f', '--addfolder', help='Add Remote Folder Queue [HTTP]', action='store', nargs='*')
        args_http.add_argument('-fi', '--addfiles', help='Add Remote Files Queue [HTTP]', action='store', nargs='*')
        args_http.add_argument('-F', '--addfolderplay', help='Add Remote Folder Queue & Play it [HTTP]', action='store', nargs='*')
        args_http.add_argument('-Fi', '--addfilesplay', help='Add Remote Folder Queue & Play it [HTTP]', action='store', nargs='*')
        args_http.add_argument('-c', '--clear-playlist', help='Clear Current Playlist [HTTP]', action='store_true')
        args_http.add_argument('-d', '--del-track', help='Delete Playlist [HTTP], example: foobar -d 1 2 3', action='store', nargs='*')
        args_http.add_argument('-l', '--list', help='List Playlist', action='store_true')
        args_http.add_argument('-b', '--browser', help='Browser Library', action='store_true')
        args_http.add_argument('-S', '--type-controller', help='Set Type Of Controller [com,http]', action='store')
        args_http.add_argument('-H', '--host', help="Remote Host control Address [HTTP]", action='store')
        args_http.add_argument('-O', '--port', help="Remote Port control Address [HTTP]", action='store')
        args_http.add_argument('-?', '--usage', help='Print All Help', action='store_true')
        args_http.add_argument('-g', '--read-config', help="Read config file", action="store_true")
        args_http.add_argument('-x', '--change-config', help='Set Change config. format: section#option#value', action='store', nargs = '*')
        args_http.add_argument('-T', '--section', help="Set Section Config", action="store")
        args_http.add_argument('-E', '--option', help="Set Option Config", action="store", nargs=2)
        args_http.add_argument('-a', '--dir-alias', help="Root of Directory Alias On Server", action="store")
        args_http.add_argument('-v', '--version', help='-v = show version | -vv = verbosity process', action='count')
        args_http.add_argument('-L', '--level-alias', help="Level Root of Directory Alias On Server", action="store", default=0)
        args_http.add_argument('-z', '--repeat', help='Repeat 0 = Default (repeat off) | 1 = Repeat Playlist | 2 = Repeat Track | 3 = Random Play | 4 = Shuffle Track | 5 = Shuffle Album | 6 = Shuffle Folders', action='store')
        args_http.add_argument('--repeat-off', help='Repeat Off', action='store_true')
        args_http.add_argument('--repeat-playlist', help='Repeat Playlist', action='store_true')
        args_http.add_argument('--repeat-track', help='Repeat Track', action='store_true')
        args_http.add_argument('--repeat-random', help='Random Play', action='store_true')
        args_http.add_argument('--shuffle-track', help='Shuffle Track', action='store_true')
        args_http.add_argument('--shuffle-album', help='Shuffle Album', action='store_true')
        args_http.add_argument('--shuffle-folder', help='Shuffle by Folder', action='store_true')
        args_http.add_argument('--seek', help='Seek for a second', action='store')
        args_http.add_argument('--root', help='Root path / Directory Containt Music files, this is for One Folder Files Selected', action='store')

        if len(sys.argv) == 1:
            if self.ctype == 'http':
                args_http.parse_args(['http', '-h'])
                options, args = args_http.parse_args()
                print("\n")
                print("Controller Use 'HTTP'")
            elif self.ctype == 'com':
                args_com.parse_args(['com', '-h'])
                print("\n")
                print("Controller Use 'COM Server'")
            else:
                parser.print_help()
        elif print_help:
            parser.print_help()
        else:        
            if self.ctype == 'http':
                options = args_http.parse_args()
                if options.host:
                    self.DATA.update({'url':options.host})
                if options.port:
                    self.DATA.update({'port':options.port})
                if options.version == 1:
                    print(self.getVersion())
                elif options.version == 2:
                    verbosity = True
                else:
                    verbosity = False
                if options.type_controller:
                    if options.type_controller == 'com' or options.type_controller == 'http':
                        self.ctype = options.type_controller
                        if options.change_config:
                            self.write_config(options.change_config)
                            if options.host:
                                configset.write_config('HTTP', 'server', self.conf, options.host)
                            if options.port:
                                configset.write_config('HTTP', 'port', self.conf, options.port)                         
                elif options.change_config:
                    #if options.type_controller:
                        #configset.write_config('CONTROL', 'type', self.conf, options.type_controller)
                    #if options.host:
                        #configset.write_config('HTTP', 'server', self.conf, options.host)
                    #if options.port:
                        #configset.write_config('HTTP', 'port', self.conf, options.port)
                    self.write_config(options.change_config)
                elif options.section:
                    if options.option:
                        print(configset.write_config2(options.section, options.option[0], self.conf, options.option[1]))
                    else:
                        args_http.parse_args(['http', '-h'])
                if options.clear_playlist:
                    self.clearPlaylist()
                elif options.play:
                    self.play()
                elif options.play_track:
                    self.playTrack(str(int(options.play_track) - 1))
                elif options.stop:
                    self.stop()
                elif options.pause:
                    self.pause()
                elif options.previous:
                    self.previous()
                elif options.next:
                    self.next()
                elif options.random:
                    self.random()
                elif options.volume:
                    self.volume(options.volume)
                elif options.repeat:
                    self.repeat(options.repeat)
                elif options.repeat_track:
                    self.repeat(2)
                elif options.repeat_playlist:
                    self.repeat(1)
                elif options.repeat_off:
                    self.repeat(0)
                elif options.repeat_random:
                    self.repeat(3)
                elif options.shuffle_track:
                    self.repeat(4)
                elif options.shuffle_album:
                    self.repeat(5)
                elif options.shuffle_folder:
                    self.repeat(6)
                # else:
                #     args_http.parse_args(['http', '-h'])
                if options.mute:    
                    self.mute()
                if options.browser:
                    self.browser()                
                if options.info:
                    self.info()    
                if options.addfiles:
                    # print "os.getcwd() =", os.getcwd()
                    if options.clear_playlist:
                        self.clearPlaylist()
                    add_files = []
                    for i in options.addfiles:
                        if options.root:
                            i = os.path.join(options.root, i)
                        else:
                            i = os.path.abspath(i)
                        # print "i =", i
                        files = self.format_alias_dir(i, options.dir_alias, options.level_alias, verbosity)
                        add_files.append(files)
                    self.addFiles(add_files)
                
                if options.addfilesplay:
                    if options.clear_playlist:
                        self.clearPlaylist()
                    add_files = []
                    for i in options.addfilesplay:
                        if options.root:
                            i = os.path.join(options.root, i)
                        else:
                            i = os.path.abspath(i)
                        # print "i =", i
                        files = self.format_alias_dir(i, options.dir_alias, options.level_alias, verbosity)
                        print(make_colors("Add file:", 'lw', 'g') + " ", make_colors(files, 'lw', 'bl'))
                        add_files.append(files)
                    self.addFiles(add_files)
                    self.stop()
                    STATUS = self.foobar2000.info(print_info=False)
                    if not STATUS:
                        STATUS = 'Stoped'
                    print(make_colors("STATUS:", 'lw', 'm'), make_colors(STATUS, 'lw', 'c'))
                    if not STATUS or STATUS == None or STATUS == "None" or STATUS == 'Stoped':
                        self.play()
                        # if self.check_playlist(add_files, self.foobar2000.playlist()[0:][0]):
                        #     print("Play ...")
                        #     self.play()
                
                if options.addfolder:
                    verbosity = False
                    if options.version == 2:
                        verbosity = True
                    
                    add_folders = []
                    for i in options.addfolder:
                        folder = self.format_alias_dir(i, options.dir_alias, options.level_alias, verbosity)
                        #print("folder [778] =", folder)
                        print(make_colors("Add Folder to Play:", 'b', 'y'), make_colors(folder, 'lw', 'bl'))
                        # print("self.add_resursive_folders(folder)=", self.add_resursive_folders(folder))
                        if len(self.add_resursive_folders(folder)[0]) > 0:
                            add_folders += self.add_resursive_folders(folder)[0]
                            add_folders.insert(0, folder)
                        if len(options.addfolder) == 1:
                            add_folders.insert(0, folder)
                    
                    if add_folders:
                        add_folders = list(set(add_folders))
                    add_folders = sorted(list(filter(lambda k: self.file_listing(k), add_folders)), reverse = True)
                    # print("add_folders =", add_folders)
                    # pause()                    
                    if add_folders:
                        # print("add_folders[0] =", add_folders[0])
                        self.playFolder(self.format_alias_dir(add_folders[0], options.dir_alias, options.level_alias, verbosity), verbosity, False, False, options.host, options.port)
                        all_files = self.file_listing(add_folders[0])
                        # print("all_files =", all_files)
                        # print("len(all_files) 0 =", len(all_files))
                        # pause()
                        for i in add_folders[1:]:
                            # print("i =", i)
                            file_numbers = self.file_listing(i)
                            # print("len(file_numbers) =", len(file_numbers))
                            # print("file_listing =", file_numbers)
                            if len(file_numbers) > 0:
                                folder = self.format_alias_dir(i, options.dir_alias, options.level_alias, verbosity)
                                # print("folder =", folder)
                                self.playFolder(folder, verbosity, False, False, options.host, options.port)
                                
                                all_files += file_numbers
                                current_playlist, last = self.foobar2000.playlist()[0:]

                                if last > 0:
                                    current_playlist = []
                                    for p in range(1, last+1):
                                        cp, last = self.foobar2000.playlist(p)[0:]
                                        current_playlist += cp
                                
                                # print("playlist =", self.foobar2000.playlist()[0])
                                # print("len(all_files) 1 =", len(all_files))
                                # print("len playlist   1 =", len(current_playlist))
                                # print("LAST =", last)
                                # pause()
                                while 1:
                                    # print("len(all_files) 2 =", len(all_files))
                                    # print("len playlist   2 =", len(current_playlist))
                                    if len(all_files) == len(current_playlist):
                                        break
                                    else:
                                        # time.sleep(1)
                                        current_playlist, last = self.foobar2000.playlist()[0:]
                                        # print("last =", last)
                                        # print("len current_playlist 1 =", len(current_playlist))
                                        if last > 0:
                                            current_playlist = []
                                            for p in range(1, last+1):
                                                cp, last = self.foobar2000.playlist(p)[0:]
                                                # print("len(cp) =", len(cp))
                                                current_playlist += cp
                                        # print("len current_playlist 2 =", len(current_playlist))
                            # pause()
                        
                    else:
                        all_files = []
                        for i in options.addfolder:
                            file_numbers = self.file_listing(i)
                            # print("file_listing =", file_numbers)
                            all_files += file_numbers
                            folder = self.format_alias_dir(i, options.dir_alias, options.level_alias, verbosity)
                            if options.version == 2:
                                verbosity = True
                            self.playFolder(folder, verbosity, False, False, options.host, options.port)
                            current_playlist, last = self.foobar2000.playlist()[0:]
                            if last > 0:
                                current_playlist = []
                                for p in range(1, last+1):
                                    cp, last = self.foobar2000.playlist(p, current_playlist)[0:]
                                    current_playlist += cp
                            while 1:
                                # print("len(all_files) =", len(all_files))
                                # print("len playlist =", len(current_playlist))
                                if len(all_files) == len(self.foobar2000.playlist()[0:][0]):
                                    break
                                else:
                                    time.sleep(1)
                                    current_playlist, last = self.foobar2000.playlist()[0:]
                                    if last > 0:
                                        current_playlist = []
                                        for p in range(1, last+1):
                                            cp, last = self.foobar2000.playlist(p, current_playlist)[0:]
                                            current_playlist += cp
                    
                    verbosity = False
        
                if options.addfolderplay:
                    verbosity = False
                    if options.version == 2:
                        verbosity = True
                    self.clearPlaylist()
                    self.stop()
                    self.clearPlaylist()
                    add_folders = []
                    for i in options.addfolderplay:
                        folder = self.format_alias_dir(i, options.dir_alias, options.level_alias, verbosity)
                        print(make_colors("Add Folder to Play:", 'b', 'y'), make_colors(folder, 'lw', 'bl'))
                        # print("self.add_resursive_folders(folder)=", self.add_resursive_folders(folder))
                        if len(self.add_resursive_folders(folder)[0]) > 0:
                            add_folders += self.add_resursive_folders(folder)[0]
                            add_folders.insert(0, folder)
                        if len(options.addfolderplay) == 1:
                            add_folders.insert(0, folder)
                    
                    if add_folders:
                        add_folders = list(set(add_folders))

                    add_folders = sorted(list(filter(lambda k: self.file_listing(k), add_folders)), reverse = True)
                    if add_folders:
                        # print("add_folders[0] =", add_folders[0])
                        self.playFolder(self.format_alias_dir(add_folders[0], options.dir_alias, options.level_alias, verbosity), verbosity, False, True, options.host, options.port)
                        all_files = self.file_listing(self.format_alias_dir(add_folders[0], options.dir_alias, options.level_alias, verbosity))
                        time.sleep(2)
                        STATUS = self.foobar2000.info(print_info=False)
                        if not STATUS:
                            STATUS = 'Stoped'
                        if isinstance(STATUS, list):
                            STATUS = " ".join(STATUS)
                        print(make_colors("STATUS:", 'lw', 'bl'), make_colors(STATUS, 'lw', 'lr'))
                        if not STATUS or STATUS == None or STATUS == "None" or STATUS == 'Stoped':    
                            if self.check_playlist(all_files, self.foobar2000.playlist()[0:][0]):
                                self.play()
                        
                        for i in add_folders[1:]:
                            # print("i =", i)
                            file_numbers = self.file_listing(i)
                            if len(file_numbers) > 0:
                                folder = self.format_alias_dir(i, options.dir_alias, options.level_alias, verbosity)
                                # print("folder =", folder)
                                self.playFolder(folder, verbosity, False, False, options.host, options.port)
                                
                                all_files += file_numbers
                                current_playlist, last = self.foobar2000.playlist()[0:]

                                if last > 0:
                                    current_playlist = []
                                    for p in range(1, last+1):
                                        cp, last = self.foobar2000.playlist(p)[0:]
                                        current_playlist += cp
                                
                                # print("playlist =", self.foobar2000.playlist()[0])
                                # print("len(all_files) 1 =", len(all_files))
                                # print("len playlist   1 =", len(current_playlist))
                                # print("LAST =", last)
                                # pause()
                                self.check_playlist(all_files, playlist = current_playlist)
    
                    else:
                        all_files = []
                        for i in options.addfolderplay:
                            file_numbers = self.file_listing(i)
                            # print("file_listing =", file_numbers)
                            all_files += file_numbers
                            folder = self.format_alias_dir(i, options.dir_alias, options.level_alias, verbosity)
                            if options.version == 2:
                                verbosity = True
                            self.playFolder(folder, verbosity, False, False, options.host, options.port)
                            if len(options.addfolderplay) > 0:
                                self.play()
                            current_playlist, last = self.foobar2000.playlist()[0:]
                            if last > 0:
                                current_playlist = []
                                for p in range(1, last+1):
                                    cp, last = self.foobar2000.playlist(p, playlist = current_playlist)[0:]
                                    current_playlist += cp
                            while 1:
                                # print("len(all_files) =", len(all_files))
                                # print("len playlist =", len(current_playlist))
                                if len(all_files) == len(self.foobar2000.playlist()[0:][0]):
                                    break
                                else:
                                    time.sleep(1)
                                    current_playlist, last = self.foobar2000.playlist()[0:]
                                    # debug(current_playlist = current_playlist, debug = True)
                                    if last > 0:
                                        current_playlist = []
                                        for p in range(1, last+1):
                                            # debug(current_playlist = current_playlist, debug = True)
                                            cp, last = self.foobar2000.playlist(p, playlist = current_playlist)[0:]
                                            current_playlist += cp
                                        break
                    
                        if len(options.addfolderplay) == 1:
                            self.play()
                    verbosity = False
                    time.sleep(2)
                    STATUS = self.foobar2000.info(print_info=False)
                    if not STATUS:
                        STATUS = 'Stoped'
                    if isinstance(STATUS, list):
                        STATUS = " ".join(STATUS)
                    print(make_colors("STATUS:", 'lw', 'bl'), make_colors(STATUS, 'lw', 'lr'))
                    if not STATUS or STATUS == None or STATUS == "None" or STATUS == 'Stoped':
                        if self.check_playlist(all_files, self.foobar2000.playlist()[0:][0]):
                            print("Play ...")
                            self.play()

                if options.list:
                    self.info()
                    print("\n")
                    #time.sleep(4)
                    self.playlist()
                    # print("\n")
                if options.seek:
                    self.seekSecond(options.seek)
                if options.usage:
                    parser.print_help()
                if options.read_config:
                    self.readConfig()
                if options.del_track:
                    all_tracks = []
                    for i in options.del_track:
                        if "," in i:
                            all_tracks += i.split(",")
                        elif "-" in i:
                            fr, to = i.split("-")
                            if fr and to:
                                all_tracks += list(range(int(fr.strip()), int(to.strip()) + 1))
                        else:
                            all_tracks.append(i)

                    self.deltrack(all_tracks)
                

            elif self.ctype == 'com':
                options = args_com.parse_args()
                if options.list:
                    self.setconfig(1000)
                elif options.type_controller:
                    if options.type_controller == 'com' or options.type_controller == 'http':
                        self.ctype = options.type_controller
                        if options.change_config:
                            configset.write_config('CONTROL', 'type', self.conf, options.type_controller)
                elif options.change_config:
                    if options.type_controller:
                        configset.write_config('CONTROL', 'type', self.conf, options.type_controller)
                if options.type:
                    if self.config(options.type):
                        pass
                    else:
                        print("ERROR !!!")
                        print(self.error)
                elif options.section:
                    if options.option:
                        print(configset.write_config2(options.section, options.option[0], self.conf, options.option[1]))
                    else:
                        print("\n")
                        args_http.parse_args(['com', '-h'])                
                elif options.kill:
                    self.kill() 
                elif options.open:
                    self.open()
                # elif options.close:
                #     self.close()   
                elif options.clear:
                    self.clear()
                elif options.play:
                    self.play()
                elif options.stop:
                    self.stop()
                elif options.pause:
                    self.pause()
                elif options.previous:
                    self.previous()
                elif options.__next__:
                    next(self)
                elif options.random:
                    self.random()
                elif options.volume:
                    self.volume(options.volume)
                elif options.mute:
                    self.mute()
                elif options.info:
                    self.info()
                elif options.usage:
                    parser.print_help() 
                elif options.read_config:
                    self.readConfig()                
                else:
                    print("\n")
                    args_com.parse_args(['http', '-h'])
            else:
                print("\n")
                print("Please re-config Type Of Controller in Config File !")
                print("\n")
                parser.print_help()

if __name__ == "__main__":
    c = control()
    c.usage()
    # c.format_playlist()
