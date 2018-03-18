#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `python_greek_names` package."""

import pytest

from click.testing import CliRunner
from python_text_utils.generic import Generic
from python_greek_names.utils import (
    normalize_name,
    as_vocative,
    as_genitive
)
from python_greek_names import cli


# @pytest.fixture
# def response():
#     """Sample pytest fixture.

    # See more at: http://doc.pytest.org/en/latest/fixture.html
    # """
    # # import requests
    # # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


# def test_content(response):
#     """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


# def test_command_line_interface():
#     """Test the CLI."""
#     runner = CliRunner()
#     result = runner.invoke(cli.main)
#     assert result.exit_code == 0
#     assert 'python_greek_names.cli.main' in result.output
#     help_result = runner.invoke(cli.main, ['--help'])
#     assert help_result.exit_code == 0
#     assert '--help  Show this message and exit.' in help_result.output



def test_normalize():
    assert normalize_name('ΜΑΡΣΕΛ') == Generic.to_unicode('Μαρσελ')
    assert normalize_name('Μαρσέλ') == Generic.to_unicode('Μαρσέλ')
    assert normalize_name('ΜΑΡΣΈΛ') == Generic.to_unicode('Μαρσέλ')
    assert normalize_name('Μαρσελ', upper=True) == Generic.to_unicode('ΜΑΡΣΕΛ')
    assert normalize_name('Μαρσέλ', upper=True) == Generic.to_unicode('ΜΑΡΣΈΛ')

