#!/usr/bin/python3

"""Entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNB class"""
    prompt = "(hbnb)"
    __classes = ["BaseModel"] # list of existing classes

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if arg:
            if arg in HBNBCommand.__classes:
                print(BaseModel().id)
                storage.save()
            else: # class name not in __classes
                print("class doesn't exist")
        else:
            print("class name missing")
    
    def do_show(self, arg):
        """Prints the string representation of an
        instance by its class name and id
        """
        if arg:
            objects = storage.all()
            list_args = arg.split()
            if list_args[0]:
                if list_args[0] in HBNBCommand.__classes:
                    if list_args[1]:
                        class_id = f"{list_args[0]}.{list_args[1]}"
                        if class_id in objects:
                            print(objects[class_id])
                        else: 
                            print("no instance found")
                    else:
                        print("instance id missing")
                else:
                    print("class doesn't exist")
            else:
                print("class name missing")
        else:
            print("class name missing")

    

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