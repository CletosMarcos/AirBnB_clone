#!/usr/bin/python3
""" contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """implements the command interpreter"""

    prompt = "(hbnb)"

    def do_EOF(self, line):
        return True

    do_quit = do_EOF

if __name__ == "__main__":
    HBNBCommand().cmdloop()
