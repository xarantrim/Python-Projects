alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"Here's the {direction}d result: {end_text}")


from Caesar_cipher_art import logo

print(logo)

end_cipher = True
get_direction = True
while end_cipher:
    while get_direction:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction == "encode" or direction == "decode":

            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            shift = shift % 26

            caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

            restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n".lower())
            if restart == "no":
                end_cipher = False
                print("Goodbye!!")
        else:
            continue
# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         # if new_position > 26:
#         #     new_letter = alphabet[new_position - shift_amount]
#         #     cipher_text += new_letter
#         # else:
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")
#
#
# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     print(f"The encoded text is {plain_text}")
#
#
# if direction == "encode":
#     shift = int(input("Type the shift number(1-26):\n"))
#     if 26 >= shift > 0:
#         encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     shift = int(input("Type the shift number(1-26):\n"))
#     decrypt(cipher_text=text, shift_amount=shift)
