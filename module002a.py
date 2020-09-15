import os
import sys
import module002
import module003
import cekrun
import Cservice
import pywintypes
import array
#import #dplay2
import e_console
import traceback

import  subprocess

filename = os.path.split(sys.argv[0])
usage = """use : """ + filename[1] + """ [ kill | help | |gui | config ]"""
usage2 = """use : """ + filename[1] + """ [ start | stop | restart | status | kill | help | |gui | config ]"""

def errorA(data,info=None):
    data = os.path.splitext(sys.argv[0])[1]
    if os.path.splitext(__file__)[1] == ".pyw":
        e_console.main(info, data)
    else:
        print("\t Error:", data)

def main(data):
    if not isinstance(data, list):
        data =  [data]
    else:
        try:
            if(data[-1] == 'kill' or data[-1] == 'stop'):
                print("len(sys.argv) =",len(sys.argv))
                if len(data) > 1:
                    for i in range(0, len(data)):
                        data_app2 = os.path.split(data[i])
                        os.system("taskkill /f /im " + data_app2[1])
                else:
                    data_app = os.path.split(data[0])
                    os.system("taskkill /f /im " + data_app[1])

            elif(data[0] == 'help'):
                print("\n")
                errorA(usage,'error')
                #print "\t", usage
            else:
                a =  []
                for i in data:
                    if 'program' in str(i).lower() and 'files' in str(i).lower():
                        if os.path.isfile(i):
                            pass
                        else:
                            if not "files (x86)" in i.lower():
                                z0 = []
                                z1 = os.path.basename(i)
                                z2 = os.path.dirname(i)
                                z0.append(z1)
                                while 1:
                                    if not z2[-5:].lower() == 'files':
                                        z1 = os.path.basename(z2)
                                        z2 = os.path.dirname(z2)
                                        z0.append(z1)
                                    else:
                                        z0.append(r'c:\Program Files (x86)')
                                        z0.reverse()
                                        zz = "\\".join(z0)
                                        i = zz
                                        break
                            else:
                                z0 = []
                                z1 = os.path.basename(i)
                                z2 = os.path.dirname(i)
                                z0.append(z1)
                                while 1:
                                    if not z2[-5:].lower() == 'files':
                                        z1 = os.path.basename(z2)
                                        z2 = os.path.dirname(z2)
                                        z0.append(z1)
                                    else:
                                        z0.append(r'c:\Program Files')
                                        z0.reverse()
                                        zz = "\\".join(z0)
                                        i = zz
                                        break
                                    
                    a.append(i)
                    #print i
                    
                    for x in range(1, len(sys.argv)):
                        if os.path.isfile(os.path.abspath(sys.argv[x])):
                            a.append(os.path.abspath(sys.argv[x]))
                        elif os.path.isdir(os.path.abspath(sys.argv[x])):
                            a.append(os.path.abspath(sys.argv[x]))
                        else:
                            a.append(sys.argv[x])
                        #print "a =", a
                    
                    if 'elinks' in str(data[0]):
                        if len(sys.argv) > 1:
                            argv_1 = os.path.basename(sys.argv[1])
                            a.remove(a[-1])
                            a.insert(1, argv_1)
                    print("a =", a)        
                    if "\\links.exe" in str(data[0][-10:]):
                        os.chdir("F:\\")
                    # else:
                    #     os.chdir(os.path.dirname(data[0]))
                    try:
                        #print os.getcwd()
                        print(__file__)
                        subprocess.Popen(a)
                    except IndexError as e:
                        er = traceback.format_exc()
                        print("\n")
                        #print "\t", usage
                        errorA(str(er) + "\n" + usage,'error')
                    except:
                        os.chdir(os.path.dirname(__file__))
                        subprocess.Popen(a)                            
        except:
            print("\n")
            er =  traceback.format_exc()
            #print "\t", usage
            print("er =", er)
            errorA(er + "\n\n" + usage,'error')
            #else:
            #    for i in range(0, len(data)):
            #        module002.main(data[i])

