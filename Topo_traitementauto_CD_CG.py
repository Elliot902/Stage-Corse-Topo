# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 10:24:17 2021

@author: Elliot Luçon
"""

'''
TRAITEMENT DONNEES TACHEO
AUTOMATISATION DU CALCUL CERCLE DROIT CERCLE GAUCHE

CONTEXTE : STAGE PLURIDISCIPLINAIRE ING2
'''

##### IMPORT #####

import sys
#import xml.etree.ElementTree as ET
from lxml import etree
import numpy as np





##### EXTRACTION FICHIER #####


##### FONCTIONS #####


def make_xml():
    node = ET.Element('foo')
    node.text = 'bar'
    doc = ET.ElementTree(node)
    return doc

def delete_element():
    path1 = 'basic.xml'
    tree = ET.parse(path1)
    root = tree.getroot()
    
    for direction in root[0][2][0].findall('direction'):
        root[0][2][0].remove(direction)
        print('New action')
    tree.write('evolution.xml')

    return None
    

def FindWayObs(root):
    '''

    Parameters
    ----------
    fichierXML : TYPE : 
        DESCRIPTION : 

    Returns : Racine de la première observation
    -------
    None.

    '''
    way = ''
    for i in range(4):
        # if root[i].tag indique "out of range" :
        #     break
            
        if ('obs' in root[i].tag):
            way = root[i].tag
            break
     
    if way != '':               
        for i in range(4):
            for j in range(4):
                if ('obs' in root[i][j].tag):
                    way = root[i][j].tag
                    break
        
    if way != '':
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    if 'obs' in root[i][j][k].tag:
                        way = root[i][j][k].tag
                        break
                    
                    
    if way=='':
        return 'Racine non trouvée'
    else:
        return way
    

#def delete_orientation():
    
#def delete_ouverture():
    
#def delete_fermeture():

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
    if dir_cercleD > 300:
        dir_cercleD = dir_cercleD - 400
    
    return dir_cercleD - (200 + dir_cercleD - dir_cercleG)/2



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




def calcul_direction_main(dicI, dicII):
    '''

    Parameters
    ----------
    dicI : TYPE : dictionnaire'
        DESCRIPTION : dictionnaire de la mesure d'angle horizontal en cercle droit
    dicII : TYPE : dictionnaire
        DESCRIPTION : dictionnaire de la mesure d'angle horizontal en cercle gauche

    Returns : (angle horizontal unique corrigé de l'erreur de tourillonnement, écart avec angle cerle droit)'
    -------
    None.

    '''
    dir_cercleD = float(dicI['val'])
    dir_cercleG = float(dicII['val'])
    
    if dir_cercleD > 300:
        dir_cercleD = dir_cercleD - 400
    
    final = dir_cercleD - (200 + dir_cercleD - dir_cercleG)/2
    erreur_tourillonnement = abs(dir_cercleD - final)
    
    return (final,erreur_tourillonnement)



def calcul_z_angle_main(dicI, dicII):
    '''

    Parameters
    ----------
    dicI : TYPE : dictionnaire'
        DESCRIPTION : dictionnaire de la mesure d'angle vertical en cercle droit
    dicII : TYPE : dictionnaire
        DESCRIPTION : dictionnaire de la mesure d'angle vertical en cercle gauche

    Returns : (angle vertical unique corrigé de l'erreur de tourillonnement, écart avec angle cerle droit)'
    -------
    None.

    '''
    vert_cercleD = float(dicI['val'])
    vert_cercleG = float(dicII['val'])
    
    final = vert_cercleD + (400 - vert_cercleD - vert_cercleG)/2
    erreur_tourillonnement = abs(vert_cercleD - final)
    return (final,erreur_tourillonnement)





if __name__ == "__main__":

   
    #path = sys.argv[1] # récupération du nom de fichier à partir de la ligne de commande
    #path0 = 'test.xml'
    #path1 = 'basic.xml'
    path = 'STMARTIN_M.xml'
    
    parser = etree.XMLParser()
    tree = etree.parse(path, parser)
    root = tree.getroot()
    namespaces = {'ns':'http://www.gnu.org/software/gama/gama-local'}
    for obs in root.xpath('//ns:obs', namespaces=namespaces):
        for direction in obs.xpath('ns:direction', namespaces=namespaces):
            print(direction.attrib['val'])
        for zangle in obs.xpath('ns:z-angle', namespaces=namespaces):
            print(zangle.attrib['val'])


    # #make_xml().write(sys.stdout) 
    
    
    # #fichier = np.genfromtxt("C:/Users/Utilisateur/Desktop/ENSG/Stage/Stage_ING2/Stage_corse_maxime_seguin/Part1_StVictorLaCoste/Traitement_donnees/Chapelle_StMartin/Topo/STMARTIN_M.xml")
    
    
    
    # #D:\obj\windows-release\37amd64_Release\msi_python\zip_amd64\ElementTree.py
    
    # #Chemin vers les packages xml de python 3.9
    # #C:\Users\Utilisateur\AppData\Local\Programs\Python\Python39\Lib\xml
    
    #import xml.etree.cElementTree as ET
    
    #root = ET.Element("root")
    #doc = ET.SubElement(root, "doc")
    
    #ET.SubElement(doc, "field1", name="blah").text = "some value1"
    #ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"
    

