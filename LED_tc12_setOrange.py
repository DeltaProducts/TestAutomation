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
Test case 12: Turn led[0] to Mode 12(Orange)
"""
user_mode = 12
DEBUG = True

from libonlp import led
from libonlp import get_leds
from time import sleep

ledobj = get_leds()  #Gets the list of LEDs
count = len(ledobj)  #Total number of LEDs
print "The count is : ",count

if count < 1:
    print("Skip this test case")
    exit()

led.set_normal(ledobj[0]) #Set state to 1 and mode to GREEN

valid = led.set_mode(ledobj[0],user_mode) #Set mode to user_mode
if valid:
    currentState = led.get_mode(ledobj[0])
else:
    DEBUG = False
    print "Test case passed"

if DEBUG:
    if currentState == user_mode:
        print "Test case passed"

    elif currentState == 'None':
        print "Check the LED capabilities"

    else:
        print "Test case failed"
