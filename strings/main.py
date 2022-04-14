# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#part 1
player_0 ='Ruud Gullit'
player_1 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = player_0 +' '+ str(goal_0) + ', ' + player_1 +' '+ str(goal_1)
report = f'{player_0} scored in the {str(goal_0)}nd minute\n{player_1} scored in the {str(goal_1)}th minute'
print(scorers)
print(report)
#part 2
player = 'Wim Kieft'
first_name = player[player.find('Wim'):player.find('Kieft')-1]
last_name_len = len(player[player.find('Kieft'):])
name_short = f'{player[0]}. {player[-last_name_len:]}'
chant = f'{first_name}! ' * len(first_name[1:] ) + f'{first_name}!'
good_chant= chant[-0] != " "

