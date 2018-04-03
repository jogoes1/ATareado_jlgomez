# coding=utf-8
import codecs
import threading
import time
from Log import logger


class BaudRateGenerator(object):

    def __init__(self):
        self.__numberOfBytesToSend = 1
        self.running = False
        self.__baudRateGeneratorThread = None
        self.__delay = 1
        self.__data = '0123456789'

    def start(self, throughput, duration):
        result = True

        if self.running:
            result = False

        if result:
            #try:
            self.running = True

        self.__baudRateGeneratorThread = threading.Thread(target=self.__baudRateGeneratorLoop, args=())
        self.__baudRateGeneratorThread.daemon = True
        self.__baudRateGeneratorThread.start()

    def __baudRateGeneratorLoop(self):
        while self.running:

            print("Inicio envío datos")
            bytes =['1']

            for index in range(len(self.__data)):
                print index
                print self.__data
                self.sendData(self.__data)
                time.sleep(self.__delay)

            print("Fin envío datos")

            print "Numero de paquete enviados= ",index*10

            self.running = False
