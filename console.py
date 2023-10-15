#!/usr/bin/python3

"""Entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import shlex
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNB class"""
    prompt = "(hbnb) "
    __classes = ["BaseModel", "User",
              "State", "City",
              "Amenity", "Place", "Review"] # list of existing classes

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if len(arg) > 0:
            list_arg = arg.split()
            if arg in HBNBCommand.__classes:
                print(eval(list_arg[0])().id)
                storage.save()
            else: # class name not in __classes
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
    
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

    def do_all(self, arg):
        """
        Prints all string representation of all instances 
        based on the class name
        """
        objects = storage.all()
        if arg:
            list_args = arg.split()
            if list_args[0] in HBNBCommand.__classes:
                class_objs = [str(v) for k, v in objects.items()
                           if list_args[0] == k.split('.')[0]]
                print(class_objs)
            else:
                print("** class doesn't exist **")
        else:
            allObjs = [str(v) for k, v in objects.items()]
            print(allObjs)

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

    def do_quit(self, arg):
        """Exit the interpreter"""
        return True
    
    def do_EOF(self, arg):
        """Exit on end-of-file input"""
        return True
    
    def emptyline(self):
        """Empty line"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()