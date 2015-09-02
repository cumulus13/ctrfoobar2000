#!/usr/bin/python

import os, sys
if os.path.isdir(r'c:/pyx'):
    sys.path.insert(0, r'c:\\pyx')
if sys.platform == 'win32':
    import module002a
if not os.path.isdir(r'f:\PROJECTS'):
    raise SystemError('Please re-Set module ctrlfoobar2000 !')
sys.path.insert(0, 'f:\PROJECTS')
#os.chdir('f:\PROJECTS\ctrfoobar2000')
from ctrfoobar2000 import control
foobar = control.control()

class foobarx(control.control):
    # def __init__(self):
    args = ['-h', '-l', '-p', '-s', '-P', '-n', '-r', '-R', '-V', '-M', '-i', '-t', '-c', '-k', '-C']
    ctype = foobar.ctype
    foobar2000 = foobar.foobar2000
    type_foobar = foobar.type_foobar
    prog_path = foobar.prog_path
    conf = foobar.conf
    host = foobar.host
    port = foobar.port
    # super(foobarx, self)

    def usagex():
        if len(sys.argv) == 1:
            c.usage()
            # data = ['c:\\Program Files\\foobar2000\\foobar2000.exe']
            # module002a.main(data)
        elif len(sys.argv) == 2:
            if sys.platform == 'win32':
                if sys.argv[1] not in args:
                    if os.path.isdir(sys.argv[1]) or os.path.isfile(sys.argv[1]):
                        data1 = [r'c:\\PROGRA~1\\foobar2000\\foobar2000.exe']
                        data2 = [r'c:\\PROGRA~2\\foobar2000\\foobar2000.exe']
                        if os.path.isfile(data1[0]):
                            module002a.main(data1)
                        else:
                            module002a.main(data2)
                    elif sys.argv[1] == '-o' or sys.argv[1] == '-O':
                        # data = ['c:\\Program Files\\foobar2000\\foobar2000.exe']
                        # module002a.main(data)
                        # c.usage()
                        usage()
                    else:
                        usage()
                else:
                    usage()
            else:
                print "\t your are not windows os !"
        else:
            usage()

if __name__ == "__main__":
    c = foobarx()
    c.usagex()
