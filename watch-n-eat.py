from random import choice

# Picks a random film plus a dish (1)
def watch_and_eat():
    try:
        watch = choice(open('film.txt').readlines()).rstrip()
        title, format = watch.split(':')
        eat = choice(open('food.txt').readlines()).rstrip()
        dish, type, origin = eat.split(':')
        print("\n" + '\033[1m' + title.capitalize() + '\033[0m' + " (" + format.capitalize() + ")\n" + '\033[1m' + dish.capitalize() + " " + type.capitalize() + '\033[0m' + " (" + origin.capitalize() + ")\n")
        while True:
            again = input("(1) Try again\n(Q) Return\n").lower()
            if again == "1":
                watch_and_eat()
                break
            elif again == "q":
                break
            else:
                continue
    except:
        print('\033[92m' + "\nYou need to add your favorite shows and dishes to the lists." + '\033[00m')


# Add menu (2)
def add_picker():
    while True:
        picker = input("\n(1) Film\n(2) Food\n(Q) Return\nWhich list do you want to add to? ").lower()
        if picker == "1":
            add_film()
        elif picker == "2":
            add_food()
        elif picker == "q":
            break
        else:
            continue

# List menu (incl. empty line remover) (3)
def list_picker():
    while True:
        picker = input("\n(1) Film\n(2) Food\n(Q) Return\nWhich list do you want to see? ").lower()
        if picker == "1":
            list_film()
        elif picker == "2":
            list_food()
        elif picker == "q":
            break
        else:
            continue

# Add film to file (2-1)
def add_film():
    while True:
        title = input('Add title: ').replace(":", "")
        format = input('Add type (movie, series, horror, etc.): ').replace(":", "")
        with open('film.txt', 'a') as f:
            if title == "" or format == "":
                print("\nSomething is missing. Try again.\n")
                add_film()
                break
            else:
                f.write(title + ':' + format + '\n')
                print("\n" + '\033[1m' + title.capitalize() + '\033[0m' + " (" + format.capitalize() + ")" + "\nAdded to the list 👍")
                break

# Add food to file (2-2)
def add_food():
    while True:
        dish = input('Name of dish: ').replace(":", "")
        type = input('Type of dish (chicken, vegan, dessert etc.): ').replace(":", "")
        origin = input('Origin (Country, book, friend etc.): ').replace(":", "")
        with open('food.txt', 'a') as f:
            if dish == "" or type == "" or origin == "":
                print("\nSomething is missing. Try again.\n")
                continue
            else:
                f.write(dish + ':' + type + ':' + origin + '\n')
                print("\n" + '\033[1m' + dish.capitalize() + " " + type.capitalize() + '\033[0m' + " " + "(" + origin.capitalize() + ") " + "\nAdded to the list 👍")
                break

# List the film file (3-1)
def list_film():
    try:
        with open('film.txt', 'r') as f:
            for list in f.readlines():
                data = list.rstrip()
                title, format = data.split(":")
                print(title.capitalize() + " (" + format.capitalize() + ")")
    except:
        print('\033[91m' + "\nYou have too many ':' in your film.txt file." + '\033[00m')

# List the food file (3-2)
def list_food():
    try:
        with open('food.txt', 'r') as f:
            for list in f.readlines():
                data = list.rstrip()
                dish, type, origin = data.split(":")
                print(dish.capitalize() + " " + type + " (" + origin.capitalize() + ")")
    except:
        print('\033[91m' + "\nYou have too many ':' in your food.txt file." + '\033[00m')

# Empty line eraser
def empty_line():
    with open('film.txt') as reader, open('film.txt', 'r+') as writer:
        for line in reader:
            if line.strip():
                writer.write(line)
                writer.truncate()
    with open('food.txt') as reader, open('food.txt', 'r+') as writer:
        for line in reader:
            if line.strip():
                writer.write(line)
                writer.truncate()

# Add empty files
def add_files():
    with open("film.txt","a") as file:
        file.write("")
    with open("food.txt","a") as file:
        file.write("")

# Start
while True:
    try:
        add_files()
        empty_line()
        mode = input("\n(1) Watch'n Eat\n(2) Add\n(3) Lists\n(Q) Exit\nPress any of the above to continue: ").lower()
        if mode == "1":
            watch_and_eat()
        elif mode == "2":
            add_picker()
        elif mode == "3":
            list_picker()
        elif mode == "q":
            quit()
        else:
            continue
    except:
        KeyboardInterrupt
        quit()
