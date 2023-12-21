from instructions import instruction
from calculator import calc
from weight_scale import scale
def mainfunct():
    #menu
    print("Calculator Project by David Onyekachi.")
    print("-------------------------")
    print("Press [1] for Calculator")
    print("Press [2] for Instructions")
    print("Press [3] for Weight Scale")
    print("Press [4] to Exit.")
    print("--------------------------")

    choice = input("User: ") #input from the user
    if choice == '1':
        calc()
    elif choice == '2':
        instruction()
        mainfunct()
    elif choice == '3':
        scale()
    elif choice == '4':
        return 0
    else:
        print("That doesn't exist")
        mainfunct()


mainfunct() #calling main function

