import base64

encryp = ""
go = True


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = (ord(clear[i]) + ord(key_c)) % 256
        enc.append(enc_c)
    encryp = (base64.urlsafe_b64encode(bytes(enc)))
    print("Encoded String:", encryp)


def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc)
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + enc[i] - ord(key_c)) % 256)
        dec.append(dec_c)
    print("Decrypted String:", "".join(dec))


print("""
▄█▄    █▄▄▄▄ ▀▄    ▄ █ ▄▄     ▄▄▄▄▀ ████▄
█▀ ▀▄  █  ▄▀   █  █  █   █ ▀▀▀ █    █   █
█   ▀  █▀▀▌     ▀█   █▀▀▀      █    █   █
█▄  ▄▀ █  █     █    █        █     ▀████
▀███▀    █    ▄▀      █      ▀
        ▀              ▀
      """)
print("(Encode), (Decode), (Code), (Help) or (Exit)?")

while go:
    kind = input(">> ").lower()

    if kind == 'encode':
        clear = input("String: ")
        key = input("Password: ")
        encode(key, clear)
        print("For decoding to work, only use the text in quotes.\n")

    elif kind == 'decode':
        print("Only input the text inside the quotes.")
        enc = input("Encrypted Text: ")
        key = input("Password: ")
        decode(key, enc)
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
        print("'Exit' will exit Crypto.")
        print("'Help' shows this help.\n")

    elif kind == '':
        pass

    elif kind == 'exit':
        break

    elif go is False:
        exit()

    else:
        print("Invalid Input.\n")
