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
 Test case 4: Set rpm to 70
"""

user_percent = 70
DEBUG = True #Static constant used for debugging

from libonlp import fan
from libonlp import get_fans
from time import sleep

fanobj = get_fans() #List of fans and their statuses
count = len(fanobj) # Count the number of fans
print "The count is: ",count

for y in range(count):
    fan.set_normal_percent(fanobj[y]) #Set percentage to 47
sleep(10)

percentlist = [] #List to store fans' speed in percentage
for x in range(count):
    percentNew = fan.set_percent(fanobj[x],user_percent)
    if(percentNew != None):
        percentlist.append(percentNew)

if DEBUG:
    print "After setting credentials"
    print percentlist

    # Pass percentage = 5 %
    user_percent_lower = user_percent - 5
    user_percent_higher = user_percent + 5

    fail = 0
    pass1 = 0

    for i in range(len(percentlist)):
        if user_percent_lower <= percentlist[i] <= user_percent_higher:
            pass1 = pass1 + 1
        else:
            fail = fail + 1

    if fail != 0:
        final = "fail"
        print "test case failed"
    elif (len(percentlist) == 0):
        print "None of the fans have SET_PERCENT capability "
    else:
        final = "pass"
        print "Test case passed"

for x in range(count):
    fan.set_normal_percent(fanobj[x])
