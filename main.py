
true_or_false = True

while true_or_false:
    print("оберіть операцію")
    print("1. Додавання: ")
    print("2. Віднімання: ")
    print("3. Множення: ")
    print("4. Ділення: ")    
    try:

        number1 = int(input("Введіть перше число "))
        number2 = int(input("Введіть друге число "))
        operation = input("виберіть операцію: ") 

        if operation == "1":
            result = number1 + number2
            print(result)

        elif operation == "2":
            result = number1 - number2
            print(result)

        elif operation == "3":
            result = number1 * number2
            print(result)

        elif operation == "4":
            result = number1 / number2
            print(result)
            
        else:
            print("Невірно задано арифметичну операцію")
    except ZeroDivisionError:
        print ("На нуль ділити не можн")
    except ValueError:
        print("only int")
    