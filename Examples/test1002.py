import random
class Animal:
    def __init__(self, legs=4, hands=0):
        self._legs = legs
        self._hands = hands


class Bird:
    def __init__(self, legs=2, wings=2):
        self._legs = legs
        self._wings = wings

class Feline(Animal):
    def __init__(self):
        Animal.__init__(self)
        #self.characteristic = characteristic
        self.characteristic = "Belong to the cat family "
    def getcharacteristic(self):
        return self.characteristic

class Caninel(Animal):
    def __init__(self):
        #Animal.__init__(self,legs,hands)
        super()
        self.characteristic = "Belongs to the dog family "
    def getcharacteristic(self):
        return self.characteristic

class Flightbirds(Bird):
    def __init__(self):
        Bird.__init__(self)
        #self.characteristic = characteristic
        self.characteristic = "fly and hunt for food "
    def getcharacteristic(self):
        return self.characteristic

class Tiger(Feline):
    def __init__(self):
        Feline.__init__(self)
        self.additional_characteristic = "can roar and are lethal predators"
    def getcharacteristic(self):
        return self.characteristic + " and " + self.additional_characteristic

class Wildcat(Feline):
    def __init__(self):
        Feline.__init__(self)
        self.additional_characteristic = "climb trees"
    def getcharacteristic(self):
        return self.characteristic + "and " + self.additional_characteristic

class Wolves(Caninel):
    def __init__(self):
        Caninel.__init__(self)
        self.additional_characteristic = "hunt in packs and have a leader"
    def getcharacteristic(self):
        return self.characteristic + "and " + self.additional_characteristic

class Eagles(Flightbirds):
    def __init__(self):
        Flightbirds.__init__(self)
        self.additional_characteristic = "fly extremely high and can see their prey from high up in the sky"
    def getcharacteristic(self):
        return self.characteristic + "and " + self.additional_characteristic
    
Terry=Tiger()
Tony=Tiger()
Will= Wildcat()
Tom=Wolves()
Herry=Wolves()
Bella=Eagles()
Bunny=Eagles()
existanimal=["Terry","Tony","Will","Tom","Herry"]
existbird=["Bella","Bunny"]

zoo={
    'animals':{'max':2,'animalslist':[]},'birds':{'max':1,'birdslist':[]}
}

 

print(len(zoo['animals']['animalslist']))
print(zoo['animals']['max'])
if (len(zoo['animals']['animalslist'])) < zoo['animals']['max']:
    print("test")
#if len(zoo(len(zoo['animals']['animalslist']))['animals']<max)
  # animalslist.append.


#x = zoo.values()

#print(x)
#tony = Eagles()
#print(tony.getcharacteristic())
#zoo = { "animals": [tony]}

#print(len(zoo['animals']))
