#!/usr/bin/env python
#!-*- coding: utf-8 -*-

#! This is my first wordlist generator

import locale
import subprocess

alfabetoMin = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z'}
alfabetoMay = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
numeros = {'0','1','2','3','4','5','6','7','8','9'}
def GrabarPalabrasClave(fichero):
    print "\n A continuación introduzca las palabras claves que servirán para generar el diccionario, para terminar escriba exit(): "
    palabra = raw_input()
    while (palabra != "exit()"):
        fichero.write(palabra)
        fichero.write("\n")
        palabra = raw_input()

    fichero.close()


def GeneraNumeros(longitud):
    for i

def GenerarFicheroClaves():
    try:
        fichero = open("keylist.txt",mode='a')
    except:
        "\t Error a la hora de generar el fichero keylist.txt. Pulse una tecla para continuar... \t"
        opcion = raw_input()
        PintarMenuPrincipal()

    GrabarPalabrasClave(fichero)


def PintarMenuPrincipal():
    subprocess.call("cls", shell=True)
    codificacion = locale.getpreferredencoding(do_setlocale=True)
    print "La codificación actual es: ", codificacion
    print "*"*60
    print "\t Escoja la opción que desea utilizar: "
    print "\n"
    print "1.- Generar fichero de claves."
    print "2.- Generar fichero de palabras."
    print "3.- Salir."
    print "\n"
    print "\t Introduzca la opción seleccionada: "


if __name__ == "__main__":
    PintarMenuPrincipal()

    opcion = int(raw_input())

    if (opcion == 1):
        fichero = GenerarFicheroClaves()
#!    elif (opcion == 2):
#!        GenerarFicheroPalabras(fichero)






