import codecs
import threading
import time
from Log import logger
import serialconnection

class SerialReader(object):


    serialPort = None

    def __init__(self,serialPort):

        print "SerialReader Instance"

        self.__serialPort=  serialPort
        self.__runLoop = False
        self.__delay = 1                                                        # reading thread delay seconds
        self.__data = None
        self.__repetitions = 10
        self.__nrOfPacketsPerIteration = 1
        self.running = False
        self.__serialReaderThread = None
        self.__tx_decoder = codecs.getincrementalencoder('ASCII')('replace')


    def start(self):
        print "Serial Reader Start"

        self.running = True
        self.__serialThread = threading.Thread(target=self.__serialReaderLoop, args=())
        self.__serialThread.daemon = True
        self.__serialThread.start()

    def stop(self):
        print "Serial Reader Stop"
        self.running = False

    def __serialReaderLoop(self):
        while self.running:
            print "__serialReaderLoop Iteration"

            #self.__serialPort.stop()
            #print "self.__serialPort.sendCommand(A)"
            print "Waiting for data"


           # while self.__serialPort.in_waiting() > 0 :
            #    self.__data += self.__serialPort.read()


            while self.__serialPort.in_waiting() > 0 :
                self.__data += self.__serialPort.read()


           # self.__serialPort.writeDirect(data)
            print "self.__data=", self.__data

            time.sleep(self.__delay)