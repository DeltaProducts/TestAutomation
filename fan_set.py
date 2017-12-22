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
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--rpm", type = int, default=0, help="set fan rpm")
parser.add_argument("--fan_percent", type = int , default=0, help="set fan rpm percent")
args = parser.parse_args()
if args.rpm == 0 and args.fan_percent == 0:
    print("No value for parameter, Use -h for usage")
else:
    from libonlp import *

    if args.rpm != 0:
        if verifyRPM(user_rpm=args.rpm) :
            print "verifyRPM Test case passed"
        else:
            print "verifyRPM Test case failed"

    if args.fan_percent != 0:
        if verifyPercent(percent=args.fan_percent) :
            print "verifyPercent Test case passed"
        else:
            print "verifyPercent Test case failed"

