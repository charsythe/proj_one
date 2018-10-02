class GameStats():
    """Track stats for game."""

    def __init__(self, ai_settings):
        """Init stats."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start in inactive state.
        self.game_active = False

        # High score should not be reset.
        self.high_score = 0

    def reset_stats(self):
        """Init stats that change during gameplay."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
