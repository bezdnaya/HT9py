def find_to ():
    searchable = input('Input searchable name or number ')
    with open ("phone_book.txt", 'r') as pb:
        p = 0
        for i in pb:
            if searchable in i:
                print(i)
                p = 1
                action = input('\n* If you want to delete this note, press 1 \n* If you want to change this press 2\n* To close this menu, press 0  \n=> ')
                if action == '1':
                    delete(i)
                elif action == '2':
                    replace(i)
        if p == 0: print ('Not found')

def delete(el):
    with open ("phone_book.txt", 'r') as rpb:
        lines = rpb.readlines()
        with open ("phone_book.txt", 'w') as wpb:
            for line in lines:
                if el not in line:
                    wpb.write(line)
    print ('Deleted')

def replace(el):
    with open ("phone_book.txt", 'r') as rpb:
        lines = rpb.readlines()
        with open ("phone_book.txt", 'w') as wpb:
            for line in lines:
                if el in line:
                    line = line.split()
                    for part in line:
                        new_note = part.replace(part, input(f'Input new info instead of {part}  => '))
                        wpb.writelines(new_note + ' ')
                        print ('Done')
                else:
                    wpb.write(str(line))




