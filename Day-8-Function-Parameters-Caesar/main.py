import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    caesar_text = ""
    shift %= 26
    if direction == "decode" and shift > 0:
        shift *= -1

    for t in text:
        if t in alphabet:
            position = alphabet.index(t)
            caesar_text += alphabet[position + shift]
        else:
            caesar_text += t
    return caesar_text

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar_text = caesar(text, shift, direction)
    print(f"The {direction}d text is {caesar_text}")
    answer = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if answer == "no":
        should_end = True
        print("Goodbye")

# def encrypt(plain_text, shift):
#     cipher_text = ""
#     for t in plain_text:
#         # give first index found
#         position = alphabet.index(t)
#         cipher_text += alphabet[position + shift]
#     return cipher_text

# def decrypt(cipher_text, shift):
#     plain_text = ""
#     for t in cipher_text:
#         position = alphabet.index(t)
#         plain_text += alphabet[position - shift]
#     return plain_text

   