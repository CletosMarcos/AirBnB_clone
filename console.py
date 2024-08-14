#!/usr/bin/python3
""" contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """implements the command interpreter"""

    prompt = "(hbnb)"

    # available classes
    classes = {"BaseModel": BaseModel, "User": User}

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
                instance = classes[obj]()
                instance.save()
                print(instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_create(self):
        print("".join(["Creates a new instance of a class,",
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

    def do_destroy(self, obj):
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
        for k in storage.all().keys():
            if obj_id == k.split(".")[1]:
                del storage.all()[k]
                storage.save()
                return
        print("** no instance found **")

    def help_destroy(self):
        print("".join(["Deletes an instance based on the class name",
                       " and id (save the change into the JSON file)"]))
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, obj):
        list_obj = []

        if obj:
            if obj not in self.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage.all().items():
                if k.split(".")[0] == obj:
                    list_obj.append(str(v))
        else:
            for k, v in storage.all().items():
                list_obj.append(str(v))

        print(list_obj)

    def help_all(self):
        print("".join(["Prints all string representation of all instances",
                       " based or not on the class name"]))
        print("[Usage]: all <className>\n")

    def do_update(self, args):
        args = args.split()

        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_key = f"{args[0]}.{args[1]}"
        if instance_key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        attr_name = args[2]
        attr_value = args[3]

        if attr_name in ["id", "created_at", "updated_at"]:
            print("** attribute cannot be updated **")

        """list_types = [str, int, float]
        if attr_value[0] != '\"' and attr_value[-1] != '\"':
            attr_value = attr_value[1:-1]
            if type()
        """
        try:
            attr_value = int(attr_value)
        except ValueError:
            pass

        """for k, v in storage.all().items:
            if k == instance_key:
                v.attr_name = attr_value
        """
        setattr(storage.all()[instance_key], attr_name, attr_value)
        storage.save()

    def help_update(self):
        print("".join([" Updates an instance based on the class name and id",
                       " by adding or updating attribute"]))
        print("Usage: update <className> <id> <attName> <attVal>\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
