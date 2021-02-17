import sys
from functions import arithmetics 
from functions import geo

print('sys.pyth: ', sys.path)
# negative beispiele könnte  konflikte mit anderen funktionen geben:
#    1- from functions.arithmetics import *  
#    2- from functions import summe 

# Konstanten in Python werden groß geschriben. konvention!
OPERATIONS = {
    '+': arithmetics.summe,
    '*': arithmetics.multiplikation,
    '-': arithmetics.substraktion,
    'dist': geo.distance,                
}

print("Name des Dokuments: ", __name__)

def parse_user_input(user_input):
    """ Zerlege den Userinput in seine Bestandteile
    Beispiel Userinput: + 3 43
    Args: 
    user_input(str): die Usereingabe
    Returns:
    tuple(operator, operand, operand)q
    """
    user_input = user_input.split()  # ['+', '3', '43]
    operator = user_input.pop(0)
    a, b = float(user_input[0]), float(user_input[1])

    return operator, a, b


def controller(operator, a, b):
    op = OPERATIONS.get(operator)
    if op:
        return op(a, b)
    raise NotImplementedError("Diese operstion ist nicht implementiert")


def main():
    """Hauptprogramm. Hier wird der User-Input verarbeitet. Abruch mit_quit"""

    while True:
        # + 3 43
        user_input = input("Bitte Berechnung ein (Operator und 2 Operanden: ")

        if user_input in ["_quit", " _exit"]:
            print("Danke. Programm beendet")
            break
        
        operator, a, b = parse_user_input(user_input)
        result = controller(operator, a, b)
        print("Ergebnisse: ", result)


if __name__ == '__main__':
    main()
