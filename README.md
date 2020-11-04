Description
----------------------
Control Foobar2000 with python + Command line

Usage
-----------
	usage: control.py  [-h] [-p] [-t PLAY_TRACK] [-s] [-P] [-n] [-r] [-R]
                       [-V VOLUME] [-m] [-i] [-f [ADDFOLDER [ADDFOLDER ...]]]
                       [-fi [ADDFILES [ADDFILES ...]]]
                       [-F [ADDFOLDERPLAY [ADDFOLDERPLAY ...]]]
                       [-Fi [ADDFILESPLAY [ADDFILESPLAY ...]]] [-c]
                       [-d [DEL_TRACK [DEL_TRACK ...]]] [-l] [-b]
                       [-S TYPE_CONTROLLER] [-H HOST] [-O PORT] [-?] [-g]
                       [-x [CHANGE_CONFIG [CHANGE_CONFIG ...]]] [-T SECTION]
                       [-E OPTION OPTION] [-a DIR_ALIAS] [-v] [-L LEVEL_ALIAS]
                       [-z REPEAT] [--repeat-off] [--repeat-playlist]
                       [--repeat-track] [--repeat-random] [--shuffle-track]
                       [--shuffle-album] [--shuffle-folder] [--seek SEEK]
                       [--root ROOT]

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
	  -f [ADDFOLDER [ADDFOLDER ...]], --addfolder [ADDFOLDER [ADDFOLDER ...]]
							Add Remote Folder Queue [HTTP]
	  -fi [ADDFILES [ADDFILES ...]], --addfiles [ADDFILES [ADDFILES ...]]
							Add Remote Files Queue [HTTP]
	  -F [ADDFOLDERPLAY [ADDFOLDERPLAY ...]], --addfolderplay [ADDFOLDERPLAY [ADDFOLDERPLAY ...]]
							Add Remote Folder Queue & Play it [HTTP]
	  -Fi [ADDFILESPLAY [ADDFILESPLAY ...]], --addfilesplay [ADDFILESPLAY [ADDFILESPLAY ...]]
							Add Remote Folder Queue & Play it [HTTP]
	  -c, --clear-playlist  Clear Current Playlist [HTTP]
	  -d [DEL_TRACK [DEL_TRACK ...]], --del-track [DEL_TRACK [DEL_TRACK ...]]
							Delete Playlist [HTTP], example: foobar -d 1 2 3
	  -l, --list            List Playlist
	  -b, --browser         Browser Library
	  -S TYPE_CONTROLLER, --type-controller TYPE_CONTROLLER
							Set Type Of Controller [com,http]
	  -H HOST, --host HOST  Remote Host control Address [HTTP]
	  -O PORT, --port PORT  Remote Port control Address [HTTP]
	  -?, --usage           Print All Help
	  -g, --read-config     Read config file
	  -x [CHANGE_CONFIG [CHANGE_CONFIG ...]], --change-config [CHANGE_CONFIG [CHANGE_CONFIG ...]]
							Set Change config. format: section#option#value
	  -T SECTION, --section SECTION
							Set Section Config
	  -E OPTION OPTION, --option OPTION OPTION
							Set Option Config
	  -a DIR_ALIAS, --dir-alias DIR_ALIAS
							Root of Directory Alias On Server
	  -v, --version         -v = show version | -vv = verbosity process
	  -L LEVEL_ALIAS, --level-alias LEVEL_ALIAS
							Level Root of Directory Alias On Server
	  -z REPEAT, --repeat REPEAT
							Repeat 0 = Default (repeat off) | 1 = Repeat Playlist
							| 2 = Repeat Track | 3 = Random Play | 4 = Shuffle
							Track | 5 = Shuffle Album | 6 = Shuffle Folders
	  --repeat-off          Repeat Off
	  --repeat-playlist     Repeat Playlist
	  --repeat-track        Repeat Track
	  --repeat-random       Random Play
	  --shuffle-track       Shuffle Track
	  --shuffle-album       Shuffle Album
	  --shuffle-folder      Shuffle by Folder
	  --seek SEEK           Seek for a second
	  --root ROOT           Root path / Directory Containt Music files, this is
							for One Folder Files Selected


Dependency
------------------
+ Foobar2000 COMServer2Helper
+ Foobar2000 HTTP Control

Author
-----------
licface (licface@yahoo.com)