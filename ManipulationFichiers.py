#!/usr/bin/env python3
# coding = utf-8

# Parametres globaux
import Parametres
# Pour dézipper le fichier
import zipfile
# Pour supprimer les fichiers
import os
# Pour télécharger le fichier
import urllib.request
# Pour le parsing du XML
import xml.etree.ElementTree as ET
# Pour la manipulation des fichiers json
import json

# On dézippe le fichier
def Unzip(fichierZIP):
	zip_ref = zipfile.ZipFile(fichierZIP, 'r')
	zip_ref.extractall()
	zip_ref.close()

def UnzipFichierCPE():
	Unzip(Parametres.fichierCPE)

# On supprime le fichier
def SupprimerFichier(fichier):
	os.remove(fichier)

# On telecharge le fichier 
def Telecharger(url, NomFichier):
	urllib.request.urlretrieve(url, NomFichier)
	
def TelechargerFichierCPE():
	TelechargerFichierCPE(Parametres.urlCPE, Parametres.fichierCPE)

# On récupère tous les noms des CPE dans un grand tableau
def GetNomsCPE():
	# On parse le fichier
	tree = ET.parse(Parametres.fichierCPE[:-4])
	root = tree.getroot()
	noms = [] # On initialise le tableau des noms
	
	# Parcours des cpe-item
	for child in root:
		# Parcours des noeuds des cpe-item
		for littlechild in child:
			# On récupère la balise name
			nom = littlechild.attrib.get('name')
			# Si nom n'est pas None, on l'affiche
			if(nom is not None):
				noms.append(nom) # On ajoute le nom courant a la liste des noms
	return(noms)

# On recupere la liste des fichiers dans le fichier Data_Liste.json
def GetListeFichiers():
	with open(Parametres.fichierDonnees) as dataFile:
		donnees = json.load(dataFile)
	return donnees["files"]

# On trie le fichier et on ne garde que les lignes uniques
def FileSortUnique(nomFichier):
	os.system("sort -u " + nomFichier + " -o " + nomFichier)



