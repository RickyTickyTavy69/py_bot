import webbrowser
from functions.greet import greet
from functions.print_help import print_help


def handle_command(message):
    print("command", message.text)
    match message:
        case "/start":
            greet(message)
        case "/help":
            print_help(message)
        case "/site", "/website":
            webbrowser.open("https://ng-project-production.up.railway.app/")