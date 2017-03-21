#!/usr/bin/env python3
# coding = utf-8

# Pour dézipper le fichier
import zipfile
# Pour supprimer les fichiers
import os
# Pour télécharger le fichier
import urllib.request

# On dézippe le fichier
def Unzip(fichierZIP):
	zip_ref = zipfile.ZipFile(fichierZIP, 'r')
	zip_ref.extractall()
	zip_ref.close()

# On supprime le fichier
def SupprimerFichier(fichier):
	os.remove(fichier)

# On telecharge le fichier 
def Telecharger(url, NomFichier):
	urllib.request.urlretrieve(url, NomFichier)
