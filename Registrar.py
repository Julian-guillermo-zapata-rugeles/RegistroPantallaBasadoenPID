"""
Julian Guillermo zapata rugeles
julianruggeles@gmail.com


Probado en UBUNTU 16.04 UBUNTU 18.04 LTS / GNU/LINUX


Este script permite realizar un seguimiento fotografico
a aplicaciones con restriccion en el dispositivo.
Ejemplo : si la aplicacion "Pagos" se encuentra en ejecución
el script capturará un pantallazo del equipo cada intervalo configurado
con el fin de realizar un seguimiento de uso apropiado

(Al realizar capturas de pantalla puede violar la privacidad )
se recomienda usarla para pruebas o por Ejemplo llevar un control de qué
paginas visitan sus hijos ó ver explicitamente (mediante capturas) el comportamiento de una persona
en una determinada aplicacion.
recuerde que por legislación algunas practicas pueden no ser apropiadas.

-- No es un Keylogger puesto no registra pulsaciones.
-- Solo realiza un seguimiento fotografico de la pantalla

Dependencias : scrot
               sudo apt-get install scrot (400kb size)
               (instalacion sencilla a travez de Apt)

Desarollo futuro:
            Adaptacion para el sistema operativo WINDOWS 7/10


"""

import os
import time

class observador():

    """ Funciones    """
    def runCapture():
        timeGet=os.popen("date").read()
        timeGet=timeGet.replace(" ","")
        timeGet=timeGet.replace("\n","")
        timeGet="scrot >> "+timeGet+".png"
        os.system(timeGet)

    def activeProgram(programName):
        process="pgrep "+programName
        pipNumber=os.popen(process).read()
        if len(pipNumber)>2:
            return True
        else:
            return False



if __name__ == '__main__':
    """ Inicio del programa """
    IntervaloTiempo = 5 # Tiempo en segundos cada cuanto hacer una captura
    programName = "firefox " # Nombre del programa  a seguir (Consulte el nombre del proceso para dicho paso)
    while True:
        retorno=observador.activeProgram(programName)
        if retorno==True:
            observador.runCapture()
        time.sleep(IntervaloTiempo  )
