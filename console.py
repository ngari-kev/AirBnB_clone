#!/usr/bin/python3
"""It is the main entry point of the command."""
import cmd


class HBNBCommand(cmd.Cmd):
    """This is the console's entry point."""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit the console."""
        return True

    def help_quit(self):
        """Shows help message for quit command."""
        print("Quit command Exits the console.")

    def do_EOF(self, arg):
        """Exits the console forcefully."""
        print("")
        return True

    def help_EOF(self):
        """Shows help message for EOF command."""
        print("EOF command exits the program")

    def emptyline(self):
        """Does nothing on empty input."""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
