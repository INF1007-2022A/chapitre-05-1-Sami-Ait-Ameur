#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number <= 0:
        number = number * -1
    return number


def use_prefixes() -> List[str]:
    a = []
    prefixes, suffixe = 'J K L M N O P Q', 'ack'
    jklmnop = prefixes.split()
    for i in range(len(jklmnop)):
        a.append(jklmnop[i] + suffixe)

    return a


def prime_integer_summation() -> int:
    s = [2, 3, 5]
    number = 6
    while len(s) < 100:
        prime = True
        for i in range(2, number//2):
                if number%i == 0:
                    prime = False
                    break
        if prime:
                s.append(number)
        number += 1

    return sum(s)


def factorial(number: int) -> int:
    numero = 1
    for i in range(number - 1):
        numero *= (number - i)
    return numero


def use_continue() -> None:
    for i in range(10):
        if i == 5:
            continue
        else:
            print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    verif_groups = []
    for group in groups:
        if len(group) > 10 or len(group) <= 3:
            verif_groups.append(False)
            continue
        if 25 in group:
            verif_groups.append(True)
            continue
        if max(group) > 70 and 50 in group:
            verif_groups.append(False)
            continue
        if min(group) < 18:
            verif_groups.append(False)
        else:
            verif_groups.append(True)

    return verif_groups

def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
