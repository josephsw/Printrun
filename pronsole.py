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
#
# Modified by Joseph Wang (josephsw) for Meta 3D Sculpting.
# http://github.com/josephsw/Scripted-Pronsole

import sys
import traceback
from printrun.pronsole import pronsole
import time

def do_connect(l):
    interp.log(_("[PS] Connecting to printer at %s" % l))
    interp.do_connect(l)

def do_load(l):
    interp.log(_("[PS] Loading GCode file at %s" % l))
    interp.do_load(l)

def do_print(l):
    interp.log(_("[PS] *** Starting print ***"))
    interp.do_print(l)

def do_settemp(l):
    interp.log(_("[PS] Setting temperature at %s" % l))
    interp.do_settemp(l)

def do_home(l):
    interp.log(_("[PS] Moving home on %s" % l))
    interp.do_home(l)

def do_move(l):
    interp.log(_("[PS] Moving to %s" % l))
    interp.do_move(l)

def do_extrude(l):
    interp.log(_("[PS] Extruding (mm, speed): %s" % l))
    interp.do_extrude(l)

def do_monitor(l):
    interp.log(_("[PS] Monitoring print every %s seconds" % l))
    interp.do_monitor(l)

def do_sleep(l):
    interp.log(_("[PS] Waiting for %s seconds" % l))
    time.sleep(int(l))

def do_settempwait(l):
    interp.log(_("[PS] Setting temperature at %s, waiting until temperature reached" % l))
    interp.do_settemp(l)
    while(interp.p.lastreadtemp < int(l) and interp.p.online):
        #print "TEMP IS: " + str(interp.p.lastreadtemp)
        interp.log(_("[PS] Current temp: " + str(interp.p.lastreadtemp)))
        interp.do_gettemp("")
        time.sleep(5)

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
    #interp.parse_cmdline(sys.argv[1:])

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
        line = commandfile.readline().strip().lower()
        while (line):
            cmdlist = line.split()
            if len(line) < 1:
                break

            line = line[len(cmdlist[0])+1:]

            funcdict[cmdlist[0]](line)
            line = commandfile.readline().strip().lower()
        interp.cmdloop()

    except SystemExit:
        interp.p.disconnect()
    except:
        print _("Caught an exception, exiting:")
        traceback.print_exc()
        interp.p.disconnect()
