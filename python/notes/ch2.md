# Software Development, Data Types, and Expressions

## The Software Development Process
- Software Development - the discipline of systematically planning, coding, and testing a complex program
- Waterfall model - A series of steps in which a software system trickles down from analysis to design to implementation.
- Software development life cycle - The process of development, maintenance, and demise of software system. Phases include analysis, design, coding, testing/verification/ maintenance, and obsolescence.
- Incremental - The process of completing a rough draft of a step in a process before moving on to the next step
- Iterative - Circling back to an earlier stage in a process before moving forward.
- Prototype - A trimmed-down version of a class or software system that still functions and allows the programmer to study its essential features
- Pseudocode - A stylized half-English, half-code language written in English but suggesting program code.
- Logic error - A type of error that cannot be detected by the computer at compile time or run time, but usually shows up in the form of unexpected output
  - Design error - also a logic error
- Test suite - A set of test cases that exercise the capabilities of a software component

### Waterfall Model Phases:
  1. Customer request - Broad statement of a problem to be solved by a computer
  2. Analysis - The phase of the software life cycle in which the programmer describes what the program will do.
  3. Design - The phase of the software life cycle in which the programmer describes how the program will accomplish its task
  4. Implementation - The phase of the software life cycle in which the program is coded in a programming language
  5. Integration - The phase of the software development life cycle during which program components are brought together and tested
  6. Maintenance - The phase of the software life cycle in which errors are repaired and changes and improvements are made.

## Data Types
- Data type - A set of values and operations on those values.
- Literal - An element of a language that evaluates to itself, such as 34 or "hi there."
- Numeric data types - Data types that represent numbers

## String Literals
- Empty string - A string that contains no characters. e.g. ' ' and ""
  - Different from a string that contains a single blank space
- newline character = `\n`
- Escape sequence - A sequence of two characters in a string, the first of which is \. The sequence stands for another character, such as the tab or newline.
  - Examples:
    - `\b` - backspace
    - `\n` - Newline
    - `\t` - horizontal tab
    - `\\` - the \ character
    - `\'` - Single quotation mark
    - `\"` - Double quotation mark

## String Concatenation
- Concatenation operator + - Used to form a new string
  - e.g. "Hi " + "there, " "Ken!"
  - The * operator can also be used to repeat strings
    - e.g. " " * 10 + "Python" repeat " " 10 times

## Variables and the Assignment Statement
- Variable - a memory location, referenced by an identifier, whose value can be changed during execution of a program.
- Symbolic constants - Names that receive a value at program start up and whose value cannot be changed
- Assignment statement - A method of giving values to variables
- Defining or Initializing - Giving a variable a value for the first time
- Variable references - The process whereby the computer looks up and returns the values of variables
- Abstraction - Substituting a simple thing for a more complex one in a program
- Program comments - Text in a program that is not executed as code, but informs the reader about what the code does.
- Docstring - A sequence of characters enclosed in triple quotation marks ('''''') that Python uses to document program components such as modules, classes, methods, and functions
- End-of-line comments - Parts of a single line of text in a program that are not executed but serve as documentation for readers.
    - Begin with a # 

### Tips for documenting code:
- Begin a program with a statement of its purpose and other information that would help orient a programmer called on to modify the program at some future date
- Accompany a variable definition with a comment that explains the variable's purpose
- Precede major segments of code with brief comments that explain their purpose. The case study program presented earlier in this chapter does this.
- Include comments to explain the workings of complex or tricky sections of code.

## Numeric Data Types and Character Sets
- Character sets - Lists of characters available for data and program statements
- Integers - Positive or negative whole numbers, or the number 0. The magnitude of an integer is limited by a computer's memory.

## Floating Point Numbers
- Infinite precision - The characteristic of a real number that its fractional part can extend for an indefinite number of digits
- Floating-point - A data type that represents real numbers in a computer program
- Decimal notation - The use of the digits 0 through 9 to represent numbers in base 10
- Scientific notation - The representation of a floating point number that uses a decimal point and an exponent to express its value

## Character Sets
- The characters in a string each map to an integer value
- ASCII set - The American Standard Code for Information Interchange ordering for a character set
- Unicode set - A character set that uses 16 bits to represent over 65,000 possible characters. These include the ASCII character set as well as symbols and ideograms in many international languages.
- Python's ord and chr functions convert characters to their numeric ASCII codes and back again, respectively.

## Expressions
- Expressions - Descriptions of a computation that produces a value
- Arithmetic expression - A sequence of operands and operators that computes a value
- Precedence rules - Rules that govern the order in which operators are applied in expressions
- Semantics - The rules for interpreting the meaning of a program in a language
- Semantic error - A type of error that occurs when the computer cannot carry out the instruction specified
- Mixed-mode arithmetic - Expressions containing data of different types; the values of these expressions will be of either type, depending on the rules for evaluating them.
- Type conversion function - You must use when working with the input of numbers. A function with the same name as the data type to which it converts
  - e.g. int(3.77) = 3 or int("33") = 33
  - Since + does not work with a string and a number, you must convert the number to a string
- Strongly typed programming language - A language in which the types of operands are checked prior to applying an operator to them, and which disallows such applications, either at run time or at compile time, when operands are not of the appropriate type

### Arithmetic Operators:
* Negation  -
* Exponentiation **
* Multiplication *
* Division /
* Quotient //
* Remainder or modulus %
* Addition +
* Subtraction -

### Evaluation of arithmetic expressions in python:
- Exponentiation has the highest precedence and is evaluated first
- Unary negation is evaluated next, before multiplication, division, and Remainder
- Multiplication, both types of division, and remainder are evaluated before addition and Subtraction
- Addition and subtraction are evaluated before Assignment
- With two exceptions, operations of equal precedence are left associative, so they are evaluated from left to right. Exponentiation and assignment operations are right associative, so consecutive instances of these are evaluated from right to left
- You can use parentheses to change the order of evaluation

## Using Functions and Modules
- Modules - Independent program components that can contain variables, functions, and classes
- Function - A chunk of code that can be treated as a unit and called to perform a task
- Arguments - Specific data values to perform function's tasks
- Parameters - Names that appear in the header of function or method definition that are assigned the values of arguments when the method or function is called
- Returning a value - The process whereby a function or method makes the value that it computes available to its caller
- Optional arguments - Arguments to a function or method that may be omitted
- Required arguments - Arguments that must be supplied by the programmer when a function or method is called
- Default behavior - Behavior that is expected and provided under normal circumstances
- To use a module, write the name of a module as a qualifier followed by a dot and the name of the resource
  - e.g. math.pi math.sqrt(2)
- You can ask for help using as such: help(math.cos)
- To import all of a module's resources: from `<module>` import *
- Main module - The module where program codes begins to execute at program startup

## Program Format and Structure
- Order for programs:
 1. Start with introductory comment starting author's name, purpose of program, and other relevant into in the form of a doc string
 2. Then, include statements that do the following:
   - Import any modules needed by the program
   - initialize important variables, suitably commented
   - prompt the user for input data and save the input data in variables.
   - process the inputs to produce the results.
   - display the results
