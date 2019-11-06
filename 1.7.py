class Animals:
    lifespan = 0
  
class Cattle (Animals):
    reproduction = "live birth"
    legs = 4
    food = ("hay", "greenery", "roots", "cereals")

class Birds (Animals):
    reproduction = "eggs"
    wings = True
    food = ("greenery", "roots", "cereals")

class Cow (Cattle):
    sound = "moo-moo"
    lifespan = 20
    horns = True
    food = Cattle.food[0], Cattle.food[1]

class Goat (Cattle):
    sound = "baa"
    lifespan = 16.5
    horns = True
    food = Cattle.food[0], Cattle.food[1]

class Sheep (Cattle):
    sound = "baa-baa"
    lifespan = 11
    horns = False
    food = Cattle.food[0], Cattle.food[1]

class Pig (Cattle):
    sound = "grunt-grunt"
    lifespan = 20
    horns = False
    food = Cattle.food[2], Cattle.food[3]

class Duck (Birds):
    sound = "quack-quack"
    lifespan = 7.5
    food = Birds.food[0], Birds.food[2]

class Chicken (Birds):
    sound = "cheep-cheep"
    lifespan = 4
    food = Birds.food[2]
  
class Goose (Birds):
    sound = "honk-honk"
    lifespan = 20
    food = Birds.food[0], Birds.food[1]
    
    
def report (console, specimen):
    try:
      if specimen.legs == 4:
        print ("As all cattle", console, "walks on 4 legs")
    except:
      None
    try:
      if specimen.wings == True:
        print ("All birds has wings. And", console, "too.")
    except:
      None
    print ("It is sounds:", specimen.sound)
    print ("Average lifespan is {} years".format(specimen.lifespan))
    if specimen.reproduction == "live birth":
      print ("Cattle are mammals.\nAnd all mammals are {} :3".format(specimen.reproduction))
    elif specimen.reproduction == "eggs":
      print ("Take care about their {}.\nIt is their children ^^".format(specimen.reproduction))
    if type(specimen.food) is tuple:
      print ("Ration: {}". format (", ".join(specimen.food)))
    else:
      print ("Ration: {}".format (specimen.food))
    try:
      if specimen.horns is True:
        print ("And it has horns!")
    except:
      return None
      
def main ():
    print ("Choose an animal at you farm. You have: cow, sheep, goat, pig, chicken, goose and duck.")  
    while True:
      console = input("\nYou have take a closer look at:").lower()
      if console == "cow":
        report(console, Cow())
      elif console == "sheep":
        report(console, Sheep())
      elif console == "pig":
        report(console, Pig())
      elif console == "goat":
        report(console, Goat())
      elif console == "chicken".lower():
        report(console, Chicken())
      elif console == "goose".lower():
        report(console, Goose())
      elif console == "duck".lower():
        report(console, Duck())
      elif console == "q":
        break
      else:
        print ("You don't have such animal at farm")
      
main ()
