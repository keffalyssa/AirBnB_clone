#!/usr/bin/python3
"""
This module defines the HBNBCommand interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """Overriding emptyline to not execute previous command."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
