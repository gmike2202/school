<!--toc:start-->
- [3.1 Definite Iteration: The for Loop](#31-definite-iteration-the-for-loop)
  - [Executing a statement a given number of times](#executing-a-statement-a-given-number-of-times)
  - [Count-Controlled Loops](#count-controlled-loops)
  - [Augmented Assignment](#augmented-assignment)
  - [Loop Errors: Off-by-One Error](#loop-errors-off-by-one-error)
  - [Traversing the Contents of a Data Sequence](#traversing-the-contents-of-a-data-sequence)
  - [Specifying the Steps in the Range](#specifying-the-steps-in-the-range)
  - [Loops that Count Down](#loops-that-count-down)
- [3.2 Formatting Text for Output](#32-formatting-text-for-output)
- [3.3 Selection: if and if-else Statements](#33-selection-if-and-if-else-statements)
  - [The Boolean Type, Comparisons, and Boolean Expressions](#the-boolean-type-comparisons-and-boolean-expressions)
  - [if-else Statements](#if-else-statements)
  - [One-Way Selection Statements](#one-way-selection-statements)
  - [Multiway if statements](#multiway-if-statements)
  - [Logical Operators and Compound Boolean Expressions](#logical-operators-and-compound-boolean-expressions)
  - [Short-Circuit Evaluation](#short-circuit-evaluation)
  - [Testing Selection Statements](#testing-selection-statements)
- [3.4 Conditional iteration: The `while` Loop](#34-conditional-iteration-the-while-loop)
  - [The Structure and Behavior of a `while` Loop](#the-structure-and-behavior-of-a-while-loop)
  - [Count Control with a `while` Loop](#count-control-with-a-while-loop)
  - [The `while True` Loop and the `break` Statement](#the-while-true-loop-and-the-break-statement)
  - [Random Numbers](#random-numbers)
  - [Loop Logic, Errors, and Testing](#loop-logic-errors-and-testing)
    - [Fail-Safe Programming](#fail-safe-programming)
<!--toc:end-->

## 3.1 Definite Iteration: The for Loop
- Loops: Statements that repeatedly execute a set of statements
- Pass: The execution of a set of statements with a loop
- Iteration: Statements that repeatedly execute a set of statements
- Definite iteration: The process of repeating a given action a preset number of times
- Indefinite iteration: The process of repeating a given action until la condition stops the repetition
- For loop: A structured loop consisting of an initializer expression, a termination expressions, an update expression, and a statement.
- Loop header: Information at the beginning of a loop that includes the conditions for continuing the iteration process
- Loop body: The action(s) performed on each iteration through a loop

### Executing a statement a given number of times
Template for for loop:
```Python
for <variable> in range(<an integer expressions>):
  <statement-1>
  .
  .
  <statement-n>
```

### Count-Controlled Loops
- When Python executes the type of for loop above, it counts from 0 to the value of the header's integer expression minus 1.
  - e.g. `for count in range(4)` goes `0 1 2 3`
- Count-controlled loops: Loops that stop when a counter variable reaches a specific limit
- Supplying two numbers to range makes it count from the first number to the second number - 1
- Alternate version of for loop:
  - `for <variable> in range (<lower bound>, upper bound + 1>): <loop body>`
- Summation: The accumulation of the sum of a sequence of numbers.

### Augmented Assignment
- Augmented assignment operations: Assignment operations that perform a designated operation, such as addition, before storing the result in a variable
  - format: `<variable> = <variable> <operator> <expression>`
  - e.g. a +=3 means a = a + 3

### Loop Errors: Off-by-One Error    
- Off-by-One error: usually seen with loops, this error shows up as a result that is one less or one greater than the expected value

### Traversing the Contents of a Data Sequence  
- List - a collection of data values that are ordered by position
- The values contained in any sequence can be visited by running a for loop as follows:
```Python
for <variable> in <sequence>:
  <do something with variable>
```
 On each pass the variable is bound to or assigned the next value in the sequence, starting with the first one and ending with the last one. 

### Specifying the Steps in the Range
- Step value: The amount by which a counter is incremented or decremented in a count-controlled loop
- You can add this step value to the range function as the third element
  - e.g. `range(1, 6, 3)` returns [1, 4]

### Loops that Count Down 
- `for count in range (10, 0, -1)` does exactly what you think

## 3.2 Formatting Text for Output 
- Tabular format: The presentation of output in columns of data that are either left-aligned or right-aligned
- Field width: The number of columns used for the output of text, such as the data characters and additional spaces
- To right-justify:
  - "%6s" % "four"
- To left-justify:
  - "%-6s" % "four"
- Template:
  - `<format string> % <datum>`
- Format string: A special syntax within a string that allows the programmer to specify the number of columns within which data are placed in a string.
- Format operator %: The operator %, when used with a format string and a set of one or more data values, return a string with the given format
- To format integers, use d instead of s
- Second form of this operation:
  - `<format string> % (<datum-1>,...,<datum-n>`
- Example formatting:
```Python
for exponent in range(7, 11):
  print("%-3d%12d" % (exponent, 10 ** exponent))
```
The above will left justify the first argument and right justify the second, by their respective number of field widths
- The format information for a data value of type float has the form:
  `%<field width>.<precision>f`
- example:
  - `"%6.3f" % 3.14` returns ` 3.140` with the additional field width to the left

## 3.3 Selection: if and if-else Statements   
- Condition: A Boolean expression used to control the flow of a computation
- Selection statements: Control statements that select some particular logical path based on the value of an expression. Also referred to as conditional statements

### The Boolean Type, Comparisons, and Boolean Expressions  
- Boolean data type: A data type whose values are True and False
- Simple boolean Expressions: The values True or False, the call of a function that returns True or False, or a comparison of two values.

### if-else Statements
- If-else statement: A selection statement that allows a program to perform alternative actions based on a condition. Also called a two-way selection statement

Python syntax for if-else statement:
```Python
if <condition>:
  <sequence of statements-1> 
else:
  <sequence of statements-2> 
```

### One-Way Selection Statements 
- If statement: A type of control statement that prevents a program from performing an action if the condition is false. Also called a one-way selection statement

Syntax:
```Python
if <condition>
  <sequence of statements>
```

### Multiway if statements
- Multiway selection statement: A type of control statement that includes two or more conditions and possible courses of action.

Syntax:
```Python
if <condition-1>:
  <sequence of statements-1>
elif <condition-n>:
  <sequence of statements-n>
else:
  <default sequence of statements>
```
### Logical Operators and Compound Boolean Expressions
- Logical Operator: Any of the logical connective operators `and, or, or not`.
- Compound Boolean Expression: Refers to the complete expression when logical connectives and negation are used to generate boolean values.
- Logical negation: The use of the logical operator `not` with a boolean expression, returning `True` if the expression is false, and `False` if the expression is true.
- Truth table: A means of listing all of the possible values of a Boolean expression.

Operator Precedence:
  - Exponentiation **
  - Arithmetic negation -
  - Multiplication, division, remainder *, /, %
  - Addition, subtraction +, -
  - Comparison ==, !=, <, >, <=, >=
  - Logical negation not
  - Logical conjunction and
  - Logical disjunction or
  - Assignment = 

### Short-Circuit Evaluation
- Short-Circuit Evaluation: The process by which a compound Boolean expression halts evaluation and returns the value of the first subexpression that evaluates to true, in the case of `or`, or false, in the case of `and`

### Testing Selection Statements
- Take extra care when testing programs with selection statements
- Firstly, make sure that all possible branches or alternatives in a selection statement are exercised.
- Examine all conditions. 
- Finally, test conditions that contain compound Boolean expressions using data that produce all of the possible combinations of values of the operands.

## 3.4 Conditional iteration: The `while` Loop
- Sentinel: A special value that indicates the end of a set of data or of a process
- Conditional iteration: A type of loop that continuous as long as a condition is true.

### The Structure and Behavior of a `while` Loop
- Continuation condition: A boolean expression that is checked to determine whether or not to continue iterating within a loop. If this expression is true, iteration continues. 
- `while` loop: A pretest loop that examines a Boolean expression before causing a statement to be executed

Syntax:
```Python 
while <condition>:
  <sequence of statements>
```
- Infinite loop: A loop in which the controlling condition is not changed in such a manner to allow the loop to terminate
- Loop control variable: A variable that is checked within the continuation condition of a loop
- Entry-control loop: A type of loop whose continuation condition is tested at the beginning of the loop. Alternate name to while loop

### Count Control with a `while` Loop
- While you can use a while loop for a count controlled loop, it can possibly bring unneeded complexity. It is up to you to decide whether your solution is easier to understand or if there's a better alternative

### The `while True` Loop and the `break` Statement  
- `break` statement: A control statement that exits a loop
- Termination condition: A Boolean expression that is checked to determine whether or not to stop iterating within a loop. If this expression is true, iteration stops.

Example:
```Python
theSum = 0.0
while True:
  data = input("Enter a number or just enter to quit: ")
  if data =="":
    break
  number = float(data)
  theSum += number
print("The sum is", theSum)
```

### Random Numbers
- Random numbers: Numbers chosen from a given sequence to simulate randomness in a computer application

Example:
```Python
import random
for roll in range(10):
  print(random.randint(1,6), end =" ")
```
The above program prints numbers from 1 to 6 10 times

### Loop Logic, Errors, and Testing
- Condition-controlled loop: A type of loop whose continuation depends on the value of a Boolean expression.
- Errors to rule out during testing the `while` loop include an incorrectly initialized loop control variable, failure to update this variable correctly within the loop, and failure to test the variable correctly in the continuation condition.

#### Fail-Safe Programming  
Categories of program errors:
  1. Syntax errors: Occur when an item of program code is not grammatically well-formed.
  2. Semantic errors: Occur when an item of program code is well-formed but the computer cannot carry out the specific operation.
  3. Logic errors: Occur when a program runs to a normal termination (no syntax or semantic errors) but does not produce the expected outputs.

- Correct: A program that produces the expected outputs for all legitimate inputs.  
- Robust: A program that avoids, traps, and recovers from illegitimate inputs or exceptional conditions in its environment.
- Fail-Safe Programming: The discipline of creating programs that avoid, trap, and recover from illegitimate inputs or exceptional conditions in their environments.


