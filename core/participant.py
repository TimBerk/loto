import time
from termcolor import cprint
from loto.core.cart import Cart


class Participant:

    def __init__(self, key, type_participant, game):
        self.key = key
        self.type = type_participant
        self.game = game
        self.cart = Cart()
        self.can_play = True
        self.winner = False

    @staticmethod
    def get_answer():
        answers = ['зачеркнуть', 'продолжить']
        cross_out = input('Зачеркнуть число или продолжить: ').lower()

        while cross_out not in answers:
            print('Введите корректный ответ')
            cross_out = input('Зачеркнуть число или продолжить: ').lower()

        return True if cross_out == answers[0] else False

    def act(self, number):
        self.cart.print_cart()
        action = {
            'computer': self.act_computer,
            'user': self.act_man
        }

        return action[self.type](number)

    def check_status(self):
        if self.winner:
            cprint(f"Игрок {self.key + 1} победил!", 'cyan')
            self.game.status = False
        elif not self.can_play:
            self.game.count_participants -= 1

    def act_computer(self, number):
        if number in self.cart.number_on_cart:
            self.cart.cross_out(number)
            if len(self.cart.number_on_cart) == 0:
                self.winner = True

    def act_man(self, number):
        if self.get_answer():
            answer = self.cart.cross_out(number)
            if answer:
                if len(self.cart.number_on_cart) == 0:
                    self.winner = True
            else:
                self.lose_game()
        else:
            if number in self.cart.number_on_cart:
                self.lose_game()

    def lose_game(self):
        self.can_play = False
        cprint('Вы проиграли', 'red')
        time.sleep(2)
