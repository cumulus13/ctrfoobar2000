import os, errno
import cekstate
import sys, time
import module004
import module002
import module006

filename = os.path.split(sys.argv[0])
datagui = ""

usage = """
         use : """ + filename[1] + """ start | stop | restart | status | set[ting] | gui (if there) | config (if there)  | help"""

usageconfig = """         use : """ + filename[1] + """ set[ting] [auto | manual | system | boot | disable] """

def guide():
    print usage
    print "\n"
    print usageconfig

def setDataGui(Datagui):
    datagui = Datagui

def getDataGui():
    return datagui

def start(data):
    try:
        if (module006.status(data) != 'RUNNING'):		
            os.system("cls")
            print "\n"
            #os.system("sc config " + data + " start= demand")
            os.system("sc start " + data)
            os.system("cls")
            #print "\n"
            #print "\t Service START Now !"
            print "\n"
            st_service = module006.status(data)
            if (module006.status(data) == "RUNNING"):
                print "\n"
                #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:6 -m:\"Service " + str(data) +   " Has been START\"\nService " + str(data) +   " Status : !\"" + st_service + "\"")
                os.system("cls")
                print "\n"
                print "\t Service Has been START"

            elif (module006.status(data) == "START_PENDING"):
                #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:6 -m:\"Service " + str(data) +   " is START_PENDING\"\nService " + str(data) +   " Status : !\"" + st_service + "\"")
                os.system("cls")
                print "\n"
                print "\t Service is START_PENDING"
                cekstate.cekstate(data)
                st_service = module006.status(data)
                if (module006.status(data) == "STOPPED"):
                    #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:2 -m:\"Service " + str(data) +   " Can't be Start, Please cek Priviledge or Configuration Services !\"")
                    #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:2 -m:\"Service " + str(data) +   " Status : !\"" + st_service + "\"")
                    os.system("cls")
                    print "\n"
                    print "\t Service Can't be Start, Please cek Priviledge or Configuration Services ! \n"
                elif (module006.status(data) == "RUNNING"):
                    #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:6 -m:\"Service " + str(data) +   " Has been START\"\nService " + str(data) +   " Status : !\"" + st_service + "\"")
                    os.system("cls")
                    print "\n"
                    print "\t Service Has been START"	
                elif (module006.status(data) == "START_PENDING"):
                    #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:6 -m:\"Service " + str(data) +   " START_PENDING\"\nService " + str(data) +   " Status : !\"" + st_service + "\"")
                    os.system("cls")
                    print "\n"
                    print "\t Please Wait Until Service is STARTED"

                else:
                    st_service = module006.status(data)
                    #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:2 -m:\"Service " + str(data) +   " is Malfunction ! \n Service Can't be Start, Please cek Priviledge or Configuration Services !\"\nService " + str(data) +   " Status : !\"" + st_service + "\"")
                    #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:2 -m:\"Service " + str(data) +   " Status : !\"" + st_service + "\"")
                    os.system("cls")
                    print "\n"
                    print "\t Service is Malfunction ! \n Service Can't be Start, Please cek Priviledge or Configuration Services ! \n"

            else:
                #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:2 -m:\"Service " + str(data) +   " Can't be Start, Please cek Priviledge or Configuration Services !\"\nService " + str(data) +   " Status : !\"" + st_service + "\"")
                os.system("cls")
                print "\n"
                print "\t Service Can't be Start, Please cek Priviledge or Configuration Services ! \n"


        else:
            print "\n"
            print "\t Service Has been START \n"
            ceksync = raw_input("\t If You Wan't to Restart type : \"r\" or \"c\" to Cancel = ")
            if (ceksync == "r"):
                stop(data)
                start(data)
            elif (ceksync == "c"):
                pass
            elif (ceksync == ""):
                os.system("cls")
                print "\n"
                print "\t You Not input a Option (r | c) \n"
                print "\t State Service Condition  = " + module006.status(data)

            else:
                os.system("cls")
                print "\n\n"
                print "\t Plase input a Valid Option (r | c) ! \n"


    except OSError, e:
        if e.errno == errno.ENOENT:
            #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:2 -m:\"Service " + str(data) +   " tidak ditemukan\"\nService " + str(data) +   " Status : !\"" + st_service + "\"")
            os.system("cls")
            print "\n"
            print "\n Program tidak ditemukan \n"

        elif e.errno == errno.ENOEXEC:
            #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:2 -m:\"Service " + str(data) +   " bukan program excutable ! \"\nService " + str(data) +   " Status : !\"" + st_service + "\"")
            os.system("cls")
            print "\n"
            print "\n Program bukan program excutable ! \n"

        else:
            #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:2 -m:\"Error Service " + str(data) +   " tidak dapat berjalan di Win32 atau Command Mode !\"\nService " + str(data) +   " Status : !\"" + st_service + "\"")
            os.system("cls")
            print "\n"
            print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"


