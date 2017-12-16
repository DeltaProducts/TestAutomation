"""
 *
 *           Copyright 2017 (C) Delta Networks, Inc.
 *
 * Licensed under the Eclipse Public License, Version 1.0 (the
 * "License"); you may not use this file except in compliance
 * with the License. You may obtain a copy of the License at
 *
 *        http://www.eclipse.org/legal/epl-v10.html
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
 * either express or implied. See the License for the specific
 * language governing permissions and limitations under the
 * License.
 *
Test case 1: Set rpm to 6000
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--rpm", help="set fan rpm")
args = parser.parse_args()
assert (args.rpm != None),"No value for parameter rpm"

test_rpm = int(args.rpm)
from libonlp import verifyRPM

if verifyRPM(user_rpm=test_rpm) :
    final = "pass"
    print "Test case passed"
else:
    final = "fail"
    print "Test case failed"


