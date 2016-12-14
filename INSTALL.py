
import os

if os.name == 'posix':
    os.system("sudo pip install pyperclip")
    print("A linux installation was detected. Would you like to install crypto to the /bin folder so")
    print("it can be run from the terminal? (y/n)")
    ask = input(">> ").lower()

    if ask == 'y':
        os.system("chmod +x crypto.py")
        os.system("sudo mv crypto.py /bin")
        print("Great! The installation was completed.")
        print("All dependencies were installed.")
        input("Press enter to finish.")

    if ask == 'n':
        print("Ok then.")
        print("All dependencies were installed.")
        input("Press enter to finish.")

else:
    os.system("pip install pyperclip")
    print("All dependencies were installed.")
    input("Press enter to finish.")
