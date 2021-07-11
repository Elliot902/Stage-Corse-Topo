# preGama
preGama effectue la réduction des séquences de mesure réalisées en cercle à droite puis cercle à gauche. Il permet de préparer les données de mesure effectuées sur le terrain pour leur calcul avec le logiciel GNU Gama.

## Organisation des données en entrée
Les mesures en cercle à droite puis cercle à gauche doivent être réalisées successivement sur le même point. En l'état actuel, preGama ne gère pas les séquences de tour d'horizon et n'effectue pas le contrôle de fermeture angulaire. On suppose ici que le contrôle de la fermeture angulaire est réalisé directement sur le terrain, en accord avec la précision angulaire de l'appareil.
Dans cette première version, preGama prend en compte uniquement les paires complètes de mesures sur chaque point (cad : angle horizontal, angle vertical et distance selon la pente). Les paires sans mesure de distance ou sans mesure d'angle vertical ne sont pour l'instant pas gérées par preGama.

## Evolutions futures
- [ ] Prise en compte des séquences de tour d'horizon avec contrôle de la fermeture angulaire et répartition de l'erreur de fermeture
- [ ] Correction des mesures de distance (température, pression atmosphérique, humidité relative, altitude)
- [ ] Prise en compte d'un coefficient de réfraction (conversion des distances selon la pente <s-distance /> en distances horizontales corrigées <distance />)
- [ ] Conversion des résultats d'ajustement en fichier SIG (Shapelfile ?) pour la visualisation du réseau et des ellipses d'erreur (script postGama ?)
- [ ] Simulation de réseau à partir d'un fichier SIG ou DXF : conversion en XML du dessin du réseau et simulation d'une série de mesures (script simuGama ?)
