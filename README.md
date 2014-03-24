minmon
======

Implement "minimize to tray" for applications that don't support it

There are numerous applications available that allow the user to minimize arbitrary programs to tray.

However, these are usually buggy in some respect or other, so minmon goes a different route. Instead of writing a complete framework, the program in question is simply started by a daemon that also generates a tray icon for it. The window manager's "close window" binding is replaced by a script that checks if the window was spawned by a minmon-controlled program. If so, it is minimized; if not, it is closed.

Single clicks on the tray icon hide all child windows, another click shows all hidden windows. Right-click allows the user to quit. It is recommended to bind a slightly modified "close window" binding to closing it without checking in order to unclutter their interface.

Note: As the windows are unmapped, the performance costs of having programs run in the background that way is extremely tiny. So this program is especially neat for usage with minimal window managers - I use it with Compiz standalone whose interface consists only of a tray.

Licensed under GPLv2, so have at it! Or mail me under git at d-reis.com. Criticism welcome, I know I'm using some ugly hacks.

David Reis, Mar 2014
