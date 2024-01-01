Main
----
The active selection is a Python script that uses the ``CommandLine``
class to parse command line arguments, continuously monitors the
clipboard for new content, and then processes that content using the
``worker`` function.

The script is encapsulated in a function named ``main``. At the start of
this function, an instance of the ``CommandLine`` class is created and
the command line arguments are parsed using the ``parse_args`` method.
The parsed arguments are stored in the ``args`` variable.

The script then enters an infinite loop, which is designed to
continuously monitor the clipboard for new content. This is done using
the ``waitForNewPaste`` function from the ``pyperclip`` module, which
blocks until the content of the clipboard changes. The new clipboard
content is converted to a string and trailing whitespace is removed
using the ``rstrip`` method.

The new clipboard content is then printed to the console and passed to
the ``worker`` function along with the ``deck`` and ``language_code``
arguments from the command line. The ``worker`` function is run
asynchronously using the ``run`` function from the ``asyncio`` module.

The infinite loop is interrupted when a ``KeyboardInterrupt`` exception
is raised, which typically happens when the user presses Ctrl+C. When
this happens, the script prints “Exiting…” to the console and exits with
a status code of 0, indicating that the script has finished
successfully.

The ``main`` function is called when the script is run directly, as
indicated by the ``if __name__ == "__main__":`` line at the end of the
script. This line ensures that the ``main`` function is not called when
the script is imported as a module.
