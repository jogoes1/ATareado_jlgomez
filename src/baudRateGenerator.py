# coding=utf-8
import codecs
import threading
import time
from Log import logger
from datetime import datetime


class BaudRateGenerator(object):

    def __init__(self):
        self.__numberOfBytesToSend = 1          # Número de bytes a enviar
        self.__bytesSentToServer = 0            # Número de bytes enviados al servidor
        self.running = False                    # Thread corriendo
        self.__baudRateGeneratorThread = None   # Thread
        self.__delay = 1                        # Delay entre ejecuciones del thread
        #self.__data = 'C'                      # Datos a enviar al servidor
        self.__stringToBuild='0123456789'       #
        self.__data = ''                        # Datos a enviar al servidor
        self.__end = '012345678901234567890123' # Fin de envío
        self.__concatenaciones = 100              # numero de concatenaciones

        for index in range(self.__concatenaciones):
            self.__data=self.__data+self.__stringToBuild

        self.__data = self.__data + self.__end

        print "Length de self.__data ",len(self.__data)

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

    def __sendThroughput(self,bytesToSend,sleepSeconds):
        for index in range(bytesToSend):
            print self.__data
            self.sendData(self.__data)
            time.sleep(sleepSeconds)

    def __baudRateGeneratorLoop(self):

        #TODO: Cambiar este parámetro por un field de la clase para ver el número de paquetes de 1024 bytes que enviamos
        veces = 1

        while self.running:

            print("Inicio envío datos")
            #self.__sendThroughput(10,1)

            initialTime=datetime.now()
            endingTime=initialTime;

            for index in range(veces):
               # print index
                #print self.__data
                self.sendData(self.__data)
                #time.sleep(self.__delay)

            self.sendData('E')

            print("Fin envío datos")
            endingTime=datetime.now()


            print "Inicio = ",initialTime
            print "Fin = ",endingTime
            print "Duración envío =",endingTime-initialTime

            #TODO: Añadir campo y cálculo de throughput de envío: Número de bytes/Tiempo
            #TODO: Modificar interfaz gráfica para introducir el número de paquetes de 1024 bytes
            #print "Numero de paquete enviados= ",index*10

            self.running = False
