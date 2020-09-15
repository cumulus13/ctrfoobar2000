Description
----------------------
Control Foobar2000 with python + Command line

Usage
-----------
		Usage: foobar.py [options]

		usage: foobar.py http [-h] [-p] [-t PLAY_TRACK] [-s] [-P] [-n] [-r] [-R]
                      [-V VOLUME] [-m] [-i] [-f ADDFOLDER] [-F ADDFOLDERPLAY]
                      [-c] [-d [DEL_TRACK [DEL_TRACK ...]]] [-l] [-b]
                      [-S TYPE_CONTROLLER] [-x] [-H HOST] [-O PORT] [-?] [-g]
                      [-T SECTION] [-E OPTION OPTION] [-a DIR_ALIAS]
                      [-L LEVEL_ALIAS]

		optional arguments:
		  -h, --help            show this help message and exit
		  -p, --play            Play Playback
		  -t PLAY_TRACK, --play-track PLAY_TRACK
		                        Play Playback Track No
		  -s, --stop            Stop Playback
		  -P, --pause           Pause Playback
		  -n, --next            Next Play
		  -r, --previous        Previous Play
		  -R, --random          Play Random
		  -V VOLUME, --volume VOLUME
		                        Set Volume, range is -100 <= value <= 0
		  -m, --mute            Mute Volume
		  -i, --info            Get info current Playing
		  -f ADDFOLDER, --addfolder ADDFOLDER
		                        Add Remote Folder Queue [HTTP]
		  -F ADDFOLDERPLAY, --addfolderplay ADDFOLDERPLAY
		                        Add Remote Folder Queue & Play it [HTTP]
		  -c, --clear-playlist  Clear Current Playlist [HTTP]
		  -d [DEL_TRACK [DEL_TRACK ...]], --del-track [DEL_TRACK [DEL_TRACK ...]]
		                        Delete Playlist [HTTP], example: foobar -d 1 2 3
		  -l, --list            List Playlist
		  -b, --browser         Browser Library
		  -S TYPE_CONTROLLER, --type-controller TYPE_CONTROLLER
		                        Set Type Of Controller [com,http]
		  -x, --store-config    Store Set Type Of Controller [com,http]
		  -H HOST, --host HOST  Remote Host control Address [HTTP]
		  -O PORT, --port PORT  Remote Port control Address [HTTP]
		  -?, --usage           Print All Help
		  -g, --read-config     Read config file
		  -T SECTION, --section SECTION
		                        Set Section Config
		  -E OPTION OPTION, --option OPTION OPTION
		                        Set Option Config
		  -a DIR_ALIAS, --dir-alias DIR_ALIAS
		                        Root of Directory Alias On Server
		  -L LEVEL_ALIAS, --level-alias LEVEL_ALIAS
		                        Level Root of Directory Alias On Server


Dependency
------------------
+ Foobar2000 COMServer2Helper
+ Foobar2000 HTTP Control

Author
-----------
licface (licface@yahoo.com)