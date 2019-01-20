import os
import sys, errno
#import dplay2
#import pyttsx
#import time
"""
def sound(svc,status):
	engine = pyttsx.init()
	rate = engine.getProperty('rate')
	engine.setProperty('rate', rate-60) #95
	engine.say('Information. Service ' + str(svc) + ', is, ' + str(status))
	engine.runAndWait()
"""

def status(service):
    try:
        data001 = os.popen("sc query " + service).readlines()
        data002 = data001[3].split("\n")
        data003 = data002[0].split("\n")
        data004 = data003[0].split(": ")
        data005 = data004[-1].split(" ")

        datan01 = data001[1].split(":")
        datan02 = datan01[1].split("\n")
        #print "datan02 = ", datan02[0]

        #data001a = data001[0].split(" 1060")
        #data001b = data001a[0].split("OpenService ")

        #print data001b[1]
        #print datan02

        #if (data001b[1] == "FAILED"):
        #	print "\t\t Please Insert The Correct Name Service !"
        #else:
        #os.system("cls");

        if(data005[2] == "RUNNING"):
            #sound(datan02[0], "RUNNING")
            #dsound = r"d:\SOUND\Apache Start.wav"
            #dplay2.play(datan02[0], "RUNNING")
            pass
        elif(data005[2] == "START_PENDING"):
			pass
            #sound(datan02[0], "START PENDING")
            #dsound = r"d:\SOUND\Apache Pending.wav"
            #dplay2.play(datan02[0], "START PENDING")
        elif(data005[2] == "STOPPED"):
            #sound(datan02[0], "STOPPED")
            #dsound = r"d:\SOUND\Apache Stop.wav"
            #dplay2.play(datan02[0], "STOPPED")
            pass
        else:
            #sound(datan02[0], "UNKNOW")
            #dsound = r"d:\SOUND\Apache Error.wav"
            #dplay2.play(datan02[0], "UNKNOW")
            pass

        print "\n"
        print "\t Service " + datan02[0] + " is : ", data005[2]

        return data005[2]


    #except IndexError, e:
    #	os.system('cls')
    #	print "\n"
    #	print "ERROR With Status : ", "1.", e, "\n"
    #	print "                     2. Service Not Found !" 
    #	print "\n"
    #	#print "\t Service " + datan02[0] + "is : ", data005[2]

    except IOError, e:
        print e