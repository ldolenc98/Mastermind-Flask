import random 

from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route("/gera_numero")

def gera_numero():
    
    i = 0
    
    L = []
    
    while i < 4:

        x = random.randrange(10)
        
        while x not in L:
            
            L.append(x)
            
            i = i + 1
    
    a = str(str(L[0]) + str(L[1]) + str(L[2]) + str(L[3]))
    
    return a

@app.route("/inicia")

def inicia():

	arquivo = open("numero.txt", "w")

    	arquivo.write(gera_numero())

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

		
if __name__ == "__main__":
    app.run(port = 8090)

