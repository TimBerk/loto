import random
from termcolor import cprint
from core.participant import Participant


CORRECT_TYPES = ['user', 'computer']


class Game:

    def __init__(self, type_participant):
        self.status = True
        self.type_participant = type_participant
        self.count_participants = len(self.type_participant)
        self.current_keg = 0
        self.participants = {}
        self.used_numbers = []

    def preparation_game(self):
        for key in range(self.count_participants):
            participant = Participant(key, self.type_participant[key], self)
            self.participants[key] = participant

    def get_keg(self):
        current_num = random.randint(1, 90)
        while current_num in self.used_numbers:
            current_num = random.randint(1, 90)
        self.current_keg = current_num
        self.used_numbers.append(current_num)

    def run(self):
        self.preparation_game()

        while self.status:
            self.get_keg()
            left_kegs = 90 - len(self.used_numbers)
            cprint(f"Новый бочонок: {self.current_keg} (осталось {left_kegs}): ", 'green')

            for key, participant in self.participants.items():
                if self.count_participants < 2:
                    cprint(f"Игра завершена(не осталось игроков)", 'red')
                    self.status = False
                    break

                if participant.can_play and self.status:
                    additional = '' if participant.type == 'user' else '(Компьютер)'
                    print(f"Ход игрока {key + 1}{additional}:")
                    participant.act(self.current_keg)
                    participant.check_status()
            print()
