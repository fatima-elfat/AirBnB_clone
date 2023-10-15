#!/usr/bin/python3
"""
The console.
It contains the entry point of the
command interpreter the HBNBCommand module.
"""

import cmd
from models import storage
from models.base_model import BaseModel
import shlex
import re
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    the command interpreter HBNBCommand.
    Attributes:
        prompt (str) : a custom prompt.
    """
    prompt = "(hbnb) "
    __clss = ["BaseModel", "User",
              "State", "City",
              "Amenity", "Place", "Review"]

    def do_quit(self, line):
        """
        exits the program on quit.
        """
        return True

    def do_EOF(self, line):
        """
        exits the program on EOF.
        """
        print()
        return True

    def emptyline(self):
        """
        doesn't execute anything.
        """
        pass

    def do_create(self, line):
        """
        creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        """
        cmd, _, _ = self.parseline(line)
        if cmd is None:
            print("** class name missing **")
        elif cmd not in self.__clss:
            print("** class doesn't exist **")
        else:
            print(eval(cmd)().id)
            storage.save()

    def do_show(self, line):
        """
        prints the string representation
        of an instance based on the class name and id.
        """
        the_dict = storage.all()
        cmd, arg, _ = self.parseline(line)
        """print("{}".format(arg))"""
        if cmd is None:
            print("** class name missing **")
        elif cmd not in self.__clss:
            print("** class doesn't exist **")
        elif arg == "":
            print("** instance id missing **")
        elif "{}.{}".format(cmd, arg) not in the_dict:
            print("** no instance found **")
        else:
            print(the_dict["{}.{}".format(cmd, arg)])

    def do_destroy(self, line):
        """
        deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        the_dict = storage.all()
        cmd, arg, _ = self.parseline(line)
        if cmd is None:
            print("** class name missing **")
        elif cmd not in self.__clss:
            print("** class doesn't exist **")
        elif arg == "":
            print("** instance id missing **")
        elif "{}.{}".format(cmd, arg) not in the_dict.keys():
            print("** no instance found **")
        else:
            del the_dict["{}.{}".format(cmd, arg)]
            storage.save()

    def do_all(self, line):
        """
        prints all string representation
        of all instances based or not on the class name.
        """
        the_dict = storage.all()
        cmd, _, _ = self.parseline(line)
        if cmd not in self.__clss:
            print("** class doesn't exist **")
        else:
            r_obj = []
            for val in the_dict.values():
                if cmd is None:
                    r_obj.append(val.__str__())
                if cmd == val.__class__.__name__:
                    r_obj.append(val.__str__())
            print(r_obj)

    def do_update(self, line):
        """
        """
        the_dict = storage.all()
        cmd, arg, _ = self.parseline(line)
        l_arg = shlex.split(arg)
        """print("{}".format(arg))"""
        b = "{}.{}".format(cmd, l_arg[0])
        a = the_dict.get(b)
        if cmd is None:
            print("** class name missing **")
        elif cmd not in self.__clss:
            print("** class doesn't exist **")
        elif arg == "":
            print("** instance id missing **")
        if a:
            if len(l_arg) < 2:
                print("** attribute name missing **")
            elif len(l_arg) < 3:
                print("** value missing **")
            else:
                if l_arg[1] not in b.__class__.__dict__.keys():
                    setattr(a, l_arg[1], l_arg[2].strip())
                else:
                    t = type(b.__class__.__dict__[l_arg[1]])
                    setattr(a, l_arg[1], t(l_arg[2].strip()))
                setattr(a, 'updated_at', datetime.now())
                storage.save()
        else:
            print("** no instance found **")

    def default(self, line):
        """
        default when preffix not recognized.
        """
        if '.' in line:
            splt_list = re.split(r'\.|\(|\)', line)
            if len(splt_list) < 2:
                print("** Unknown syntax:", line)
            elif splt_list[0] not in self.__clss:
                print("** class doesn't exist **")
            else:
                if splt_list[1] == 'show':
                    id_cls = splt_list[2][1:-1]
                    self.do_show(splt_list[0] + ' ' + id_cls)
                elif splt_list[1] == 'destroy':
                    id_cls = splt_list[2][1:-1]
                    self.do_destroy(splt_list[0] + ' ' + id_cls)
                elif splt_list[1] == 'all':
                    self.do_all(splt_list[0])
                elif splt_list[1] == 'count':
                    self.do_count(splt_list[0])
                elif splt_list[1] == 'update':
                    id_arg = splt_list[2].split(',', 1)
                    if len(id_arg) < 2:
                        print("** attribute not found **")
                    if id_arg[1].strip()[0] != "{":
                        args = splt_list[2].split(",", 2)
                        self.do_update(" ".join(
                            [splt_list[0]] + [a.strip(" \"") for a in args]
                            ))
                    else:
                        arg, args = splt_list[2].strip("}").split("{")
                        args = args.split(",")
                        r = [splt_list[0]] + [arg.split(",")[0]]
                        for a in args:
                            self.do_update(
                                " ".join(
                                    r + [b.strip("\" ") for b in a.split(":")]
                                    ))
                else:
                    print("** Unknown syntax:", line)

    def do_count(self, line):
        """
        retrieves the number of instances of class
        """
        the_dict = storage.all()
        cmd, _, _ = self.parseline(line)
        if cmd is None:
            print("** class name missing **")
        count = 0
        for val in the_dict.values():
            if cmd == val.__class__.__name__:
                count += 1
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
