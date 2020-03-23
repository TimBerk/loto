from termcolor import cprint
from core.game import Game, CORRECT_TYPES


if __name__ == "__main__":
    types = []

    count = int(input("Введите количество игроков: "))
    while 5 < count or count < 2:
        cprint('Укажите корректное количество игроков(от 2 до 5)', 'red')
        count = int(input("Введите количество игроков: "))

    for _ in range(count):
        new_type = input("Введите тип игрока: ").lower()
        while new_type not in CORRECT_TYPES:
            cprint('Укажите корректный тип игрока(user или computer)', 'red')
            new_type = input("Введите тип игрока: ").lower()
        types.append(new_type)

    game = Game(types)
    game.run()
