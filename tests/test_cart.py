import pytest
from core.cart import Cart
from tests.const import CART_NUMBERS, NUMBER_ON_CART


@pytest.fixture
def local_cart():
    cart = Cart()
    cart.number_on_cart = NUMBER_ON_CART.copy()
    cart.cart_numbers = CART_NUMBERS
    return cart


class TestCart:

    def test_print_str(self, local_cart):
        test_number = 73
        if test_number not in local_cart.number_on_cart:
            assert local_cart.print_str(73) == "̶7̶3 "
        else:
            assert local_cart.print_str(73) == "73 "

    def test_format_number(self):
        cart = Cart()
        assert " ̶5" == cart.format_number(5)

    def test_cross_out_true(self, local_cart):
        assert local_cart.cross_out(73) is True

    def test_cross_out_false(self, local_cart):
        assert local_cart.cross_out(5) is False
