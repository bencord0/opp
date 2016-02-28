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
import logging
import os
import subprocess

from opp import subcommands

logger = logging.getLogger(__name__)
build_parser = subcommands.add_parser('build')
build_parser.add_argument('repository',
                          help='<vendor>/<repo> path. e.g. bencord0/opp')


def build(args):
    logger.info('build: {}'.format(args))

    path = os.path.abspath(args.repository)

    build_script = 'BUILD'
    build_script_path = os.path.join(path, build_script)

    subprocess.check_call([build_script_path], cwd=path)
