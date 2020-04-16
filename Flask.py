import random 

from flask import Flask, request, jsonify

import gerador

from pymongo import MongoClient


app = Flask(__name__)

@app.route("/gera_numero")

def gera_numero1():
    
	return gerador.gera_numero()

@app.route("/inicia")

def inicia():

	arquivo = open("numero.txt", "w")

    	arquivo.write(gera_numero1())

    	arquivo.close
	
	return jsonify({"Status":"OK"})

@app.route("/tentativa", methods=['GET'])

def comparador():

	L = []

	i = 0

	num = request.args.get('num')

	b = str(num)
	
	arquivo = open("numero.txt", "r")
	
	a = arquivo.read()

	lista = list(a)

	if len(b) == 4:

		while i < len(lista):

			if b[i] in lista:

				if b[i] == lista[i]:

					L.append("1")
			
					i = i + 1

				else:

					L.append("0")

					i = i + 1
			else:

				i = i + 1
		
		x = ""

		resultado = x.join(L)	
	
		return jsonify({"Status": resultado})

	else:

		return "O numero deve ter 4 digitos"

		
if __name__ == "__main__":
    app.run(port = 8090)



