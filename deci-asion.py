from random import choice

# Picks a random anime plus a dish (1)
def watch_and_eat():
    pass

# Picks a random anime from  file (4)
def watch_anime():
    anime = choice(open('anime.txt').readlines()).rstrip()
    title, format = anime.split(':')
    print('\n' + title.capitalize() + " (" + format.capitalize() + ")\n")

# Picks a random dish form file (5)
def eat_food():
    food = choice(open('food.txt').readlines()).rstrip()
    dish, type, origin = food.split(':')
    print('\n' + dish.capitalize() + " " + type.capitalize() + " (" + origin.capitalize() + ")\n")



# Add an anime to the file
def add_anime():
    while True:
        title = input('Title: ')
        format = input('Is it a movie or a serie: ')
        with open('anime.txt', 'a') as f:
            if title == "" or format == "":
                print("\nSomething is missing..\n")
                add_anime()
            else:
                f.write(title + ':' + format + '\n')
                print("\nGreat\n")
                break


# List the entire anime file
def list_anime():
    with open('anime.txt', 'r') as f:
        for list in f.readlines():
            data = list.rstrip()
            title, format = data.split(":")
            print(title.capitalize() + " (" + format.capitalize() + ")")
            

def add_food():
    while True:
        dish = input('Dish: ')
        type = input('Type: ')
        origin = input('Origin: ')
        with open('food.txt', 'a') as f:
            if dish == "" or type == "" or origin == "":
                print("\nSomething is missing..\n")
                continue
            else:
                f.write(dish + ':' + type + ':' + origin + '\n')
                print("\nGreat\n")
                break
            

def list_food():
    with open('food.txt', 'r') as f:
        for list in f.readlines():
            data = list.rstrip()
            dish, type, origin = data.split(":")
            print(dish.capitalize() + " " + type + " (" + origin.capitalize() + ")")
    

def add_picker():
    while True:
        picker = input("Do you want add to the 'Anime' or 'Food' list?\n(Q to go back): ").lower()
        if picker == "q":
            break
        
        if picker == "anime":
            add_anime()
        elif picker == "food":
            add_food()
        else:
            print("Try again.. ")
            continue


def list_picker():
    while True:
        picker = input("Do you want to show the list of 'Anime' or 'Food'?\n(Q to go back): ").lower()
        if picker == "q":
            break

        if picker == "anime":
            list_anime()
        elif picker == "food":
            list_food()
        else:
            print("Try again.. ")
            continue


while True:
    choice = input(
        "(1) Watch & Eat\n(2) Add\n(3) List\nPress any of the above to get a suggestion: "
        ).lower()

    if choice == "q" or choice == "quit":
        break

    if choice == "1" or choice == "wae" or choice == "watch & eat":
        watch_and_eat()
    elif choice == "watch":
        watch_anime()
    elif choice == "eat" or choice == "only eat":
        eat_food()
    elif choice == "add":
        add_picker()
    elif choice == "list":
        list_picker()
    else:
        print("Hmmm, try again.. ")
        continue
