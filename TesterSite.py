#!/usr/bin/env python3
# coding = utf-8

# Import des bibliotheques
import ManipulationURL # Pour la manipulation des URLs
import ManipulationFichiers # Pour trier le fichier
import urllib.parse # Pour garder ce qu il faut de l url

# On essaye les URLs du site
def Rapport(url):
	url = ManipulationURL.URLOnline(url)
	cheminRapport = "Reports/" + urllib.parse.urlsplit(url).netloc + ".txt"
	liste = ManipulationURL.GetListePath()
	for path in liste:
		resultat = ManipulationURL.URLOnline(url + path)
		if(resultat != ""):
			fichier = open(cheminRapport, "a")
			fichier.write(resultat + "\n")
			fichier.close()

	# On trie le fichier et on garde les lignes uniques
	ManipulationFichiers.FileSortUnique(cheminRapport)

