
'''
programer: Sandy Yang
Data:2023-09-27
Discribe: 
This program for ordering a pizza.
If user order one topping, the price shoule be $8; 
If user order 2 topping, the price shoule be $10;
If user order 3 topping, the price shoule be $12;
If user order 4 topping or everything, the price shoule be $14;
'''

#ask user's last name
last_name = input("What is your last name? ")
# function items show all the choice
def items(key):
    if (key == 1):
        return "Cheese"
    elif (key == 2):
        return "Pineapple"
    elif (key == 3):
        return "Pepperoni"
    if (key == 4):
        return "Ham"
    elif (key == 5):
        return "Everything"
    else:
        return "Done"
# Define a dictionary
extras = {1:2,2:2,3:2,4:2,5:8,6:False}
keys = list(extras)
# Ask the user for toppings until they select "Done"
# set tally=0 for counting the price
tally = 0
# List chosetopping will store user's choice
chosetopping=[]

choosing = True
while (choosing):
    for i in range(0, len(keys)):
        x = keys[i]
        print(str(x) + ".) " + items(x))
    choice = input("Choose a topping: ")
    # if user choose "Done",finished selecting toppings
    if (int(choice) == 6):
        choosing = extras[6]
    # account the price
    if (tally <= 6):
        tally = tally + extras[int(choice)]
    else:
        choosing = extras[6]
    #if user choose everything,thi price should be 14,finished selecting toppings
    if (int(choice) == 5):
        choosing = False
        tally = 8
    # put user's choice to chosetopping list
    chosetopping.append(items(int(choice)))  
    # remove the user's choice on the screen
    keys.remove(int(choice))
# Print the last name
print(f"Hello, {last_name}")
# Print the chosen topping
if "Done" in chosetopping:
    chosetopping.remove("Done")
if "Everything" in chosetopping:
    print("Your toping include everything")
else:
    print("Your toping include:"+ ','.join(chosetopping))
# Pring the total price
print("Your total comes to: ${:.2f}".format(6 + tally,2))
    
    



    
    

    


