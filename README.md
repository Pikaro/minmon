minmon 0.1.0a
======

Implement "minimize to tray" for applications that don't support it

There are numerous applications available that allow the user to minimize arbitrary programs to tray.

However, these are usually buggy in some respect or other, so minmon goes a different route. Instead of writing a complete framework, the program in question is simply started by a daemon that also generates a tray icon for it. The window manager's "close window" binding is replaced by a script that checks if the window was spawned by a minmon-controlled program. If so, it is minimized; if not, it is closed.

Single clicks on the tray icon hide all child windows, another click shows all hidden windows. Right-click allows the user to quit. It is recommended to bind a slightly modified "close window" binding to closing it without checking in order to unclutter their interface.

Note: As the windows are unmapped, the performance costs of having programs run in the background that way is extremely tiny. So this program is especially neat for usage with minimal window managers - I use it with Compiz standalone whose interface consists only of a tray.

Licensed under GPLv2, so have at it! Or mail me under git at d-reis.com. Criticism welcome, I know I'm using some ugly hacks.

David Reis, Mar 2014

======

USAGE

- Put .config/minmon in ~/.config (you can change the path of the script directory in minmonrc, but minmonrc needs to be under .config)
- Put minmon in your $PATH
- minmon start
  This launches the daemon; it opens a FIFO in /tmp to watch for incoming commands to execute.
  It is recommended to put this in your Autostart, .xinitrc, .compiz-session or what have you.
- Rebind your window manager's "close window" keys to ~/.config/minmon/minmon-close (i. e. your equivalent to Alt+F4)
- minmon launch xterm
- Try closing the xterm that opens as usual. It seems to close, but your tray will have an xterm icon. Click that, and it reappears; click it again, it disappears again. Right-click the icon to terminate the xterm.
- Try the same on a normal xterm - it doesn't get and icon and closes normally.
- Put things such as minmon launch firefox, minmon launch evolution, minmon launch xchat... in your autostart. If you hand it the -min parameter (minmon -min firefox) it will start minimized. (This works in like 95% of cases because sometimes, unexpected child windows will spawn first.)
- minmon stop and minmon restart are mainly for playing around with things and not really useful to the average user. They're not for interacting with children, only with the daemon! minmon-close, minmon-hide-all, minmon-state-visible etc. can be freely abused in order to produce scripted behavior.

======

HISTORY

current

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

- Better way to start minimized (is there a reliable "main window" identifier?)
- inotifywait alternative? Takes _too long_!

=====

BUGS

- -min sometimes doesn't work
- Firefox windows become unresponsive until unmapped and mapped sometimes. Why?
