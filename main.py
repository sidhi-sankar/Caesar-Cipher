# Defining a list of letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Defining the encryption and decryption function 
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char not in alphabet:
      end_text += char
    else:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

from art import logo
print(logo)
# Asking if the user wants to continue using the program
running_stat = True
while running_stat == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  # To convert the higher values to a range of 0 - 25
  if shift > 25:
    val = round(shift % 26)
    shift = val
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  stat = input("\nDo you want to restart the cipher program again?\nType 'yes' if you want to continue or 'no' if you want to exit the program: \n").lower()
  if stat == "yes":
    running_stat = True
  else:
    running_stat = False