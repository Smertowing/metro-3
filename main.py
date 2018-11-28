manager_list = ['for','while','if','elif','=<','=>','!=','==','in','<','>']
assigment_list = ['=']

set_manager = set()
set_assigment = set()
set_input = set()
set_trash = set()

set_chepin_ext = set()

set_manager_chep = set()
set_assigment_chep  = set()
set_input_chep  = set()
set_trash_chep  = set()

operators = ['+', '-', '*', '**', '/', '//', '%', '@', '<<',
                  '>>', '&', '|', '^', '~', '<', '>', '<=', '>=',
                  '==', '!=', '=', '+=', '*=', '/=', '-=', '%=',
                  '**=', '//=','False', 'None', 'True', 'and', 'as', 'assert', 'break',
                'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
                'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
                'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
                'try', 'while', 'with', 'yield',' ']
operators_set = set(operators)
operands = []

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


def chepin_exetended(list):
    for str in list:
        temp_str = str.replace(' ','')
        ind_1 = temp_str.find('=input(')
        if ind_1 != -1:
            variables = temp_str[:ind_1]
            set_chepin_ext.add(variables)
        else:
            ind_2 = temp_str.find('print')
            if ind_2 != -1:
                temp_str = temp_str[ind_2+len('print'):]
                temp_str = temp_str[temp_str.find('(')+1:temp_str.find(')')]
                if temp_str.find(',') == -1:
                    set_chepin_ext.add(temp_str)
                else:
                    str_list = temp_str.split(',')
                    for el in str_list:
                        set_chepin_ext.add(el)

def spen_req(string):
    import re
    #string = string.replace(' ', '')
    temp_str_list = re.findall(r'[^\n+=,-:. ]+', string)
    #print(temp_str_list)
    for elem in temp_str_list:
        elem = elem.replace(' ','')
        if elem not in operators_set:
            if elem.find('(') == -1:
                operands.append(elem)
                #print(operands)
            else:
                temp_string = string[string.find('(')+1:string.find(')')]
                # print(temp_string)
                spen_req(temp_string)


def spen(list_of_string):
    for string in list_of_string:
        spen_req(string)
    return dict(Counter(operands))

from collections import Counter


def main(filename):

    file = open(filename,'r')
    main_list = file.readlines()
    file.close()
    # print(main_list)

    for i in range(len(main_list)):

        manager_string(main_list[i])

    for i in range(len(main_list)):

        input_string(main_list[i])

    for i in range(len(main_list)):

        assigment_string(main_list[i])

    # print(len(set_manager), set_manager)
    # print(len(set_assigment), set_assigment)
    # print(len(set_input),set_input)
    # print(len(set_trash),set_trash)
    #
    # print('\n')

    chepin_exetended(main_list)

    set_manager_chep = set_chepin_ext.intersection(set_manager)
    set_assigment_chep = set_chepin_ext.intersection(set_assigment)
    set_input_chep = set_chepin_ext.intersection(set_input)
    set_trash_chep = set_chepin_ext.intersection(set_trash)

    # print(len(set_manager_chep), set_manager_chep)
    # print(len(set_assigment_chep), set_assigment_chep)
    # print(len(set_input_chep), set_input_chep)
    # print(len(set_trash_chep), set_trash_chep)

    dict_operands = spen(main_list)
    for key in dict_operands:
        dict_operands[key]-=1

    return [[set_manager,set_assigment,set_input,set_trash],[set_manager_chep,set_assigment_chep,set_input_chep,set_trash_chep],dict_operands]

if __name__ == '__main__':
    main('kek.txt')