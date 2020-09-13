#!/usr/bin/env python

"""Tests for `dummyTest` package."""


import unittest
from click.testing import CliRunner

from dummyTest import dummyTest
from dummyTest import cli


class TestDummytest(unittest.TestCase):
    """Tests for `dummyTest` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'dummyTest.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
