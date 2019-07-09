#Chatbot in Python
#using fuzzywuzzy

#see bug at the end of file, line 109

#this FIRST attempt will try to implement Q&A
#by means of matching list element and key in dict

#Ahora deberia hacer una logica con un input
#y que ese input use el fuzzywuzzy para que
#compare los match.
#despues habria q guardar ese match para comparar con
#el key del dict y sacar segun cual sea el match mas alto <-VER COMO HACER->al final lo hice diferente
#de ahi con un random de los index de los values
#elegir una respuesta al azar, 
#ESTO SE PUEDE HACER CON choice que elige de una list
#que seria el VALUE del dict
#o
#Esta seria la otra opcion
#hasta ahora estaria entre 0 y 2
#da error (TRY CATCH??) usar recursividad, <- esto NO LO HICE
#
#luego imprimir la respuesta por pantalla
#y volver al input

#VER la cantidad de veces a responder
#se puede hacer un while para poner
#la cantidad de veces acorde a las
#respuestas e implentar un saludo 
#de despedida

from inOut import inputList
from inOut import outputDict

from fuzzywuzzy import fuzz

import random


def chat():

	chatCount=0

	while yesNo=="y" and chatCount<21:

		inputText=input("\nEnter message: ")

		maxVal=0
		textOut=""

		for i in inputList:
			fuzzVal=fuzz.partial_ratio(i,inputText)
			# print(fuzzVal) #75
			if fuzzVal>maxVal: #75>0
				textOut=i      #Imprime String the list
				maxVal=fuzzVal #0=75 osea maxVal=75
			else:
				pass


		reply=""

		if textOut in outputDict:
			reply=random.choice(outputDict[textOut])
			print("\n"+reply)
			chatCount+=1
			
			if chatCount==21:
				print("\nSorry I'm lost for words, see you soon.")
				chatCount+=1

		elif outputDict.get(textOut)==None:
			print("\nSorry I can't undestand you, try again")
			chatCount-=1

		else:
			pass

def noValidation(yesNo):
	

	if yesNo=="n":
		print("\nOk. No chat then.")

	elif yesNo=="y":
		print("\nGreat let's chat \nI will reply a limited ammount of times")

		chat()

	else:
		print("\nSorry wrong letter. Try again.")
		
		yesNo=yesNo=input("\nPress y/n: ")[0]
		yesNo=yesNo.lower()

		noValidation(yesNo)


print("Welcome!!! Do you wanna chat?\n")

yesNo=input("Press y/n: ")[0]

yesNo=yesNo.lower()

val=noValidation(yesNo) #aca llama a la funcion para validar

	
'''
BUG: if you press other letter than y or n it will prompt
an error message and will ask you to enter a leter again
but if you press y after that it will come out.

And if you press y in the first attempt it will work

I really don't know why this is happening'''











