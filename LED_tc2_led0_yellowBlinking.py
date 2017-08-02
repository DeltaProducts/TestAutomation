
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
 Test case 2: Turn led[0] to Mode 15(Yellow_Blinking)
"""

user_mode = 15
DEBUG = True

from libonlp import led
from libonlp import get_leds
from time import sleep

ledobj = get_leds() #List of LEDs
count = len(ledobj) #Total number of LEDs
print "The count is : ",count

led.set_normal(ledobj[0]) #Set state to 1 and mode to GREEN

valid = led.set_mode(ledobj[0],user_mode)#Set the LED to user mode

if valid:
    sleep(3)
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