def stop(data):
    try:
        st_service = module006.status(data)
        if (module006.status(data) != 'STOPPED'):
            #os.system("cls")
            print "\n"
            #print data, "\n"
            #os.system("sc config " + data + " start= demand")
            os.system('net stop ' + data)
            #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:6 -m:\"Service " + str(data) +   " STOP Now !\"\nService " + str(data) +   " Status : !\"" + st_service + "\"")
            os.system("cls")
            print "\n"
            print "\t Service STOP Now !"

        else:
            #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:6 -m:\"Service " + str(data) +   " Has been STOP\"\nService " + str(data) +   " Status : !\"" + st_service + "\"")
            os.system('cls')
            print "\n"
            print "\t Service Has been STOP"


    except OSError, e:
        if e.errno == errno.ENOENT:
            #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:2 -m:\"Service " + str(data) +   " tidak ditemukan\"\nService " + str(data) +   " Status : !\"" + st_service + "\"")
            os.system("cls")
            print "\n"
            print "\n Program tidak ditemukan \n"

        elif e.errno == errno.ENOEXEC:
            #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:2 -m:\"Service " + str(data) +   " bukan program excutable ! \"\nService " + str(data) +   " Status : !\"" + st_service + "\"")
            os.system("cls")
            print "\n"
            print "\n Program bukan program excutable ! \n"

        else:
            #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:2 -m:\"Error Service " + str(data) +   " tidak dapat berjalan di Win32 atau Command Mode !\"\nService " + str(data) +   " Status : !\"" + st_service + "\"")
            os.system("cls")
            print "\n"
            print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"


def restart(service):
    st_service = module006.status(service)
    #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:6 -m:\"Service " + str(service) +   " being RESTART !\"\nService " + str(service) +   " Status : !\"" + st_service + "\"")
    os.system("cls")
    print "\n"
    stop(service)
    start(service)
    #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:6 -m:\"Service " + str(service) +   " has been RESTART !\"\nService " + str(service) +   " Status : !\"" + st_service + "\"")
    os.system("cls")
    print "\n"

def status(service):
    try:
        os.system("cls")
        #os.system("sc query tomcat6")
        print "\n"

        #data001 = os.popen("sc " + service).readlines()
        #data002 = data001[3].split("\n")
        #data003 = data002[0].split("\n")
        #data004 = data003[0].split(": ")
        #data005 = data004[-1].split(" ")
        #print data005
        #os.system("cls");
        #print "\n"
        #print "\t Service is : ", data005[2]
        #datax = data
        module004.status(service)

    except IndexError, e:
        #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:2 -m:\"ERROR With Status : " + str(e) + "\"\nService " + str(service) +   " Status : !\"" + st_service + "\"")
        os.system("cls")
        print "\n"
        print "ERROR With Status : ", e

        print "\n"
        #print "\t Service is : ", data005[2]

    except OSError, e:
        if e.errno == errno.ENOENT:
            #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:2 -m:\"Service " + str(service) +   " tidak ditemukan\"\nService " + str(service) +   " Status : !\"" + st_service + "\"")
            os.system("cls")
            print "\n"
            print "\n Program tidak ditemukan \n"

        elif e.errno == errno.ENOEXEC:
            #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:2 -m:\"Service " + str(service) +   " bukan program excutable ! \"\nService " + str(service) +   " Status : !\"" + st_service + "\"")
            os.system("cls")
            print "\n"
            print "\n Program bukan program excutable ! \n"

        else:
            #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:2 -m:\"Error Service " + str(service) +   " tidak dapat berjalan di Win32 atau Command Mode !\"\nService " + str(service) +   " Status : !\"" + st_service + "\"")
            os.system("cls")
            print "\n"
            print "\n Error, Program tidak dapat berjalan di Win32 atau Command Mode ! \n"


    except NameError, e:
        #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:2 -m:\"" + str(e) + "\"\nService " + str(service) +   " Status : !\"" + st_service + "\"")
        os.system("cls")
        print "\n"
        print "\t\t", e


