import winsound
import os
import sys

def play(data):
    winsound.PlaySound(data, winsound.SND_ALIAS)


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            cek = sys.argv[1].split(".")
            if cek[1] == "mp3":
                print("\n")
                print("\t Sorry this not support MP3 file ! \n")
            else:
                data = sys.argv[1]
                play(data)
        else:
            dsound = r"H:\MUSIC\SOUND\knock.wav"
            play(dsound)
            print("\n")
            print("\t use : " + os.path.split(sys.argv[0])[1] + " [file wav]")
    except IndexError as e:
        print("\n")
        print("\t Please Input A Sound File Name ! \n")
