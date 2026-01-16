SmartBot
========

.. automodule:: pywgb.bot._smart
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

SmartBot Class
--------------

.. autoclass:: pywgb.bot._smart.SmartBot
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

   .. automethod:: send
   .. automethod:: upload

Markdown Features
-----------------

The SmartBot provides access to Markdown features through the ``markdown_feature`` proxy:

.. code-block:: python

   from pywgb import SmartBot
   
   bot = SmartBot("your-key")
   
   # Markdown v1 colored text
   green_text = bot.markdown_feature.green("Success")
   gray_text = bot.markdown_feature.gray("Info")
   orange_text = bot.markdown_feature.orange("Warning")
   
   # Markdown v2 table
   data = [["Name", "Value"], ["Item1", "100"]]
   table = bot.markdown_feature.list2table(data)
