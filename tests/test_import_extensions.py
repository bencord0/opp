import importlib
import pkg_resources
import unittest


class TestImportExtensions(unittest.TestCase):
    def test_import_extensions(self):
        '''
            Does a basic import test of extensions listed in 'opp.commands'.
        '''
        opp_commands = pkg_resources.get_entry_map('opp')['opp.commands']
        for command in opp_commands.values():
            command.load()
