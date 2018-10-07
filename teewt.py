#!/usr/bin/env python3

import curses

stdscr = curses.initscr()

curses.noecho()

curses.cbreak()

stdscr.keypad(False)
curses.echo()

curses.endwin()
