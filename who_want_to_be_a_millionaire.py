from random import randint #comand randint
player_name = input('Write your name: ')
player_surname = input('Write your surname: ')
points = 0 #points which you will give
false_ans = 0
def random_question(player_name, player_surname, points, false_ans):
    while false_ans != 3:
        questions = {'How many stars on USA flag?' : '50', 
                    'What year was born Sakharov?' : '1921',
                    'Near which mountain-volcano was the gem tanzanite found for the first time?' : 'Kilimanjaro',
                    'What headdress was worn during the ball by Tatyana Larina, the heroine of the novel "Eugene Onegin"?' : 'Crimson beret',
                    "What product in different countries is called daddy's beard and grandmother's hair?" : 'Cotton candy',
                    'What is the name of the red rag in the hands of a matador?' : 'Muleta',
                    'What astronomical phenomenon can the inhabitants of the Earth observe every 75-76 years?' : "Appearance of Halley's Comet",
                    'How many carats is pure gold?' : '24'} #questions and answers
        random_index = randint(0, len(questions) - 1) #random index
        quest_list = list(questions.keys()) #questions list
        ans_list = list(questions.values()) #answer list
        true_ans = ans_list[random_index] #find true answer
        answer = input(f'{quest_list[random_index]}: ') #your answer
        # TODO - Сделать цикл. Пока что, задается только 1 вопрос
        # TODO - Добавить функционал (например, пропустить вопрос)
        def true_false(points, quest_list, random_index, false_ans):
            if answer == true_ans:
                print('True!!! Next question, please!') #If answer is True
                points += 25
                questions.pop(f'{quest_list[random_index]}')
                quest_list.pop(random_index)
                print(points)
                random_question(player_name, player_surname, points, false_ans)
            elif answer != true_ans:
                print('Not right! Next question, please!') #If answer is False
                points -= 25
                questions.pop(f'{quest_list[random_index]}')
                quest_list.pop(random_index)
                false_ans += 1
                print(points)
                print(false_ans)
                print(quest_list)
                random_question(player_name, player_surname, points, false_ans)
        true_false(points, quest_list, random_index, false_ans)
        def result_file(player_name, player_surname, points):
            with open('Your result', 'w') as file:
                file.write(f'Name: {player_name}. Surname: {player_surname}. Points: {points}')
                file.close()
        if len(questions) == 0:
            print('Game over.')
            print("Your result in the file 'Your result.txt'.")
            result_file(player_name, player_surname, points)
            break
    print('Game over.')
    print("Your result in the file 'Your result.txt'.")
    result_file(player_name, player_surname, points)
count = 1
while count != 0:
    random_question(player_name, player_surname, points, false_ans)
    count-=1
# TODO - Задача которую нужно сделать
# FIXME - Задача которую нужно исправить

'''
Tasks 
1. Залить код на Github в другой ветке
2. (Опционально) придумать свои правила оформления веток (как они будут называться)
3. Поправить код и залить изменения в ветку
4. Ознакомиться с системой контроля версий: https://git-scm.com/book/ru/v2/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%9E-%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B5-%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8F-%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D0%B9
'''