# Informations utilisateur • Robot Discord

Ce bot Discord très simple vous permet **d'obtenir des informations sur un utilisateur** via la commande `userinfo`, ou lorsqu'un nouveau membre rejoindre votre serveur.
> Ce projet a pour but de fournir un exemple concret aux utulisateurs souhaitant apprendre l'utilisation de [discord.py](https://github.com/Rapptz/discord.py).

![](https://i.imgur.com/RKgSNJJ.png)

## Configuration
Avant de lancer le robot, il est nécessaire de le configurer. Pour cela, renommez le fichier `config-example.json` en `config.json`. Voici les variables que vous pouvez personnaliser :

| Nom du paramètre | Description                                                                         |
|------------------|-------------------------------------------------------------------------------------|
| **token**        | Token à utiliser pour se connecter à un robot                                       |
| prefix           | Préfixe des commandes                                                               |
| activity         | Texte d'activité (Regarde ...)                                                      |
| join_logs_chan   | Identifiant du salon des logs des nouveaux utilisateurs (supprimer pour désactiver) |

## Lancement
Assurez vous d'avoir **Python 3.6** au minimum d'installé sur votre machine.

**Installation des dépendances :** `pip install -r requirements.txt`  
**Lancement du bot :** `python main.py`

## License
```
Copyright 2019 baptiste0928

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
