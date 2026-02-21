## 4.1 Accessing Characters and Substrings in Strings
- Substrings: Strings that represent a segment of another string

### The Structure of Strings  
- Data structure: A compound unit consisting of several data values.
- String: A sequence of zero or more characters
- Immutable data structure: A data structure in which one cannot insert, remove, or revise the values contained therein

### The Subscript Operator  
- Subscript operator: The symbols [], which enclose an integer or range of integers, that allow a program to access a character or a substring at a given position a range of positions in a string.
  - e.g. `<a string> [<an integer expression>]`
- Index: The relative position of a component of a linear data structure of collection

### Slicing for Substrings  
- Extension: The characters following the period in a filename, indicating the type of file.
- Slicing: An operation that returns a subsection of a linear collection, for example, a sublist or a substring
  - e.g. name = "myfile.txt" `name[0:1]` returns 'm' or `name[-3:]` returns 'txt' or 
  - When two integer positions are included in the slice, the range of characters in the substring extends from the first position up to but not including the second position.
  - When the integer is omitted on either side of the colon, all of the characters extending to the end or beginning are included in the substring

### Testing for a Substring with `in` Operator    
- The left operand of in is a target substring, and the right operand in the string to be searched. Returns True if the target string is somewhere in the search string or False otherwise.

Example:
```python
# Traverses list of filenames and prints just filenames that have a .txt extension
fileList = ["myfile.txt", "myprogram.exe", "yourfile.txt"]
for fileName in fileList:
  if ".txt" in fileName: 
    print(fileName)
```

## 4.2 Data Encryption
- Sniffing software: Programs that allow the user to spy on data transmissions over a network
- Data encryption: The process of transforming data so that others cannot use it
  - e.g. Examples include FTPS, HTTPS, which are secure versions of FTP and HTTP, respectively
- Cipher text: The output of an encryption process
- Decrypts: Translates encrypted data to a form that can be used
- Plaintext: The source text or input for an encryption process
- Keys: Items that are associated with a value and which are used to locate that value in a dictionary
  - Allows two parties to encrypt and decrypt messages
- Caesar cipher: An encryption method that replaces characters with other characters a given distance away in the character set.
- Recall `ord` function returns ordinal position of a character value in ASCII sequence, whereas `chr` is the inverse function
- Block cipher - An encryption method that replaces characters with other characters located in a two-dimensional grid of characters
- Invertible matrix - A data structure used in block cipher. Determines the values of the encrypted characters and provides the key.

## 4.3 Strings and Number Systems  
- Decimal number system
- Binary number system
- octal (base 8)
- Hexadecimal (Base 16): Uses the digits 0 through 9 and A through F

### The Position System for Representing Numbers  
- Positional notation: The type of representation used in based number systems, in which the position of each digit denotes a power in the system's base.
- Positional value: The value resulting from multiplying the digit at a given position by the number's base raised to the power specific by that position $base^{position}$.

### Converting Binary to Decimal  
- Bit string: A string containing the binary digits 0 and 1.
- Multiply the value of each bit (0 or 1) by its positional value and add the results

### Converting Decimal to Binary  
- One algorithm uses division and subtraction. This algorithm repeatedly divides the decimal number by 2. After each division, the remainder is placed at the beginning of a string of bits. The quotient becomes the next dividend in the process. The string of bits is initially empty, and the process continuous while the decimal number is greater than 0

### Conversion Shortcuts  
- One shortcut is to learn to count through the numbers corresponding to the decimal values 0 through 8.
- Numbers that contain exact powers of 2 contain a 1 followed by a number of zeros that equal the exponent used to computer that power of 2.
- Decimal numbers that are one less than the exact power of 2 contain all 1s. Thus, a quick way to compute the decimal value of the $11111_2 \text{ is } 2^5-1, \text{ or } 31_{10}$

