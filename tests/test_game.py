from core.game import Game


class TestGame:

    def test_create_players(self):
        local_types = [1, 2, 1]
        game = Game(local_types)
        game.preparation_game()
        assert len(local_types) == len(game.participants)

    def test_stop_game_with_alone_player(self):
        local_types = [1]
        game = Game(local_types)
        game.run()
        assert game.status is False

    def test_get_kegs(self):
        local_types = [1]
        game = Game(local_types)
        game.used_numbers = [1, 2, 56, 78, 65, 56, 12, 22, 56]
        assert game.get_keg() not in game.used_numbers

    def test_get_kegs_in_range(self):
        local_types = [1]
        game = Game(local_types)
        game.used_numbers = list(range(1, 90))
        game.get_keg()
        assert game.current_keg == 90
