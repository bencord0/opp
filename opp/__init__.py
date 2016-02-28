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
"""
OPP unified tool

`opp` is the standalone CLI entrypoint to access the development and
deployment tools provided by the Opps-enheimer suite.
"""
import logging
from argparse import ArgumentParser

__version__ = '1'

LOG_LEVELS = {
    'info': logging.INFO,
    'debug': logging.DEBUG,
}

parser = ArgumentParser(description='OPP development and deployment tools')
parser.add_argument('--log-level', default='info', choices=LOG_LEVELS.keys())
subcommands = parser.add_subparsers(title='subcommands', dest='subcommand')
SUBCOMMANDS = {}

__all__ = ['__version__', 'subcommands', 'SUBCOMMANDS']
