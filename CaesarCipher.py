alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
runtime = True

while runtime == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26 #debug for integers entered above the list number.

    def caesar(plain_text, shift_amount):
        result_text = ""
        for letter in plain_text:
            if letter in plain_text:
                if letter in alphabet:
                    position = alphabet.index(letter)
                    if direction == "encode":
                        type = "encoded"
                        new_position = position + shift_amount
                    elif direction == "decode":
                        type = "decoded"
                        new_position = position - shift_amount
                    new_letter = alphabet[new_position]
                    result_text += new_letter
                else: #debug for symbols/numbers/spaces
                    result_text += letter
        print(f"The {type} text is {result_text}")
    caesar(plain_text=text, shift_amount=shift)

    further_caesar = input("Type 'yes' if you want to go again. Otherwise, type 'no.'\n").lower()
    if further_caesar == "no":
        runtime = False


# Original attempt below, the code hasn't been organised and formatted to be shorter.
# The above code is the complete and also shortened by roughly half.


# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")
#
# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         cipher_position = alphabet.index(letter)
#         new_position = cipher_position - shift_amount
#         new_letter = alphabet [new_position]
#         plain_text += new_letter
#     print(plain_text)
#
#
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)
#
