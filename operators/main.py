# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line


#The language spoken the most in Switzerland is the same as in Spain.
switzerland_most_spoken_language = 'German'
spain_most_spoken_language = 'Castilian Spanish'
print(switzerland_most_spoken_language == spain_most_spoken_language)

#The most prevalent religion in Switzerland is the same as in Spain.
switzerland_prevalent_religion = 'Roman Catholic'
spain_prevalent_religion = 'Roman Catholic'
print(switzerland_prevalent_religion == spain_prevalent_religion)

#The name length of Spain's capital does not equal that of Switzerland.
switzerland_capital_name = 'Bern'
spain_capital_name = 'Madrid'
print(len(switzerland_capital_name) != len(spain_capital_name))

#Switzerland's GDP is greater than Spain's GDP.
switzerland_GPD = 731502000000
spain_GPD = 1393351000000
print(switzerland_GPD > spain_GPD)

#The population growth is less than 1% in Switzerland and Spain.
switzerland_pop_growth_rate = 0.65
spain_pop_growth_rate = 0.13
print(switzerland_pop_growth_rate < 1 and spain_pop_growth_rate < 1)

#At least one of the two countries has a population count of over 10 million.
switzerland_pop_count = 8508698
spain_pop_count = 47163418
print(switzerland_pop_count > 10000000 or spain_pop_count > 10000000)

#Exactly one of the two countries has a population count of over 10 million.
print(switzerland_pop_count > 10000000 and spain_pop_count <= 10000000  or switzerland_pop_count <= 10000000 and spain_pop_count > 10000000)

'''if switzerland_pop_count > 10000000 and spain_pop_count > 10000000 print (False)
if switzerland_pop_count < 10000000 and spain_pop_count < 10000000 print(False)
if switzerland_pop_count > 10000000 or spain_pop_count > 10000000 print(True)'''

