from colorama import Fore, Style
from color_function import greet


welcome_banner = r'''
  ___          _     _              _     _           _   
 / _ \        (_)   | |            | |   | |         | |  
/ /_\ \___ ___ _ ___| |_ __ _ _ __ | |_  | |__   ___ | |_ 
|  _  / __/ __| / __| __/ _` | '_ \| __| | '_ \ / _ \| __|
| | | \__ \__ \ \__ \ || (_| | | | | |_  | |_) | (_) | |_ 
\_| |_/___/___/_|___/\__\__,_|_| |_|\__| |_.__/ \___/ \__|
'''


commands = f'''
{Fore.BLUE}1){Style.RESET_ALL} {Fore.YELLOW}hello{Style.RESET_ALL} - {Fore.BLUE}greet the assistant bot{Style.RESET_ALL}
{Fore.BLUE}2){Style.RESET_ALL} {Fore.YELLOW}add username phone{Style.RESET_ALL} - {Fore.BLUE}add a new contact with name and phone number{Style.RESET_ALL}
{Fore.BLUE}3){Style.RESET_ALL} {Fore.YELLOW}change username old_phone new_phone{Style.RESET_ALL} - {Fore.BLUE}change the phone number for an existing contact{Style.RESET_ALL}
{Fore.BLUE}4){Style.RESET_ALL} {Fore.YELLOW}phone username{Style.RESET_ALL} - {Fore.BLUE}show the phone number of the contact{Style.RESET_ALL}
{Fore.BLUE}5){Style.RESET_ALL} {Fore.YELLOW}add-birthday username DD.MM.YYYY{Style.RESET_ALL} - {Fore.BLUE}add a birthday for the specified contact{Style.RESET_ALL}
{Fore.BLUE}6){Style.RESET_ALL} {Fore.YELLOW}show-birthday username{Style.RESET_ALL} - {Fore.BLUE}show the birthday of the specified contact{Style.RESET_ALL}
{Fore.BLUE}7){Style.RESET_ALL} {Fore.YELLOW}birthdays{Style.RESET_ALL} - {Fore.BLUE}show birthdays for the next 7 days{Style.RESET_ALL}
{Fore.BLUE}8){Style.RESET_ALL} {Fore.YELLOW}remove-phone username phone{Style.RESET_ALL} - {Fore.BLUE}remove a phone number{Style.RESET_ALL}
{Fore.BLUE}9){Style.RESET_ALL} {Fore.YELLOW}remove-contact username{Style.RESET_ALL} - {Fore.BLUE}remove entire contact{Style.RESET_ALL}
{Fore.BLUE}10){Style.RESET_ALL} {Fore.YELLOW}show username{Style.RESET_ALL} - {Fore.BLUE}display full contact details{Style.RESET_ALL}
{Fore.BLUE}11){Style.RESET_ALL} {Fore.YELLOW}all{Style.RESET_ALL} - {Fore.BLUE}show all saved contacts{Style.RESET_ALL}
{Fore.BLUE}12){Style.RESET_ALL} {Fore.YELLOW}help{Style.RESET_ALL} - {Fore.BLUE}show this help menu{Style.RESET_ALL}
{Fore.BLUE}13){Style.RESET_ALL} {Fore.YELLOW}exit or close{Style.RESET_ALL} - {Fore.BLUE}exit the application{Style.RESET_ALL}
'''

def init():
    print(greet(welcome_banner))
    print(commands)
    print()