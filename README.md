# BetterPrint-Python
Une façon revisité du print() de python.


## Sommaire
* [Description rapide](#description)
* [Comment l'utiliser ?](#utilisation)
* [Module utilisé](#modules)
* [Image](#image)


## ⚠ Testé avec le terminal de VSCode et celui de windows par défaut.
### Description
Il vous permet d'utiliser ces différentes fonctions :
- printError() -> Afficher un message d'erreur
- printWarning() -> Afficher un message d'avertissement
- printLog() -> Fonction principale qui remplace le print() habituel
- timer() -> Permet de lancer un timer pour mesurer le temps d’exécution en millisecondes


### Utilisation
```
printError("Vous avez oublié un espace !")
```
```
printWarning("Attention à la syntaxe !")
```
```
printLog("Salut je suis un message ! Et en plus on me spécifie que je suis du texte, génial !", {"debug": True)
```

PS pour le timer : Utiliser le en début de votre script comme ceci `timer(True)` et à la fin pour avoir le temps en ms `timer(False)`


### Modules
Les modules utilisé sont `time` et `colorama`.


### Image
![betterPrint_Python](https://i.imgur.com/zlK3Fo1.png)
