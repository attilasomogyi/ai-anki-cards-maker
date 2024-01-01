Commandline
-----------

The active selection is a Python class named ``CommandLine`` that is
used to parse command line arguments for a program. This class is part
of a larger project that appears to be a command-line tool for creating
Anki cards.

The ``CommandLine`` class uses the ``argparse`` module from Python’s
standard library to parse command line arguments. The ``argparse``
module makes it easy to write user-friendly command-line interfaces. The
module parses command-line arguments and generates usage messages and
errors.

In the ``__init__`` method of the ``CommandLine`` class, an
``ArgumentParser`` object is created with a description of the program.
Then, several arguments are added to the parser:

-  A ``--version`` argument that displays the version of the program and
   then exits.
-  A ``--deck`` argument that specifies the name of the deck. This
   argument is required, as indicated by ``required=True``.
-  A ``--language`` argument that specifies the language code. The
   choices for this argument are fetched from the ``Language`` class,
   which is imported from the ``ankicardmaker.languages`` module. This
   class appears to load a list of languages from a JSON file and
   provides methods to get language codes and names.

The ``parse_args`` method of the ``CommandLine`` class calls the
``parse_args`` method of the ``ArgumentParser`` object, which parses the
command line arguments and returns them as a namespace object. If any
arguments are unrecognized, an error message is displayed and the
program exits.
