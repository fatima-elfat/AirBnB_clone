#!/usr/bin/python3

"""Entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import shlex
import re
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNB class"""
    prompt = "(hbnb) "
    __classes = [
        "BaseModel", "User",
        "State", "City",
        "Amenity", "Place", "Review"]  # list of existing classes

    __commands = {
        "show",
        "count",
        "all",
        "destroy",
        "update"
    }

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if len(arg) > 0:
            list_arg = arg.split()
            if arg in HBNBCommand.__classes:
                print(eval(list_arg[0])().id)
                storage.save()
            else:  # class name not in __classes
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_create(self):
        """
        Help command for create
        """
        print("Create a BaseModel and save json in a file\n")

    def precmd(self, line):
        """ Get the line before interpretation"""
        if len(line):
            l_c = line.split()
            if len(l_c):
                l_last = line.split("{")
                l_upd = line.split("\"")
                all_instances = storage.all()
                ll_cc = l_c[0].split("(")
                c_l = ll_cc[0].split(".")
                if len(ll_cc) == 2:
                    l_arg = ll_cc[1].split("\"")
                else:
                    return line
                if len(c_l) == 2 and c_l[0] in self.__classes\
                        and c_l[1] in self.__commands:
                    s_c = c_l[1] + " " + c_l[0]
                    if ll_cc[1] == ")":
                        return s_c
                    elif len(l_arg) == 3 and l_arg[2] == ")":
                        return s_c + " " + l_arg[1]
                    elif len(l_upd) == 7 and l_upd[6] == ")":
                        return s_c + " " + l_arg[1] + " "\
                            + l_upd[3] + " \"" + l_upd[5] + "\""
                    elif len(l_last):
                        try:
                            dict_up = json.loads(
                                str("{" + l_last[1][:-1].replace("'", "\"")))
                            s_c = c_l[0] + " " + l_arg[1]
                            for k, v in dict_up.items():
                                self.do_update(
                                    s_c + " \"" + k + "\" \"" + str(v) + "\"")
                            ans = c_l[1] + " " + s_c + " \"" + \
                                k + "\" \"" + str(v) + "\""
                            return ans
                        except FileNotFoundError:
                            return line
                    else:
                        return line
                else:
                    return line
            else:
                return line
        else:
            return line

    def do_show(self, arg):
        """Prints the string representation of an
        instance by its class name and id
        """
        if arg:
            objects = storage.all()
            list_args = arg.split()
            if list_args[0]:
                if list_args[0] in HBNBCommand.__classes:
                    if len(list_args) >= 2:
                        class_id = f"{list_args[0]}.{list_args[1]}"
                        if class_id in objects:
                            print(objects[class_id])
                        else:
                            print("** no instance found **")
                    else:
                        print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
            else:
                print("** class name missing **")
        else:
            print("** class name missing **")

    def help_show(self):
        """
        Help command
        """

        msg = "Prints the string representation of an instance "
        msg += "based on the class name and id\n"
        print(msg)

    def do_destroy(self, arg):
        """Deletes an instance from memory
          by its class name and id"""
        if arg:
            objects = storage.all()
            list_args = arg.split()
            if list_args[0]:
                if list_args[0] in HBNBCommand.__classes:
                    if list_args[1]:
                        class_id = f"{list_args[0]}.{list_args[1]}"
                        if class_id in objects:
                            del objects[class_id]
                            storage.save()
                        else:
                            print("** no instance found **")
                    else:
                        print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
            else:
                print("** class name missing **")
        else:
            print("** class name missing **")

    def help_destroy(self):
        """
        Help command to destroy
        """
        print("Deletes an instance based on the class name and id\n")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based on the class name
        """
        objects = storage.all()
        if arg:
            list_args = arg.split()
            if list_args[0] in HBNBCommand.__classes:
                class_objs = [
                    str(v) for k, v in objects.items()
                    if list_args[0] == k.split('.')[0]
                    ]
                print(class_objs)
            else:
                print("** class doesn't exist **")
        else:
            allObjs = [str(v) for k, v in objects.items()]
            print(allObjs)

    def help_all(self):
        """
        Help command
        """

        msg = "Prints all string representation of all instances "
        msg += "based or not on the class name\n"
        print(msg)

    def do_update(self, line):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        the_dict = storage.all()
        cmd, arg, _ = self.parseline(line)
        l_arg = shlex.split(arg)
        """print("{}".format(arg))"""
        b = "{}.{}".format(cmd, l_arg[0])
        a = the_dict.get(b)
        if cmd is None:
            print("** class name missing **")
        elif cmd not in self.__classes:
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

    def help_update(self):
        """
        Help command for updating
        """

        msg = "Updates an instance based on the class "
        msg += "name and id by adding or updating attribute\n"
        msg += "Usage: update <class name> <id> <attribute name>  "
        msg += "\"<attribute value>\"\n"
        print(msg)

    def default(self, line):
        """
        default when preffix not recognized.
        """
        if '.' in line:
            splt_list = re.split(r'\.|\(|\)', line)
            if len(splt_list) < 2:
                print("** Unknown syntax:", line)
            elif splt_list[0] not in self.__classes:
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

    def help_count(self):
        """
        Help command for count
        """

        msg = "Count the amount of instances in a given class\n"
        print(msg)

    def do_quit(self, arg):
        """Exit the interpreter"""
        return True

    def help_quit(self):
        """
        Help command for quitting the program
        """
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        """Exit on end-of-file input"""
        return True

    def help_EOF(self):
        """
        Help command for EOF
        """
        print("EOF command to exit the program\n")

    def emptyline(self):
        """Empty line"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
