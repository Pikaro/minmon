minmon 0.1.0a
======

**Implement "minimize to tray" for applications that don't support it**

Lots of applications don't support minimizing to tray, which is annoying if the user's desktop doesn't feature a task bar or similar means of control.

minmon introduces that capability using a very simple idea: Using xdotool, xprop, wmctrl and xwininfo, it associates windows with their process IDs and maps and unmaps those instead of closing them if the process was started through minmon.

This approach is less prone to bugs than other, more complicated routes, but only useful in limited circumstances. Most importantly, it does not work if the user closes a window through its window decorations, only if a key or mouse button is used to do so.

======

DEPENDENCIES

All dependencies should already be present on an average Linux desktop.

- xdotool
- xprop
- xwininfo
- wmctrl
- Gtk2

======

USAGE

- Put `minmon` and `minmon-systray.py` in your $PATH
- Rebind your window manager's "close window" key (i. e. your equivalent to Alt+F4) to `minmon windowclose`
- `minmon launch xterm`
- The xterm is now bound to a newly created systray icon, which can be used to hide, unhide and close it.
- The key bound to `minmon windowclose` will hide windows opened through minmon launch, but still close ordinary applications normally.
- If you hand minmon the -min parameter (minmon -min firefox) it will start minimized. (This works in like 95% of cases because sometimes, unexpected child windows will spawn first.)

======

HISTORY

0.3.0

- got rid of daemon architecture, scratch rewrite, everything's much cleaner and nicer now

0.2.0

- eliminated 'bug' that forced double clicks to hide windows (caused by offscreen 1x1 windows...?)
- checking for TMP directory now, inotifywait takes too long to set up watches

0.2.0a

- cleaned up daemon
- suppressing all kinds of annoying "error" messages now
- popup windows will always close normally
- eliminated "sleep" loops, replaced with inotifywait
- moved cleanup functions to minmon script
- files live under .config now - crude, but meh

0.1.0a

- First upload to github

======

TODO

- Better way to start minimized

=====

BUGS

none known
