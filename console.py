#!/usr/bin/python3
"""AirBnB clone - The console."""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review

CLASSES = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
           "City": City, "State": State, "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """Command interpreter to manage your AirBnB clone objects."""

    prompt = "(hbnb) "

    def do_list(self, arg):
        """List available Classes."""
        print(*CLASSES)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on End Of File."""
        print()
        return True

    def emptyline(self):
        """Prevent repeat the last nonempty command on emptyline command."""
        pass

    def do_create(self, arg):
        """Create a new instance of a Airbnb Class.

        Usage: create <Class>
        """
        if len(arg) < 1:
            print("** class name missing **")
            return False
        arg_list = arg.split()
        try:
            if arg_list[0] in CLASSES:
                new_instance = CLASSES[arg_list[0]]()
            new_instance.save()
            print(new_instance.id)
        except:
            print("** class doesn't exist **")
            return False

    def do_show(self, arg):
        """Print the string representation of an instance.

        Usage: show <Class> <id>
               Class.show(<id>)
        """
        arg_list = shlex.split(arg)
        if len(arg_list) == 0:
            print("** class name missing **")
        elif len(arg_list) and arg_list[0] not in CLASSES:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            instance = arg_list[0] + "." + arg_list[1]
            if instance in storage.all():
                print(storage.all()[instance])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id.

        Usage: destroy <Class> <id>
               <Class>.destroy(<id>)
        """
        if len(arg) == 0:
            print("** class name missing **")
        else:
            arg_list = shlex.split(arg)
            if arg_list[0] not in CLASSES:
                print("** class doesn't exist **")
            elif len(arg_list) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(arg_list[0], arg_list[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, arg):
        """Print all string representation of all instances.

        Usage: all [Class]
               Class.all()
               Class.count()
        """
        if arg:
            if arg in CLASSES:
                for obj in storage.all().values():
                    if type(obj).__name__ == arg:
                        print(obj)
            else:
                print("** class doesn't exist **")
        else:
            for obj in storage.all().values():
                print(obj)

    def do_update(self, arg):
        """Update an instance based on the class name and id.

        Usage: update <class name> <id> <attribute name> "<attribute value>"
               <Class>.update(<id>, <attribute name>, <attribute value>)
               <class name>.update(<id>, <dictionary representation>)
               """
        arg_list = shlex.split(arg)
        if arg_list and arg_list[0] not in CLASSES:
            print("** class doesn't exist **")
        elif not arg:
            print("** class name missing **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif len(arg_list) == 2:
            print("** attribute name missing **")
        elif len(arg_list) == 3:
            print("** value missing **")
        else:
            objs = arg_list[0] + "." + arg_list[1]
            if objs in storage.all():
                setattr(storage.all()[objs], arg_list[2], arg_list[3])
                storage.save()
            else:
                print("** no instance found **")

    def count(self, arg):
        """Count instances of a Class."""
        count = 0
        arg_list = arg.split(' ')
        for key in storage.all():
            obj_class = storage.all()[key]
            if arg_list[0] == obj_class.__class__.__name__:
                count += 1
        print(count)

    def get_line(self, args):
        """Strip the argument and return a string of command."""
        new_list = []
        new_list.append(args[0])
        try:
            my_dict = eval(
                args[1][args[1].find('{'):args[1].find('}')+1])
        except Exception:
            my_dict = None
        if isinstance(my_dict, dict):
            new_str = args[1][args[1].find('(')+1:args[1].find(')')]
            new_list.append(((new_str.split(", "))[0]).strip('"'))
            new_list.append(my_dict)
            return new_list
        new_str = args[1][args[1].find('(')+1:args[1].find(')')]
        new_list.append(" ".join(new_str.split(", ")))
        return " ".join(i for i in new_list)

    def default(self, arg):
        """Called on an input line when the command is not recognized."""
        arg_list = arg.split('.')
        if len(arg_list) >= 2:
            if arg_list[1] == "all()":
                self.do_all(arg_list[0])
            elif arg_list[1] == "count()":
                self.count(arg_list[0])
            elif arg_list[1][:4] == "show":
                self.do_show(self.get_line(arg_list))
            elif arg_list[1][:7] == "destroy":
                self.do_destroy(self.get_line(arg_list))
            elif arg_list[1][:6] == "update":
                args = self.get_line(arg_list)
                if isinstance(args, list):
                    keys = args[0] + ' ' + args[1]
                    for key, val in args[2].items():
                        self.do_update(keys + ' "{}" "{}"'.format(key, val))
                else:
                    self.do_update(args)
        else:
            cmd.Cmd.default(self, arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
