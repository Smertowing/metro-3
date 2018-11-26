manager_list = ['for','while','if','elif']
assigment_list = ['=']

set_manager = set()
set_assigment = set()
set_input = set()
set_trash = set()


def manager_string(string):

    for mem in manager_list:

        if string.find(mem) != -1:

            ind = string.find(mem)
            elem = string[ind + len(mem) + 1:]
            elem = elem[:elem.find(' ')]
            ind_1 = elem.find(':')

            if ind_1 != -1:
                elem = elem[:ind_1]

            string = string[:ind] + string[ind + len(mem) + len(elem) + 2:]

            if elem.find('(') == -1 and (not(elem.isnumeric())):
                set_manager.add(elem)

            manager_string(string)


def assigment_string(string):

    string = string.replace(' ', '')

    for operand in assigment_list:
        ind = string.find(operand)

        if string[:ind].endswith('+') or string[:ind].endswith('-') or string[:ind].endswith('*'):
            string = string[:ind-1]+string[ind+1:]
            ind -= 1

        if ind != -1:

            if string[:ind] not in set_manager:
                mem = string.find('=input(')

                if string[:ind] in set_trash:
                    set_trash.discard(string[:ind])
                    set_assigment.add(string[:ind])
                    return

                if string[:ind] in set_input and mem == -1:
                    #print(set_input,string)
                    set_input.discard(string[:ind])
                    set_assigment.add(string[:ind])
                    return

                elif not string[:ind] in set_input and mem == -1 and not string[:ind] in set_assigment:
                    set_trash.add(string[:ind])
                    return


def input_string(string):

    string = string.replace(' ','')

    ind = string.find('=input(')
    if ind != -1:

        set_input.add(string[:ind])


def main(filename):

    file = open(filename,'r')
    main_list = file.readlines()
    file.close()
    #print(main_list)

    for i in range(len(main_list)):

        manager_string(main_list[i])

    for i in range(len(main_list)):

        input_string(main_list[i])

    for i in range(len(main_list)):

        assigment_string(main_list[i])

    print(len(set_manager), set_manager)
    print(len(set_assigment), set_assigment)
    print(len(set_input),set_input)
    print(len(set_trash),set_trash)

    return [set_manager,set_assigment,set_input,set_trash]

if __name__ == '__main__':
    main('kek.txt')