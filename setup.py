#!/usr/bin/env python
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
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

from opp import __version__


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['tests']
        self.test_suite = True

    def run_tests(self):
        import pytest
        sys.exit(pytest.main(self.test_args))


setup(
    name='opp',
    version=__version__,
    author='Ben Cordero',
    author_email='bencord0@condi.me',
    packages=[
        'opp',
        'opp.commands',
    ],
    install_requires=[
        'stevedore',
    ],
    tests_require=[
        'pytest',
    ],
    cmdclass={'test': PyTest},
    provides=[
        'opp.commands',
    ],
    entry_points={
        'opp.commands': [
            'build = opp.commands.build:build',
        ],
        'console_scripts': [
            'opp = opp.__main__:main',
        ],
    },
    zip_safe=False,
)
