def sumation(number1,number2):
    return number1 + number2

def extraction(number1,number2):
    return number1 - number2

def multiplication(number1,number2):
    return number1 * number2

def division(number1,number2):
    return number1 / number2

calculateType = {   
"+" : sumation ,
"-" : extraction ,
"*" : multiplication ,
"/" : division 
}

def calculator():
    for symbol in calculateType:
        print(f"{symbol}")
    continues = True

    while continues:
        selectedsymbol = input(f"Please select a symbol for what you want to calculate.  ")
        number1 = int(input("Please enter first number. "))
        number2 = int(input("Please enter second number. "))
        calculating = calculateType[selectedsymbol]
        result = calculating(number1,number2)
        print(f"{number1} {selectedsymbol} {number2} = {result}")
        last = input("Do you want to do new calculate Yes/No ")
        if last == "No":
            continues = False
            print("Good Bye...")
        elif last == "Yes":
            continues = True    
        else:
            print("You made a wrong keystroke")        
calculator()
