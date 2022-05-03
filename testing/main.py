
def get_none():
    return None


def flatten_dict(my_dict):
    my_list = []
    for x in my_dict:
        my_list += [my_dict.get(x)]
    return my_list


def super_flatten_dict(my_dict):
    my_list = []
    for x in my_dict:
        if type(my_dict[x]) is dict:
            my_list += flatten_dict(my_dict[x])
        else:
            my_list += [my_dict.get(x)]
    return my_list


my_dict = {
    'a': {
        'inner_a': 42,
        'inner_b': 350},
    'b': 3.14
    }


print(super_flatten_dict(my_dict))
