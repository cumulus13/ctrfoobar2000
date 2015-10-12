#!/usr/bin/python
import configset
import os, sys

MODULE_PATH = configset.read_config('MODULE','path')

if sys.platform == 'win32':
    if os.path.isdir(r'c:/pyx'):
        sys.path.insert(0, r'c:\\pyx')    
    import module002a
if not os.path.isdir(MODULE_PATH):
    raise SystemError('Please re-Set module ctrlfoobar2000 !')
else:
    sys.path.insert(0, MODULE_PATH)

from ctrfoobar2000 import control
foobar = control.control()

class foobarx(control.control):
    def __init__(self):
        super(foobarx, self)
        self.args = ['-h', '-l', '-p', '-s', '-P', '-n', '-r', '-R', '-V', '-M', '-i', '-t', '-c', '-k', '-C']
        self.ctype = foobar.ctype
        self.foobar2000 = foobar.foobar2000
        self.type_foobar = foobar.type_foobar
        self.prog_path = foobar.prog_path
        self.conf = foobar.conf
        self.host = foobar.host
        self.port = foobar.port
        # super(foobarx, self)

    def usagex(self):
        if len(sys.argv) == 1:
            foobar.usage()
            # data = ['c:\\Program Files\\foobar2000\\foobar2000.exe']
            # module002a.main(data)
        elif len(sys.argv) == 2:
            if sys.platform == 'win32':
                if sys.argv[1] not in self.args:
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
                        foobar.usage()
                    else:
                        foobar.usage()
                else:
                    foobar.usage()
            else:
                print "\tWARNING: your are not windows os !\n"
                foobar.usage()
        else:
            foobar.usage()

if __name__ == "__main__":
    c = foobarx()
    c.usagex()
