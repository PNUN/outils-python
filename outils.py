import json
import os


def jsonWriter(dico, mafile):
    chemin = os.path.dirname(__file__)
    cheminconfig = os.path.join(chemin, mafile)

    try:
        with open(cheminconfig, "w") as source:
            json.dump(dico, source, indent=4)
        mes = 'yes'
    except Exception as mes:
        print(mes)
        mes = 'nope'
    return mes


def jsonReader(mafile):
    chemin = os.path.dirname(__file__)

    cheminconfig = os.path.join(chemin, mafile)

    dico = {}

    try:
        with open(cheminconfig, "r") as source:
            dico = json.load(source)

    except Exception as mes:

        print('Problème lecture de ' + mafile + ' :' + str(mes))
        print(dico)
        return dico

    finally:
        print(dico)

        return dico

