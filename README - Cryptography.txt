
PROJECT DESCRIPTION AND GUIDELINES PROVIDED ON ASSIGNMENT INSTRUCTIONS

Cryptography is an ancient study of secret writing. There is a wealth of literature in this field. An extremely readable book on this subject is The Code Book by Simon Singh. This is a field of study that is of particular relevance in Computer Science. Given the widespread use of computers, one of the things people are interested in is making transactions over the internet more secure.

There are two classes of ciphers - substitution ciphers and transposition ciphers. The substitution ciphers replace individual characters in a string. Transposition ciphers on the other hand scramble the characters in the string. We will look at two representative ciphers in both the classes. The transposition cipher that you will implement is called Rail Fence Cipher. For the subsitution cipher we have chosen the Vigenere Cipher.

Rail Fence Cipher: 

The rail fence cipher is also known as the zigzag cipher and is a form of a transposition cipher that jumbles up the order of the letters. The rail fence cipher works by writing your plain-text downwards and diagonally on successive rows. The number of rows is given by a key. Once you reach the bottom row, you traverse upwards and diagonally. After you reach the top row, the direction is changed again, leading to a zigzag manner in which the plain-text is written. After the plain-text is written in this form, the rows are combined to create the cipher-text.

For example, let us consider the plaintext helloworld with key = 3.

Plain Text: h e l l o w o r l d

Key: 3

To encrypt this message we first write over three lines as follows:

h	-	-	-	o	-	-	-	l	-
-	e	-	l	-	w	-	r	-	d
-	-	l	-	-	-	o	-	-	-

The cipher text in this case is written by reading off the top row, then the second row, then the last row from left to right.

Cipher Text: h o l e l w r d l o

To decrypt a given cipher text, you would need to reconstruct the list. First construct a 2D list with number of rows equal to the given key and number of columns equal to the length of the cipher text. Next, traverse the 2D list in the same diagonal manner as encoding and mark the cells in this 2D list that should contain a character. Then, traverse the list row by row and fill in the characters of your ciphertext. Lastly, read the matrix in the diagonal fashion to uncover your plain-text.

In the transposition cipher you are merely scrambling all the characters in the plain text. In your assignment keep all the characters of the plain text - lower case letters, upper case letters, digits, punctuation marks and spaces. Your cipher text will have all the characters (unchanged) from the plain text.

Vigenere Cipher: 

Substitution ciphers can be broken by frequency analysis. To make the cipher more secure you can use two or more letters to encrypt. The Vigenere cipher uses a pass phrase to encrypt and decrypt.

        a b c d e f g h i j k l m n o p q r s t u v w x y z

    a   a b c d e f g h i j k l m n o p q r s t u v w x y z
    b   b c d e f g h i j k l m n o p q r s t u v w x y z a 
    c   c d e f g h i j k l m n o p q r s t u v w x y z a b
    d   d e f g h i j k l m n o p q r s t u v w x y z a b c 
    e   e f g h i j k l m n o p q r s t u v w x y z a b c d 
    f   f g h i j k l m n o p q r s t u v w x y z a b c d e 
    g   g h i j k l m n o p q r s t u v w x y z a b c d e f 
    h   h i j k l m n o p q r s t u v w x y z a b c d e f g 
    i   i j k l m n o p q r s t u v w x y z a b c d e f g h 
    j   j k l m n o p q r s t u v w x y z a b c d e f g h i 
    k   k l m n o p q r s t u v w x y z a b c d e f g h i j 
    l   l m n o p q r s t u v w x y z a b c d e f g h i j k 
    m   m n o p q r s t u v w x y z a b c d e f g h i j k l 
    n   n o p q r s t u v w x y z a b c d e f g h i j k l m 
    o   o p q r s t u v w x y z a b c d e f g h i j k l m n 
    p   p q r s t u v w x y z a b c d e f g h i j k l m n o 
    q   q r s t u v w x y z a b c d e f g h i j k l m n o p 
    r   r s t u v w x y z a b c d e f g h i j k l m n o p q 
    s   s t u v w x y z a b c d e f g h i j k l m n o p q r  
    t   t u v w x y z a b c d e f g h i j k l m n o p q r s 
    u   u v w x y z a b c d e f g h i j k l m n o p q r s t 
    v   v w x y z a b c d e f g h i j k l m n o p q r s t u
    w   w x y z a b c d e f g h i j k l m n o p q r s t u v 
    x   x y z a b c d e f g h i j k l m n o p q r s t u v w 
    y   y z a b c d e f g h i j k l m n o p q r s t u v w x 
    z   z a b c d e f g h i j k l m n o p q r s t u v w x y 

Let us say we want to encrypt helloworld and we use as our pass phrase seal. Here is how we would lay the phrases out. The pass phrase is repeated over and over again in order with the text that needs to be encrypted. The letter from the pass phrase marks the row and the letter from the plain text marks the column.

       Pass Phrase: sealsealse
        Plain Text: helloworld
    Encrypted Text: zilwgaocdh

To decrypt, we would reverse the process. Use the same pass phrase seal repeatedly with the encrypted text. This time, the letter from the pass phrase marks the column. Within that column search for the encrypted letter. That row indicates the plain text.

       Pass Phrase: sealsealse
    Encrypted Text: zilwgaocdh
        Plain Text: helloworld

In your implementation of the Vigenere cipher you will not use the 2-D list. You must come up with a formula that will allow you to do the transformation. Also you must write a function to filter the input string. This function will first convert the string to lower case and then remove all characters that are not lower case letters.

Input: 

Your input will be from a file cipher.in. Do not hard code the name of the file in your program. You will read the file from stdin. Here is a typical input file:

helloworld
3
holelwrdlo
3
helloworld
seal
zilwgaocdh
seal

The first set of input will be to encode and decode using the rail fence cipher. The second set of input will be to encode and decode using the Vignere cipher. Here are the explanations of each line in the input file. Assume that there are no errors in the input file.

1. plain text to be encoded using rail fence cipher
2. key for the rail fence cipher
3. encoded text to be decoded using rail fence cipher
4. key for the rail fence cipher
5. plain text to be encoded using Vignere cipher
6. pass phrase (no spaces) for the Vignere cipher
7. encoded text to be decoded using Vignere cipher
8. pass phrase (no spaces) for the Vignere cipher

Output: 

Your TestCipher program will test the encoding and decoding methods of the two Cipher algorithms. Your output will look something like this:

Rail Fence Cipher

Plain Text: helloworld
Key: 3
Encoded Text: holelwrdlo

Encoded Text: holelwrdlo
Enter Key: 3
Decoded Text: helloworld

Vigenere Cipher

Plain Text: helloworld
Pass Phrase: seal
Encoded Text: zilwgaocdh

Encoded Text: zilwgaocdh
Pass Phrase: seal
Decoded Text: helloworld
