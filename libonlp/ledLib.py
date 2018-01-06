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
 Description: ONLP LED module
"""

import ctypes
from time import sleep
from sysLib import *
ledlib = ctypes.CDLL(LIB_ONLP)

#onlp_led_status
class onlp_led_status_t(ctypes.Structure):
    ONLP_LED_STATUS_PRESENT = (1 << 0)
    ONLP_LED_STATUS_FAILED = (1 << 1)
    ONLP_LED_STATUS_ON = (1 << 2)

#onlp_led_caps
class onlp_led_caps_t(ctypes.Structure):
    ONLP_LED_CAPS_ON_OFF = (1 << 0)
    ONLP_LED_CAPS_CHAR = (1 << 1)
    ONLP_LED_CAPS_RED = (1 << 10)
    ONLP_LED_CAPS_RED_BLINKING = (1 << 11)
    ONLP_LED_CAPS_ORANGE = (1 << 12)
    ONLP_LED_CAPS_ORANGE_BLINKING = (1 << 13)
    ONLP_LED_CAPS_YELLOW = (1 << 14)
    ONLP_LED_CAPS_YELLOW_BLINKING = (1 << 15)
    ONLP_LED_CAPS_GREEN = (1 << 16)
    ONLP_LED_CAPS_GREEN_BLINKING = (1 << 17)
    ONLP_LED_CAPS_BLUE = (1 << 18)
    ONLP_LED_CAPS_BLUE_BLINKING = (1 << 19)
    ONLP_LED_CAPS_PURPLE = (1 << 20)
    ONLP_LED_CAPS_PURPLE_BLINKING = (1 << 21)
    ONLP_LED_CAPS_AUTO = (1 << 22)
    ONLP_LED_CAPS_AUTO_BLINKING = (1 << 23)

#onlp_led_mode
class onlp_led_mode_t(ctypes.Structure):
    ONLP_LED_MODE_OFF = 0
    ONLP_LED_MODE_ON = 1
    ONLP_LED_MODE_BLINKING = 3
    ONLP_LED_MODE_RED = 10
    ONLP_LED_MODE_RED_BLINKING = 11
    ONLP_LED_MODE_ORANGE = 12
    ONLP_LED_MODE_ORANGE_BLINKING = 13
    ONLP_LED_MODE_YELLOW = 14
    ONLP_LED_MODE_YELLOW_BLINKING = 15
    ONLP_LED_MODE_GREEN = 16
    ONLP_LED_MODE_GREEN_BLINKING = 17
    ONLP_LED_MODE_BLUE = 18
    ONLP_LED_MODE_BLUE_BLINKING = 19
    ONLP_LED_MODE_PURPLE = 20
    ONLP_LED_MODE_PURPLE_BLINKING = 21
    ONLP_LED_MODE_AUTO = 22
    ONLP_LED_MODE_AUTO_BLINKING = 23

class onlp_oid_hdr_t(ctypes.Structure):
    _fields_ = [("id", ctypes.c_uint),
               ("description", ctypes.c_char * 128),
               ("poid", ctypes.c_uint),
               ("coids", ctypes.c_uint * 32)]

class onlp_led_info_t(ctypes.Structure):
    _fields_ = [("hdr", onlp_oid_hdr_t),
               ("status", ctypes.c_uint),
               ("caps", ctypes.c_uint),
               ("mode", ctypes.c_int),
               ("character", ctypes.c_int)]

ledlist = [] #list to store all the objects of LED
"""
Initialize the led
"""
ledlib.onlp_led_init.restype = ctypes.c_int

"""
Set the mode of LED
"""
ledlib.onlp_led_mode_set.argtypes = [ctypes.c_uint,ctypes.c_int]
ledlib.onlp_led_mode_set.restype = ctypes.c_int

"""
Set the state of LED
Parameter 1:id
Parameter 2: ON/OFF(1 for ON and 0 for OFF)
"""
ledlib.onlp_led_set.argtypes = [ctypes.c_uint,ctypes.c_int]
ledlib.onlp_led_set.restype = ctypes.c_int


class led:
    CAPABILITY = ['ONLP_LED_CAPS_ON_OFF',
                  'ONLP_LED_CAPS_CHAR',
                  '','','','','','',
                  '','',
                  'ONLP_LED_CAPS_RED',
                  'ONLP_LED_CAPS_RED_BLINKING',
                  'ONLP_LED_CAPS_ORANGE',
                  'ONLP_LED_CAPS_ORANGE_BLINKING',
                  'ONLP_LED_CAPS_YELLOW',
                  'ONLP_LED_CAPS_YELLOW_BLINKING',
                  'ONLP_LED_CAPS_GREEN',
                  'ONLP_LED_CAPS_GREEN_BLINKING',
                  'ONLP_LED_CAPS_BLUE',
                  'ONLP_LED_CAPS_BLUE_BLINKING',
                  'ONLP_LED_CAPS_PURPLE',
                  'ONLP_LED_CAPS_PURPLE_BLINKING',
                  'ONLP_LED_CAPS_AUTO',
                  'ONLP_LED_CAPS_AUTO_BLINKING']
    STATE = ['OFF','ON']
    def __init__(self,id):
        ledlib.onlp_led_init()
        onlp_led = onlp_led_info_t()
        ledlib.onlp_led_info_get(led_oid, ctypes.byref(onlp_led))
        self.led_oid = id
        self.hdr = onlp_led.hdr
        self.status = onlp_led.status
        self.caps = onlp_led.caps
        self.mode = onlp_led.mode
        self.character = onlp_led.character
        self.caps_list = self.get_caps()

    """
    Set the mode(color) of LED
    Parameter 1: LED object
    Parameter 2: user_mode
    """
    def set_mode(self,user_mode):
        print "\nSetting mode to ",user_mode
        if(self.caps & (1 << user_mode)):
            ledlib.onlp_led_set(self.led_oid,1)
            ledlib.onlp_led_mode_set(self.led_oid,user_mode)
            return True
        else:
            print "LED not capable of setting mode to ",user_mode
            print self.caps_list
            return False

    """
    Set the state(ON/OFF) of LED
    Parameter 1: LED object
    Parameter 2: user_state(0 for OFF/1 for ON)
    """
    def set_state(self,user_state):
        print("Setting state for LED %s , oid %s to %s" %
              (self.hdr.description, self.led_oid,self.STATE[user_state]))
        if(self.caps & (1<<0)):
            ledlib.onlp_led_set(self.led_oid,user_state)
            return True
        else:
            print "This LED is not capable of turning ON and OFF."
            print self.caps_list
            return False

    """
    Set the char of LED
    Parameter 1: LED object
    Parameter 2: user_char
    """
    def set_char(self,user_char):
        ledlib.onlp_led_char_set(self.led_oid,user_char)
        print "Setting char to ",user_char

    """
    Get the capabiities of a particular LED
    Parameter: LED object
    """
    def get_caps(self):
        index = []
        x = int(bin(self.caps)[2:])
        y = len(str(x))

        for i in range(y):
            if((x & (1 << i))!=0):
                index.append(self.CAPABILITY[i])
        return index

    """
    Get the mode of a particular LED
    Parameter :LED object
    Return value: Current mode of the LED
    """
    def get_mode(self):
        onlp_led = onlp_led_info_t()
        ledlib.onlp_led_info_get(self.led_oid, ctypes.byref(onlp_led))
        print "Color Mode :",self.CAPABILITY[onlp_led.mode]
        return onlp_led.mode

    """
    Get the state of a particular LED
    Parameter: LED object
    Return value: Current state of the LED(0 for OFF/1 for ON)
    """
    def get_state(self):
        onlp_led = onlp_led_info_t()
        ledlib.onlp_led_info_get(self.led_oid, ctypes.byref(onlp_led))
        if (onlp_led.mode) != 0:
            state = 1
        else:
            state = 0
        print "State :",self.STATE[state]
        return state

    """
    Print all the attributes of LED
    Parameter: LED object
    """
    def print_all(self):
        onlp_led = onlp_led_info_t()
        ledlib.onlp_led_info_get(self.led_oid, ctypes.byref(onlp_led))
        print "\nled_oid:",self.led_oid
        print "description:",onlp_led.hdr.description
        print "status:",onlp_led.status
        print "caps:",onlp_led.caps,self.caps_list
        print "mode:",onlp_led.mode
        self.get_mode()
        print "character:",onlp_led.character
        self.get_state()

    """
    Turn the LED on and set it to Mode 16(GREEN)
    Parameter: LED object
    """
    def set_normal(self):
        ledlib.onlp_led_set(self.led_oid,1)
        ledlib.onlp_led_mode_set(self.led_oid,16)
        print "\nTurn the LED on and set it to Mode 16(GREEN)\n"

"""
Returns the list of LEDs
"""
def get_leds():
    global led_oid
    led_oid = 0x5000001

    while(True):
        led1 = led(led_oid)
        ledlist.append(led1)
        led1.print_all()
        if((led1.status == 1)|(led1.status == 5)):
            print "\n"
        else:
            break
        led_oid = led_oid + 1
    return ledlist
