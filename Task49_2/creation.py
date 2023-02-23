def creation_note():
    name = input('Input abonent name ')
    number = input('Input abonent phone number ')
    with open ('phone_book.txt', 'a') as pb:
        pb.writelines('\n' + name + " ")
        pb.write(number)



def show_notes():
    from os import system
    system('cls')
    data = open("phone_book.txt", 'r')
    for line in data:
        print (line)
    data.close()

