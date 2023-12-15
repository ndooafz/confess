import os
import time
from pyfiglet import Figlet
from colorama import Fore, init

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_text_animation(text, delay=1.0, clear=True):
    fig = Figlet(font='slant')
    if clear:
        clear_screen()
    for line in text.splitlines():
        print(Fore.RED + fig.renderText(line))
        time.sleep(delay)

    def ask_question(question):
        print(Fore.GREEN + question)
        response = input(Fore.Yellow + "Yes or No?: ").lower()
        return response

    def main():
        display_text_animation("I", delay=0,5)
        display_text_animation("I like", delay=0,5)
        display_text_animation("I like you", delay=0,5)

        # Display static text like animation I Like You

        response = ask_question("Do you like me?")

        if response == 'yes':
            display_text_animation("I love", delay=0,5)
            display_text_animation("I love you", delay=0,5)

            # Display static text like animation I love you
            print(Fore.RED + "Hehe<3")

        elif response == 'no':
            display_text_animation("Thanks", delay=0,5)
            display_text_animation("for", delay=0,5)
            display_text_animation("answering", delay=0,5)
            clear_screen()
            display_text_animation("Thanks for answering :(", delay=0,5)

if __name__ == "__main__":
    main()