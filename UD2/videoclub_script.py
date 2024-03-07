bbdd = {
    "Fight Club" : {"Name": "Fight Club", "Duration": 139, "Genre": "Drama"},
    "Good Will Hunting": {"Name": "Good Will Hunting", "Duration": 126, "Genre": "Drama"}
}

genre = ["Others", "Fiction", "Horror", "Comedy", "Animation"]

def insert_film(name, duration, genre):
    bbdd[name] = {"Name": name, "Duration": duration, "Genre": genre}

def insert_genre():
    x = input("Insert the genre: ")
    genre.append(x)

def list_detail():
    detail = input("Enter the detail you want to display (Name, Duration or Genre): ").capitalize()

    if detail == "Name":
        print("Film Names:")
        for name in bbdd.keys():
            print(name)
    elif detail == "Duration":
        total_duration = 0
        for name, details in bbdd.items():
            total_duration += details['Duration']
        print(f"Total Duration of all films: {total_duration} minutes")

    elif detail == "Genre":
        print("Film Genres:")
        for name, details in bbdd.items():
            print(f"{name}: {details['Genre']}")
    else:
        print("Invalid detail. Please choose from Name, Duration, or Genre.")


def film_information():
    film_name = input("Enter the name of the film: ")
    if film_name in bbdd:
        details = bbdd[film_name]
        print(f"Name: {details['Name']}, Duration: {details['Duration']} minutes, Genre: {details['Genre']}")
    else:
        print(f"The film '{film_name}' does not exist in the database.")

def film_detail(film, detail):
    if film in bbdd:
        details = bbdd[film]
        if detail == "Duration":
            print(f"Duration: {details['Duration']} minutes")
        elif detail == "Genre":
            print(f"Genre: {details['Genre']}")
        else:
            print("Invalid detail. Please choose from Name, Duration, or Genre.")
    else:
        print(f"The film '{film}' does not exist in the database.")

def delete_film():
    film_name = input("Enter the name of the film you want to delete: ")
    if film_name in bbdd:
        del bbdd[film_name]
        print(f"The film '{film_name}' has been deleted.")
    else:
        print(f"The film '{film_name}' does not exist in the database.")

menu = {
    "1": "Add film",
    "2": "Add genre",
    "3": "List films",
    "4": "List detail",
    "5": "Film information",
    "6": "Information detail",
    "7": "Delete films",
    "8": "Exit program"
}

selected_option = ""

while selected_option != "8":
    for key, value in menu.items():
        print(f"{key}: {value}")

    selected_option = input("Select an option (1-8): ")

    if selected_option == "1":
        print("You chose the option:", menu["1"])
        name = input("Insert name of the film: ")
        duration = input("Insert duration of the film: ")

        i = 1
        for g in genre:
            print(f"{i}. {g}")
            i += 1

        genre_select = int(input("Select which genre you want to choose (If you want to add a genre select 0): "))

        if genre_select == 0:
            insert_genre()
            genre_select = len(genre)

        insert_film(name, duration, genre[genre_select - 1])

    elif selected_option == "2":
        print("You chose the option:", menu["2"])
        insert_genre()

    elif selected_option == "3":
        print("You chose the option:", menu["3"])
        for movie_info in bbdd.values():
            print("-" * 20)
            print(f"Name: {movie_info['Name']}")
            print(f"Duration: {movie_info['Duration']} minutes")
            print(f"Genre: {movie_info['Genre']}\n")

    elif selected_option == "4":
        list_detail()

    elif selected_option == "5":
        film_information()

    elif selected_option == "6":
        film_name = input("Enter the name of the film: ")
        if film_name in bbdd:
            print("Select detail:")
            print("1. Duration")
            print("2. Genre")

            detail_choice = input("Enter your choice (1-2): ")

            if detail_choice == "1":
                film_detail(film_name, "Duration")
            elif detail_choice == "2":
                film_detail(film_name, "Genre")
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        else:
            print(f"The film '{film_name}' does not exist in the database.")

    elif selected_option == "7":
        delete_film()

print("Exiting program.")