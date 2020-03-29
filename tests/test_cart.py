import pytest
from core.cart import Cart
from tests.const import NUMBER_ON_CART, CART_NUMBERS


@pytest.fixture
def local_cart():
    cart = Cart()
    cart.number_on_cart = NUMBER_ON_CART.copy()
    cart.cart_numbers = CART_NUMBERS
    return cart


class TestCart:

    def test_print_str(self):
        cart = Cart()
        assert cart.print_str(5) == " ̶5 "

    def test_format_number(self):
        cart = Cart()
        assert " ̶5" == cart.format_number(5)

    def test_cross_out_true(self, local_cart):
        assert local_cart.cross_out(73) is True

    def test_cross_out_false(self, local_cart):
        assert local_cart.cross_out(5) is False
