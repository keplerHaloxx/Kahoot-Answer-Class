from KahootClass import Kahoot
from colorama import Fore

def custom_print(color: Fore, text: str, newline=False):
    if newline:
        print(f'{color}{text}{Fore.RESET}\n')
    else:
        print(f'{color}{text}{Fore.RESET}')

def custom_input(color: Fore, text: str, return_text=True):
    if return_text:
        return input(f'{color}{text}{Fore.RESET}')
    else:
        input(f'{color}{text}{Fore.RESET}')

try:
    _id = input('Quiz ID: ')
    while not Kahoot(_id).data:
        custom_print(Fore.LIGHTRED_EX, 'Enter a valid ID', True)
        _id = input('Quiz ID: ')

    kahoot = Kahoot(_id)


    custom_print(Fore.LIGHTYELLOW_EX, f'< Choices >\n{Fore.LIGHTGREEN_EX}1{Fore.RESET} = {Fore.CYAN}Print all answers\n{Fore.LIGHTGREEN_EX}2{Fore.RESET} = {Fore.CYAN}Print answer by question number')
    print_type = custom_input(Fore.RESET, 'Answer: ', True)

    while print_type not in ['1', '2']:
        custom_print(Fore.LIGHTRED_EX, 'Please input a valid answer', True)
        custom_print(Fore.LIGHTYELLOW_EX, f'< Choices >\n{Fore.LIGHTGREEN_EX}1{Fore.RESET} = {Fore.CYAN}Print all answers\n{Fore.LIGHTGREEN_EX}2{Fore.RESET} = {Fore.CYAN}Print answer by question number')
        print_type = custom_input(Fore.RESET, 'Answer: ', True)

    if print_type == '1':
        for i in range(kahoot.get_quiz_length()):
            if kahoot.get_answer(i) is not None:
                if kahoot.get_question_details(i)['type'] == 'open_ended':
                    print(f'{Fore.RESET}< Question {i + 1} >\n{Fore.LIGHTYELLOW_EX}Q: {kahoot.get_question_names()[i]}\n{Fore.LIGHTGREEN_EX}A: ' + f'{Fore.LIGHTMAGENTA_EX} or {Fore.LIGHTGREEN_EX}'.join(kahoot.get_answer(i)) + '\n' + Fore.RESET)
                else:
                    print(f'{Fore.RESET}< Question {i + 1} >\n{Fore.LIGHTYELLOW_EX}Q: {kahoot.get_question_names()[i]}\n{Fore.LIGHTGREEN_EX}A: ' + f'{Fore.LIGHTMAGENTA_EX} | {Fore.LIGHTGREEN_EX}'.join(kahoot.get_answer(i)) + '\n'  + Fore.RESET)

    elif print_type == '2':
        while True:
            num = custom_input(Fore.RESET, '\nEnter Question Number: ')
            while not num.isdigit() or int(num) < 1 or int(num) > kahoot.get_quiz_length():
                custom_print(Fore.LIGHTRED_EX, 'Enter A Valid Question Number')
                num = custom_input(Fore.RESET, '\nEnter Question Number: ')

            custom_print(Fore.RESET, f'\n< Question {int(num)} >')
            if kahoot.get_question_details(int(num) - 1)['type'] == 'open_ended':
                custom_print(Fore.LIGHTYELLOW_EX, f'Q: {kahoot.get_question_names()[int(num) - 1]}\n{Fore.LIGHTGREEN_EX}A: ' + f'{Fore.LIGHTMAGENTA_EX} or {Fore.LIGHTGREEN_EX}'.join(kahoot.get_answer(int(num) - 1)))
            else:
                custom_print(Fore.LIGHTYELLOW_EX, f'Q: {kahoot.get_question_names()[int(num) - 1]}\n{Fore.LIGHTGREEN_EX}A: ' + f'{Fore.LIGHTMAGENTA_EX} | {Fore.LIGHTGREEN_EX}'.join(kahoot.get_answer(int(num) - 1)))

except KeyboardInterrupt:
    print(Fore.LIGHTRED_EX + '\nCancelled{Fore.RESET}\n')
