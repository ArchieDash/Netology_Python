class Animals:
    lifespan = 0
    animal_class = ""
    green_food = ("hay", "greenery")
    food = ("roots", "cereals")


class Cattle(Animals):
    def __init__(self, animal_class="CATTLE"):
        self.animal_class = animal_class


class Birds(Animals):
    def __init__(self, animal_class="BIRD"):
        self.animal_class = animal_class


class Cow(Cattle):
    sound = "moo-moo"
    lifespan = 20
    horns = True
    food = Animals.green_food


class Goat(Cattle):
    sound = "baa"
    lifespan = 16.5
    horns = True
    food = Animals.green_food


class Sheep(Cattle):
    sound = "baa-baa"
    lifespan = 11
    horns = False
    food = Animals.green_food


class Pig(Cattle):
    sound = "grunt-grunt"
    lifespan = 20
    horns = False
    food = Animals.food


class Duck(Birds):
    sound = "quack-quack"
    lifespan = 7.5
    food = Animals.food[1], Animals.green_food[1]


class Chicken(Birds):
    sound = "cheep-cheep"
    lifespan = 4
    food = Animals.food[1]


class Goose(Birds):
    sound = "honk-honk"
    lifespan = 20
    food = Animals.green_food[1], Animals.food[0]


def report(specimen):
    print("\n", specimen.animal_class)
    print("It is sounds:", specimen.sound)
    print("Average lifespan is {} years".format(specimen.lifespan))
    if type(specimen.food) is tuple:
        print("Ration: {}".format(", ".join(specimen.food)))
    else:
        print("Ration: {}".format(specimen.food))
    try:
        if specimen.horns is True:
            print("And it has horns!")
    except:
        return None


def main():
    print("Choose an animal at you farm.\nYou have: cow, sheep, goat, pig, chicken, goose and duck. Q - for quit.")
    while True:
        console = input("\nYou have take a closer look at:").lower()
        if console == "cow":
            report(Cow())
        elif console == "sheep":
            report(Sheep())
        elif console == "pig":
            report(Pig())
        elif console == "goat":
            report(Goat())
        elif console == "chicken":
            report(Chicken())
        elif console == "goose":
            report(Goose())
        elif console == "duck":
            report(Duck())
        elif console == "q":
            break
        else:
            print("You don't have such animal at farm")


main()
