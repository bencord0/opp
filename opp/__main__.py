# Copyright (C) 2016 Ben Cordero <bencord0@condi.me>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""Main entrypoint for the opp tool"""
import argparse
import logging
import sys

from stevedore import extension
from opp import LOG_LEVELS, parser, SUBCOMMANDS


def main():
    # Resolve subcommands from plugin entrypoints
    commands = extension.ExtensionManager(namespace='opp.commands')

    # For each entry_point in the 'opp.commands' namespace, add the callable
    # to the `SUBCOMMANDS` table. This causes their modules to be imported
    # and run code to add their own subparser args.
    def add_extension(ext):
        SUBCOMMANDS[ext.name] = ext.plugin
    commands.map(add_extension)

    # Avoid KeyError exceptions, make them useful
    SUBCOMMANDS[None] = lambda args: parser.print_help()

    # Now that subcommands have registered their subparsers, parse them all.
    args = parser.parse_args()

    # Top-level args
    logging.basicConfig(
        level=LOG_LEVELS[args.log_level],
        format='%(message)s')

    # Let subcommands use the args untouched.
    sys.exit(SUBCOMMANDS[args.subcommand](args))


if __name__ == '__main__':
    main()
