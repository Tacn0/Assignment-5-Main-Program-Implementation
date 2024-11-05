# Program lets user write and read from a note text file

def print_main_screen():
    print(">---------- NOTETAKER ----------<")
    print("    - Welcome to Notetaker! -")
    print()
    help_command()


def write_command():
    print()
    print("-Enter Text Below-")
    print()
    user_input = input()
    f = open("note.txt", "w")
    f.write(user_input)
    f.close()
    print()


def read_command():
    print()
    print("-Note text displayed below-")
    print()
    f = open("note.txt", "r")
    print(f.read())
    print()


def help_command():
    print("  Command  |   Action")
    print("-----------|------------------------------------------------")
    print("   write   |   Replace the text of your note. Will require further input")
    print("   read    |   Display the current note text")
    print("   help    |   Provides information on how to use Notetaker")
    print("   exit    |   Exits the program")
    print("-----------|------------------------------------------------")
    print()


def command_select():
    print("> Use command 'help' if you are ever lost!")
    user_input = input("> Enter command: ")
    print()
    if user_input == "write":
        write_command()
        command_select()
    elif user_input == "read":
        read_command()
        command_select()
    elif user_input == "help":
        help_command()
        command_select()
    elif user_input == "exit":
        print("Exiting Notetaker...")
    else:
        print("Error: Command not found")
        print()
        command_select()


# User input
if __name__ == "__main__":
    print_main_screen()
    command_select()
