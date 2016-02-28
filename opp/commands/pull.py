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
from posixpath import join
import subprocess

from opp import subcommands

logger = logging.getLogger(__name__)
pull_parser = subcommands.add_parser('pull')
pull_parser.add_argument('repository',
                         help='<vendor>/<repo> path. e.g.: bencord0/opp')
pull_parser.add_argument('--mirror', '-m',
                         default='https://github.com',
                         help='Base url to pull from')
pull_parser.add_argument('--path', default=None,
                         help='directory to clone the repostoy too')

def pull(args):
    logger.info('pull: {}'.format(args))

    path = args.path or args.repository
    if os.path.exists(path):
        os.chdir(path)
        subprocess.check_call(['git', 'pull'])

    else:
        clone_command = [
            'git', 'clone', join(args.mirror, args.repository), path]
        subprocess.check_call(clone_command)
