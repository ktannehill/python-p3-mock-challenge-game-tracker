class Game:
    all = []

    def __init__(self, title):
        self.title = title
        type(self).all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str):
            raise TypeError("Title must be a string")
        elif not len(new_title):
            raise ValueError("Title must contain characters")
        elif hasattr(self, "title"):
            raise AttributeError("Already set title")
        else:
            self._title = new_title

    def results(self):
        return [result for result in Result.all if result.game is self]

    def players(self):
        return list({result.player for result in self.results()})

    def average_score(self, player):
        player_scores = [result.score for result in Result.all if result.player is player and result.game is self]
        if len(player_scores):
            return sum(player_scores) / len(player_scores)
        else:
            return 0
class Player:
    all = []

    def __init__(self, username):
        self.username = username
        type(self).all.append(self)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if not isinstance(new_username, str):
            raise TypeError("Username must be a string")
        elif not 1 < len(new_username) < 17:
            raise ValueError("Username must be between 2-16 characters")
        else:
            self._username = new_username

    def results(self):
        return [result for result in Result.all if result.player is self]

    def games_played(self):
        return list({result.game for result in self.results()})

    def played_game(self, game):
        for result in Result.all:
            if result.game == game:
                if result.player is self:
                    return True
        return False

    def num_times_played(self, game):
        game_counter = 0
        for result in Result.all:
            if result.game == game:
                if result.player is self:
                    game_counter +=1
        return game_counter
    
    @classmethod
    def highest_scored(cls, game):
        # receives game object
        # returns player with higest avg score
        # set winner, avg score, and highest avg
        # collect all games for that game
        # iterate through all players
        # iterate through games
        # check if player played game
        # average scores
        # reset highest score
        winner = None
        temp_avg = 0
        highest_avg = 0
        games = [result for result in Result.all if result.game is game]
        for player in cls.all:
            scores = [game.score for game in games if game.player is player]
            if len(scores):
                temp_avg = sum(scores) / len(scores)
            if temp_avg > highest_avg:
                highest_avg = temp_avg
                winner = player
            temp_avg = 0
        return winner

class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        type(self).all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, new_score):
        if not isinstance(new_score, int):
            raise TypeError("Score must be an integer")
        elif not 1 <= new_score <= 5000:
            raise ValueError("Score must be between 1-5000")
        elif hasattr(self, "score"):
            raise AttributeError("Already set score")
        else:
            self._score = new_score

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, new_player):
        if not isinstance(new_player, Player):
            raise TypeError("Player must be of class Player")
        else:
            self._player = new_player

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, new_game):
        if not isinstance(new_game, Game):
            raise TypeError("Game must be of class Game")
        else:
            self._game = new_game