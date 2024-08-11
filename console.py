#!/usr/bin/python3
""" contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel


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

    def do_create(self, obj):
        classes = ["BaseModel"]

        if obj:
            # for k, v in classes.items():
            if obj in classes:
                instance = BaseModel()
                instance.save()
                print(instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_create(self):
        print("".join(["Creates a new instance of BaseModel,",
                    " saves it (to the JSON file) and prints the id"]))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
