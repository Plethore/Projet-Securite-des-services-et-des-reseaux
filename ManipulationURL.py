#!/usr/bin/env python3
# coding = utf-8

# Pour utiliser os.popen
import os
# Pour utiliser GetListeFichiers
import ManipulationFichiers
import json

# Renvoie vrai si l'URL passée en paramètre est en ligne, faux sinon. NOTE : On suit les redirections
def URLOnline(url):
	# On recupere l'en-tête de la page
	resultat = os.popen("curl -s --head " + url, 'r')
	resultat = resultat.read()
	# Si il y a une redirection, on suit la redirection
	if(resultat.find("Location: ") != -1):
		return(URLOnline((resultat[resultat.find("Location: ")+10:resultat.find("\n", resultat.find("Location: "))])))
	
	# Si il y a un resultat, c'est que le site existe
	if(resultat != ""):
		# On garde juste le code de l'en-tête
		code = int(resultat[0:resultat.find("\n")].split(' ')[1])
		# Si c'est un code 2XX, 3XX, 401, ou 403 la page est bonne
		if(((code >= 200) and (code <= 399)) or (code == 401) or (code == 403)):
			return(True)
	# Si resultat est vide ou si c'est un autre code, la page n'est pas bonne
	return(False)

def GetListePath():
	liste = ManipulationFichiers.GetListeFichiers()
	listePath = []
	for file in liste:
		with open(file) as dataFile:
			donnees = json.load(dataFile)
		listePath.append(donnees["path"])
	return listePath






