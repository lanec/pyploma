# pyploma
Automatically exported from code.google.com/p/pyploma

Plantilla LaTeX

\documentclass[12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[spanish]{babel}
\usepackage{mathpazo}
\renewcommand{\familydefault}{\rmdefault}
\usepackage[landscape,a4paper]{geometry}
\geometry{verbose,tmargin=0cm,bmargin=0cm,lmargin=0cm,rmargin=0cm}
\usepackage{fancybox}
\usepackage{calc}
\usepackage{multicol}
\usepackage{graphicx}

\begin{document}
~
\vspace{1cm}
\begin{center}

\huge{Un Bioinformatiquillo (https://bioinformatiquillo.wordpress.com)\\ certifica que}

\vspace{1cm}

\Huge{\textbf{%pointname

}}

\vspace{1cm}

\Large{con D.N.I. no.%pointdni

ha asistido y superado los estudios\\ con una califiaci\'on de %pointcalification

en el}

\vspace{1cm}

\Huge{\textbf{I CURSO DE REALIZACIÓN DE DIPLOMAS CON PYPLOMA}}

\vspace{1cm}

\Large{celebrado el 6 de julio de 2011 vitualmente en el blog, con una duraci\'on de un ratillo}

\vspace{.5cm}

\Large{Y para que as\'i conste se expide el siguiente certificado en el ciberespacio a \today.}

\vspace{.5cm}

\begin{multicols}{3}

\small Delegado de asusntos LaTeros\\
\vspace{3cm}
León Delátex Pérez
%\vspace{1cm} 

Director de Pythonismo\\
\vspace{3cm}
Ser Piente Grande
%\vspace{1cm} 

El/La Alumno/a\\
\vspace{3cm}
~~~~~~~~~~

\end{multicols}

\tiny El blog Un Bioinformatiquillo, con domicilio en el Vía Láctea s/n

\end{center}
\end{document}
Script en Python

Periquillo de los Palotes	00000001-A	NOTABLE
Rodolfo Chiquilicuatre	000000002-B	SOBRESALIENTE
Chavo del Ocho	00000003-C	APROBADO
Script en Python

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
