from audioop import reverse
from pickle import TRUE
from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """
#shortest_names: takes a list of country names and returns a list of country names that have the shortest length. 
# If there is only one country with the shortest name the list will contain only that country name, otherwise multiple countries should be in the list. Use a for-loop and len!
def shortest_names(countries):
    countries.sort(key=len)
    shortests = []
    for x in countries:
        if len(x) == len(countries[0]) :
            shortests += [x]
    return shortests

#most_vowels: takes a list of country names and returns a list with the top three countries that have the most vowels in their name. 
# The country with the most vowels should be on position 0 in the list, the country with the second-most on position 1, and so on. 
# If there are multiple countries with the same number of vowels the order does not matter. To sidestep the y-issue: we count aeiou as vowels.

def most_vowels(countries):
    most_vowels_list = []
    def vowels_count(country_name):
        vowels = ['a','e','i','o','u']
        count = 0       
        for y in country_name.lower():
            if y in vowels:
                count += 1 
        return count
    countries.sort(key=vowels_count)
    
    for i in range(3):
        most_vowels_list += [countries[-i-1]]
        print(countries[-i-1])
    print(countries)
  
  
    return most_vowels_list 




#alphabet_set: takes a list of country names and returns a list of country names whose letters can be combined to form the complete alphabet. How short can you get your list to be?
#Letter case is not relevant, so 'a' is the same letter as 'A' with regards to the alphabet.
#Solutions with 14 or fewer countries are accepted as correct.
def alphabet_set(countries):
    alphabet_check = [ 'q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'] 
    alpha_names = []
    def letters_count(country_name):
         count = 0       
         for y in country_name.lower():
            if y in alphabet_check:
                count += 1 
         return count
    countries.sort(key=letters_count,reverse= True)
    for x in countries:
        for y in alphabet_check:
            if y in list(x): 
               alphabet_check.remove(y)
               if x not in alpha_names : 
                    alpha_names += [x]
    return alpha_names

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """
    
   # shortest_names(countries)
    #most_vowels(countries)
    print(alphabet_set(countries))
