.. _anki_card_maker.py:

anki_card_maker.py
==================

This module contains the AnkiCardMaker class, which is used to create Anki cards.

Classes
-------

.. class:: AnkiCardMaker

   This class is used to create Anki cards.

   .. attribute:: api_key

      The API key for the Anki application.

   .. attribute:: url

      The URL for the Anki application.

   .. method:: __init__()

      The constructor for the AnkiCardMaker class. It initializes the api_key and url attributes.

   .. method:: request(action, **params)

      Creates a request for the Anki application.

      :param action: The action to be performed.
      :type action: str
      :param params: The parameters for the action.
      :type params: dict
      :return: The request.
      :rtype: dict

   .. method:: invoke(action, **params)

      Invokes an action on the Anki application.

      :param action: The action to be performed.
      :type action: str
      :param params: The parameters for the action.
      :type params: dict
      :return: The result of the action.
      :rtype: dict

   .. method:: make_note(deck_name, front, back, allow_duplicates=False)

      Creates a note for an Anki card.

      :param deck_name: The name of the deck.
      :type deck_name: str
      :param front: The front of the card.
      :type front: str
      :param back: The back of the card.
      :type back: str
      :param allow_duplicates: Whether to allow duplicate cards.
      :type allow_duplicates: bool, optional
      :return: The note.
      :rtype: dict