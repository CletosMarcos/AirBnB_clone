#!/usr/bin/python3
""" contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """implements the command interpreter"""

    prompt = "(hbnb)"

    # available classes
    classes = ["BaseModel"]

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("Quit command to exit the program")

    do_quit = do_EOF
    help_quit = help_EOF

    def emptyline(self):
        pass

    def do_create(self, obj):
        if obj:
            # for k, v in classes.items():
            if obj in self.classes:
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
        print("[Usage]: create <className>\n")

    def do_show(self, obj):
        objt = obj.partition(" ")
        class_name = objt[0]
        obj_id = objt[2]

        if not class_name:
            print("** class name missing **")
            return
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if not obj_id:
            print("** instance id missing **")
            return

        # check if the id exists in the list of available objs (json file)
        list_obj = storage.all()
        for k, v in list_obj.items():
            if obj_id == k.split(".")[1]:
                print(v)
                return
        print("** no instance found **")
 
    def help_show(self):
        print("".join(["Prints the string representation of an instance",
                       " based on the class name and id"]))
        print("[Usage]: show <className> <objectId>\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
