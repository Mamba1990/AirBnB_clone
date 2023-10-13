#!/usr/bin/python3
"""Represents the HBnB console."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curlyBraces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curlyBraces is None:
        if brackets is None:
            return [j.strip(",") for j in split(arg)]
        else:
            llexer = split(arg[:brackets.span()[0]])
            ret_l = [j.strip(",") for j in llexer]
            ret_l.append(brackets.group())
            return ret_l
    else:
        llexer = split(arg[:curlyBraces.span()[0]])
        ret_l = [j.strip(",") for j in llexer]
        ret_l.append(curlyBraces.group())
        return ret_l


class HBNBCommand(cmd.Cmd):
    """Represents the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The prompt's command.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyLine(self):
        """No action if receiving an empty line."""
        pass

    def default(self, arg):
        """The defaulted behavior for cmd module during an invalid input"""
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        _match = re.search(r"\.", arg)
        if _match is not None:
            arg_l = [arg[:_match.span()[0]], arg[_match.span()[1]:]]
            _match = re.search(r"\((.*?)\)", arg_l[1])
            if _match is not None:
                _command = [arg_l[1][:_match.span()[0]], _match.group()[1:-1]]
                if _command[0] in arg_dict.keys():
                    call = "{} {}".format(arg_l[0], _command[1])
                    return arg_dict[_command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        arg_l = parse(arg)
        if len(arg_l) == 0:
            print("** class name missing **")
        elif arg_l[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg_l[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        arg_l = parse(arg)
        obj_dict = storage.all()
        if len(arg_l) == 0:
            print("** class name missing **")
        elif arg_l[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_l) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_l[0], arg_l[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg_l[0], arg_l[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        arg_l = parse(arg)
        obj_dict = storage.all()
        if len(arg_l) == 0:
            print("** class name missing **")
        elif arg_l[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_l) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_l[0], arg_l[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arg_l[0], arg_l[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        arg_l = parse(arg)
        if len(arg_l) > 0 and arg_l[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_l = []
            for ob in storage.all().values():
                if len(arg_l) > 0 and arg_l[0] == ob.__class__.__name__:
                    obj_l.append(ob.__str__())
                elif len(arg_l) == 0:
                    obj_l.append(ob.__str__())
            print(obj_l)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        arg_l = parse(arg)
        ct = 0
        for ob in storage.all().values():
            if arg_l[0] == ob.__class__.__name__:
                ct += 1
        print(ct)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        arg_l = parse(arg)
        obj_dict = storage.all()

        if len(arg_l) == 0:
            print("** class name missing **")
            return False
        if arg_l[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg_l) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_l[0], arg_l[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(arg_l) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_l) == 3:
            try:
                type(eval(arg_l[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg_l) == 4:
            ob = obj_dict["{}.{}".format(arg_l[0], arg_l[1])]
            if arg_l[2] in ob.__class__.__dict__.keys():
                val_type = type(ob.__class__.__dict__[arg_l[2]])
                ob.__dict__[arg_l[2]] = val_type(arg_l[3])
            else:
                ob.__dict__[arg_l[2]] = arg_l[3]
        elif type(eval(arg_l[2])) == dict:
            ob = obj_dict["{}.{}".format(arg_l[0], arg_l[1])]
            for k, v in eval(arg_l[2]).items():
                if (k in ob.__class__.__dict__.keys() and
                        type(ob.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(ob.__class__.__dict__[k])
                    ob.__dict__[k] = valtype(v)
                else:
                    ob.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
