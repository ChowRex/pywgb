#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module

- Author: Rex Zhou <879582094@qq.com>
- Created Time: 2025/5/27 14:58
- Copyright: Copyright © 2025 Rex Zhou. All rights reserved.
"""
from os import getenv
from pathlib import Path
from random import randint
from urllib.parse import urlparse, unquote

from dotenv import load_dotenv
from pytest import raises

# pylint: disable=import-error
from src.pywgb.utils import ImageWeComGroupBot
from src.pywgb.utils import MarkdownWeComGroupBot
from src.pywgb.utils import NewsWeComGroupBot
from src.pywgb.utils import TextWeComGroupBot
from src.pywgb.utils import FileWeComGroupBot
from src.pywgb.utils import MediaUploader

env_file = Path(__file__).parent.with_name(".env")
load_dotenv(env_file, override=True)
VALID_KEY = getenv("VALID_KEY")
TEST_VALID_ARTICLES = [{
    "title":
        "中秋节礼品领取",
    "description":
        "今年中秋节公司有豪礼相送",
    "url":
        "www.qq.com",
    "picurl":
        "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png"
}]


def test_text_initial() -> None:
    """
    Test TextWeComGroupBot initialisation.
    :return:
    """
    valid_url = getenv("VALID_URL")
    print()
    print("Check valid key:", VALID_KEY)
    print("Check valid url:", valid_url)
    # Verify valid key and url
    bot = TextWeComGroupBot(VALID_KEY)
    assert urlparse(unquote(bot.doc)).fragment == bot._doc_key  # pylint: disable=protected-access
    assert VALID_KEY == bot.key
    assert f"TextWeComGroupBot({VALID_KEY})" == str(bot)
    assert valid_url.split("=")[-1] == TextWeComGroupBot(valid_url).key
    # Verify invalid key and url
    invalids = {
        getenv("INVALID_KEY"): "Invalid key format",
        getenv("INVALID_URL"): "Invalid key format",
        None: "Key is required",
    }
    for code, msg in invalids.items():
        with raises(ValueError) as exception_info:
            TextWeComGroupBot(code)
        assert msg in str(exception_info.value)


def test_markdown_initial() -> None:
    """
    Test MarkdownWeComGroupBot initialisation.
    :return:
    """
    # Verify valid key and url
    bot = MarkdownWeComGroupBot(VALID_KEY)
    assert urlparse(unquote(bot.doc)).fragment == bot._doc_key  # pylint: disable=protected-access
    assert VALID_KEY == bot.key


def test_image_initial() -> None:
    """
    Test ImageWeComGroupBot initialisation.
    :return:
    """
    # Verify valid key and url
    bot = ImageWeComGroupBot(VALID_KEY)
    assert urlparse(unquote(bot.doc)).fragment == bot._doc_key  # pylint: disable=protected-access
    assert VALID_KEY == bot.key


def test_news_initial() -> None:
    """
    Test NewsWeComGroupBot initialisation.
    :return:
    """
    # Verify valid key and url
    bot = NewsWeComGroupBot(VALID_KEY)
    assert urlparse(unquote(bot.doc)).fragment == bot._doc_key  # pylint: disable=protected-access
    assert VALID_KEY == bot.key


def test_file_initial() -> None:
    """
    Test NewsWeComGroupBot initialisation.
    :return:
    """
    # Verify valid key and url
    bot = FileWeComGroupBot(VALID_KEY)
    assert urlparse(unquote(bot.doc)).fragment == bot._doc_key  # pylint: disable=protected-access
    assert VALID_KEY == bot.key
    uploader = MediaUploader(VALID_KEY)
    assert urlparse(unquote(uploader.doc)).fragment == uploader._doc_key  # pylint: disable=protected-access
    assert VALID_KEY == uploader.key


def test_successful_send() -> None:
    """
    Test send message function
    :return:
    """
    bot = TextWeComGroupBot(getenv("VALID_KEY"))
    print(bot)
    result = bot.send(f"This is a test TEXT message: {randint(1, 100)}")
    print(result)
    assert result["errcode"] == 0
    bot = MarkdownWeComGroupBot(getenv("VALID_KEY"))
    print(bot)
    result = bot.send(f"## This is a test Markdown message: {randint(1, 100)}")
    print(result)
    assert result["errcode"] == 0
    bot = ImageWeComGroupBot(getenv("VALID_KEY"))
    print(bot)
    result = bot.send(file_path=Path(__file__).with_name("test.png"))
    print(result)
    assert result["errcode"] == 0
    bot = NewsWeComGroupBot(getenv("VALID_KEY"))
    print(bot)
    result = bot.send(articles=TEST_VALID_ARTICLES)
    print(result)
    assert result["errcode"] == 0
    bot = FileWeComGroupBot(getenv("VALID_KEY"))
    print(bot)
    result = bot.send(file_path=Path(__file__).with_name("test.png"))
    print(result)
    assert result["errcode"] == 0


def test_overheat() -> None:
    """
    Test overheat function
    :return:
    """
    bot = TextWeComGroupBot(getenv("VALID_KEY"))
    bot.send("This message was delayed by overheat", test="overheat")


def test_oversize_image() -> None:
    """
    Test oversize image send
    :return:
    """
    bot = ImageWeComGroupBot(getenv("VALID_KEY"))
    file = Path(__file__).with_name("test.png")
    with raises(TypeError) as exception_info:
        bot.send(file_path=file, test="wrong_format_image")
    assert "Just support image type: jpg or png" in str(exception_info.value)
    with raises(BufferError) as exception_info:
        bot.send(file_path=file, test="oversize_image")
    assert "The image is too large, more than 2M" in str(exception_info.value)


def test_request_exception() -> None:
    """
    Test request exception
    :return:
    """
    bot = TextWeComGroupBot(getenv("VALID_KEY"))
    with raises(ConnectionRefusedError) as exception_info:
        bot.send("This message WON'T be sent, cause by request error",
                 test="request_error")
    assert "Unable to initiate API request correctly" in str(
        exception_info.value)
    with raises(IOError) as exception_info:
        bot.send("This message WON'T be sent, cause by API error",
                 test="api_error")
    assert "Request failed, please refer to the official manual" in str(
        exception_info.value)


def test_wrong_articles() -> None:
    """
    Test wrong articles
    :return:
    """
    bot = NewsWeComGroupBot(getenv("VALID_KEY"))
    # Test empty articles
    with raises(ValueError) as exception_info:
        bot.send(articles=[])
    assert "No articles found" in str(exception_info.value)
    # Test oversize articles
    with raises(ValueError) as exception_info:
        articles = [TEST_VALID_ARTICLES for _ in range(9)]
        bot.send(articles=articles)
    assert "Too many articles." in str(exception_info.value)
    # Test data error and parameter error
    tests = {
        "article_data_error": "data is not a dict",
        "article_parameter_error": "lack required parameter",
    }
    for code, msg in tests.items():
        with raises(ValueError) as exception_info:
            bot.send(articles=TEST_VALID_ARTICLES, test=code)
        assert msg in str(exception_info.value)


def test_wrong_file() -> None:
    """
    Test wrong file
    :return:
    """
    bot = FileWeComGroupBot(getenv("VALID_KEY"))
    # Test empty articles
    with raises(ValueError) as exception_info:
        bot.send(file_path=None)
    assert "file_path must be provided" in str(exception_info.value)
