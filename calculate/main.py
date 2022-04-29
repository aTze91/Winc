# Do not modify these lines
__winc_id__ = '499e67d5cb54448e93cee7465be2c866'
__human_name__ = 'calculate'

# Add your code after this line
broccoli = 2
potato = 3
brussel_sprout = 7
leek = 2
sum_one_each = broccoli + potato + brussel_sprout+leek
avg_price = sum_one_each / 4
num_potatoes = 7
num_broccolis = 5
num_brussel_sprouts = 10
num_leeks = 2
sum_total = broccoli*num_broccolis + potato*num_potatoes + brussel_sprout*num_brussel_sprouts + leek*num_leeks
discount_percentage = 30
discounted_sum_total = sum_total - sum_total/100*discount_percentage

print(discounted_sum_total)
