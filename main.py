from termcolor import cprint
from core.game import CORRECT_TYPES, Game


if __name__ == "__main__":
    types = []

    count = int(input("Введите количество игроков: "))
    while 5 < count or count < 2:
        cprint('Укажите корректное количество игроков(от 2 до 5)', 'red')
        count = int(input("Введите количество игроков: "))

    print("Типы игроков: user - 1 или computer - 2")
    for num_player in range(count):
        new_type = int(input(f"Введите тип игрока {num_player + 1}: "))
        while new_type not in CORRECT_TYPES:
            cprint('Укажите корректный тип игрока', 'red')
            new_type = int(input("Введите тип игрока: "))
        types.append(new_type)

    game = Game(types)
    game.run()
