import random
class Animal:
    def __init__(self, legs=4, hands=0):
        self._legs = legs
        self._hands = hands
    def getLegs(self):
        return self._legs
    def getHands(self):
        return self._hands


class Bird:
    def __init__(self, legs=2, wings=2):
        self._legs = legs
        self._wings = wings
    def getLegs(self):
        return self._legs
    def getWings(self):
        return self._wings


class Feline(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.characteristic = "belongs to the cat family "
    def getCharacteristic(self):
        return self.characteristic

class Caninel(Animal):
    def __init__(self):
        Animal.__init__(self)
        #super()
        self.characteristic = "belongs to the dog family "
    def getCharacteristic(self):
        return self.characteristic

class Flightbirds(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.characteristic = "flys and hunts for food "
    def getCharacteristic(self):
        return self.characteristic

class Tiger(Feline):
    def __init__(self):
        Feline.__init__(self)
        self.additionalCharacteristic = "can roar and are lethal predators"
    def getCharacteristic(self):
        return self.characteristic + " and " + self.additionalCharacteristic
    
    
class Wildcat(Feline):
    def __init__(self):
        Feline.__init__(self)
        self.additionalCharacteristic = "climbs trees"
    def getCharacteristic(self):
        return self.characteristic + "and " + self.additionalCharacteristic
    

class Wolves(Caninel):
    def __init__(self):
        Caninel.__init__(self)
        self.additionalCharacteristic = "hunt in packs and have a leader"
    def getCharacteristic(self):
        return self.characteristic + "and " + self.additionalCharacteristic
    
    
class Eagles(Flightbirds):
    def __init__(self):
        Flightbirds.__init__(self)
        self.additionalCharacteristic = "flys extremely high and can see their prey from high up in the sky"
    def getCharacteristic(self):
        return self.characteristic + "and " + self.additionalCharacteristic
    
Terry=Tiger()
Will= Wildcat()
Herry=Wolves()
Bella=Eagles()
Bunny=Eagles()
Robin=Eagles()
existAnimal=["Terry","Will","Herry"]
existBird=["Bella","Bunny","Robin"]
zoo={
    'animals':
        {
         'max':2,
         'animalslist':[]
        },
    'birds':{
             'max':1,
             'birdslist':[]
             }
}


def addAnimal(newanimal):
    if newanimal not in zoo['animals']['animalslist']:
        zoo['animals']['animalslist'].append(newanimal)

choosingAnimal = True
while (choosingAnimal):
    addAnimal(random.choice(existAnimal))
    if (len(zoo['animals']['animalslist'])) >= zoo['animals']['max']:
        choosingAnimal=False  
        
   

print("Congratuation! You have creat a zoo which includes 2 animals and 1 bird") 

chooseAnimalList=zoo['animals']['animalslist']
for j in range(0,len(chooseAnimalList)):
    print(f"Animal {chooseAnimalList[j]} in the zoo. It is a {eval(chooseAnimalList[j]).__class__.__name__}. It\
 has {eval(chooseAnimalList[j]).getLegs()} legs and {eval(chooseAnimalList[j]).getHands()} hands. It\
 {eval(chooseAnimalList[j]).getCharacteristic()}")
    
def addBird(newbird):
    if newbird not in zoo['birds']['birdslist']:
        zoo['birds']['birdslist'].append(newbird)

choosingBird = True
while (choosingBird):
    addBird(random.choice(existBird))
    if (len(zoo['birds']['birdslist'])) >= zoo['birds']['max']:
        choosingBird=False  
        
chooseBirdList=zoo['birds']['birdslist']
for k in range(0,len(chooseBirdList)):
    print(f"Bird {chooseBirdList[k]} in the zoo. It is a {eval(chooseBirdList[k]).__class__.__name__}. It\
 has {eval(chooseBirdList[k]).getLegs()} legs and {eval(chooseBirdList[k]).getWings()} wings. It\
 {eval(chooseBirdList[k]).getCharacteristic()}")

