# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться в файле. 
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле 
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека) 
# 4. Использование функций. Ваша программа не должна быть линейной


from creation import creation_note
from creation import show_notes
from find_to import find_to

action = input ('\n* For new note, press 1 \n* Want to see all contacts? Press 2 \n* Looking for particular note? Press 3\n* To close this menu, press 0 => ')

while action != '0':
    if action == "1":               
        creation_note()
        action = input ('\n* For new note, press 1 \n* Want to see all contacts? Press 2 \n* Looking for particular note? Press 3\n* To close this menu, press 0 \n=> ')
    elif action == "2":
        show_notes()
        action = input ('\n* For new note, press 1 \n* Want to see all contacts? Press 2 \n* Looking for particular note? Press 3\n* To close this menu, press 0 => ')
    elif action == "3":
        find_to()
        action = input ('\n* For new note, press 1 \n* Want to see all contacts? Press 2 \n* Looking for particular note? Press 3\n* To close this menu, press 0 => ')

    elif action == "0":
        exit()
    else:
        print ('Choose another number')
        action = input ('\n* For new note, press 1 \n* Want to see all contacts? Press 2 \n* Looking for particular note? Press 3\n* To close this menu, press 0 => ')

