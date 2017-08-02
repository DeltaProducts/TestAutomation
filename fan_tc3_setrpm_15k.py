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
Test case 3: Set rpm to 15000
"""
DEBUG = True #Static constant used for debugging
user_rpm = 15000

from libonlp import fan
from libonlp import get_fans
from time import sleep

fanobj = get_fans() #List fans and their statuses
count = len(fanobj) # Count the number of fans
print "The count is: ",count

for y in range(count):
    fan.set_normal_speed(fanobj[y]) #Set speed to 8000 rpm
sleep(5)


rpmlist = [] #list to store all the fans' rpm
for x in range(count):
    rpmold = fan.get_rpm(fanobj[x]) #rpm before setting to user_rpm
    rpmNew = fan.set_rpm(fanobj[x],user_rpm)
    if(rpmNew != None):
        rpmlist.append(rpmNew)

if DEBUG:
    print "After setting credentials"
    print rpmlist

    # Pass percentage
    user_rpm_lower = user_rpm - 500
    user_rpm_higher = user_rpm + 500

    fail = 0
    pass1 = 0

    for i in range(len(rpmlist)):
        if user_rpm_lower <= rpmlist[i] <= user_rpm_higher:
            pass1 = pass1 + 1
        else:
            fail = fail + 1

    if fail != 0:
        final = "fail"
        print "Test case failed"
    else:
        final = "pass"
        print "Test case passed"

for x in range(count):
    fan.set_normal_speed(fanobj[x])
