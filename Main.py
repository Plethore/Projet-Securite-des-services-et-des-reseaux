#!/usr/bin/env python3
# coding = utf-8

# Import des bibliotheques
import ManipulationFichiers # Pour la manipulation des fichiers
import Parametres # On importe le fichier qui contient les parametres
import TesterSite # Essaye tous les chemins des fichiers Data pour le site

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

TesterSite.Rapport(Parametres.siteCible1)
TesterSite.Rapport(Parametres.siteCible2)

# Suppression des fichiers
#ManipulationFichiers.SupprimerFichier(Parametres.fichierCPE)
#ManipulationFichiers.SupprimerFichier(Parametres.fichierCPE[:-4])

# Calcul de la durée du programme
print("Temps d'execution = ", time.time() - temps)
