# import colored
#
# Intialiser les listes : Notes France, EN-US
#
# DEBUT SCRIPT
#
__MODES__ = ["IONIEN", "DORIAN", "PHRYGIEN", "LYDIEN", "MIXOLYDIEN", "EOLIAN", "LOCRIEN"]
__NOTES__ = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
__NOTES_FR__ = ["DO", "DO#", "RE", "RE#", "MI", "FA", "FA#", "SOL", "SOL#", "LA", "LA#", "SI"]


# NOTES US_FR
class NOTES_US_FR:
    def __init__(self):
        # Affiche la correspondance Notes France -> EN-US
        print("NOTES US EQUALS FR - MUSIC THEORY")
        print("[ NOTES US = FR ]")
        for w, item in enumerate(__NOTES__):
            print(w, item, " -----> ", __NOTES_FR__[w])


class FIND_MODE:
    def __init__(self, your_mode):
        # Affiche un titre
        print("FIND YOUR MODES - MUSIC THEORY")
        # Initialise Deux listes et l'indice à 0 pour matcher avec la NOTE
        indice = 0
        # Boucle pour chaques MODES
        for x in __MODES__:
            # Affecte l'indice pour la note de départ du mode
            if x == "IONIEN":
                indice = 9
            if x == "DORIAN":
                indice = 7
            if x == "PHRYGIEN":
                indice = 5
            if x == "LYDIEN":
                indice = 4
            if x == "MIXOLYDIEN":
                indice = 2
            if x == "EOLIAN":
                indice = 0
            if x == "LOCRIEN":
                indice = -2
            if x == your_mode or your_mode == "ALL":
                print("[ " + x + " ]")
                # Boucle pour chaques notes du mode en cours
                for y, item in enumerate(__NOTES__, start=0):
                    lmbd = lambda y, b: y + b
                    print(y, " _ ", __NOTES__[y], " -----> ", __NOTES__[lmbd(y, indice)])
                    # Affecte l'indice pour la note après le dernière note de la liste, soit B = Si
                    if __NOTES__[lmbd(y, indice)] == "B" and x == "IONIEN":
                        indice = -3
                    if __NOTES__[lmbd(y, indice)] == "B" and x == "DORIAN":
                        indice = -5
                    if __NOTES__[lmbd(y, indice)] == "B" and x == "PHRYGIEN":
                        indice = -7
                    if __NOTES__[lmbd(y, indice)] == "B" and x == "LYDIEN":
                        indice = -8
                    if __NOTES__[lmbd(y, indice)] == "B" and x == "MIXOLYDIEN":
                        indice = -10
                    if __NOTES__[lmbd(y, indice)] == "B" and x == "EOLIAN":
                        indice = 0
                    if __NOTES__[lmbd(y, indice)] == "B" and x == "LOCRIEN":
                        indice = -2
                print("")


# En cours,...
"""class CHORDS:
    def __init__(self, tonique, tierce, quarte, quinte, sept, huit, neuf, onze, douze):
        print("[ YOUR CHORDS ]")
        indice = 2
        if tierce == "MAJOR":
            indice = 2
            key = NOTES.index(tonique)
            lmbd = lambda y, b: y + b
            print("TONIQUE = ", NOTES[key], " ; ", "TIERCE = ", NOTES[lmbd(key, indice)])
        else:
            key = NOTES.index(tonique)
            lmbd = lambda y, b: y + b
            print("TONIQUE = ", NOTES[key], " ; ", "TIERCE = ", NOTES[lmbd(key, indice)], "b")"""

#
# END SCRIPT
#
#
FIND_MODE("ALL")
