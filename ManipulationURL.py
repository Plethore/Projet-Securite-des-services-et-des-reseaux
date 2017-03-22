#!/usr/bin/env python3
# coding = utf-8

# Pour utiliser os.popen
import os

def URLOnline(url):
	#if(os.system("curl -s --head " + url + " | head -n 1 | grep \"HTTP/1.[01] [23]\"") is not None):
	resultat = os.popen("curl -s --head " + url + " | head -n 1 | grep \"HTTP/1.[01] [23]\"", 'r')
	resultat = resultat.read()
	# Si la variable resultat n'est pas vide, c'est qu'il y a une réponse 
	if(resultat != ""):
		# On recupere juste le code
		resultat = resultat.split(" ")[1]
		# Si c'est un code 2XX, 3XX, 401, ou 403 la page est bonne
		if(((int(resultat) >= 200) and (int(resultat) <= 399)) or (int(resultat) == 401) or (int(resultat) == 403)):
			return(True)
	# Si resultat est vide ou si c'est un autre code, la page n'est pas bonne
	return(False)



