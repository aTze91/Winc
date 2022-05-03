# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line


class Player():

    def __init__(self, name, speed, endurance, accuracy):
        self.name = name
        if speed > 1:
            raise ValueError('speed must be a float between 0 and 1 (inclusive)')
        else:
            self.speed = speed
        if endurance > 1:
            raise ValueError('endurance must be a float between 0 and 1 (inclusive)')
        else:
            self.endurance = endurance
        if accuracy > 1:
            raise ValueError('accuracy must be a float between 0 and 1 (inclusive)')
        self.accuracy = accuracy

    def introduce(self):
        return f'Hello everyone, my name is {self.name}.'

    def strength(self):
        if self.speed >= self.endurance and self.speed >= self.accuracy:
            higher = ('speed', self.speed)
        if self.endurance > self.speed and self.endurance >= self.accuracy:
            higher = ('endurance', self.endurance)
        if self.accuracy > self.speed and self.accuracy > self.endurance:
            higher = ('accuracy', self.accuracy)
        return higher

    pass


class Commentator():
    def __init__(self, name):
        self.name = name

    def sum_player(self, player):
        try:
            return player.speed + player.endurance + player.accuracy
        except TypeError:
            print('I need a class Player')

    def compare_players(self, player_1, player_2, attribute):

        if getattr(player_1, attribute) > getattr(player_2, attribute):
            return player_1.name
        if getattr(player_1, attribute) < getattr(player_2, attribute):
            return player_2.name
        if getattr(player_1, attribute) == getattr(player_2, attribute):
            if player_1.strength()[1] > player_2.strength()[1]:
                return player_1.name
            if player_1.strength()[1] < player_2.strength()[1]:
                return player_2.name
            if player_1.strength()[1] == player_2.strength()[1]:
                return 'These two players might as well be twins!'

    pass
