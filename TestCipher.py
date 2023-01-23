#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  File: TestCipher.py

#  Description: Program implements Rail Fence Cipher and Vigenere Cipher
 
#  Student Name: Gaytri Riya Vasal

#  Course Name: CS 313E 

#  Unique Number: 51120

#  Date Created: 2/2/2022

#  Date Last Modified: 2/4/2022

import sys

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode ( strng, key ):
    
    # removes whitespace in strng
    #new_strng = strng.replace(" ", "")
    # number of rows in matrix key
    rows = int(key)
    # number of columns in matrix is length of strng
    cols = len(strng)
    # creates a rows x cols matrix of "-"
    matrix = [["-" for i in range(cols)] for j in range(rows)]
    
    # increments row
    row_counter = 1
    
    # sets row and col to 0
    row = 0
    col = 0
    
    # traverse through each character in strng
    for ch in strng:
        # sets matrix at (row, col) to ch
        matrix[row][col] = ch
        # checks to see if row + row_counter exceeds bounds
        if row + row_counter < 0 or row + row_counter >= rows:
            # multiplies row_counter by -1 so zig-zag can go the opposite way
            row_counter *= -1
        # increase row by row_counter
        row += row_counter
        # col increases by 1
        col += 1
    
    # empty string to store encoded text
    encode_result = ""
    # traverse through matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != "-":
                # adds characters to encode_result by row
                encode_result += matrix[i][j]
                
   
    return encode_result

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode ( strng, key ):
    
    # removes whitespace in strng
    # new_strng = strng.replace(" ", "")
    # number of rows in matrix is key
    rows = int(key)
    # number of cols in matrix is length of strng
    cols = len(strng)
    # creates a rows x cols matrix
    matrix = [["" for i in range(cols)] for j in range(rows)]
    
    # increments row
    row_counter = 1
    
    # sets row and col to 0
    row = 0
    col = 0
    
   
   # marks cells that need to be filled by characters
   # loop through number of cols
    for i in range(cols):
        # marks cells in matrix that should contain a character
        matrix[row][col] =  "-"
        if row + row_counter < 0 or row + row_counter >= rows:
            # multiplies row_counter by -1 so zig zag pattern can continue in opposite way
            row_counter *= -1
        # increase row by row_counter
        row += row_counter
        # increase col by 1
        col += 1
    
    
    # replaces cells with "-" with respective character
    # keeps track of new_strng index
    strng_index = 0
    # traverse through matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "-":
                # replaces dash with new_strng at current index
                matrix[i][j] = strng[strng_index]
                # moves to next character of new_strng 
                strng_index += 1
    
    
    # reads matrix in diagonal fashion
    # empty string to store decoded text
    decode_result = ""
    
    # increments row by 1
    row_counter = 1
    
    # sets row and col to 0
    row = 0
    col = 0
    
    # loop through number of cols
    for i in range(cols):
        # adds (row, col) character to decode_result
        decode_result += matrix[row][col]
        if row + row_counter < 0 or row + row_counter >= rows:
            # multiplies row_counter by -1 so zig zag pattern can continue in the other direction
            row_counter *= -1
        # increase row by row_counter
        row += row_counter
        # increase col by 1
        col += 1 
    
    
    return decode_result

#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string ( strng ):
    
    # converts all characters to lower case
    strng = strng.lower()
    # loops through each character in strng
    for ch in strng:
        if not ch.isalpha():
            # removes non-alpha characters
            strng = strng.replace(ch, "")
            
    return strng	# placeholder for the actual return statement

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def encode_character (p, s):
    
    # checks to see if ascii value of pass character and difference between "a" and s is
    # less than the ascii value of "122"
    if (ord(p) + (ord(s) - 97)) <= 122:
        # starts at p and adds s - a letters
        return chr((ord(p) + ord(s)) - 97)

    else:
        # exceeds past z; restarts alphabet
        return chr((ord(p) + (ord(s) - 97)) - 26)

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character decoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def decode_character (p, s):
    # checks if s and p difference is greater than 0
    if (ord(s) - ord(p)) >= 0:
        # starts at a and adds s - a characters
        return chr(97 + (ord(s) - ord(p)))
        
    else:
        # exceeds past z; restarts alphabet
        return chr(ord(s) + 123 - ord(p))
    


#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: functions returns a single string that repeats the phrase until
#           it is the length of strng
def phrase_extension (strng, phrase):
    # filters phrase
    phrase = filter_string(phrase)
    # empty string that stores extended phrase
    new_phrase = ""
    # keeps track of phrase index
    phrase_index = 0
    # loops through length of strng
    for j in range(len(strng)):
        # adds phrase at current index to new_phrase
        new_phrase += phrase[phrase_index]
        if phrase_index == len(phrase) - 1:
            # resets index to 0 when it approaches bound
            phrase_index = 0
        else:
            # increase index by 1 to add next character to phrase
            phrase_index += 1
    return new_phrase




#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode ( strng, phrase ):
    # filter strng
    strng = filter_string(strng)
    # extends phrase to length of strng
    phrase = phrase_extension(strng, phrase)
    
    # instantiate empty list
    encodedstring = []

    # loops through length of strng
    for i in range(len(strng)):
        # encodes each character of strng 
        encodedstring.append(encode_character(phrase[i], strng[i]))

    return ''.join(encodedstring)

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode ( strng, phrase ):
    # filters strng
    strng = filter_string(strng)
    # extends phrase to length of strng
    phrase = phrase_extension(strng, phrase)
    
    # instantiate empty list
    decodedstring = []

    # loops through length of string
    for i in range(len(strng)):
        # decodes each character of string
        decodedstring.append(decode_character(phrase[i], strng[i]))

    return ''.join(decodedstring)
  

def main():
  # read the plain text from stdin
  rf_plaintext = sys.stdin.readline()

  # read the key from stdin
  encode_key = sys.stdin.readline()

  # encrypt and print the encoded text using rail fence cipher
  print("Rail Fence Cipher")
  print()
  print("Plain Text:", rf_plaintext)
  print("Key:", encode_key)
  print("Encoded Text:", rail_fence_encode(rf_plaintext, encode_key))
  print()
  
  # read encoded text from stdin
  rf_encoded_text = sys.stdin.readline()
   
  # read the key from stdin
  decode_key = sys.stdin.readline()

  # decrypt and print the plain text using rail fence cipher
  print("Encoded Text:", rf_encoded_text)
  print("Key:", decode_key)
  print("Plain Text:", rail_fence_decode(rf_encoded_text, decode_key))
  print()

  # read the plain text from stdin
  v_plaintext = sys.stdin.readline()

  # read the pass phrase from stdin
  encode_pass = sys.stdin.readline()

  # encrypt and print the encoded text using Vigenere cipher
  print("Vigenere Cipher")
  print()
  print("Plain Text:", v_plaintext)
  print("Pass:", encode_pass)
  print("Encoded Text:", vigenere_encode(v_plaintext, encode_pass))
  print()

  # read the encoded text from stdin
  v_encoded_text = sys.stdin.readline()

  # read the pass phrase from stdin
  decode_pass = sys.stdin.readline()

  # decrypt and print the plain text using Vigenere cipher
  print("Encoded Text:", v_encoded_text)
  print("Pass:", decode_pass)
  print("Plain Text:", vigenere_decode(v_encoded_text, decode_pass))
  print()


# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
  




