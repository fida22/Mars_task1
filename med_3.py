def decrypt(message):
    #converting message into upper case
    message=message.upper()

    #result is used to store final output
    result=[]
    for i in range (len(message)):
        # Shift each character back by its 1-based position and convert it back to a character
        result.append(chr(ord(message[i])-(i+1)))

    # Join the characters to form the decrypted message
    result=''.join(result)

    return result
