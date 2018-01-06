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
Test case 9: Turn led[3] to state 0(OFF)
"""

user_state = 0
DEBUG = True

from libonlp import led
from libonlp import get_leds
from time import sleep


ledobj = get_leds()
count = len(ledobj)
print "The count is : ",count

if count < 4:
    print("Skip this test case")
    exit()

led.set_normal(ledobj[3]) #Set state to 1 and mode to GREEN

valid = led.set_state(ledobj[3],user_state) #Set state to user state

if valid:
    currentState = led.get_mode(ledobj[3])
else:
    DEBUG = False
    print "Test case passed"

if DEBUG:
    if currentState == user_state:
        print "Test case passed"

    elif currentState == 'None':
        print "Check the LED capabilities"

    else:
        print "Test case failed"

led.set_normal(ledobj[3]) #Set state to 1 and mode to GREEN
