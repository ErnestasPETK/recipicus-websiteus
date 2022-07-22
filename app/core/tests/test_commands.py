"""
    Test the commands module.
"""

from unittest.mock import patch  # in order to mock behavior of the database
from psycopg2 import (
    OperationalError as Psycopg2Error,
)  # one of the possibilities of the errors

from django.core.management import (
    call_command,
)  # noqa allows to call command by the name
from django.db.utils import (
    OperationalError,
)  # noqa one of the possibilities of the errors
from django.test import SimpleTestCase  # allows to do unit test


@patch("core.management.commands.wait_for_db.Command.check")
class CommandTests(SimpleTestCase):
    """
    Tests commands
    """

    def test_wait_for_db_ready(self, patched_check):
        """
        Test waiting for the database when the database is already ready.
        """
        patched_check.return_value = True
        call_command("wait_for_db")
        patched_check.assert_called_once_with(databases=["default"])

    @patch("time.sleep")
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """
        Test waiting for the database when getting OperationalError.
        Applies to patch commands from the inside out:
        1. patch time.sleep
        2. patch core.management.commands.wait_for_db.Command.check
        """

        patched_check.side_effect = (
            [Psycopg2Error] * 2 + [OperationalError] * 3 + [True]
        )
        """
        The side_effect mocking command will call the database 2 + 3 + 1 times.
        The first 2 calls will check for the Psycopg2Error.
        The next 3 calls will check for the OperationalError.
        The last call will return True.
        """

        call_command("wait_for_db")  # this will call "wait_for_db" command
        self.assertEqual(
            patched_check.call_count, 6
        )  # this will check if the command was called 6 times
        patched_check.assert_called_with(
            databases=["default"]
        )  # since it will call multiple times "assert_called_with"
