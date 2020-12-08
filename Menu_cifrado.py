import argparse
import detectSpanish
#  ----------Descifrado Cesar------------
def descifrar(message, clave):
    #message = input('Ingresa el mensaje: ')
    espacios = 1
    while espacios > 0:
        #clave = input('Ingresa tu palabra clave para cifrar: ')
        espacios = clave.count(' ')
        if clave.isalpha() == False:
            espacios += 1
    key = len(clave)

    SYMBOLS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890 !?.'

    translated = ''

    for symbol in message:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

    print(translated)

#  ------------------Cifrado Cesar----------------------
def cifrar(message, clave):
    #message = input('Ingresa el mensaje: ')
    espacios = 1
    while espacios > 0:
        #clave = input('Ingresa tu palabra clave para cifrar: ')
        espacios = clave.count(' ')
        if clave.isalpha() == False:
            espacios += 1
    key = len(clave)

    SYMBOLS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890 !?.'

    translated = ''

    for symbol in message:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex + key

            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

    print(translated)

#  ------------------Hackear Cesar----------------------
def hackear(message):
    # Caesar Cipher Hacker
    # https://www.nostarch.com/crackingcodes (BSD Licensed)

    #message = input('Ingresa el mensaje: ')
    SYMBOLS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890 !?.'

    # Loop through every possible key:
    for key in range(len(SYMBOLS)):
        # It is important to set translated to the blank string so that the
        # previous iteration's value for translated is cleared.
        translated = ''

        # The rest of the program is almost the same as the original program:

        # Loop through each symbol in `message`:
        for symbol in message:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key

                # Handle the wrap-around:
                if translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)

                # Append the decrypted symbol:
                translated = translated + SYMBOLS[translatedIndex]

            else:
                # Append the symbol without encrypting/decrypting:
                translated = translated + symbol

        # Display every possible decryption:
        if detectSpanish.isEnglish(translated) == True:
            print('Key #%s: %s' % (key, translated))


"""try:
    parser = argparse.ArgumentParser(description='Cifra, descifra o hackea un mensaje')
    parser.add_argument('-m', '--modo', type=str, metavar='', help='Cifra[c], descifra[d] o hackea[h]')
    parser.add_argument('-msj', '--mensaje', type=str, metavar='', help='mensaje de entrada')
    parser.add_argument('-c', '--clave', type=str, metavar='', help='clave que se le dio')
    args=parser.parse_args()
    #print(args)
    modo=args.modo
    mensaje=args.mensaje
    clave=args.clave
    if modo == "c" and mensaje != None and clave != None:
        print("Cidrado Cesar")
        print("Mensaje: "+ mensaje, "Clave: "+clave)
        cifrar(mensaje, clave)
    elif modo == "d" and mensaje != None and clave != None:
        print("Descifrado Cesar")
        print("Mensaje: "+ mensaje, "Clave: "+clave)
        descifrar(mensaje, clave)
    elif modo == "h" and mensaje != None and clave == None:
        print("Hackeo Cesar")
        hackear(mensaje)
    else:
        print("Opción no valida, intente de nuevo")
except TypeError:
    print("Error, formato de entrada no valido")"""
