import string

def caesar(text,shift,alphabets):
  '''Algorithm to encrypt password'''
  global shifted_alphabets,table,final_shifted_alphabets, final_alphabets

  def shift_alphabets(alphabets):
    return alphabets[shift:] + alphabets[:shift]

  shifted_alphabets = tuple(map(shift_alphabets, alphabets))
  final_alphabets = ''.join(alphabets)
  final_shifted_alphabets = ''.join(shifted_alphabets)
  table = str.maketrans(final_alphabets, final_shifted_alphabets) 

  return text.translate(table)

message = "La Plateforme"

shift_interval = 3

print("Ceci est le message original: " + message)

encrypt = caesar(message,shift_interval ,[string.ascii_lowercase, string.ascii_uppercase, string.punctuation])

print("Ceci est le message encrypter: " + encrypt)

decrypt = caesar(encrypt,26-shift_interval ,[string.ascii_lowercase, string.ascii_uppercase, string.punctuation])

print("Ceci est le message decrypter: " + decrypt)