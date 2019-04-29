#encoding=utf-8
"""
@version: 1
@author: Duke
@file:__init__.py.py
@time:2019/4/28 5:02 PM
"""


class CommandError(Exception):
    """
    """
    def __str__(self):
        return "command error"


class CommandModuleError(Exception):
    """
    """
    def __str__(self):
        return "command module error"


class CommandNotDefined(Exception):
    """
    """
    def __str__(self):
        return "command not defined"


class Command:
    def __init__(self, module, subcommond, *args):
        self.module = module
        self.subcommond = subcommond
        self.args = args
        self.cmd = None

    def register(self):
        try:
            if not hasattr(self.module, self.subcommond):
                raise CommandNotDefined
            else:
                self.cmd = getattr(self.module, self.subcommond)
        except Exception, e:
            raise e

    def execute(self):
        try:
            self.cmd.execute(*self.args)
        except Exception, e:
            print e
            modes = dir(self.module)
            lines = ["\t" + m + "\n" for m in modes if not m.startswith("_")]
            firstline = "args error\nargs:\n"
            print "".join([firstline, ] + lines)


def execute_commands(management, *args):
    if not hasattr(management, "commands"):
        raise CommandModuleError
    else:
        cmd_module = getattr(management, "commands")
    if len(args) < 2:
        raise CommandError
    subcommand = args[1]
    comm = Command(cmd_module, subcommand, *tuple(args[2:]))
    comm.register()
    comm.execute()
