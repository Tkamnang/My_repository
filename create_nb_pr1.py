def est_premier(nombre):
    """Détermine si un nombre est premier."""
    if nombre <= 1:
        return False
    if nombre <= 3:
        return True
    if nombre % 2 == 0 or nombre % 3 == 0:
        return False
    i = 5
    while i * i <= nombre:
        if nombre % i == 0 or nombre % (i + 2) == 0:
            return False
        i += 6
    return True

def diviseurs(nombre):
    """Retourne la liste des diviseurs d'un nombre."""
    diviseurs_liste = []
    for i in range(1, int(nombre**0.5) + 1):
        if nombre % i == 0:
            diviseurs_liste.append(i)
            if i != nombre // i:
                diviseurs_liste.append(nombre // i)
    return diviseurs_liste

def main():
    """Fonction principale du programme."""
    nombre_utilisateur = int(input("Entrez un nombre entier : "))

    if est_premier(nombre_utilisateur):
        print(f"{nombre_utilisateur} est un nombre premier.")
    else:
        print(f"{nombre_utilisateur} n'est pas un nombre premier.")

    print("Les diviseurs de", nombre_utilisateur, "sont :")
    for diviseur in diviseurs(nombre_utilisateur):
        print(diviseur)

    if est_premier(nombre_utilisateur):
        mk_string = str(nombre_utilisateur)
        last_num = int(mk_string[-1])
        transition = nombre_utilisateur - last_num
        transition2 = transition * 10 + last_num
        transition3 = transition * 100 + last_num
        print(f"{transition2} Occurrence suivante en 10")
        print(f"{transition3} Occurrence suivante en 100")

if __name__ == "__main__":
    main()
