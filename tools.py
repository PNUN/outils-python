import json
import os


def ReadTheDict(dictname):
    """Read the json file specified in mydict
     mydict = 'myfile.json' """
    path = os.path.dirname(__file__)
    pathandname = os.path.join(path, dictname)
    try:
        with open(pathandname, "r") as source:
            readeddict = json.load(source)
    except Exception as mes:
        print('Oops! something went wrong when reading json : ' + str(mes))
        readeddict = {}
    finally:
        return readeddict


def WriteTheDict(mydict , dictname = 'poub.json'):
    """Write the dict in the json file in dictname = 'myfile.json'"""
    path = os.path.dirname(__file__)
    pathandname = os.path.join(path, dictname)

    try:
        with open(pathandname, "w") as source:
            json.dump(mydict, source, indent=4)
        answer = True
    except Exception as mes:
        print('Oops! something went wrong when writing json : ' + str(mes))
        answer = False
    finally:
        return answer

if __name__ == '__main__':
    duck = {'duck': 'walk like a duck'}
    if WriteTheDict(duck, 'duck.json'):
        print(ReadTheDict('duck.json'))
        
