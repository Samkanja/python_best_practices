import os
from collections import OrderedDict
import business_logic
from dataclasses import dataclass

def print_bookmarks(bookmarks):
    for bookmark in bookmarks:
        print('\t'.join(
            str(field) if field else ''
            for field in bookmark
        ))


class Option:
    def __init__(self,name,command,pred_call=None) -> None:
        self.name = name
        self.command = command
        self.pred_call = pred_call

    def _handle_message(self,message):
        if isinstance(message, list):
            print_bookmarks(message)
        else:
            print(message)

    
    def choose(self):
        data = self.pred_call() if self.pred_call else None
        message = self.command.execute(data) if data else self.command.execute()
        self._handle_message(message)

    def __str__(self) -> str:
        return self.name

    
def clear_screen():
    clear = 'cls' if os.name ==  'nt' else 'clear'
    os.system(clear)

def print_options(options):
    for shortcut , option in options.items():
        print(f'({shortcut}) {option}')
    print()
def option_choice_is_valid(choice, options):
    return choice in options or choice.upper() in options


def get_option_choice(options):
    choice = input('Choose an option: ')
    while not option_choice_is_valid(choice, options):
        print("Invalid choice")
        choice = input("Choose an option: ")
    return options[choice.upper()]

def get_user_input(label, required=True):
    value = input(f'{label}: ')
    while required  and not value: 
        value = input(f'{label}: ') or None
    return value

def get_new_bookmark_data():
    return {
        'title' : get_user_input('Title'),
        'url' : get_user_input('URL'),
        'notes' : get_user_input('Notes',required=False)
    }

def get_bookmark_id_for_deletion():
    return get_user_input('Enter a bookmark ID to delete')


def loop():
    clear_screen()

    options = OrderedDict({
        'A' : Option('Add a bookmark',business_logic.AddBookmarkCommand(), pred_call=get_new_bookmark_data),
        'B' : Option('List bookmarks by date', business_logic.ListBookmarksCommand()),
        'T' : Option('List bookmarks by title', business_logic.ListBookmarksCommand(order_by='title')),
        'D' : Option('Delete a bookmark',business_logic.DeleteBookmarkCommand(),pred_call=get_bookmark_id_for_deletion),
        'Q' : Option('Quit',business_logic.QuitCommand()),

    })

    print_options(options)

    chosen_option = get_option_choice(options)
    clear_screen()
    chosen_option.choose()

    _ = input('Press Enter to return to menu')
    



if __name__ == '__main__':
    business_logic.CreateBookmarksTableCommand().execute()

    while True:
        loop()