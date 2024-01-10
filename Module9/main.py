dict_contacts = dict()

def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return 'Wrong name'
        except IndexError:
            return 'Wrong amount values'
        except ValueError:
            return "Give me Name and Phone Number, please"
    return inner

@input_error
def get_hello() -> str:
    return "How can I help you?"

@input_error
def get_add(data: list) -> None:
    if data[0] in dict_contacts:
        raise KeyError
    if not (data[1]).isnumeric():
        raise ValueError
    dict_contacts.update({data[0]: data[1]})
    print("Done!")

@input_error
def get_change(data: list) -> None:
    if not (data[1]).isnumeric():
        raise ValueError
    dict_contacts[data[0]] = data[1]
    print('Number was changed!')

@input_error
def get_phone(data: list) -> str:
    return (f'Number: {dict_contacts[data[0]]}')

@input_error
def get_show_all() -> dict:
    if not dict_contacts:
        return 'Your contact list is empty'
    return dict_contacts

@input_error
def get_end_program():
    return 'Good bye! Thank you for your time!'

def get_wrong_command():
    return 'Wrong command.. Try again, please!'


COMMANDS = {
    'hello': get_hello,
    'add': get_add,
    'change': get_change,
    'phone': get_phone,
    'show all': get_show_all,
    'good bye': get_end_program,
    'close': get_end_program,
    'exit': get_end_program,
    'wrong command': get_wrong_command
}

def get_handler(processed_comand):
    if processed_comand not in COMMANDS:
        return COMMANDS['wrong command']
    return COMMANDS[processed_comand]


# Parser for all commands that you wrote
# I have problem with commands that has two and more words
def comand_parser(comand):
    result = {
        'comand': '',
        'data': []
    }
    if comand.lower() == 'show all' or comand.lower() == 'good bye':
        result['comand'] = comand.lower()
        return result['comand'], result['data']
    
    command_list = comand.split(' ')
    result['comand'] = command_list[0].lower()
    result['data'] = command_list[1:]
    return result['comand'], result['data']
# ================================================

def main():
    while True:
        comand = input('Waiting comand: ')
        processed_comand, data = comand_parser(comand)
        if data:
            result = get_handler(processed_comand)(data)
        if not data:
            result = get_handler(processed_comand)()
        if type(result) is dict:
            for key, value in result.items():
                print(f'Contact: "{key}"  Number: {value}')
                continue
        elif result:
            print(result)
            if result == 'Good bye! Thank you for your time!':
                break


if __name__ == '__main__':
    print('HELLO! This is Command Line Interface')
    print("I'm your PhoneBook assistant")
    print("--------------")
    main()
