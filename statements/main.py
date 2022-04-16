__winc_id__ = "7599944cfbd94b47beffdbab7a208931"
__human_name__ = "statements"
'''Below we have three statements, each consisting of a number of expressions. Each statement begins with a variable name followed by an assignment operator (=). The rest of each statement consists of an expression that should evaluate to True, but none of them do. Some might not even run at all.

Your task is to fix these bugs in our code by changing only the use of parentheses (( )) to change the order in which the expressions are evaluated. For example:

# Example 1
# Statement with bug
should_be_true = 1 + 1 * 2 == 4

# Fixed statement
should_be_true = (1 + 1) * 2 == 4

# Example 2
# Statement with bug
should_be_true = True and (True or False) and False

# Fixed line
should_be_true = (True and True) or (False and False)

# There may be more than one correct solution
should_be_true = True and True or False and False
Here are the three statements you should fix. When you start the exercise with Wincpy you will find this code snippet in main.py as well.

one = 5 % 2 + 3 == 0
two = ('Piano'[0:0] == '' + 'Guitar')[0:0]
three = 2 ** 3 + 3 - 2 * 11 == 42'''


one = 5 % (2 + 3) == 0
two = ("Piano"[0:0] == "" + "Guitar"[0:0])
three = 2 ** (3 + 3) - 2 * 11 == 42

print(one, two, three)
