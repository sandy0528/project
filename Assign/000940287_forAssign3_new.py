bottles_number_words= {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 
8: 'Eight', 9: 'Nine',10:'Ten',11:'Eleven',12:'Twelve', 13:'Thirteen',14:'Fourteen',15:'Fifteen'}

for bottles_number in range(100, 0, -1):
    if bottles_number == 1:
        first_bottle_words = "bottle"
        second_bottle_words = "No more bottles"   
    elif bottles_number==2:
        first_bottle_words = "bottles"
        second_bottle_words= "bottle"
    else:
        first_bottle_words = "bottles"
        second_bottle_words= "bottles"

    if bottles_number in bottles_number_words.keys():
        print (f"{bottles_number_words[bottles_number]} {first_bottle_words} of beer on the wall,")
        print( f"{bottles_number_words[bottles_number]} {first_bottle_words} of beer!")
        print("Take one down,")
        print ("Pass it around,")
        if bottles_number == 1:
            print( f"{second_bottle_words} of beer on the wall!\n")
        else:
            print(f"{bottles_number_words[bottles_number-1]} {second_bottle_words} of beer on the wall! \n")
    else:
        print (f"{bottles_number} {first_bottle_words} of beer on the wall,")
        print( f"{bottles_number} {first_bottle_words} of beer!")
        print("Take one down,")
        print("Pass it around,")
        if bottles_number==16:
           print(f"{bottles_number_words[bottles_number-1]} {second_bottle_words} of beer on the wall! \n")
        else:
           print(f"{bottles_number-1} {second_bottle_words} of beer on the wall! \n")
    
       
