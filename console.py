#!/usr/bin/python3
""" contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """implements the command interpreter"""

    prompt = "(hbnb)"

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("Quit command to exit the program")

    do_quit = do_EOF
    help_quit = help_EOF

    def emptyline(self):
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
