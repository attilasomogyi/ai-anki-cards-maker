Worker
------

The active selection is the main entry point of a Python application.
This script is designed to be run from the command line and uses several
imported modules and functions to perform its tasks.

The script begins by importing necessary modules and functions.
``CommandLine`` is a custom class from the ``ankicardmaker.commandline``
module that handles command line argument parsing. ``worker`` is a
function from the ``ankicardmaker.worker`` module that processes the
content from the clipboard. ``paste`` and ``waitForNewPaste`` are
functions from the ``pyperclip`` module that interact with the system
clipboard. ``run`` is a function from the ``asyncio`` module that runs a
coroutine.

The ``main`` function is defined next. It begins by creating an instance
of the ``CommandLine`` class and calling its ``parse_args`` method to
parse command line arguments. These arguments are stored in the ``args``
variable.

The function then enters a ``try`` block to handle potential exceptions.
Inside this block, an infinite ``while`` loop is started. This loop
waits for new content to be added to the clipboard. When new content is
detected, it is passed to the ``worker`` function along with the name of
the Anki deck and the language code to add cards to.

If a ``KeyboardInterrupt`` exception is raised (which happens when the
user presses Ctrl+C), the loop is broken, a message is printed to the
console, and the program exits.

Finally, the script checks if it is being run as the main module (as
opposed to being imported by another script). If it is, it calls the
``main`` function to start the application.
