from random import choice

# Picks a random film plus a dish (1)
def watch_and_eat():
    watch = choice(open('film.txt').readlines()).rstrip()
    title, format = watch.split(':')
    eat = choice(open('food.txt').readlines()).rstrip()
    dish, type, origin = eat.split(':')
    print("\n" + title.capitalize() + " (" + format.capitalize() + ")\n" + dish.capitalize() + " " + type.capitalize() + " (" + origin.capitalize() + ")\n")
    while True:
        again = input("(1) Try again\n(Q) Exit\n").lower()
        if again == "1":
            watch_and_eat()
        elif again == "q" or again == "":
            quit()
        else:
            continue

# Add menu (2)
def add_picker():
    while True:
        picker = input("\n(1) Film\t(11) See list\n(2) Food\t(22) See list\n(Q) Return\nWhich list do you want to add to? ").lower()
        if picker == "q":
            break
        
        if picker == "1" or picker == "film":
            add_film()
        if picker == "11" or picker == "film list":
            list_film()
        elif picker == "2" or picker == "food":
            add_food()
        elif picker == "22" or picker == "food list":
            list_food()
        elif picker == "q":
            break
        elif picker == "qq":
            quit()
        else:
            continue

# List menu (3)
def list_picker():
    while True:
        picker = input("\n(1) Film\n(2) Food\n(Q) Return\nWhich list do you want to see? ").lower()
        if picker == "q":
            break

        if picker == "1" or picker == "film":
            list_film()
        elif picker == "2" or picker == "food":
            list_food()
        else:
            continue

# Add film to file (2-1)
def add_film():
    while True:
        title = input('Add title: ')
        format = input('Add type (movie, series, horror, etc.): ')
        with open('film.txt', 'a') as f:
            if title == "" or format == "":
                print("\nSomething is missing. Try again.\n")
                add_film()
            else:
                f.write(title + ':' + format + '\n')
                print("\n" + title.capitalize() + " " + format.capitalize() + "\nAdded 👍")
                break

# Add food to file (2-2)
def add_food():
    while True:
        dish = input('Dish: ')
        type = input('Type: ')
        origin = input('Origin: ')
        with open('food.txt', 'a') as f:
            if dish == "" or type == "" or origin == "":
                print("\nSomething is missing. Try again.\n")
                continue
            else:
                f.write(dish + ':' + type + ':' + origin + '\n')
                print("\n" + dish.capitalize() + " " + type.capitalize() + " " + "(" + origin.capitalize() + ") " + "\nAdded 👍")
                break
            
# List the film file (3-1)
def list_film():
    with open('film.txt', 'r') as f:
        for list in f.readlines():
            data = list.rstrip()
            title, format = data.split(":")
            print(title.capitalize() + " (" + format.capitalize() + ")")
            
# List the food file (3-2)
def list_food():
    with open('food.txt', 'r') as f:
        for list in f.readlines():
            data = list.rstrip()
            dish, type, origin = data.split(":")
            print(dish.capitalize() + " " + type + " (" + origin.capitalize() + ")")
    
# Start
while True:
    mode = input("\n(1) Watch'n Eat\n(2) Add\n(3) Lists\n(Q) Exit\nPress any of the above to get a suggestion: ").lower()
    
    if mode == "q" or mode == "quit":
        quit()

    if mode == "1" or mode == "":
        watch_and_eat()
    elif mode == "2" or mode == "add":
        add_picker()
    elif mode == "3" or mode == "list":
        list_picker()
    else:
        watch_and_eat()
