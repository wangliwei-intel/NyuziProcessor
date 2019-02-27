#!/usr/bin/env python3
#
# Copyright 2011-2015 Jeff Bush
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

'''
Test load_sync/store_sync instructions by having four threads update
variables round-robin.
'''

import sys

sys.path.insert(0, '../..')
import test_harness


@test_harness.test(['verilator'])
def multicore(_, target):
    test_harness.build_program(['multicore.S'])
    result = test_harness.run_program(target)
    if 'ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`' not in result:
        raise test_harness.TestException('Output mismatch:\n' + result)

test_harness.execute_tests()
