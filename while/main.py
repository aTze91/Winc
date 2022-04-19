from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

'''unique_koala_facts: takes an integer as an argument and returns that number of unique koala facts in a list. 
Note that there are only a limited number of unique facts in the dataset. For high arguments your function should try to return all unique facts in the dataset.
 No worries: the number of facts is small enough that this should be feasible. You can set an iteration limit of 1000.'''

def unique_koala_facts(n):
    d = 0
    koala_facts = []
    while n > 0 : 
          fact_x = random_koala_fact()
          if fact_x not in koala_facts : 
                  koala_facts += [fact_x]
                  n -= 1 
          d += 1
          if d == 1000: 
             break
    return koala_facts    
'''
num_joey_facts: young marsupials are called 'joeys'. How many unique facts mentioning this term are in our facts dataset? 
Count them by getting facts from random_koala_fact until you have seen some particular fact 10 times, then return how many unique joey facts you counted in the dataset.'''

def num_joey_facts():
    particular_fact = random_koala_fact()
    count = 0
    joey_facts = []
    while count < 10:
        fact_x = random_koala_fact()
        if fact_x == particular_fact:
           count += 1
        if 'joey' in fact_x and fact_x not in joey_facts:
            joey_facts += [fact_x]
    return len(joey_facts)

'''koala_weight: somewhere in the data is a fact about how heavy a koala is. This function should return that weight in kilogram (kg) as an integer.'''

def koala_weight():
    weight = 0
    while bool(weight) == False:
          koala_fact = random_koala_fact()
          if "kg" in koala_fact:
                     
                     print(koala_fact)
                     weight =int( koala_fact[koala_fact.find('Kg')-4:koala_fact.find('Kg')-2])
    return weight

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(random_koala_fact())
    print(unique_koala_facts(100))
    print (num_joey_facts())
    print(koala_weight())
   
