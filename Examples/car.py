class car:
    numberwheel=4

    def __init__(self,companyname,modelname,year,seats):
        self.companyname=companyname
        self.modelname=modelname
        self.year=year
        self.seats=seats
        self.speed=0
        
    def getCompanyname(self):
        return self.companyname
    def getModelname(self):
        return self.modelname
    def getyear(self):
        return self.year
    def getseats(self):
        return self.seats
    def getspeed(self):
        return self.speed

    @staticmethod
    def getnumberofwheels():
        return car.numberwheel

    def accelerate(self):
        currentspeed=self.speed
        self.speed+=5
        print(f"Car accelerates from {currentspeed} to {self.speed}")

    def brake(self):
        currentspeed=self.speed
        if currentspeed>=5:
            self.speed-=5
            print(f"Car barke from {currentspeed} to {self.speed}")
        elif currentspeed <= 5 and currentspeed > 0:
            self.speed = 0
            print(f"Car accelerates from {currentspeed} to {self.speed}")
        else:
            print("Car already stopped.")
            

civic = car("toyota","civic",2020,4)

print("companyname: ", civic.getCompanyname())
print("modelname: ",civic.getModelname())
print("year: ",civic.getyear())
print("number_of_seats: ",civic.getseats())
print("number_of_wheels: ",civic.getnumberofwheels())
print("current_speed: ",civic.speed)
civic.accelerate()
civic.accelerate()
civic.accelerate()
civic.brake()
civic.speed
print("current_speed: ",civic.getspeed())
         
        


          