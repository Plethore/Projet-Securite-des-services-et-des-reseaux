#!/usr/bin/env python3
# coding = utf-8

# Import des bibliotheques
import ManipulationFichiers # Pour la manipulation des fichiers
import ManipulationURL # Pour la manipulation des URLs
import Parametres # On importe le fichier qui contient les parametres

# Pour calculer la durée de l'exécution
import time
temps = time.time()

# Téléchargement du fichier des CPE et on le dézipe
#ManipulationFichiers.TelechargerFichierCPE()
#ManipulationFichiers.UnzipFichierCPE()

#listeNoms = ManipulationFichiers.GetNomsCPE(Parametres.fichierCPE[:-4])
#for nom in listeNoms:
#	if(nom.find("wordpress") != -1):
#		print(nom)

liste = ManipulationURL.GetListePath()
for path in liste:
	print(Parametres.siteCible1 + path)
	print(ManipulationURL.URLOnline(Parametres.siteCible1 + path))
	print(Parametres.siteCible2 + path)
	print(ManipulationURL.URLOnline(Parametres.siteCible2 + path))

# Suppression des fichiers
#ManipulationFichiers.SupprimerFichier(Parametres.fichierCPE)
#ManipulationFichiers.SupprimerFichier(Parametres.fichierCPE[:-4])

# Calcul de la durée du programme
print("Temps d'execution = ", time.time() - temps)
