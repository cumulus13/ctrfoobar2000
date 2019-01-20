import sys,os
import errno
import traceback
from subprocess import Popen

def main(data):
    
    sprt = " "
    
    try:
        #os.system("start " + data + sprt + sys.argv[1])
        #os.execlp(data).joint(sys.argv[1])
        #os.system(data)
        #os.startfile(data)
        if len(data) == 2:
            Popen([str(data[0]) , str(data[1])])
        else:
            #Popen([data , " "])
            if ".bat" in data:
                os.system(data)
            else:
                os.startfile(data)
        """
        if "notepad" in str(data):
            mypath = r"c:\WINDOWS"
            data_pre = str(data).split("notepad")
            #datax = os.path.split(data_pre[0])
            print "data_pre = ", data_pre
            #print "datax = ", datax
            
            os.spawnv(os.P_WAIT, r"c:\WINDOWS", ('notepad', str(data_pre[1])))
        else:
            datax = os.path.split(data)
            print "datax = ", datax
            os.spawnv(os.P_WAIT, str(datax[0]), (str(data[1]), ''))
        
        #if data_pre[1] != None or data_pre[1] != "" or data_pre[1] != 0:
        #    os.spawnv(os.P_NOWAIT, datax[0], data[1], data_pre[1])
        #else:
        #    os.spawnv(os.P_NOWAIT, datax[0], data[1], '')
        """
    except OSError, e:
        data_e = traceback.format_exc()
        if e.errno == errno.ENOEXEC:
            #os.system("cls")
            print "\n";
            print "\t\t Program Tidak Dapat Di Eksekusi !"
            print "\n"
            print "\t\t Programming development : "
            print "\n"
            print "\t\t " + str(data_e)
        elif e.errno == errno.ENOENT:
            #os.system("cls")
            print "\n";
            print "\t\t Program Tidak Dapat Ditemukan !"
            print "\n"
            print "\t\t Programming development : "
            print "\n"
            print "\t\t " + str(data_e)
        else:
            #os.system("cls")
            print "\n";
            print "\t\t Program Tidak Dapat Berjalan Pada Mode System Operasi Win32 !"
            print "\n"
            print "\t\t Programming development : "
            print "\n"
            print "\t\t " + str(data_e)
            
    except IndexError, e:
        os.system('cls')
        data_e = traceback.format_exc()
        print "\n"
        print "\t\t Programming development : "
        print "\n"
        print "\t\t " + str(data_e)

def kill(data):
    
    sprt = " "
    
    try:
        data2 = os.path.split(data)[1]
        #os.system("start " + data + sprt + sys.argv[1])
        #os.execlp(data).joint(sys.argv[1])
        os.system("processx -k " + data2)
        
    except OSError, e:
        
        if e.errno == errno.ENOEXEC:
            #os.system("cls")
            print "\n";
            print "\t\t Program Tidak Dapat Di Eksekusi !"
        elif e.errno == errno.ENOENT:
            #os.system("cls")
            print "\n";
            print "\t\t Program Tidak Dapat Ditemukan !"
        else:
            #os.system("cls")
            print "\n";
            print "\t\t Program Tidak Dapat Berjalan Pada Mode System Operasi Win32 !"
            
    except IndexError, e:
        os.system('cls')
        print "\n"
        print "\t Error With Status : ", e
