def calculer_moyenne(notes):
  """Calcule et retourne la moyenne d'une liste de notes."""
  if not notes:
    return 0.0
  return sum(notes) / len(notes)


def afficher_resultat(nom, moyenne):
  """Affiche le nom, la moyenne et la mention/décision finale."""
  # Attribution de la mention et décision
  if moyenne >= 16:
    mention = "Très bien"
    decision = "Admis(e)"
  elif moyenne >= 14:
    mention = "Bien"
    decision = "Admis(e)"
  elif moyenne >= 12:
    mention = "Assez bien"
    decision = "Admis(e)"
  elif moyenne >= 10:
    mention = "Passable"
    decision = "Admis(e)"
  else:
    mention = "Insuffisante"
    decision = "Ajourné(e)"

  print("-" * 40)
  print(f"Étudiant : {nom}")
  print(f"Moyenne  : {moyenne:.2f} / 20")
  print(f"Mention  : {mention}")
  print(f"Décision : {decision}")
  print("-" * 40)

  return decision


def main():
  nb_etudiants = 5
  etudiants_admis = 0
  etudiants_ajournes = 0

  print("=== GESTION DES NOTES DES ÉTUDIANTS ===")

  # Boucle pour saisir les notes de 5 étudiants
  for i in range(1, nb_etudiants + 1):
    print(f"\n--- Saisie pour l'étudiant {i} ---")
    nom = input(f"Nom de l'étudiant {i} : ")

    notes = []
    # Supposons 3 matières par étudiant pour calculer une moyenne pertinente
    nb_matieres = 3
    print(
        f"Veuillez saisir les {nb_matieres} notes (entre 0 et 20) pour cet"
        " étudiant :"
    )

    for j in range(1, nb_matieres + 1):
      # Saisie initiale
      try:
        note = float(input(f"  Note {j} : "))
      except ValueError:
        note = -1  # Force l'entrée dans la boucle while si ce n'est pas un nombre

      # Vérification de la note avec une boucle while si elle est invalide
      while note < 0 or note > 20:
        print("  [Erreur] La note doit être comprise entre 0 et 20.")
        try:
          note = float(input(f"  Veuillez ressaisir la note {j} : "))
        except ValueError:
          note = -1

      notes.append(note)

    # Calcul de la moyenne
    moyenne = calculer_moyenne(notes)

    # Affichage du résultat et comptage
    decision = afficher_resultat(nom, moyenne)

    if decision == "Admis(e)":
      etudiants_admis += 1
    else:
      etudiants_ajournes += 1

  # Bilan final
  print("\n" + "=" * 40)
  print("BILAN FINAL DE LA SESSION")
  print(f"Nombre total d'étudiants évalués : {nb_etudiants}")
  print(f"Nombre d'étudiants admis : {etudiants_admis}")
  print(f"Nombre d'étudiants ajournés : {etudiants_ajournes}")
  print("=" * 40)


# Lancement du programme
if __name__ == "__main__":
  main()