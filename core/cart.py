import random


class Cart:
    count_str = 3
    count_clm = 9

    def __init__(self):
        self.numbers = random.sample(range(1, 91), 15)
        self.number_on_cart = {}
        self.cart_numbers = {}
        self.status = True
        self.generate_cart()

    def get_random_num(self):
        """Получение рандомного числа для карточки игрока"""
        value = random.choice(self.numbers)
        while value in self.number_on_cart:
            value = random.choice(self.numbers)
        return value

    def generate_cart(self):
        """Генерация игровой карточки"""
        for str_i in range(0, self.count_str):
            str_random = random.sample(range(1, 10), 5)
            numbers_str = {}
            for clm_i in range(0, self.count_clm):
                if (clm_i + 1) in str_random:
                    value = self.get_random_num()
                    self.number_on_cart[value] = [str_i, clm_i]
                else:
                    value = 0
                numbers_str[clm_i] = value
            self.cart_numbers[str_i] = numbers_str

    def print_cart(self):
        """Печать игровой карточки"""
        cart = '------ Ваша карточка -----\n'
        for num_str, str_numbers in self.cart_numbers.items():
            str_print = ''
            for value in str_numbers.values():
                str_print += self.print_str(value)
            cart += str_print + "\n"
        cart += '--------------------------'
        print(cart)

    def print_str(self, value):
        """Формирование поля"""
        if value == 0:
            str_print = '   '
        elif value not in self.number_on_cart:
            cor_num = self.format_number(value)
            str_print = f'{cor_num} '
        elif value < 10:
            str_print = f' {str(value)} '
        else:
            str_print = f'{str(value)} '
        return str_print

    def cross_out(self, number):
        """Зачеркивание числа"""
        try:
            del self.number_on_cart[number]
            return True
        except Exception:
            self.status = False

        return False

    @staticmethod
    def format_number(number):
        """Формирование зачеркнутого числа"""
        str_num = str(number)
        result = ['\u0336' + x for x in str_num]
        result = ''.join(result)
        return result if len(str_num) > 1 else ' ' + result
