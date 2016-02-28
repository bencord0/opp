#!/bin/bash
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

TOP_DIR="$(dirname $(readlink -f "${BASH_SOURCE[0]}"))"
INPUT_DIR="${INPUT_DIR:-${TOP_DIR}/INPUT}"
OUTPUT_DIR="${OUTPUT_DIR:-${TOP_DIR}/OUTPUT}"

rm -rf "${OUTPUT_DIR}"
mkdir -p "${INPUT_DIR}"
mkdir -p "${OUTPUT_DIR}"

if [ ! -d venv ]; then
	pyvenv venv
fi

source venv/bin/activate
pip install -U pex
python setup.py test
pex -vv -o "${OUTPUT_DIR}/opp.pex" --no-wheel --disable-cache . -m opp
