def load_dog_data(filename="chien2.txt"):
    dog_data = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            data_started = False
            for line in lines:
                if '------' in line:
                    data_started = True
                    continue
                if data_started and line.strip() and not line.startswith('| Race'):
                    parts = [p.strip() for p in line.split('|') if p.strip()]
                    if len(parts) == 5:
                        dog_data.append({
                            "Race": parts[0],
                            "Enfants": parts[1],
                            "Sportif": parts[2],
                            "Logement": parts[3],
                            "Taille": parts[4]
                        })
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{filename}' n'a pas été trouvé.")
        return None
    return dog_data

def get_user_preferences():
    print("\n--- Bienvenue à AdopteUnChien ! ---")
    print("Répondez à quelques questions pour découvrir votre compagnon idéal.\n")

    logement = ""
    while logement not in ["appartement", "maison"]:
        logement = input("Vivez-vous en appartement ou en maison ? (appartement/maison) : ").lower().strip()
        if logement not in ["appartement", "maison"]:
            print("Entrée invalide. Veuillez répondre par 'appartement' ou 'maison'.")

    sportif = ""
    while sportif not in ["oui", "non"]:
        sportif = input("Êtes-vous sportif ? (oui/non) : ").lower().strip()
        if sportif not in ["oui", "non"]:
            print("Entrée invalide. Veuillez répondre par 'oui' ou 'non'.")

    enfants = ""
    while enfants not in ["oui", "non"]:
        enfants = input("Avez-vous des enfants ? (oui/non) : ").lower().strip()
        if enfants not in ["oui", "non"]:
            print("Entrée invalide. Veuillez répondre par 'oui' ou 'non'.")

    taille = ""
    while taille not in ["petit", "moyen", "grand"]:
        taille = input("Préférez-vous un chien de petite, moyenne ou grande taille ? (petit/moyen/grand) : ").lower().strip()
        if taille not in ["petit", "moyen", "grand"]:
            print("Entrée invalide. Veuillez répondre par 'petit', 'moyen' ou 'grand'.")

    return {
        "Logement": logement,
        "Sportif": sportif,
        "Enfants": enfants,
        "Taille": taille
    }

def find_matching_dogs(preferences, dog_data):
    matching_dogs = []
    for dog in dog_data:
        if (dog["Logement"].lower() == preferences["Logement"] and
            dog["Sportif"].lower() == preferences["Sportif"] and
            dog["Enfants"].lower() == preferences["Enfants"] and
            dog["Taille"].lower() == preferences["Taille"]):
            matching_dogs.append(dog["Race"])
    return matching_dogs

def main():
    dog_data = load_dog_data()
    if dog_data is None:
        return

    user_preferences = get_user_preferences()
    matching_dogs = find_matching_dogs(user_preferences, dog_data)

    print("\n--- Voici les chiens qui pourraient vous correspondre : ---")
    if matching_dogs:
        for dog_race in matching_dogs:
            print(f"- {dog_race}")
    else:
        print("Désolé, nous n'avons pas trouvé de chien correspondant exactement à vos critères.")
        print("N'hésitez pas à essayer de nouvelles combinaisons !")

if __name__ == "__main__":
    main()