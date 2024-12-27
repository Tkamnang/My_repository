def est_premier(nombre):
  """Fonction pour déterminer si un nombre est premier.

  Args:
    nombre: Le nombre à vérifier.

  Returns:
    True si le nombre est premier, False sinon.
  """

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
  """Fonction pour trouver tous les diviseurs d'un nombre.

  Args:
    nombre: Le nombre dont on cherche les diviseurs.

  Returns:
    Une liste contenant tous les diviseurs du nombre.
  """

  diviseurs_liste = []
  for i in range(1, nombre + 1):
    if nombre % i == 0:
      diviseurs_liste.append(i)
  return diviseurs_liste

# Demander à l'utilisateur d'entrer un nombre
nombre_utilisateur = int(input("Entrez un nombre entier : "))

# Vérifier si le nombre est premier et afficher le résultat
if est_premier(nombre_utilisateur):
  print(nombre_utilisateur, "est un nombre premier.")
else:
  print(nombre_utilisateur, "n'est pas un nombre premier.")

# Afficher tous les diviseurs du nombre
print("Les diviseurs de", nombre_utilisateur, "sont :", diviseurs(nombre_utilisateur))
if est_premier(nombre_utilisateur):
    mk_string = str(nombre_utilisateur)
    last_num = int(mk_string[-1])
    transition = nombre_utilisateur - last_num
    transition2 = transition * 10 + last_num
    transition3 = transition * 100 + last_num
    print(transition2, "Occurence suivante en 10")
    print(transition3, "Occurence suivante en 100")
