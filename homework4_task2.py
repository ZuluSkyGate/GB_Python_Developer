# Задача 2. Недоделка
# Вы пришли на работу в компанию по разработке игр, целевая аудитория —
# дети и их родители. У предыдущего программиста было задание сделать две
# игры в одном приложении, чтобы пользователь мог выбирать одну из них.
# Однако программист , на место которого вы пришли, перед увольнением не
# успел выполнить эту задачу и оставил только небольшой шаблон проекта.
# Используя этот шаблон, реализуйте игры «Камень, ножницы, бумага» и «Угадай
# число».
# Правила игры «Камень, ножницы, бумага»: программа запрашивает у
# пользователя строку и выводит , победил он или проиграл. Камень бьёт
# ножницы, ножницы режут бумагу , бумага кроет камень.
# Правила игры «Угадай число»: программа запрашивает у пользователя число
# до тех пор, пока он не отгадает загаданное.

def rock_paper_scissors():

    player = int(input("1 - камень, 2 - ножницы, 3 - бумага. Введите ваш выбор: "))
    computer = 1

    if player == computer:
        print("Ничья!")
    elif (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
        print("Вы выиграли!")
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        print("Вы проиграли!")
    else:
        print("Неверная команда. Попробуйте снова.")

def guess_the_number():
    number = 7
    while True:
        guess_num = int(input('Введите число: '))
        if guess_num > number:
            print('Число больше, чем нужно. Попробуйте ещё раз!')
        elif guess_num < number:
            print('Число меньше, чем нужно. Попробуйте ещё раз!')
        else:
            print('Поздравляю, вы угадали! Возврат в главное меню.')
            break
def main_menu():
    while True:
        print('Во что хотите поиграть?')
        game = int(input('1 - Камень, ножницы, бумага; 2 - Угадай число; 3 - Выйти: '))
        if game == 1:
            rock_paper_scissors()
        elif game == 2:
            guess_the_number()
        elif game == 3:
            print('Выход из программы.')
            break
        else:
            print('Неверная команда. Попробуйте снова.')
main_menu()