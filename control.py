# import pyfoobar
import configset
import optparse
import sys
import os
import subprocess

class control(object):
	def __init__(self):
		super(control, self)
		self.conf = configset.get_config_file('pyfoobar.ini')
		cfg = configset.cfg
		cfg.read(self.conf)
		self.type_foobar = cfg.options('TYPE')
		self.error = ''
		self.nircmd = r"c:\EXE\nircmd.exe"

	def play(self):
		import pyfoobar
		foobar2000 = pyfoobar.foobar()
		try:
			return foobar2000.play()
		except:
			print "\t Error communication with Foobar2000 COM Server !"

	def stop(self):
		import pyfoobar
		foobar2000 = pyfoobar.foobar()
		try:
			return foobar2000.stop()
		except:
			print "\t Error communication with Foobar2000 COM Server !"

	def pause(self):
		import pyfoobar
		foobar2000 = pyfoobar.foobar()
		try:
			return foobar2000.pauseplay()
		except:
			print "\t Error communication with Foobar2000 COM Server !"

	def previous(self):
		import pyfoobar
		foobar2000 = pyfoobar.foobar()
		try:
			return foobar2000.previous()
		except:
			print "\t Error communication with Foobar2000 COM Server !"

	def next(self):
		import pyfoobar
		foobar2000 = pyfoobar.foobar()
		try:
			return foobar2000.next()
		except:
			print "\t Error communication with Foobar2000 COM Server !"

	def random(self):
		import pyfoobar
		foobar2000 = pyfoobar.foobar()
		try:
			return foobar2000.playRandom()
		except:
			print "\t Error communication with Foobar2000 COM Server !"

	def volume(self, vol):
		import pyfoobar
		foobar2000 = pyfoobar.foobar()
		try:
			return foobar2000.setVolumeLevel(vol)
		except:
			print "\t Error communication with Foobar2000 COM Server !"

	def mute(self):
		import pyfoobar
		foobar2000 = pyfoobar.foobar()
		try:
			return foobar2000.mute()
		except:
			print "\t Error communication with Foobar2000 COM Server !"

	def info(self):
		import pyfoobar
		foobar2000 = pyfoobar.foobar()
		try:
			print "\n"
			print "\t Track    :", foobar2000.getCurrentTrack()
			print "\t Artist   :", foobar2000.getCurrentArtist()
			print "\t Album    :", foobar2000.getCurrentAlbum()
			print "\t Playlist :", foobar2000.currentActivePlaylist()
			state_play = foobar2000.isPlaying()
			state_pause = foobar2000.isPaused()
			if state_play:
				print "\t State    : Playing"
			elif state_pause:
				print "\t State    : Pause"
			else:
				print "\t State    : Unknown"

		except:
			print "\t Error communication with Foobar2000 COM Server !"

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
		if os.path.isdir(os.path.join(os.getenv('programfiles'), 'foobar2000')):
			os.rmdir(os.path.join(os.getenv('programfiles'), 'foobar2000'))
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
				if os.path.isdir(os.path.join(os.getenv('programfiles'), 'foobar2000')):
					os.rmdir(os.path.join(os.getenv('programfiles'), 'foobar2000'))
				if os.path.isdir(os.path.join(os.getenv('appdata'), 'foobar2000')):
					os.rmdir(os.path.join(os.getenv('appdata'), 'foobar2000'))
				os.chdir(os.getenv('programfiles'))
				os.system("mklink /d \"%s\\foobar2000\" \"%s\"" %(os.getenv('programfiles'), configset.read_config('TYPE', i)))
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

def usage(print_help=None):
	print "\n"
	# try:
	# 	c = control(pyfoobar.foobar)
	# except:
		# print "\t Error communication with Foobar2000 COM Server !"
	c = control()
	parser = optparse.OptionParser()
	parser.add_option('-l', '--list', help='List type of foobar2000', action='store_true')
	parser.add_option('-p', '--play', help='Play Playback', action='store_true')
	parser.add_option('-s', '--stop', help='Stop Playback', action='store_true')
	parser.add_option('-P', '--pause', help='Pause Playback', action='store_true')
	parser.add_option('-n', '--next', help='Next Play', action='store_true')
	parser.add_option('-r', '--previous', help='Previous Play', action='store_true')
	parser.add_option('-R', '--random', help='Play Random', action='store_true')
	parser.add_option('-V', '--volume', help='Set Volume, range is -100 <= value <= 0', action='store')
	parser.add_option('-m', '--mute', help='Mute Volume', action='store_true')
	parser.add_option('-i', '--info', help='Get info current Playing', action="store_true")
	parser.add_option('-t', '--type', help='Set Type of Foobar2000', action='store', type=int)
	parser.add_option('-C', '--clear', help='Clear all Configuration', action='store_true')
	parser.add_option('-k', '--kill', help='Terminate Foobar2000 running', action='store_true')
	parser.add_option('-o', '--open', help='Just run Foobar2000', action='store_true')
	parser.add_option('-c', '--close', help='Just close Foobar2000', action='store_true')
	options, args = parser.parse_args()
	if len(sys.argv) == 1:
		parser.print_help()
	elif print_help:
		parser.print_help()
	elif options.list:
		c.setconfig(1000)
	else:
		if options.type:
			# print "options.type =", options.type
			if c.config(options.type):
				pass
			else:
				print "ERROR !!!"
				print c.error
		elif options.kill:
			c.kill()
		elif options.clear:
			c.clear()
		elif options.open:
			c.open()
		elif options.close:
			c.close()
		else:
			if options.play:
				c.play()
			elif options.stop:
				c.stop()
			elif options.pause:
				c.pause()
			elif options.previous:
				c.previous()
			elif options.next:
				c.next()
			elif options.random:
				c.random()
			elif options.volume:
				c.volume(options.volume)
			elif options.mute:
				c.mute()
			elif options.info:
				c.info()

if __name__ == "__main__":
	# c = control()
	usage()
