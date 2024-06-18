text = 'Hello Zaira'
custom_key = 'python'

def vigenere(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + key) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

vigenere(text, custom_key)
# Vigenere cipher 
    # where the key for each letter is determined by another text, called the key 