import module006
import module004
import os
import sys
import time
import dplay

def cekstate(data):

    datacek001 = "START_PENDING"

    for i in range(0, 50):
        waitme = ". " * (i/5)

        if datacek001 == module006.status(data):
            os.system("cls")
            print("\n")

            try:
                print("\n")
                print("\t\t Please wait . " + str(waitme)) 
            except:
                pass


        else:
            pass
            #print "data = " , module006.status(data)

    time.sleep(9)	
    #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:1 -m:\"Now Service " + str(data) +   " is RUNNING\"")
    os.system("cls")
    print("\n")
    print("\t\t Now Service " + data + " is " + module006.status(data))
    """if(module006.status(data) == "RUNNING"):
        dsound = r"d:\SOUND\Apache Start.wav"
        dplay.play(dsound)
    elif(module006.status(data) == "START_PENDING"):
        dsound = r"d:\SOUND\Apache Pending.wav"
        dplay.play(dsound)
    elif(module006.status(data) == "STOPPED"):
        dsound = r"d:\SOUND\Apache Stop.wav"
        dplay.play(dsound)
    else:
        dsound = r"d:\SOUND\Apache Error.wav"
        dplay.play(dsound)"""

def cekstate2(data):

    datacek001 = "START_PENDING"

    for i in range(0, 50):
        waitme = ". " * (i/5)

        if datacek001 == module006.status(data):
            os.system("cls")
            print("\n")

            try:
                os.system("sc query " + data)
                print("\n")
                print("\t\t Please wait . " + str(waitme)) 
            except:
                pass


        else:
            pass
            os.system("cls")
            print("\n\n")
            print("\t\t Now Service " + data + " is " + module006.status(data))
            sys.exit()
            #print "data = " , module006.status(data)

    time.sleep(9)	
    #os.system("sysloggen -q -t:192.168.128.1 -p:516 -f:1 -s:1 -m:\"Now Service " + str(data) +   " is RUNNING\"")
    os.system("cls")
    print("\n")
    print("\t\t Now Service " + data + " is " + module006.status(data))
