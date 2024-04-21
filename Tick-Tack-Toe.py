print("Нумерация ячеек поля:")

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
          ]

# создаем матрицу игрового поля
playing_area = matrix
# переменная для записи данных о выборе игрока
choice_pl = None
# переменные для проверки равенства
horizontal_1 = horizontal_2 = horizontal_3 = verical_1 = verical_2 = verical_3 = diagonal_1 = diagonal_2 = None


def my_matrix(matrix):
    """Функция выводит игрокам матрицу с нумерацией"""
    for i in range(3):
        for j in range(3):
            print(matrix[i][j], end=" ")
        print()


def check():
    """Функция проверяет истинность равенства горизонталей, диагоналей и вертикалей,
    возвращет булево значение"""
    horizontal_1 = playing_area[0][0] == playing_area[0][1] == playing_area[0][2]
    horizontal_2 = playing_area[1][0] == playing_area[1][1] == playing_area[1][2]
    horizontal_3 = playing_area[2][0] == playing_area[2][1] == playing_area[2][2]
    verical_1 = playing_area[0][0] == playing_area[1][0] == playing_area[2][0]
    verical_2 = playing_area[0][1] == playing_area[1][1] == playing_area[2][1]
    verical_3 = playing_area[0][2] == playing_area[1][2] == playing_area[2][2]
    diagonal_1 = playing_area[0][0] == playing_area[1][1] == playing_area[2][2]
    diagonal_2 = playing_area[2][0] == playing_area[1][1] == playing_area[0][2]
    return horizontal_1 or horizontal_2 or horizontal_3 or verical_1 or verical_2 or verical_3 or diagonal_1 or diagonal_2


def choice(sign):
    """Функция принимает данные от игрока с выбором позиции,
    в качестве аргумента передается знак, которым играет пользователь х или о,
    возвращает выбор игрока"""
    answer = input(f"Ваш символ {sign}. Сделайте выбор пустой ячейки для хода: ")
    while True:
        if (1 <= int(answer) <= 9):
            return answer
        else:
            print("Ошибка, такой номер отсутствет")
            answer = input(f"Ваш символ {sign}. Сделайте выбор пустой ячейки для хода: ")


def player(sign):
    """Функция отмечает выбор игрока на игровом поле,
    принимает один параметр - знак игрока х или о,
    ничего не возвращает"""
    global choice_pl
    choice_pl = choice(sign)
    if choice_pl == '1':
        playing_area[0][0] = sign
        my_matrix(playing_area)
    elif choice_pl == '2':
        playing_area[0][1] = sign
        my_matrix(playing_area)
    elif choice_pl == '3':
        playing_area[0][2] = sign
        my_matrix(playing_area)
    elif choice_pl == '4':
        playing_area[1][0] = sign
        my_matrix(playing_area)
    elif choice_pl == '5':
        playing_area[1][1] = sign
        my_matrix(playing_area)
    elif choice_pl == '6':
        playing_area[1][2] = sign
        my_matrix(playing_area)
    elif choice_pl == '7':
        playing_area[2][0] = sign
        my_matrix(playing_area)
    elif choice_pl == '8':
        playing_area[2][1] = sign
        my_matrix(playing_area)
    elif choice_pl == '9':
        playing_area[2][2] = sign
        my_matrix(playing_area)


def game():
    """Функция воспроизводит игровой процесс,
    после первых 5 ходов, выполняется проверка условия на победу,
    по достижении 9 ходов функция завершается и возвращает ничью"""
    global choice_pl, verical_3, verical_2, verical_1, horizontal_1, horizontal_2, horizontal_3, diagonal_1, diagonal_2

    my_matrix(matrix)
    player("x")
    player("o")
    player("x")
    player("o")
    player("x")
    if check():
        return "Победа! Игра окончена!"
    else:
        player("o")
        if check():
            return "Победа! Игра окончена!"
        else:
            player("x")
            if check():
                return "Победа! Игра окончена!"
            else:
                player("o")
                if check():
                    return "Победа! Игра окончена!"
                else:
                    player("x")
                    return "Ничья!"

print(game())