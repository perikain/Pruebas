#!/usr/bin/env python
#!-*- coding: utf-8 -*-

import zipfile
from itertools import permutations
from itertools import combinations
from itertools import chain
import datetime






alfabetoMin = 'abcdefghijklmnñopqrstuvwxyz'
alfabetoMay = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
numeros = '01234'

def AtacarFicheroZIP(ficheroZip, ficheroclaves):
    if zipfile.is_zipfile(ficheroZip):
        print "Fichero ZIP Válido..."
    else:
        print "El fichero ZIP no es válido..."
        exit()

    fichero = zipfile.ZipFile(ficheroZip,mode="r")
#!    print "El fichero %s contiene los siguientes ficheros: \n" %(ficheroZip)
#!
#!    listaFicheros = fichero.namelist()
#!    for i in xrange (len(listaFicheros)):
#!        print listaFicheros[i]

    print "Información referente al fichero %s: " %(ficheroZip)
    listaInformacion = fichero.infolist()
    for info in fichero.infolist():
        print info.filename
        print '\tComment:\t', info.comment
        print '\tModified:\t', datetime.datetime(*info.date_time)
        print '\tSystem:\t\t', info.create_system, '(0 = Windows, 3 = Unix)'
        print '\tZIP version:\t', info.create_version
        print '\tComprimido:\t', info.compress_size, 'bytes'
        print '\tDescomprimido:\t', info.file_size, 'bytes'
        print '\tTipo de compresión:\t', info.compress_type

    print "\nA continuación se procederá a atacar por fuerza bruta el fichero %s para descubrir su clave: " %ficheroZip
    print "\n¿Desea continuar?(s/N)"


def GenerarNumeros(longitud):
    fichero = open("claves.txt", mode='at')

    lista = []
    numero = ""
#!    lista = list(chain(*map(lambda x: permutations(numeros, longitud), range(0, len(numeros) + 1))))
#!    lista = list(permutations(numeros,longitud))
    lista = list(permutations(numeros))

    palabra = ""
    for i in range(len(lista)):
        for j in range (len(lista[i])):
            palabra = palabra + str(lista[i][j])
        fichero.write(palabra + "\n")
        palabra = ""

    fichero.close()




if __name__ == "__main__":
    GenerarNumeros(3)
    AtacarFicheroZIP("ficheroZipconClave.zip","claves.txt")


