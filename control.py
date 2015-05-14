import traceback
import configset
import argparse
import sys
import os
import subprocess

class control(object):
    def __init__(self, host=None, port=None):
        super(control, self)
        self.host = host
        self.port = port
        self.conf = configset.get_config_file('pyfoobar.ini')
        cfg = configset.cfg
        cfg.read(self.conf)
        self.type_foobar = cfg.options('TYPE')
        self.error = ''
        self.nircmd = r"c:\EXE\nircmd.exe"
        self.ctype = configset.read_config('CONTROL', 'type')
        if self.ctype == 'com':
            import pyfoobar
            self.foobar2000 = pyfoobar.foobar()
        elif self.ctype == 'http':
            import pyfoobar_http
            self.foobar2000 = pyfoobar_http.foobar(self.host, self.port)
        if not os.getenv('PROCESSOR_ARCHITECTURE') == 'x86':
            self.prog_path = os.getenv('ProgramFiles(x86)')
        else:
            self.prog_path = os.getenv('ProgramFiles')       

    def play(self):
        #print "self.ctype =", self.ctype
        #print "self.foobar2000 =", self.foobar2000
        try:
            return self.foobar2000.play()
        except:
            #print traceback.format_exc_syslog_growl(True)
            self.check_connection()
            print "\t Error communication with Foobar2000 [COM|HTTP] Server !"

    def stop(self):
        try:
            return self.foobar2000.stop()
        except:
            self.check_connection()
            print "\t Error communication with Foobar2000 [COM|HTTP] Server !"

    def pause(self):
        try:
            return self.foobar2000.pauseplay()
        except:
            self.check_connection()
            print "\t Error communication with Foobar2000 [COM|HTTP] Server !"

    def previous(self):
        try:
            return self.foobar2000.previous()
        except:
            self.check_connection()
            print "\t Error communication with Foobar2000 [COM|HTTP] Server !"

    def next(self):
        try:
            return self.foobar2000.next()
        except:
            self.check_connection()
            print "\t Error communication with Foobar2000 [COM|HTTP] Server !"

    def random(self):
        try:
            return self.foobar2000.playRandom()
        except:
            self.check_connection()
            print "\t Error communication with Foobar2000 [COM|HTTP] Server !"

    def volume(self, vol):
        try:
            return self.foobar2000.setVolumeLevel(vol)
        except:
            self.check_connection()
            print "\t Error communication with Foobar2000 [COM|HTTP] Server !"

    def mute(self):
        try:
            return self.foobar2000.mute()
        except:
            self.check_connection()
            print "\t Error communication with Foobar2000 [COM|HTTP] Server !"

    def info(self):
        try:
            print "\n"
            print "\t Track    :", self.foobar2000.getCurrentTrack()
            print "\t Artist   :", self.foobar2000.getCurrentArtist()
            print "\t Album    :", self.foobar2000.getCurrentAlbum()
            print "\t Playlist :", self.foobar2000.currentActivePlaylist()
            state_play = self.foobar2000.isPlaying()
            state_pause = self.foobar2000.isPaused()
            if state_play:
                print "\t State    : Playing"
            elif state_pause:
                print "\t State    : Pause"
            else:
                print "\t State    : Unknown"

        except:
            self.check_connection()
            print "\t Error communication with Foobar2000 [COM|HTTP] Server !"

    def clearPlaylist(self):
        return self.foobar2000.clearPlaylist()

    def addFolder(self, folder):
        return self.foobar2000.addFolder(folder)

    def playFolder(self, folder):
        return self.foobar2000.playFolder(folder)

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
        if os.path.isdir(os.path.join(self.prog_path, 'foobar2000')):
            os.rmdir(os.path.join(self.prog_path, 'foobar2000'))
        if os.path.isdir(os.path.join(os.getenv('appdata'), 'foobar2000')):
            os.rmdir(os.path.join(os.getenv('appdata'), 'foobar2000'))

    def open(self):
        import module002a
        del(sys.argv[1])
        data = ['c:\\Program Files\\foobar2000\\foobar2000.exe']
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
                print "\t " + str(self.type_foobar.index(l) + 1) + ".", str(l2[0]).title(), str(l2[1]).title()
            print "\n"
            q = raw_input("Please Select your Type [use option -t for direct option]: ")
            if q == '':
                usage(True)
            else:
                q = int(q)
                self.config(q, verbosity)
        else:
            usage(True)

    def readConfig(self):
        f = open(self.conf).read()
        print f
        print "\n"
        print configset.read_all_config(self.conf)
        print "\n"

    def check_connection(self):
        if self.foobar2000.check_connection() != True:
            print "\t Please re-config config file for server and host or use option -H and option -O [HTTP]"
            print "\n"          
        return self.foobar2000.check_connection()

    def usage(self, print_help=None):
        print "\n"
        parser = argparse.ArgumentParser()
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
        parser.add_argument('-x', '--store-config', help='Store Set Type Of Controller [com,http]', action='store_true')
        parser.add_argument('-f', '--addfolder', help='Add Remote Folder Queue [HTTP]', action='store')
        parser.add_argument('-F', '--addfolderplay', help='Add Remote Folder Queue & Play it [HTTP]', action='store')
        parser.add_argument('-c', '--clear-playlist', help='Clear Current Playlist [HTTP]', action='store_true')
        parser.add_argument('-H', '--host', help="Remote Host control Address [HTTP]", action='store')
        parser.add_argument('-O', '--port', help="Remote Port control Address [HTTP]", action='store')      
        parser.add_argument('-g', '--read-config', help="Read config file", action="store_true")
        parser.add_argument('-?', '--usage', help='Print All Help', action='store_true')
        parser.add_argument('-T', '--section', help="Set Section Config", action="store")
        parser.add_argument('-E', '--option', help="Set Option Config", action="store", nargs=2)        

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
        args_com.add_argument('-x', '--store-config', help='Store Set Type Of Controller [com,http]', action='store_true')
        args_com.add_argument('-?', '--usage', help='Print All Help', action='store_true')
        args_com.add_argument('-g', '--read-config', help="Read config file", action="store_true")
        args_com.add_argument('-T', '--section', help="Set Section Config", action="store")
        args_com.add_argument('-E', '--option', help="Set Option Config", action="store", nargs=2)

        args_http = subparser.add_parser('http', help='Type Controller "http"')
        args_http.add_argument('-p', '--play', help='Play Playback', action='store_true')
        args_http.add_argument('-s', '--stop', help='Stop Playback', action='store_true')
        args_http.add_argument('-P', '--pause', help='Pause Playback', action='store_true')
        args_http.add_argument('-n', '--next', help='Next Play', action='store_true')
        args_http.add_argument('-r', '--previous', help='Previous Play', action='store_true')
        args_http.add_argument('-R', '--random', help='Play Random', action='store_true')
        args_http.add_argument('-V', '--volume', help='Set Volume, range is -100 <= value <= 0', action='store')
        args_http.add_argument('-m', '--mute', help='Mute Volume', action='store_true')
        args_http.add_argument('-i', '--info', help='Get info current Playing', action="store_true")
        args_http.add_argument('-f', '--addfolder', help='Add Remote Folder Queue [HTTP]', action='store')
        args_http.add_argument('-F', '--addfolderplay', help='Add Remote Folder Queue & Play it [HTTP]', action='store')
        args_http.add_argument('-c', '--clear-playlist', help='Clear Current Playlist [HTTP]', action='store_true')
        args_http.add_argument('-l', '--list', help='List Playlist', action='store_true')
        args_http.add_argument('-S', '--type-controller', help='Set Type Of Controller [com,http]', action='store')
        args_http.add_argument('-x', '--store-config', help='Store Set Type Of Controller [com,http]', action='store_true')
        args_http.add_argument('-H', '--host', help="Remote Host control Address [HTTP]", action='store')
        args_http.add_argument('-O', '--port', help="Remote Port control Address [HTTP]", action='store')
        args_http.add_argument('-?', '--usage', help='Print All Help', action='store_true')
        args_http.add_argument('-g', '--read-config', help="Read config file", action="store_true")
        args_http.add_argument('-T', '--section', help="Set Section Config", action="store")
        args_http.add_argument('-E', '--option', help="Set Option Config", action="store", nargs=2)        

        if len(sys.argv) == 1:
            if self.ctype == 'http':
                args_http.parse_args(['http', '-h'])
                options, args = args_http.parse_args()
                print "\n"
                print "Controller Use 'HTTP'"
            elif self.ctype == 'com':
                args_com.parse_args(['com', '-h'])
                print "\n"
                print "Controller Use 'COM Server'"
            else:
                parser.print_help()
        elif print_help:
            parser.print_help()
        else:
            if self.ctype == 'http':
                options = args_http.parse_args()
                #self.__init__(options.host, options.port)
                #if options.host:
                    #self.host = options.host
                #if options.port:
                    #self.port = options.port
                if options.type_controller:
                    if options.type_controller == 'com' or options.type_controller == 'http':
                        self.ctype = options.type_controller
                elif options.store_config:
                    if options.type_controller:
                        configset.write_config('CONTROL', 'type', self.conf, options.type_controller)
                    if options.host:
                        configset.write_config('HTTP', 'server', self.conf, options.host)
                    if options.host:
                        configset.write_config('HTTP', 'port', self.conf, options.port)     
                elif options.section:
                    if options.option:
                        print configset.write_config2(options.section, options.option[0], self.conf, options.option[1])
                    else:
                        args_http.parse_args(['http', '-h'])
                elif options.clear_playlist:
                    self.clearPlaylist()
                elif options.play:
                    #print "option PLAY"
                    self.play()
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
                elif options.mute:
                    self.mute()
                elif options.info:
                    self.info()    
                elif options.list:
                    print "NOT YEST !!!"  
                elif options.addfolder:
                    self.addFolder(options.addfolder)
                elif options.addfolderplay:
                    self.playFolder(options.addfolderplay)
                elif options.usage:
                    parser.print_help()
                elif options.read_config:
                    self.readConfig()
                else:
                    args_http.parse_args(['http', '-h'])

            elif self.ctype == 'com':
                options = args_com.parse_args()
                if options.list:
                    self.setconfig(1000)
                elif options.type_controller:
                    if options.type_controller == 'com' or options.type_controller == 'http':
                        self.ctype = options.type_controller
                elif options.store_config:
                    if options.type_controller:
                        configset.write_config('CONTROL', 'type', self.conf, options.type_controller)
                if options.type:
                    if self.config(options.type):
                        pass
                    else:
                        print "ERROR !!!"
                        print self.error
                elif options.section:
                    if options.option:
                        print configset.write_config2(options.section, options.option[0], self.conf, options.option[1])
                    else:
                        args_http.parse_args(['com', '-h'])                
                elif options.kill:
                    self.kill() 
                elif options.open:
                    self.open()
                elif options.close:
                    self.close()   
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
                elif options.next:
                    self.next()
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
                    args_com.parse_args(['http', '-h'])
            else:
                print "\n"
                print "Please re-config Type Of Controller in Config File !"
                print "\n"
                parser.print_help()

if __name__ == "__main__":
    c = control()
    c.usage()