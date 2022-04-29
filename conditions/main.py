# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line


def farm_action(weather, day_time, cow_milking_status, cows_location, season, slurry_tank, grass_status):

    if cows_location == 'pasture' and day_time == 'night' or cows_location == 'pasture' and weather == 'rainy':
        return 'take cows to cowshed'
    elif cow_milking_status is True:
        if cows_location == 'cowshed':
            return 'milk cows'
        else:
            return 'take cows to cowshed\nmilk cows\ntake cows back to pasture'
    elif slurry_tank is True and weather != 'sunny' and weather != 'windy':
        if cows_location == 'cowshed':
            return 'fertilize pasture'
        else:
            return 'take cows to cowshed\nfertilize pasture\ntake cows back to pasture'
    elif grass_status is True and season == 'spring' and weather == 'sunny':
        if cows_location == 'cowshed':
            return 'mow grass'
        else:
            return 'take cows to cowshed\nmow grass\ntake cows back to pasture'
    return 'wait'
