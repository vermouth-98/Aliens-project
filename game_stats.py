from save_file import read_file
class GameStats():
    #Track statistics for alien invastion . 

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.get_high_core()
    def get_high_core(self):
        self.high_score = read_file(self.ai_settings)

    def reset_stats(self):
        ''' initialize statistic that can change during the game '''
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
    