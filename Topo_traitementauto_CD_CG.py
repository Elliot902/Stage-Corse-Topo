# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 10:24:17 2021

@author: Elliot Luçon (ENSG) & Maxime Seguin (MC - DRAC de Corse)
"""

'''
TRAITEMENT DONNEES TACHEO
AUTOMATISATION DU CALCUL CERCLE DROIT CERCLE GAUCHE

CONTEXTE : STAGE PLURIDISCIPLINAIRE ING2
'''

##### IMPORT #####

import sys
from lxml import etree
from lxml import builder # pour construire un fichier XML
import numpy as np





##### EXTRACTION FICHIER #####


##### FONCTIONS #####


def calcul_direction(dir_cercleD, dir_cercleG):
    '''

    Parameters
    ----------
    dir_cercleD : TYPE : float
        DESCRIPTION : angle horizontal en cercle droit
    dir_cercleG : TYPE : float
        DESCRIPTION : angle horizontal en cercle gauche

    Returns : angle horizontal unique corrigé de l'erreur de tourillonnement'
    -------
    None.

    '''
    dir_cercle = float()
    
    if dir_cercleD < 200:
        dir_cercle = (dir_cercleG+dir_cercleD - 200)/2
    
    if dir_cercleD > 200:
        dir_cercle = (dir_cercleG+dir_cercleD + 200)/2
        
    if (dir_cercleD == 200 and dir_cercleG > 200):
        dir_cercle = (dir_cercleG + dir_cercleD - 200)/2
    
    if (dir_cercleD == 200 and dir_cercleG < 200):
        dir_cercle = (dir_cercleG + dir_cercleD + 200)/2
    
    return np.round(dir_cercle, decimals=4)



def calcul_z_angle(vert_cercleD, vert_cercleG):
    '''

    Parameters
    ----------
    vert_cercleD : TYPE : float
        DESCRIPTION : angle vertical en cercle droit
    vert_cercleG : TYPE : float
        DESCRIPTION : angle vertical en cercle gauche

    Returns : angle vertical unique corrigé de l'erreur de tourillonnement'
    -------
    None.

    '''
    return vert_cercleD + (400 - vert_cercleD - vert_cercleG)/2



if __name__ == "__main__":

   
    #path = sys.argv[1] # récupération du nom de fichier à partir de la ligne de commande
    path = 'STMARTIN_M.xml'
    
    #fichierResultat = sys.argv[2] # récupération du nom de fichier de sortie
    nomFichierResultat = 'resultat.xml'
    fichierSortie = open(nomFichierResultat,'w')
    
    parser = etree.XMLParser()
    tree = etree.parse(path, parser)
    root = tree.getroot()
    namespaces = {'ns':'http://www.gnu.org/software/gama/gama-local'}
    for obs in root.xpath('//ns:obs', namespaces=namespaces):

        fichierSortie.write('<obs from="'+obs.attrib['from']+'" from_dh="'+obs.attrib['from_dh']+'">\n')
        
        direction = obs.xpath('ns:direction', namespaces=namespaces)
        zAngle = obs.xpath('ns:z-angle', namespaces=namespaces)
        sDistance = obs.xpath('ns:s-distance', namespaces=namespaces)

        for i in range(0,len(direction)-1):
            if (direction[i].attrib['to'] == direction[i+1].attrib['to'] and direction[i].attrib['to_dh'] == direction[i+1].attrib['to_dh']):
                
                fichierSortie.write('<direction to="'+direction[i].attrib['to']+'" val="')
                fichierSortie.write(str(calcul_direction(float(direction[i].attrib['val']),float(direction[i+1].attrib['val']))))
                fichierSortie.write('" to_dh="'+direction[i].attrib['to_dh']+'" />\n')
                
                fichierSortie.write('<z-angle to="'+zAngle[i].attrib['to']+'" val="')
                fichierSortie.write(str())
                fichierSortie.write('" to_dh="'+zAngle[i].attrib['to_dh']+'" />\n')
            
                fichierSortie.write('<s-distance to="'+sDistance[i].attrib['to']+'" val="')
                fichierSortie.write(str(np.round((float(sDistance[i].attrib['val'])+float(sDistance[i+1].attrib['val']))/2, decimals=3)))
                fichierSortie.write('" to_dh="'+sDistance[i].attrib['to_dh']+'" />\n')
                
        
        
#        for zangle in obs.xpath('ns:z-angle', namespaces=namespaces):
#            print(zangle.attrib['val'])
        fichierSortie.write('</obs>\n')
    fichierSortie.close()

    

