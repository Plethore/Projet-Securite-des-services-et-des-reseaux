#!/usr/bin/env python3
# coding = utf-8

# Import des bibliotheques
import xml.etree.ElementTree as ET # Pour le parsing du XML
import ManipulationFichiers # Pour la manipulation des fichiers
import ManipulationURL # Pour la manipulation des URLs
import Parametres # Definit les parametres generaux

# Pour calculer la durée de l'exécution
import time 
temps=time.time()

# Téléchargement du fichier des CPE
ManipulationFichiers.Telecharger(Parametres.url, Parametres.fichierCPE)
# On dézipe le fichier
ManipulationFichiers.Unzip(Parametres.fichierCPE)

# On parse le fichier
tree = ET.parse(Parametres.fichierCPE[:-4])
root = tree.getroot()
#print(root.tag)

# Parcours des cpe-item
for child in root:
	# Parcours des noeuds des cpe-item
	for littlechild in child:
		# On récupère la balise name
		nom = littlechild.attrib.get('name')
		# Si nom n'est pas None, on l'affiche
		if(nom is not None):
			print(nom)

print(ManipulationURL.URLOnline("google.fr"))

ManipulationFichiers.SupprimerFichier(Parametres.fichierCPE)
ManipulationFichiers.SupprimerFichier(Parametres.fichierCPE[:-4])

# Calcul de la durée du programme
print("Temps d'execution = ", time.time() - temps)
