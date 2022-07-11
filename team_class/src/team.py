class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
    def add_player(self, new_player):
        self.players.append(new_player)
    
    def has_player(self, has_player):
        if has_player in self.players:
            return True
        else:
            return False


    points = 0

    def play_game(self, play_game):
        if play_game == True:
            self.points += 3
        else: 
            self.points == 0
        return
    
           
    
    # def play_game(self, play_game):
    #     if play_game == False:
    #         self.points -= 3
    #         return