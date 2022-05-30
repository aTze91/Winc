from main import Specialist, Homeowner
franco = Specialist('franco', {'cuoco': 8, 'barman': 3})
gianni = Specialist('gianni', {'cuoco': 4, 'pittore': 7})
alessia = Specialist('alessia', {'cuoco': 2, 'barman': 10})
specialists = [franco, gianni, alessia]
carla = Homeowner('carla', 'kempenlaan', ['cuoco', 'barman', 'pittore'])
assert carla.contracts(specialists) == {'cuoco': "franco", 'barman': 'alessia', 'pittore': 'gianni'}

print(carla.contracts(specialists))
print(carla.__dict__['name'])