def services(data):
    try:
        if(len(sys.argv) > 1):
            if(sys.argv[1] == "stop"):
                for i in range (0,10):
                    try:
                        Cservice.WService(data[i]).stop()
                        print("\n")
                        data_status = Cservice.WService(data[i]).status()
                        #dplay2.play(data[i], data_status)
                        print("\t Service " + data[i] + " is " + data_status)
                    except pywintypes.error as e:
                        er = traceback.format_exc()
                        errorA(str(er),'error')
            elif(sys.argv[1] == "start"):
                for i in range (0, 10):
                    try:
                        Cservice.WService(data[i]).start()
                        print("\n")
                        data_status = Cservice.WService(data[i]).status()
                        #dplay2.play(data[i], data_status)
                        print("\t Service " + data[i] + " is " + data_status)
                    except pywintypes.error as e:
                        er = traceback.format_exc()
                        errorA(str(er),'error')
            elif(sys.argv[1] == "restart"):
                for i in range (0, 10):
                    try:
                        Cservice.WService(data[i]).restart
                        print("\n")
                        data_status = Cservice.WService(data[i]).status()
                        #dplay2.play(data[i], data_status)
                        print("\t Service " + data[i] + " is " + data_status)
                    except pywintypes.error as e:
                        er = traceback.format_exc()
                        errorA(str(er),'error')
            elif(sys.argv[1] == "status"):
                for i in range (0, 10):
                    print("\n")
                    data_status = Cservice.WService(data[i]).status()
                    #dplay2.play(data[i], data_status)
                    print("\t Service " + data[i] + " is " + data_status)
            else:
                print("\n")
                print("\t" + usage2)
        else:
            print("\n")
            print("\t" + usage2)

    except IndexError as e:
        print("\n\n")
        er = traceback.format_exc()
        errorA(str(er),'error')

def services2(data, svc): #data = list of application[] svc = list of services[]
    try:
        if(len(sys.argv) > 1):
            if(sys.argv[1] == "stop"):
                for i in range (0, len(svc)):
                    try:
                        Cservice.WService(svc[i]).stop()
                        print("\n")
                        data_status = Cservice.WService(svc[i]).status()
                        #dplay2.play(svc[i], data_status)
                        print("\t Service " + svc[i] + " is " + data_status)
                    except pywintypes.error as e:
                        for x in range (0, len(svc)):
                            try:
                                Cservice.WService(svc[x]).stop()
                            except pywintypes.error as e:
                                er = traceback.format_exc()
                                errorA(str(er),'error')
                                print("\n")

                data_status = Cservice.WService(svc[i]).status()
                #dplay2.play(svc[x], data_status)
                print("\t Service " + svc[x] + " is " + data_status)
                print("\n")
                appname = os.path.split(data[i])[1]
                os.system("taskkill /f /im " + str(appname))
                #dplay2.#dplay2(appname, " is killed !")
                print("\n")
                print("\t Program " + appname.split(".exe")[0] + " is killed !")

            elif(sys.argv[1] == "start"):
                for i in range (0, len(svc)):
                    try:
                        Cservice.WService(svc[i]).start()
                        print("\n")
                        data_status = Cservice.WService(svc[i]).status()
                        #dplay2.play(data[i], data_status)
                        print("\t Service " + data[i] + " is " + data_status)
                        appname = os.path.split(data[i])[1]
                        os.system(data[x])
                        #dplay2.#dplay2(data[i], " has been started !")
                        print("\n")
                        print("\t Program " + data[i] + " has been started ! \n")
                    except pywintypes.error as e:
                        er = traceback.format_exc()
                        errorA(str(er),'error')
            elif(sys.argv[1] == "status"):
                for i in range (0, len(svc)):
                    print("\n")
                    data_status = Cservice.WService(svc[i]).status()
                    #dplay2.play(svc[i], data_status)
                    print("\t Service " + svc[i] + " is " + data_status)
                    appname = os.path.split(data[i])[1]
                    cekrun.cek2(appname.split(".exe")[0])
            else:
                print("\n")
                print("\t" + usage2)
        else:
            print("\n")
            print("\t" + usage2)

    except IndexError as e:
        print("\n\n")
        er = traceback.format_exc()
        errorA(str(er),'error')
        #print "\t ERROR = ", str(e)
    except pywintypes.error as e:
        er = traceback.format_exc()
        errorA(str(er),'error')
        print("\n")
        print("\t ERROR = ", str(e))
        for i in range (0, len(svc)):
            print("\n")
            data_status = Cservice.WService(svc[i]).status()
            #dplay2.play(svc[i], data_status)
            print("\t Service " + svc[i] + " has been " + data_status)

