from random import randint #comand randint
player_name = input('Write your name: ')
player_surname = input('Write your surname: ')
points = 0 #points which you will give
false_ans = 0
skip_ans = 0
def random_question(player_name, player_surname,
                    points, false_ans, skip_ans):

    def true_false(points, questions, quest_list, 
                   true_ans, random_index, false_ans, skip_ans):
            if answer == true_ans:
                print('True!!! Next question, please!') #If answer is True
                points += 25
                questions.pop(f'{quest_list[random_index]}')
                quest_list.pop(random_index)
                ans_list.pop(random_index)
            
            elif answer == '???':
                skip_ans += 1
                questions.pop(f'{quest_list[random_index]}')
                quest_list.pop(random_index)
                ans_list.pop(random_index)
                
            else:
                print('Not right! Next question, please!') #If answer is False
                points -= 25
                questions.pop(f'{quest_list[random_index]}')
                quest_list.pop(random_index)
                ans_list.pop(random_index)
                false_ans += 1

            return points, false_ans, questions, quest_list, skip_ans

    def result_file(player_name, player_surname, points):
            with open('Your result', 'a') as file:
                file.write(f'Name: {player_name}. Surname: {player_surname}. Points: {points}\n')
                file.close()

    questions = {'How many stars on USA flag?' : '50', 
                    'What year was born Sakharov?' : '1921',
                    'Near which mountain-volcano was the gem tanzanite found for the first time?' : 'Kilimanjaro',
                    'What headdress was worn during the ball by Tatyana Larina, the heroine of the novel "Eugene Onegin"?' : 'Crimson beret',
                    "What product in different countries is called daddy's beard and grandmother's hair?" : 'Cotton candy',
                    'What is the name of the red rag in the hands of a matador?' : 'Muleta',
                    'What astronomical phenomenon can the inhabitants of the Earth observe every 75-76 years?' : "Appearance of Halley's Comet",
                    'How many carats is pure gold?' : '24'} # questions and answers
    
    quest_list = list(questions.keys()) #questions list
    ans_list = list(questions.values()) #answer list
    
    while false_ans != 3 or len(questions) != 0:
        random_index = randint(0, len(questions) - 1) #random index
        answer = input(f'{quest_list[random_index]}: ').strip().lower() #your answer
        true_ans = ans_list[random_index].lower() # find true answer            
        result = true_false(points, questions, quest_list, 
                            true_ans, random_index, false_ans, skip_ans)
        points = result[0]
        false_ans = result[1]
        questions = result[2]
        quest_list = result[3]
    
    print('Game over.')
    print("Your result in the file 'Your result.txt'.")
    result_file(player_name, player_surname, points)

# TODO - написать функцию которая будет чистить список результатов DID
# TODO Пользователь может пропустить вопрос DID
# TODO - Подсказка по вопросу
while True or ask == 'Y':
    ask_result_delet = input("Do you want to delet your result from file 'Your result.txt'? Y/N: ")
    ask = input("Start? Y/N: ") # Question: "Do you want to continue game?"
    if ask_result_delet == 'Y':
        with open('Your result', 'w') as file:
            file.write('New Result: \n')
        random_question(player_name, player_surname,
                        points, false_ans, skip_ans)
    elif ask == 'Y':
        random_question(player_name, player_surname,
                        points, false_ans, skip_ans)
    elif ask != 'Y':
        break
    else:
        random_question(player_name, player_surname,
                        points, false_ans, skip_ans)
# TODO - дождатса урока
# TODO - добавить функцию 
'''
Tasks 
1. Залить код на Github в другой ветке
2. (Опционально) придумать свои правила оформления веток (как они будут называться)
3. Поправить код и залить изменения в ветку
4. Ознакомиться с системой контроля версий: https://git-scm.com/book/ru/v2/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%9E-%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B5-%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8F-%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D0%B9
'''
