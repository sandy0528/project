'''
programer: Sandy Yang
Data:2023-10-03
Discribe: 
This program for practice error process and use lambdas and higher order functions

''' 

from functools import reduce

#create Class Animal
class Animal:
    def __init__(self, legs=4, hands=0):
        self.__legs = legs
        self.__hands = hands
    

    def getLegs(self):
        return self.__legs
    def getHands(self):
        return self.__hands

#create Class Bird
class Bird:
    def __init__(self, legs=2, wings=2):
        self.__legs = legs
        self.__wings = wings
    def getLegs(self):
        return self.__legs
    def getWings(self):
        return self.__wings

# create class Feline, inherite class Animal. add characteristic attributes
class Feline(Animal):
    def __init__(self):
        Animal.__init__(self)
        self._characteristic = "belongs to the cat family "
    def getCharacteristic(self):
        return self._characteristic
    
#create class Caninel, inherite class Animal. add characteristic attributes
class Caninel(Animal):
    def __init__(self):
        Animal.__init__(self)
        #super()
        self._characteristic = "belongs to the dog family "
    def getCharacteristic(self):
        return self._characteristic

#create class Flightbirds, inherite class Bird. add characteristic attributes
class Flightbirds(Bird):
    def __init__(self):
        Bird.__init__(self)
        self._characteristic = "flys and hunts for food "
    def getCharacteristic(self):
        return self._characteristic
    
# create class Tiger, inherite class Feline, add additionalCharacteristic attributes 
class Tiger(Feline):
    def __init__(self):
        Feline.__init__(self)
        self.__additionalCharacteristic = "can roar and are lethal predators"
    def getCharacteristic(self):
        return self._characteristic + " and " + self.__additionalCharacteristic
    
 # create class Wildcat, inherite class Feline, add additionalCharacteristic attributes    
class Wildcat(Feline):
    def __init__(self):
        Feline.__init__(self)
        self.__additionalCharacteristic = "climbs trees"
    def getCharacteristic(self):
        return self._characteristic + "and " + self.__additionalCharacteristic
    
# create class Wolves, inherite class Caninel, add additionalCharacteristic attributes
class Wolves(Caninel):
    def __init__(self):
        Caninel.__init__(self)
        self.__additionalCharacteristic = "hunt in packs and have a leader"
    def getCharacteristic(self):
        return self._characteristic + "and " + self.__additionalCharacteristic
    
  # create class Eagles, inherite class Flightbirds, add additionalCharacteristic attributes  
class Eagles(Flightbirds):
    def __init__(self):
        Flightbirds.__init__(self)
        self.__additionalCharacteristic = "flys extremely high and can see their prey from high up in the sky"
    def getCharacteristic(self):
        return self._characteristic + "and " + self.__additionalCharacteristic
 # create zoo class
class Zoo:
    def __init__(self):
        self.__animalList = list()
        self.__birdList = list()
    # add animal or bird to self.__animalList or self.__birdList
    def addAnimalOrBird(self,newanimalorbird):
        try:
            if not isinstance(newanimalorbird, (Animal,Bird)):
                raise ValueError("Invalid type. Only instances of Animal or Bird classes are allowed.")
        
            #Using filter function to ensure that only one object of each animal class can be added to the zoo. For example, zoo can have only one tiger. If we try to add more, print a message stating, animal already added.
            if any(filter(lambda animal: animal.__class__.__name__ == newanimalorbird.__class__.__name__, self.__animalList)) or any(filter(lambda bird: bird.__class__.__name__ == newanimalorbird.__class__.__name__, self.__birdList)):  
                raise ValueError (f"{newanimalorbird.__class__.__name__} already added to the zoo.")
            # if it is an animal and animal<2, add this animal to zoo
            if isinstance(newanimalorbird,Animal):
                if len(self.__animalList) < 2:
                    self.__animalList.append(newanimalorbird.__class__.__name__)
                    print(f"{newanimalorbird.__class__.__name__} successful to add")
                else:
                    print(f"zoo already have max animals.")
             # if it is a bird and bird<1, add this bird to zoo       
            else:
                if len(self.__birdList) < 1:
                    self.__birdList.append(newanimalorbird.__class__.__name__) 
                    print(f"{newanimalorbird.__class__.__name__} successful to add")
                else:
                    print(f"zoo already have max birds")
        except ValueError as e:
            print(e)

    # show the zoo all animals and bird information
    def looking(self):
        
        if len(self.__animalList) == 0 and len(self.__birdList) == 0:
            print("Zoo empty")

        def animalInfo(animal):
            return f"{animal} in the zoo. It is a Animal. It has {eval(animal)().getLegs()} legs and {eval(animal)().getHands()} hands. {eval(animal)().getCharacteristic()}" 
        
        def birdInfo(bird):
            return f"{bird} in the zoo. It is a Bird. It has {eval(bird)().getLegs()} legs and {eval(bird)().getWings()} wings. {eval(bird)().getCharacteristic()}"
        
        #animalStrings = list(map(animalInfo, self.__animalList))
        #birdstrings = list(map(birdInfo, self.__birdList))
        zooPrint = reduce(lambda x, y: "\n".join([x, y]), list(map(animalInfo, self.__animalList)) + list(map(birdInfo, self.__birdList))," ")
        print(zooPrint)
    
    #   look at all the canines in the zoo, use a filter function with lambdas for it. 
    def lookAtCanines(self):
        canines = filter(lambda animal: isinstance(eval(animal)(), Caninel), self.__animalList)
        canineInfo = list(map(lambda animal: f"{animal} in the zoo. It is a Canine. It has {eval(animal)().getLegs()} legs and {eval(animal)().getHands()} hands. {eval(animal)().getCharacteristic()}", canines))
        if canineInfo:
            print("\n".join(canineInfo))
        else:
            print("No canines in the zoo.")
    # filter out tiger in the zoo and look at them
    def lookAtTigers(self):
        tigers = filter(lambda animal: animal.startswith('Ti') and animal.endswith('er'), self.__animalList)
        tigerInfo = list(map(lambda animal: f"{animal} in the zoo. It has {eval(animal)().getLegs()} legs and {eval(animal)().getHands()} hands. {eval(animal)().getCharacteristic()}", tigers))
        
        if tigerInfo:
             print("\n".join(tigerInfo))
        else:
            print("No tigers in the zoo.")  
            
InvalidInput = "InvalidInput"
zoo = Zoo()
zoo.looking()
Terry=Tiger()
zoo.addAnimalOrBird(InvalidInput)
zoo.addAnimalOrBird(Terry)
zoo.addAnimalOrBird(Wolves())
zoo.addAnimalOrBird(Wildcat())
zoo.addAnimalOrBird(Eagles())
zoo.looking()
zoo.lookAtCanines()
zoo.lookAtTigers()