# preGama
preGama effectue la réduction des séquences de mesure réalisées en cercle à droite puis cercle à gauche. Il permet de préparer les données de mesure effectuées sur le terrain pour leur calcul avec le logiciel GNU Gama.

## Organisation des données en entrée
Les mesures en cercle à droite puis cercle à gauche doivent être réalisées successivement sur le même point. En l'état actuel, preGama ne gère pas les séquences de tour d'horizon et n'effectue pas le contrôle de fermeture angulaire. On suppose ici que le contrôle de la fermeture angulaire est réalisé directement sur le terrain, en accord avec la précision angulaire de l'appareil.
Dans cette première version, preGama prend en compte uniquement les paires complètes de mesures sur chaque point (cad : angle horizontal, angle vertical et distance selon la pente). Les paires sans mesure de distance ou sans mesure d'angle vertical ne sont pour l'instant pas gérées par preGama.
