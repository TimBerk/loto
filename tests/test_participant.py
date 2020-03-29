import pytest
from core.game import Participant
from tests.const import CART_NUMBERS, NUMBER_ON_CART


@pytest.fixture
def pc_participant():
    local_participant = Participant(0, 2, None)
    local_participant.cart.number_on_cart = NUMBER_ON_CART.copy()
    local_participant.cart.cart_numbers = CART_NUMBERS
    return local_participant


class TestParticipants:

    def test_player_lose(self):
        local_participant = Participant(0, 1, None)
        local_participant.lose_game()
        assert local_participant.can_play is False

    def test_act_computer(self, pc_participant):
        pc_participant.act_computer(73)
        count_numbers = len(pc_participant.cart.number_on_cart)
        assert count_numbers == (len(NUMBER_ON_CART) - 1)

    def test_act_computer_not_exist_number(self, pc_participant):
        pc_participant.act_computer(5)
        count_numbers = len(pc_participant.cart.number_on_cart)
        assert count_numbers == len(NUMBER_ON_CART)
