# Do not modify these lines
from pickle import APPEND
from turtle import update
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line


def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport = {
            'name': name,
            'date_of_birth': date_of_birth,
            'place_of_birth': place_of_birth,
            'height': height,
            'nationality': nationality,
        }
    return passport


def add_stamp(passport, country):
    if country != passport['nationality']:
        if 'stamps' in passport:
            if country not in passport['stamps']:
                passport['stamps'] += [country]
        else:
            passport['stamps'] = [country]
    return passport


def add_biometric_data(passport, name, value, date):
    if 'biometric' not in passport:
        x = {
            'biometric': {
                name: {
                    'value': value,
                    'date': date
                    }
                }
            }
        passport.update(x)
    else:
        passport['biometric'][name] = {
                'value': value,
                'date': date
                 }
    return passport
