# Do not modify these lines
__winc_id__ = '63ce21059cf34d3d8ffef497ede7e317'
__human_name__ = 'comments'

# Add your code after this line
"""We are going to calculate how much will cost the dinner,
yes us you see it will be a vegan dinner  """

# setting the price of each product
broccoli = 2
potato = 3
brussel_sprout = 7
leek = 2

sum_one_each = broccoli + potato + brussel_sprout + leek
avg_price = sum_one_each / 4  # calulating the average price
# setting how many pieces of each product we will buy
num_potatoes = 7
num_broccolis = 5
num_brussel_sprouts = 10
num_leeks = 2

sum_total = broccoli * num_broccolis + potato * num_potatoes + brussel_sprout * num_brussel_sprouts + leek * num_leeks
discount_percentage = 30
discounted_sum_total = sum_total - sum_total / 100 * discount_percentage  # calculating the total cost with a 30% discount

print(discounted_sum_total)
""" is been a nice dinner afterall,
    I like broccoli """
