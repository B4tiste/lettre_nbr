import n_letter
import any_letter
import os


def clear(): return os.system('cls')


# clear()

if __name__ == "__main__":

    lettres = input('Entrer les lettres à rechercher : ').lower()

    a = n_letter.analyse(lettres)

    if a == False:

        print("Recherches de mots avec un nombre de lettres inférieur...")
        any_letter.analyse(lettres)
