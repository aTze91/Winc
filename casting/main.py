# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
# Part 1

# Create a variable leek_price with an integer value of 2.
leek_price = 2
# Cast this into a string and use the +-operator to print a string like this one, only with the correct price in it:
# 'Leek is 50 euro per kilo.'
print(f'Leek is {str(leek_price)} euro per kilo.')


# Part 2
# We got an order for four leeks! Store the string 'leek 4' in a variable.
order = 'leek 4'
# Use find and slicing to extract the number from this string.
# Cast it into an integer.
# Use this and leek_price to compute the sum total and store it in sum_total. Print out the value for this variable.
sum_total = int(order[order.find('4'):]) * leek_price
print(sum_total)


# Part 3
# Broccoli costs 2.34 euros per kg. We got an order: 'broccoli 1.6'.
# Create one variable for the broccoli price and one for the order.
order = 'broccoli 1.6'
broccoli_price = 2.34
# Compute the total price for this order.
sum_total = round(float(order[order.find('1.6'):]) * broccoli_price, 2)

# Use the +-operator to assemble and print a string that looks like the following:
print(order[order.find('1.6'):] + 'kg broccoli costs ' + str(sum_total) + "e")
# '1.6kg broccoli costs 500.34e'