def gui(infodata):
    try:
        #st_service = module006.status(infodata)
        data = infodata
        module002.main(data)
    except IOError, e:
        #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:2 -m:\"" + str(e) + "\"" )
        os.system("cls")
        print "\n"
        print "\t\t e"

    except IndexError, e:
        #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:2 -m:\"" + str(e) + "\"" )
        os.system("cls")
        print "\n"
        print "\t\t e"


def setting(data, set):
    try:
        st_service = module006.status(data)
        os.system("sc config " + data + " start= " + set)
    except NameError, e:
        #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:2 -m:\"" + str(e) + "\"\nService " + str(data) +   " Status : !\"" + st_service + "\"")
        os.system("cls")
        print "\n"
        print e

def set(data):
    try:
        os.system("scite " + data)
    except NameError, e:
        os.system("cls")
        print "\n"
        print e

def main(datax):
    try:
        st_service = module006.status(datax)
        if (len(sys.argv) <= 1):
            os.system("cls")
            try:
                status(datax)
                print "\n"
                print "\t\t", usage, "\n"
            except IndexError, e:
                #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:2 -m:\" No Services Found ! \"\nService " + str(datax) +   " Status : !\"" + st_service + "\"")
                os.system('cls')
                print "\n"
                print "\t\t No Services Found ! \n"
                print "\t\t", usage, "\n"
            except TypeError, e:
                #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:2 -m:\" No Services Found ! \"\nService " + str(datax) +   " Status : !\"" + st_service + "\"")
                os.system('cls')
                print "\t\t No Services Found ! \n"
                print "\t\t", usage, "\n"

        else:		
            if (sys.argv[1] == "help"):
                os.system("cls")
                print "\n"
                print "\t\t", usage

            elif (sys.argv[1] == "start"):
                start(datax)

            elif (sys.argv[1] == "stop"):
                stop(datax)

            elif (sys.argv[1] == "restart"):
                stop(datax)
                start(datax)
                #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:6 -m:\"Service " + str(datax) +   " Has Been RESTART\"\nService " + str(datax) +   " Status : !\"" + st_service + "\"")
                os.system("cls")
                print "\n"
                print "\t Service Has Been RESTART"


            elif (sys.argv[1] == "status"):
                status(datax)

            elif (sys.argv[1] == "gui"):
                dataGui = getDataGui()
                gui(dataGui)

            elif (sys.argv[1] == "setting" or "set"):
                if (sys.argv[2] > 1):
                    if (sys.argv[2] == "auto"):
                        setconf = "auto"
                        setting(datax, setconf)

                    elif (sys.argv[2] == "manual"):
                        setconf = "demand"
                        setting(datax, setconf)

                    elif (sys.argv[2] == "boot"):
                        setconf = "boot"
                        setting(datax, setconf)

                    elif (sys.argv[2] == "system"):
                        setconf = "system"
                        setting(datax, setconf)

                    elif (sys.argv[2] == "disable"):
                        setconf = "disabled"
                        setting(datax, setconf)
                else:
                    print "\n"
                    print usageconfig

            else:
                #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:6 -m:\"There no Option, Please Input a Valid Option or Wrong Name Service \"\nService " + str(data) +   " Status : !\"" + st_service + "\"")
                os.system("cls")
                print "\n"
                print "\t\tThere no Option, Please Input a Valid Option or Wrong Name Service\n"
                print "\t\t", usage

    except IndexError, e:
        os.system("cls")
        print "\n"
        print e
        print "\n\n"
        print "\t\t", usage


if __name__ == '__main__':
    main()







