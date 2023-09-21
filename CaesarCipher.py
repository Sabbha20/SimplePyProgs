logo = '''
   _____ _____ _____  _    _ ______ _____     _____ ______           _____ ______ _____  
  / ____|_   _|  __ \| |  | |  ____|  __ \   / ____|  ____|   /\    / ____|  ____|  __ \ 
 | |      | | | |__) | |__| | |__  | |__) | | |    | |__     /  \  | (___ | |__  | |__) |
 | |      | | |  ___/|  __  |  __| |  _  /  | |    |  __|   / /\ \  \___ \|  __| |  _  / 
 | |____ _| |_| |    | |  | | |____| | \ \  | |____| |____ / ____ \ ____) | |____| | \ \ 
  \_____|_____|_|    |_|  |_|______|_|  \_\  \_____|______/_/    \_\_____/|______|_|  \_\
                                                                                          '''
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher_msg(msg, shifting, disha):
  final_msg=""
  shifting %= 26
  if disha  == "decode":
    shifting = shifting * (-1)
  for letters in msg:
    if letters not in alphabet:
      final_msg+=letters
    else:
      position = alphabet.index(letters)
      new_pos = position + shifting
      if new_pos > 25:
        new_pos-=26
      final_msg+=alphabet[new_pos]
  print(f'The {disha}d msg is: {final_msg}')

should_continue = True

while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  cipher_msg(msg=text, shifting=shift, disha=direction)

  res = input("Do you want to continue? y for YES, n for NO -> \n").lower()
  if res == 'n':
    should_continue = False
    print("BYE BYE!!!!")