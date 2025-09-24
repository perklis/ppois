from tag_games import TagGame

class GameInterface:
    def __init__(self):
        self.game = TagGame()
        self.actions = {
            '1': self.show_field,
            '2': self.to_move,
            '3': self.check_solution,
            '4': self.create_new_field,
        }

    def show_menu(self):
        print("1 - Показать поле\n2 - Сделать ход (w/s/a/d)\n3 - Проверить решение")
        print("4 - Создать новое поле\n0 - Выйти")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Выберите действие:")
            if choice == '0':
                break
            action = self.actions.get(choice)
            if action:
                action()
            else:
                print("Нет такого выбора")
    
    def show_field(self):
        self.game.print_field()    

    def to_move(self):
        self.game.print_field()
        move = input("Введите направление (w/a/s/d): ").lower()
        if move not in ['w', 'a', 's', 'd']:
            print("Нет такого направления")
            return
        try:
            steps = int(input("Сколько плиток сместить: "))
        except ValueError:
            print("Нужно ввести число")
            return
        if steps <= 0:
            print("Количество должно быть положительным")
            return
        if not self.game.move_cells(move, steps):
            print("Невозможно сделать этот ход")
            return
        self.game.print_field()
        if self.game.is_solved():
            print("Игра решена")
            exit()

    def check_solution(self):
        print("Игра пройдена" if self.game.is_solved() else "Игра не пройдена")

    def create_new_field(self):
        self.game.create_field()
        print("Новое поле сгенерировано")
