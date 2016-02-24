# -*- coding: utf-8 -*-
# Este generador de diplomas lee una lista con nombre, dni y calificación para
# rellenarlos en una plantilla LaTeX con un marcador para cada campo.
# Opcionalemente compila los ficheros LaTeX generados y los une en uno solo.
# Si la plantilla LaTeX da error de compilación, pulsar intro varias veces.

print "Pyploma: Generador de diplomas en formatos LaTeX y pdf.\n"

# Invocar al terminal
from commands import *
import commands
def run_command(cmd):
	getstatusoutput(cmd)

# Cargar lista de nombres
lista = open("listadip", "r").readlines()

#contador
a = 100

for line in lista: # para cada persona...

	a += 1 #contador
	b = str(a) #pasa el contador a cadena
	salida = open("output" + b + ".tex","w") # crea fichero LaTeX para cada persona
	person = line[0:-1].split("\t") # pasar la cadena en lista

	text = open("certi.tex") # abrir documento LaTeX
	text = text.read() # leer documento LaTeX
	text_list = list(text) # pasa a lista

	y_cali = text.find("%pointcalification") # busca marcador de calificación
	z_cali = len("%pointcalification")+1
	text_list[y_cali+z_cali:y_cali+z_cali] = list(person[2]) # inserta calificación

	y_dni = text.find("%pointdni") # lo mismo para el dni
	z_dni = len("%pointdni")+1
	text_list[y_dni+z_dni:y_dni+z_dni] = list(person[1])

	y_name = text.find("%pointname") # lo mismo para el nombre
	z_name = len("%pointname")+1
	text_list[y_name+z_name:y_name+z_name] = list(person[0])

	text_final = "".join(text_list) # de lista a cadena

	salida.write(text_final) # guarda los cambio en el fichero creado
	salida.close() # cierra el fichero creado

	run_command(str("pdflatex " + "output" + b + ".tex")) # compila el fichero LaTeX a pdf (opcional)
	print person[0] #control

run_command(str("pdftk output*.pdf cat output todos_diplomas.pdf")) # crea pdf con todos los diplomas creados (opcional)

print "\n¡FINAL DE LA OPERACIÓN!" #control