### Octal and Hexadecimal Numbers  
- The main benefit of the octal system is the ease of converting octal numbers to and from binary
- To convert from octal to binary, you start by assuming that each digit in the octal number represents three digits in the corresponding binary number. Then start with the leftmost octal digit and write down the corresponding binary digits, padding these to the left with 0s to the count of 3, if necessary. Proceed until you have converted all of the octal digits.
- To convert binary to octal, begin at the right and factor the bits into groups of three bits each. Then convert each group of three bits to the octal digit they represent.
- To convert hexadecimal to binary, realize that each digit in the hexadecimal number is equivalent to four digits in the binary number. Thus, to convert from hexadecimal to binary, replace each hexadecimal digit with the corresponding 4-bit binary number.
- To convert from binary to hexadecimal, factor the bits into groups of four and look up the corresponding hex digits. 

## 4.4 String Methods  
- Methods: Chunks of code that can be treated as a unit and invoked by name. A method is called with an object or class.
  - Behaves like a function but has slightly different syntax.
  - The split method obtains a list of the words contained in an input string.
- Object: A data value that has an internal state and a set of operations for manipulating that state

The syntax of a method call:
  - `<an object>.<method name>(<argument-1>,..., <argument-n>)`
- In Python, all data values are objects, and every data type includes a set of methods to use with objects of that type    

## 4.5 Text Files  
- Text file: A file that contains characters and is readable and writable by text editors.
- The main advantages of taking input data from a file are the following:
  - The data set can be much larger
  - The data can be input much more quickly and with less chance of error
  - The data can be used repeatedly with the same program or with different programs

### Writing Text to a File
- Mode string: A string argument to the open function, such as 'r' or 'w', that indicates whether the file is being opened for input or output
  - e.g. `f=open("myfile.txt", 'w')`
  - r for input files, w for output files
- When all of the outputs are finished, the file should be closed using the close method as such `f.close()`
- Failure to close an output file can result in data being lost
- Buffer: the area of computer memory used to transmit data to and from external storage

### Writing Numbers to a File  
- Any other data type must first be converted to a string to be able to be used with the write method

### Reading Text from a File  
- Code to open "myfile.txt" for input: `f=open("myfile.txt", 'r')`
- The method `read` inputs the entire contents of the file as a single string. If the file contains multiple lines of text, the newline characters will be embedded in this string.
  - e.g `text = f.read()`
- To repeat an input, the file must be reopened in order to reuse it for another input process.    
- `readline` method consumes a line of input and returns this string, including the newline

Example:
```python
f = open("myfile.txt", 'r')
while True:
  line = f.readline()
  if line == "":
    break
  print(line)
  # the output is:
  # First line.
  #
  # Second line.
```

### Reading Numbers from a File
- All file input operations return data to the program as strings. If these strings represent other types of data, such as integers or floating-point numbers, the programmer must convert them to the appropriate type.
  - Can be done using int and float
- During input, integers separated by a newline can be read with a simple for loop.
- To convert each line the `strip` method can be used to remove the newline and then running the `int` function to obtain the integer value.
Example:
```python
f = open("integers.txt")
theSum=0
for line in f:
  line=line.strip()
  number=int(line)
  theSum+=number
print ("The sum is", theSum)
```

- Obtaining numbers separated by spaces from a text files is a bit trickier
Example:
```python
f = open("integers.txt", 'r')
theSum=0
for line in f:
  wordlist = line.split()
  #the split method strips the line of the newline
  for word in wordlist:
    number=int(word)
    theSum+=number
print("The sum is", theSum) 
```

### Accessing and Manipulating Files and Directories on Disk
- Root directory: The directory at the top or beginning of a file system
- Current working directory: The directory to which a running program is attached, in which a file can be accessed directly by its name
- Pathname: A chain of directory names that allows the computer to access a file on a file system
- Absolute pathname: A pathname that begins with the file system's root directory
- Relative pathname: A pathname that begins just above or below the current working directory
- When designing Python programs that interact with files, it's a good idea to include error recovery.
  - Before opening a file for input, check to see if a file with the given pathname exists on the disk
- Bottom-up testing: The process of testing more basic program components before one tests the components that depend on them
- Driver: A method used to test other methods
