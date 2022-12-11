from tkinter import *

raiz=Tk()

miFrame=Frame(raiz)

miFrame.pack()

operacion=""

resultado = 0
#-------------Pantalla-----------------------------------

numeroPantalla=StringVar()
pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, pady=5, columnspan=5)
pantalla.config(background="black", fg="#03f943", justify="right")
numeroPantalla.set(0)

#-------------Pulsaciones tecladp---------------------------

def numeroPulsado(num):
	
	global operacion

	if operacion=="suma" :

		numeroPantalla.set(num)

		operacion=""


	elif operacion=="resta":

		numeroPantalla.set("-" + num)
 
		operacion=""

	elif operacion=="multiplicar":

		numeroPantalla.set(num)

		operacion=""

	elif operacion=="dividir":

		numeroPantalla.set(num)

		operacion=""


	else:
		haycoma = numeroPantalla.get()
		haycoma = haycoma.count(".")

		if numeroPantalla.get()=="0" :
			numeroPantalla.set(num)
		elif haycoma>0 and num == ".":
			pass
		elif haycoma<0 and num == ".":
			numeroPantalla.set(numeroPantalla.get() + num)
		else:
			numeroPantalla.set(numeroPantalla.get() + num)      

#-----------------Boton borrar---------------------------------

def borrar():
	global resultado

	global operacion

	numeroPantalla.set(0)
	resultado = 0
	operacion = ""

#-----------------Funcion suma---------------------------

def suma(num):

	global operacion

	global resultado

	if resultado != 0:

		resultado = resultado + float(num) 

		numeroPantalla.set(resultado)	

		resultado = 0 

	else: 

		resultado+=float(num)
	
		operacion="suma"

		numeroPantalla.set(0)	

#-----------------Funcion resta---------------------------

def resta(num):

	global operacion

	global resultado
	
	if resultado != 0:

		resultado= resultado + float(num) 

		numeroPantalla.set(resultado)	

		resultado = 0 

	else:

		resultado = float (num) 
		numeroPantalla.set("-")
		operacion="resta"


#-----------------Funcion dividir---------------------------

def dividir(num):

	global operacion

	global resultado

	if resultado != 0:

		resultado= resultado / float(num) 
		numeroPantalla.set(resultado)
		resultado = 0 

	else:
		resultado = float(num)
		operacion="dividir"
		numeroPantalla.set(0)



#-----------------Funcion multiplicar---------------------------

def multiplicar(num):

	global operacion

	global resultado



	if resultado != 0 :

		resultado = float(num) * resultado
		numeroPantalla.set(resultado)
		resultado = 0 
	
	else :
		resultado = float(num)
		operacion="multiplicar"	
		numeroPantalla.set(0)



#___________________funcion el_resultado__________________

def el_resultado():

	global resultado

	numeroPantalla.set(resultado+float(numeroPantalla.get()))

#-------------fila1--------------------------------------

boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDividir=Button(miFrame, text="/", width=3, command=lambda:dividir(numeroPantalla.get()))
botonDividir.grid(row=2, column=4)
botonborar=Button(miFrame, text="CE", width=3, command=lambda:borrar())
botonborar.grid(row=2, column=5)

#-------------fila2--------------------------------------

boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMultiplicar=Button(miFrame, text="*", width=3, command=lambda:multiplicar(numeroPantalla.get()))
botonMultiplicar.grid(row=3, column=4)

#-------------fila3--------------------------------------

boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRest=Button(miFrame, text="-", width=3, command=lambda:resta(numeroPantalla.get()))
botonRest.grid(row=4, column=4)

#-------------fila4--------------------------------------

botoncoma=Button(miFrame, text=".", width=3, command=lambda:numeroPulsado("."))
botoncoma.grid(row=5, column=1)
boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=2)
botonIgual=Button(miFrame, text="=", width=3, command=lambda:el_resultado())
botonIgual.grid(row=5, column=3)
botonSuma=Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSuma.grid(row=5, column=4)

raiz.mainloop()