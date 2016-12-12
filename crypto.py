import base64
import core


encryp = ""
go = True

print("""
▄█▄    █▄▄▄▄ ▀▄    ▄ █ ▄▄     ▄▄▄▄▀ ████▄
█▀ ▀▄  █  ▄▀   █  █  █   █ ▀▀▀ █    █   █
█   ▀  █▀▀▌     ▀█   █▀▀▀      █    █   █
█▄  ▄▀ █  █     █    █        █     ▀████
▀███▀    █    ▄▀      █      ▀
        ▀              ▀
      """)
print("(Encode), (Decode), (Code) or (Help)?")

while go:
    kind = input(">> ").lower()

    if kind == 'encode':
        clear = input("String: ")
        key = input("Password: ")
        core.encode(key, clear)
        print("For decryption to work, only copy the text in quotes.\n")

    elif kind == 'decode':
        print("Only input the text inside the quotes.")
        enc = input("Encrypted Text: ")
        key = input("Password: ")
        core.decode(key, enc)
        print()

    elif kind == 'code':
        if encryp == "":
            print("You have not generated a Base64 Code yet. Please type 'encode' to generate one.\n")
        else:
            print(base64.urlsafe_b64encode(bytes(enc)))

    elif kind == 'help':
        print("Crypto Help")
        print("'Encode' will encode a String with a Key into Base64.")
        print("'Decode' will decode a String from Base64. Have your Key on hand.")
        print("'Code' will show the most recently generated code again.")
        print("'Help' shows this help.\n")

    elif kind == '':
        pass

    else:
        print("Invalid Input.\n")
