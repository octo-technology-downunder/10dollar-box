import MFRC522
import time
import os
from firebase import firebase


url = 'https://shining-fire-5877.firebaseio.com'

def readNfc():
    MIFAREReader = MFRC522.MFRC522()
    reading = True
    while reading:

        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        (status,backData) = MIFAREReader.MFRC522_Anticoll()
        if status == MIFAREReader.MI_OK:
            uidStr = str(backData[0]) + "" + str(backData[1]) + "" + str(backData[2]) + "" + str(backData[3]) + "" + str(backData[4])
            print "Card detected", uidStr, time.time()

	    os.system("omxplayer ../hello.mp3")
            fb = firebase.FirebaseApplication(url, None)
            result = fb.get('/nfc-cards', uidStr)
            val = 0
            if result:
              val = result['value']
	    fb.put('/nfc-cards', uidStr, {"value":val + 1, "time": time.time()})

readNfc()
