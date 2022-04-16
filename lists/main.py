# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
'''Composer John Williams has written a great many pieces for a lot of different films. He's written so many, 
in fact, that he has asked you to write a number of functions to help him keep it all organized.'''

#Write a function alphabetical_order that takes one argument: a list of strings that represent film names. 
#It returns a list of the same films in alphabetical order. We have not discussed sorting lists yet, 
#so you should probably search the web to see if there's a good approach out there. Your solution should not be longer than a few lines.

def alphabetical_order(film_names):
    film_names_sorted = sorted(film_names)
    return film_names_sorted

#Write a function won_golden_globe that takes a film name and returns True or False based on whether or not this movie won a Golden Globe.
#This page will come in handy: Wikipedia -- List of awards and nominations received by John Williams
#A nomination is not a win.
#You are not allowed to do string-to-string comparisons in this function, so no string_a == string_b!
#John is not very tidy with his archive, so the captitalization of the names might not be correct. Look into using the lower-function on the given film string.

def won_golden_globe(film_name):
    won_golden_globes = ['jaws','star wars: episode iv – a new hope','e.t. the extra-terrestrial','memoirs of a geisha']
    if film_name.lower() in won_golden_globes: return True
    return False

#John's son Joseph accidentally mixed in some of his own work as lead singer for Toto with a list of his dad's compositions. 
# Write a function remove_toto_albums that takes a list of strings, removes Joseph's Toto albums from it and returns the tidy list.
#Use this information: Wikipedia -- Joseph Williams (musician)
#It is not certain that all of Joseph's Toto albums are in the list received by remove_toto_albums, but they might! Don't let your script run into any errors.
#Joseph did not inherit his dad's sloppiness with capitalization, so his Toto albums would be listed correctly.
#Search the web on how to remove an item from a list by value.

def remove_toto_albums(albums):
    toto_albums = ['Fahrenheit','The Seventh One','Toto XX(lead vocals on "Last Night" and “In A Word”)','Falling in Between(co-lead vocals on "Bottom Of Your Soul")','Toto XIV','Old Is New']
    tidy_list = albums + toto_albums
    tidy_list = albums.remove(toto_albums)
    return tidy_list