class GameStats():
    """Track stats for game."""

    def __init__(self, ai_settings):
        """Init stats."""
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """Init stats that change during gameplay."""
        self.ships_left = self.ai_settings.ship_limit
