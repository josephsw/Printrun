#!/usr/bin/env python

# This file is part of the Printrun suite.
#
# Printrun is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Printrun is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Printrun.  If not, see <http://www.gnu.org/licenses/>.

import sys
import traceback
from printrun.pronsole import pronsole

def do_connect(l):
    return

def do_load(l):
    return

def do_print(l):
    return

def do_settemp(l):
    return

def do_home(l):
    return

def do_move(l):
    return

def do_extrude(l):
    return

def do_monitor(l):
    return

def do_sleep(l):
    return

def do_settempwait(l):
    return

# Convert command.txt strings into function calls
funcdict = {
    "connect": do_connect,
    "load": do_load,
    "print": do_print,
    "settemp": do_settemp,
    "home": do_home,
    "move": do_move,
    "extrude": do_extrude,
    "monitor": do_monitor,
    "sleep": do_sleep,
    "settempwait": do_settempwait,
}

if __name__ == "__main__":

    interp = pronsole()
    '''interp.parse_cmdline(sys.argv[1:])
    try:
        interp.cmdloop()'''

    # SYNTAX:
    # connect <port> <baud>
    # load <file>
    # print
    # settemp <temp/abs/off/pla>
    # home <x/y/z>
    # move <x/y/z> <val>
    # extrude <amount> <speed>
    # monitor <secs>

    # CUSTOM SYNTAX:
    # sleep <secs>
    # settempwait <temp/abs/off/pla>


    try:
        commandfile = open("commands.txt", "rU")

        # Read commands from file
        while (line = commandfile.readline().strip().lower()):
            cmdlist = line.split()
            if len(line) < 1:
                break

            line = line[len(cmdlist[0])+1:]

            funcdict[cmdlist[0]](line)
            
    except SystemExit:
        interp.p.disconnect()
    except:
        print _("Caught an exception, exiting:")
        traceback.print_exc()
        interp.p.disconnect()
