'''
programer: Sandy Yang
Data:2023-10-02
Discribe: 
This program creat a zoo which include 2 animals and 1 bird
''' 

import random
#create Class Animal
class Animal:
    def __init__(self, legs=4, hands=0):
        self._legs = legs
        self._hands = hands
    def getLegs(self):
        return self._legs
    def getHands(self):
        return self._hands

#create Class Bird
class Bird:
    def __init__(self, legs=2, wings=2):
        self._legs = legs
        self._wings = wings
    def getLegs(self):
        return self._legs
    def getWings(self):
        return self._wings

# create class Feline, inherite class Animal. add characteristic attributes
class Feline(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.characteristic = "belongs to the cat family "
    def getCharacteristic(self):
        return self.characteristic
    
#create class Caninel, inherite class Animal. add characteristic attributes
class Caninel(Animal):
    def __init__(self):
        Animal.__init__(self)
        #super()
        self.characteristic = "belongs to the dog family "
    def getCharacteristic(self):
        return self.characteristic

#create class Flightbirds, inherite class Bird. add characteristic attributes
class Flightbirds(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.characteristic = "flys and hunts for food "
    def getCharacteristic(self):
        return self.characteristic
    
# create class Tiger, inherite class Feline, add additionalCharacteristic attributes 
class Tiger(Feline):
    def __init__(self):
        Feline.__init__(self)
        self.additionalCharacteristic = "can roar and are lethal predators"
    def getCharacteristic(self):
        return self.characteristic + " and " + self.additionalCharacteristic
    
 # create class Wildcat, inherite class Feline, add additionalCharacteristic attributes    
class Wildcat(Feline):
    def __init__(self):
        Feline.__init__(self)
        self.additionalCharacteristic = "climbs trees"
    def getCharacteristic(self):
        return self.characteristic + "and " + self.additionalCharacteristic
    
# create class Wolves, inherite class Caninel, add additionalCharacteristic attributes
class Wolves(Caninel):
    def __init__(self):
        Caninel.__init__(self)
        self.additionalCharacteristic = "hunt in packs and have a leader"
    def getCharacteristic(self):
        return self.characteristic + "and " + self.additionalCharacteristic
    
  # create class Eagles, inherite class Flightbirds, add additionalCharacteristic attributes  
class Eagles(Flightbirds):
    def __init__(self):
        Flightbirds.__init__(self)
        self.additionalCharacteristic = "flys extremely high and can see their prey from high up in the sky"
    def getCharacteristic(self):
        return self.characteristic + "and " + self.additionalCharacteristic
 
 #instance class   
Terry=Tiger()
Will= Wildcat()
Herry=Wolves()
Bella=Eagles()
Bunny=Eagles()
Robin=Eagles()
#put instance in list
existAnimal=["Terry","Will","Herry"]
existBird=["Bella","Bunny","Robin"]
#define a zoo dic
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

#function addAnimal
def addAnimal(newanimal):
    if newanimal not in zoo['animals']['animalslist']:
        zoo['animals']['animalslist'].append(newanimal)
#random choose animal, until achieve max animal
choosingAnimal = True
while (choosingAnimal):
    addAnimal(random.choice(existAnimal))
    if (len(zoo['animals']['animalslist'])) >= zoo['animals']['max']:
        choosingAnimal=False  
           

print(f"Congratuation! You have created a zoo which includes {zoo['animals']['max']} animals and {zoo['birds']['max']}  bird ") 
print()
# print choose animal's features and characteristics
chooseAnimalList=zoo['animals']['animalslist']
for j in range(0,len(chooseAnimalList)):
    print(f"{eval(chooseAnimalList[j]).__class__.__name__} {chooseAnimalList[j]} in the zoo. It is a Animal.It\
 has {eval(chooseAnimalList[j]).getLegs()} legs and {eval(chooseAnimalList[j]).getHands()} hands. It\
 {eval(chooseAnimalList[j]).getCharacteristic()}")
#function addBird   
def addBird(newbird):
    if newbird not in zoo['birds']['birdslist']:
        zoo['birds']['birdslist'].append(newbird)
#random choose bird
choosingBird = True
while (choosingBird):
    addBird(random.choice(existBird))
    if (len(zoo['birds']['birdslist'])) >= zoo['birds']['max']:
        choosingBird=False  
#print choosen bird        
chooseBirdList=zoo['birds']['birdslist']
for k in range(0,len(chooseBirdList)):
    print(f"{eval(chooseBirdList[k]).__class__.__name__} {chooseBirdList[k]} in the zoo. It is a Bird. It\
 has {eval(chooseBirdList[k]).getLegs()} legs and {eval(chooseBirdList[k]).getWings()} wings. It\
 {eval(chooseBirdList[k]).getCharacteristic()}")

