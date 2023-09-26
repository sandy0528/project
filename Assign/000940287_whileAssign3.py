
bottles_number=100
bottles_number_words= {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 
8: 'eight', 9: 'nine',10:'Ten',11:'Eleven',12:'Twelve', 13:'Thirteen',14:'Fourteen',15:'Fifteen'}

while bottles_number>0:
    if bottles_number == 1:
        first_bottle_words = "bottle"
        second_bottle_words = "No more bottles"   
    elif bottles_number==2:
        first_bottle_words = "bottles"
        second_bottle_words= "bottle"
    else:
        first_bottle_words = "bottles"
        second_bottle_words= "bottle"

    if bottles_number in bottles_number_words.keys():
        print ( f"{bottles_number_words[bottles_number]}  {first_bottle_words} of beer on the wall,")
        print( f"{bottles_number_words[bottles_number]}  {first_bottle_words}  of beer!")
        print("Take one down,")
        print ("Pass it around,")
        if bottles_number == 1:
            print( f"{second_bottle_words}  of beer on the wall!\n")
        else:
            print(bottles_number_words[bottles_number-1] + " " + second_bottle_words +" " + "of beer on the wall! \n")
    else:
        print ( f"{bottles_number}  {first_bottle_words} of beer on the wall,")
        print( f"{bottles_number}  {first_bottle_words}  of beer!")
        print("Take one down,")
        print ("Pass it around,")
        if bottles_number==16:
           print(f"{bottles_number_words[bottles_number-1]}  {second_bottle_words} of beer on the wall! \n")
        else:
           print(f"{bottles_number-1}  {second_bottle_words} of beer on the wall! \n")

    bottles_number-=1
       