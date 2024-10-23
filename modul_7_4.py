team1_name = 'Мастер кода'
team2_name = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

a = ('В команде Мастера кода участников: %s!' %team1_num)
print(a)
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print('Волшебники данных решили задачи за {}!'. format(team2_time))
print(f'Команды решили {score_1} и {score_2} задач.')
if score_1 > score_2:
    print(f'Результат битвы: победа команды {team1_name}!')
elif score_1 == score_2:
    print(f'Ничья!')
else:
    print(f'Результат битвы: победа команды {team2_name}!')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
