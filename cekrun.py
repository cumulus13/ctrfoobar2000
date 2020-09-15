import os
import sys
#import #dplay2

filename = os.path.split(sys.argv[0])[1]
usage = """use : """ + filename + """[name of application]"""
datacek = []
datafinal = []

def cek(cek):
	try:
		#cek = sys.argv[1]
		data = os.popen("tasklist").readlines()
		for i in range(0, len(data)):
			if(cek in data[i]):
				datacek.append(data[i])
			else:
				pass
				
		if len(datacek) > 1:
			print("\n")
			#print "May your application name is : \n"
			for x in range(0, len(datacek)):
				data_s01 = datacek[x].split(".exe")
				datafinal.append(data_s01[0])
		else:
			return False
			
		return True
		#print datafinal
				#return datafinal
		#print datacek,"\n"
		#print len(datacek)
	except IndexError as e:
		os.system("cls")
		print("\n")
		print(usage)


def cek2(cek):
	try:
		#cek = sys.argv[1]
		data = os.popen("tasklist").readlines()
		for i in range(0, len(data)):
			if(cek in data[i]):
				datacek.append(data[i])
			else:
				pass
				
		if len(datacek) > 1:
			#dplay2.play2(str(cek).split(".exe")[0], ", is RUNNING")
			print("\n")
			print("\t Aplication " + str(cek).split(".exe")[0] + " is : RUNNING")
			print("\t May your application name is : \n")
			for x in range(0, len(datacek)):
				data_s01 = datacek[x].split(".exe")
				datafinal.append(data_s01[0])
				print("\t " + str(x + 1) + ".",data_s01[0] + ".exe")
			
		else:
			if len(datacek) > 0:
				#dplay2.play2(str(cek).split(".exe")[0], ", is RUNNING")
				print("\n")
				print("\t Aplication " + str(cek).split(".exe")[0] + " is : RUNNING")
			else:
				#dplay2.play2(str(cek).split(".exe")[0], ", is NOT RUNNING")
				print("\n")
				print("\t Aplication " + str(cek) + " is : NOT RUNNING")
				#print datafinal		
				return False
			
		return True
		
				#return datafinal
		#print datacek,"\n"
		#print len(datacek)
	except IndexError as e:
		os.system("cls")
		print("\n")
		print(usage)

		
if __name__ == '__main__':
	#datax = cek(sys.argv[1])
	cek2(sys.argv[1])
	#print datax