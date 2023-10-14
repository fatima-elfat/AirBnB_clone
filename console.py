#!/usr/bin/python3

"""Entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter"""

    prompt = "(hbnb)"
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