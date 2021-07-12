# betterPrint par Dragorzor
# Fonction disponible : printError(), printWarning(), printLog(), timer()

import time

Reset = "\x1b[0m"
Bright = "\x1b[1m"

BgBlue = "\x1b[44m"

FgBlack = "\x1b[30m"
FgRed = "\x1b[31m"
FgGreen = "\x1b[32m"
FgYellow = "\x1b[33m"
FgBlue = "\x1b[34m"
FgMagenta = "\x1b[35m"
FgCyan = "\x1b[36m"
FgWhite = "\x1b[37m"

global timeSaved
timeSaved = 0

def printError(text):
    """
    Affiche un message d'erreur
    @param text La variable que vous souhaitez afficher ou juste du texte.
    """
    print(
        Reset +
        FgRed +
        Bright +
        "❌ - Une erreur est survenue :\n" +
        Reset +
        FgYellow +
        text +
        "\n" +
        Reset
    )

def printWarning(text):
    """
    Affiche un message d'avertissement
    @param text La variable que vous souhaitez afficher ou juste du texte.
    """
    print(
        Reset +
        FgRed +
        Bright +
        "⚠ - Attention :\n" +
        Reset +
        FgYellow +
        text +
        "\n" +
        Reset
    )

def printLog(text, argument = {"debug": False, "sep": ""}):
    """
    Remplace le print() par defaut de python pour vous donner plus d'information et de style !

    @param argument {"debug": ?, "sep": ?}

    Exemple pour activé le type de paramètre qui est donné
    printLog("Salut", {"debug": True}) -> "Texte : Salut"
    printLog("Salut", True) -> "Texte : Salut"

    Exemple pour utilisé un séparateur précis
    printLog("Salut ici", {"sep": "=>"}) -> "Salut => ici" 

    """
    if(type(argument) == dict):
        try:
            if(argument["sep"] != ""): text = argument["sep"].join(text.split(" "))
        
            if(argument["debug"] == True):
                print(
                    Reset +
                    FgGreen +
                    Bright +
                    "🟢 - CONSOLE :" +
                    FgMagenta +
                    "< DEBUG >\n" +
                    checkType(text) +
                    Reset +
                    FgWhite,
                    text,
                    "\n" +
                    Reset
                )
            else:
                print(
                    Reset +
                    FgGreen +
                    Bright +
                    "🟢 - CONSOLE\n" +
                    Reset +
                    FgWhite,
                    text,
                    Reset +
                    "\n"
                )
        except:
            print(
                Reset +
                FgGreen +
                Bright +
                "🟢 - CONSOLE\n" +
                Reset +
                FgWhite,
                text,
                Reset +
                "\n"
            )
    else:
        if(argument == True):
                print(
                    Reset +
                    FgGreen +
                    Bright +
                    "🟢 - CONSOLE :" +
                    FgMagenta +
                    "< DEBUG >\n" +
                    checkType(text) +
                    Reset +
                    FgWhite,
                    text,
                    "\n" +
                    Reset
                )
        else:
            print(
                Reset +
                FgGreen +
                Bright +
                "🟢 - CONSOLE\n" +
                Reset +
                FgWhite,
                text,
                Reset +
                "\n"
            )

def timer(active):
    """
    Un timer pour savoir en ms combien de temps vos opération prend.
    @param active Booléen si vrai vous l'activez, si faux ça le désactive.
    """
    global timeSaved
    if(timeSaved == 0): timeSaved = (time.time() * 1000)

    if(active == True):
        return print(
            Reset +
            Bright +
            FgBlue +
            "✅ - TIMER ON\n" +
            Reset
        )
    
    if((active == False) & (timeSaved != 0.0)):
        endTimer = (time.time() * 1000) - timeSaved
        timeSaved = 0
        return print(
            Reset +
            Bright +
            FgRed +
            "⭕ - TIMER OFF\n" +
            FgYellow +
            f"Temps : {FgBlue} {round(endTimer)} ms" +
            Reset
        )

def checkType(text):
    if(type(text) == int): return(f"{FgYellow}Nombre entier : {Reset}")
    if(type(text) == float): return(f"{FgYellow}Nombre décimal : {Reset}")
    if(type(text) == tuple): return(f"{FgMagenta}Tuple : {Reset}")
    if(type(text) == list): return(f"{FgMagenta}List : {Reset}")
    if(type(text) == set): return(f"{FgMagenta}Set : {Reset}")
    if(type(text) == frozenset): return(f"{FgMagenta}Frozenset : {Reset}")
    if(type(text) == dict): return(f"{FgMagenta}Dictionnaire : {Reset}")
    if(type(text) == complex): return(f"{FgMagenta}Complexe : {Reset}")
    if(type(text) == bytes): return(f"{FgMagenta}Bytes : {Reset}")
    if(type(text) == bytearray): return(f"{FgMagenta}Bytes Array : {Reset}")
    if(type(text) == str): return(f"{FgBlue}Texte : {Reset}")
    if(type(text) == bool): return(f"{FgCyan}Booléen : {Reset}")
    return(f"{FgCyan}Méthode / Fonction / Autre: {Reset}")

# timer(True)

# printError("Il te manque un espace !")
# printWarning("Il pleut !")

# printLog("Salut je suis du texte !", True)
# printLog(printLog, True)
# printLog(True, True)
# printLog(666, True)
# printLog(66.6, True)
# printLog(["Michel", "Jack"], True)
# printLog(set([3, 5, 7]), True)
# printLog({"USER": "Michel", "ID": "0123456789"}, True)
# printLog(('abc', 'def', 1997, 2000), True)

# printLog(frozenset(['Elsa', 'Otto']), True)
# printLog(b'ab\xff', True)
# printLog(bytearray(b'ab\xff'), True)
# printLog(complex(2,3), True)

# printLog("Simple message dans la console, hi !")
# printLog("Bonjour je suis un texte avec un séparateur qui est '=>' !", {"sep": " => "})

# i = 0
# test = ["1"]
# while i < 89999:
#     number = int(test[i]) * 235
#     test.append(number)
#     i += 1

# timer(False)