def services3(data):
    try:
        if(len(sys.argv) > 1):
            if(sys.argv[1] == "stop"):
                for i in range (0,10):
                    try:
                        os.system("sc stop " + data[i])
                        print("\n")
                        data_status = os.system("sc query " + data[i])
                        #dplay2.play(data[i], data_status)
                        print("\t Service " + data[i] + " is " + data_status)
                    except pywintypes.error as e:
                        pass
            elif(sys.argv[1] == "start"):
                for i in range (0, 10):
                    try:
                        os.system("sc start " + data[i])
                        print("\n")
                        data_status = os.system("sc query " + data[i])
                        #dplay2.play(data[i], data_status)
                        print("\t Service " + data[i] + " is " + data_status)
                    except pywintypes.error as e:
                        pass
            elif(sys.argv[1] == "restart"):
                for i in range (0, 10):
                    try:
                        Cservice.WService(data[i]).restart
                        print("\n")
                        data_status = Cservice.WService(data[i]).status()
                        #dplay2.play(data[i], data_status)
                        print("\t Service " + data[i] + " is " + data_status)
                    except pywintypes.error as e:
                        pass
            elif(sys.argv[1] == "status"):
                for i in range (0, 10):
                    print("\n")
                    data_status = os.system("sc query " + data[i])
                    #dplay2.play(data[i], data_status)
                    print("\t Service " + data[i] + " is " + data_status)
            else:
                print("\n")
                print("\t" + usage2)
        else:
            print("\n")
            print("\t" + usage2)

    except IndexError as e:
        print("\n\n")
        er = traceback.format_exc()
        errorA(str(er),'error')
        #print "\t ERROR = ", str(e)

def services4(data, svc):
    try:
        if(len(sys.argv) > 1):
            if(sys.argv[1] == "stop"):
                for i in range (0, len(svc)):
                    try:
                        os.system("sc stop " + svc[i])

                        print("\n")
                        data_status = os.system("sc query " + svc[i])
                        #dplay2.play(svc[i], data_status)
                        print("\t Service " + svc[i] + " is " + data_status)
                    except pywintypes.error as e:
                        for x in range (0, len(svc)):
                            try:
                                os.system("sc stop " + svc[x])
                            except pywintypes.error as e:
                                pass
                    print("\n")
                    data_status = os.system("sc query " + svc[x])
                    #dplay2.play(svc[x], data_status)
                    print("\t Service " + svc[x] + " is " + data_status)
                    print("\n")
                    appname = os.path.split(data[i])[1]
                    os.system("taskkill /f /im " + str(appname))
                    #dplay2.#dplay2(appname, " is killed !")
                    print("\n")
                    print("\t Program " + appname.split(".exe")[0] + " is killed !")

            elif(sys.argv[1] == "start"):
                for i in range (0, len(svc)):
                    try:
                        os.system("sc start " + svc[i])
                        print("\n")
                        data_status = os.system("sc query " + svc[i])
                        #dplay2.play(svc[i], data_status)
                        print("\t Service " + svc[i] + " is " + data_status)
                        appname = os.path.split(data[i])[1]
                        os.system(data[x])
                        #dplay2.#dplay2(data[i], " has been started !")
                        print("\n")
                        print("\t Program " + data[i] + " has been started ! \n")
                    except pywintypes.error as e:
                        pass

            elif(sys.argv[1] == "status"):

                for i in range (0, len(svc)):
                    print("\n")
                    data_status = os.system("sc query " + svc[i])
                    #dplay2.play(svc[i], data_status)
                    print("\t Service " + svc[i] + " is " + data_status)
                    appname = os.path.split(data[i])[1]
                    cekrun.cek2(appname.split(".exe")[0])

            else:
                print("\n")
                print("\t" + usage2)
        else:
            print("\n")
            print("\t" + usage2) 

    except IndexError as e:
        print("\n\n")
        er = traceback.format_exc()
        errorA(str(er),'error')
    except pywintypes.error as e:
        print("\n")
        print("\t ERROR = ", str(e))
        for i in range (0, len(svc)):
            print("\n")
            data_status = os.system("sc query " + svc[i])
            #dplay2.play(svc[i], data_status)
            print("\t Service " + svc[i] + " has been " + data_status)


def main2(data,service):
    data_app = os.path.split(data)
    try:
        if (len(sys.argv) > 1):
            if(sys.argv[1] == 'kill'):
                os.system("taskkill /f /im " + data_app[1])
                module003.stop(service)
            elif(sys.argv[1] == 'help'):
                print("\n")
                print("\t", usage2)
            elif(sys.argv[1] == "start" or "stop" or "restart" or "status"):
                if(sys.argv[1] == "restart"):
                    os.system("taskkill /f /im " + data_app[1])
                    module003.main(service)
                elif(sys.argv[1] == "start"):
                    module002.main(data)
                    module003.main(service)
                elif(sys.argv[1] == "stop"):
                    os.system("taskkill /f /im " + data_app[1])
                    module003.main(service)
                elif(sys.argv[1] == "status"):
                    module003.main(service)
                    cekrun.cek2(data_app[1].split(".exe")[0])
                else:
                    pass
            else:
                print("\n")
                print("\t", usage2)
        else:
            module003.start(service)
            module002.main(data)
    except IndexError as e:
        print("\n")
        er = traceback.format_exc()
        errorA(str(er) + "\n" + usage2,'error')
"""
if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError, e:
        er = traceback.format_exc()
        errorA(str(er),'error')
"""