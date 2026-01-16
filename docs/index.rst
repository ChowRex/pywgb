pywgb - Wecom Group Bot Python API
====================================

.. image:: https://codecov.io/gh/ChowRex/pywgb/graph/badge.svg?token=1SDIUB46RU
   :target: https://codecov.io/gh/ChowRex/pywgb
   :alt: Code Coverage

.. image:: https://img.shields.io/pypi/v/pywgb
   :target: https://pypi.org/project/pywgb/
   :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/pywgb
   :target: https://pypi.org/project/pywgb/
   :alt: Python Versions

A comprehensive Python API for Wecom (WeChat Work) Group Bots, supporting multiple
message types with automatic type detection and intelligent routing.

Features
--------

* 🤖 **Smart Bot**: Automatic message type detection
* 📝 **Multiple Message Types**: Text, Markdown (v1 & v2), Images, Files, Voice, News, Template Cards
* 🎨 **Rich Formatting**: Colored text, tables, lists, code blocks
* 🔒 **Rate Limiting**: Built-in overheat detection (20 msg/min)
* ✅ **Type Hints**: Full type annotation support
* 🧪 **Well Tested**: High test coverage with pytest
* 📚 **Comprehensive Docs**: Sphinx documentation with examples

Quick Start
-----------

Installation
~~~~~~~~~~~~

.. code-block:: bash

   # Basic installation
   pip install pywgb
   
   # Full installation (includes voice message support)
   pip install "pywgb[all]"

Basic Usage
~~~~~~~~~~~

.. code-block:: python

   from pywgb import SmartBot
   
   # Initialize bot with webhook key
   bot = SmartBot("your-webhook-key-or-url")
   
   # Send text message
   bot.send("Hello, World!")
   
   # Send markdown message
   bot.send("# Title\n**Bold text**")
   
   # Send image
   bot.send(file_path="screenshot.png")
   
   # Send with mentions
   bot.send("Important!", mentioned_list=["@all"])

Message Types
-------------

Text Messages
~~~~~~~~~~~~~

.. code-block:: python

   from pywgb.bot import TextBot
   
   bot = TextBot("your-key")
   bot.send("Plain text message")
   
   # With mentions
   bot.send(
       "Team meeting at 3 PM",
       mentioned_list=["user123"],
       mentioned_mobile_list=["13800138000"]
   )

Markdown Messages
~~~~~~~~~~~~~~~~~

**Markdown v1** (with colored text):

.. code-block:: python

   from pywgb.bot import MarkdownBot
   
   bot = MarkdownBot("your-key")
   
   # Colored text
   msg = f"Status: {MarkdownBot.green('Online')}"
   bot.send(msg)

**Markdown v2** (with tables):

.. code-block:: python

   from pywgb.bot import MarkdownBotV2
   
   bot = MarkdownBotV2("your-key")
   
   # Create table
   data = [
       ["Name", "Age", "Score"],
       ["Alice", "25", "95"],
       ["Bob", "30", "87"]
   ]
   table = MarkdownBotV2.list2table(data)
   bot.send(f"# Report\n{table}")

Image, Voice, and File Messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from pywgb.bot import ImageBot, VoiceBot, FileBot
   
   # Image (PNG/JPG, max 2MB)
   ImageBot("your-key").send(file_path="chart.png")
   
   # Voice (AMR format, max 2MB, max 60s)
   VoiceBot("your-key").send(file_path="audio.amr")
   
   # File (5B < size < 20MB)
   FileBot("your-key").send(file_path="document.pdf")

News Articles
~~~~~~~~~~~~~

.. code-block:: python

   from pywgb.bot import NewsBot
   
   bot = NewsBot("your-key")
   bot.send(articles=[
       {
           "title": "Breaking News",
           "url": "https://example.com",
           "description": "Important update",
           "picurl": "https://example.com/image.jpg"
       }
   ])

Template Cards
~~~~~~~~~~~~~~

.. code-block:: python

   from pywgb.bot import TextCardBot
   
   bot = TextCardBot("your-key")
   bot.send(
       main_title={"title": "Notification"},
       sub_title_text="Details here",
       card_action={"type": 1, "url": "https://example.com"}
   )

API Reference
-------------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api/modules
   api/smartbot
   api/bots
   api/decorators

Core Classes
~~~~~~~~~~~~

.. autosummary::
   :toctree: api/generated
   :recursive:

   pywgb.SmartBot
   pywgb.bot.TextBot
   pywgb.bot.MarkdownBot
   pywgb.bot.MarkdownBotV2
   pywgb.bot.ImageBot
   pywgb.bot.VoiceBot
   pywgb.bot.FileBot
   pywgb.bot.NewsBot
   pywgb.bot.TextCardBot
   pywgb.bot.NewsCardBot

Rate Limiting
-------------

Wecom enforces a rate limit of **20 messages per minute** per bot. The library
automatically handles this with the ``detect_overheat`` decorator:

.. code-block:: python

   bot = SmartBot("your-key")
   
   # Send 21 messages rapidly
   for i in range(21):
       bot.send(f"Message {i}")
   
   # Output after 20th message:
   # Cooling down: 60s ... 59s ... 58s ...
   # Automatically retries after cooldown

Best Practices
--------------

1. **Use SmartBot for convenience**: Let it auto-detect message types
2. **Use specific bots for performance**: When you know the exact type
3. **Handle rate limits**: Be aware of the 20 msg/min limit
4. **Validate file sizes**: Check limits before sending
5. **Use type hints**: Leverage IDE autocomplete and type checking

Limitations
-----------

* **Rate Limit**: 20 messages per minute per bot
* **Text/Markdown**: Max 2048/4096 bytes (UTF-8)
* **Images**: PNG/JPG only, max 2MB
* **Voice**: AMR format only, max 2MB, max 60 seconds
* **Files**: 5B to 20MB
* **News**: Max 8 articles per message

Contributing
------------

Contributions are welcome! Please visit the `GitHub repository <https://github.com/ChowRex/pywgb>`_.

License
-------

MIT License - see LICENSE file for details.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
