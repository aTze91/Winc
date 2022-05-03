from main import get_none, flatten_dict, super_flatten_dict


def test_get_none():
    assert get_none() is None
    return None


def test_flatten_dict():
    # assert flatten_dict.my_dict is dict
    assert flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14}) == [{'inner_a': 42, 'inner_b': 350}, 3.14]
    return None


def test_super_flatten_dict():
    # assert flatten_dict.my_dict is dict
    assert super_flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14}) == [42, 350, 3.14]
    return None
