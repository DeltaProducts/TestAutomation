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
 Description: ONLP System module
"""
import ctypes
from time import sleep
import os, re

def platform():
    f = os.popen('uname -a')
    output = f.read()
    if re.search("x86_64",output):
        return '/lib/x86_64-linux-gnu/libonlp.so'
    elif re.search("arm",output):
        return '/lib/arm-linux-gnueabi/libonlp.so'
    else :
        return '/lib/x86_64-linux-gnu/libonlp.so'

LIB_ONLP=platform()
syslib = ctypes.CDLL(LIB_ONLP)

class onlp_onie_info_t(ctypes.Structure):
    _fields_ = [("product_name",ctypes.c_char_p),
                ("part_number",ctypes.c_char_p),
                ("serial_number",ctypes.c_char_p),
                ("MAC",ctypes.c_ubyte * 6),
                ("manufacture_date",ctypes.c_char_p),
                ("device_version",ctypes.c_ubyte),
                ("label_revision",ctypes.c_char_p),
                ("platform_name",ctypes.c_char_p),
                ("onie_version",ctypes.c_char_p),
                ("mac_range",ctypes.c_ushort),
                ("manufacturer",ctypes.c_char_p),
                ("country_code",ctypes.c_char_p),
                ("vendor",ctypes.c_char_p),
                ("diag_version",ctypes.c_char_p),
                ("service_tag",ctypes.c_char_p),
                ("crc",ctypes.c_uint),
                ("list_head_t",ctypes.c_char_p * 2),
                ("_hdr_id_string",ctypes.c_char_p),
                ("_hdr_version",ctypes.c_ubyte),
                ("_hdr_length",ctypes.c_ubyte),
                ("_hdr_valid_crc",ctypes.c_ubyte)]

class onlp_oid_hdr_t(ctypes.Structure):
    _fields_ = [("id", ctypes.c_uint),
               ("description", ctypes.c_char * 128),
               ("poid", ctypes.c_uint),
               ("coids", ctypes.c_uint * 32)]

class onlp_platform_info_t(ctypes.Structure):
    _fields_ = [("cpld_versions",ctypes.c_char_p),
                ("other versions",ctypes.c_char_p)]


class onlp_sys_info_t(ctypes.Structure):
    _fields_ = [("hdr",onlp_oid_hdr_t),
                ("onie_info",onlp_onie_info_t),
                ("platform",onlp_platform_info_t)]

class sys:
    def __init__(self,id):
        syslib.onlp_sys_init()
        onlp_sys = onlp_sys_info_t()
        syslib.onlp_sys_info_get(ctypes.byref(onlp_sys))
        self.sys_oid = id
        self.hdr = onlp_sys.hdr
        self.onie_info = onlp_sys.onie_info
        self.platform = onlp_sys.platform

"""
Initialize the system API
"""
syslib.onlp_sys_init.restype = ctypes.c_int

"""
Get the system information Structure
Parameter: Recieves the system Structure
"""
syslib.onlp_sys_info_get.argtypes = [ctypes.POINTER(onlp_sys_info_t)]

def get_sys():
    global sys_oid
    sys_oid = 0x1000001
    sys1 = sys(sys_oid)
    print "\n"
    print "Product name: ",sys1.onie_info.product_name
    print "Serial Number: ",sys1.onie_info.serial_number
    print "MAC Range: ",sys1.onie_info.mac_range
    print "Manufacturer: ",sys1.onie_info.manufacturer
    print "Manufacture Date: ",sys1.onie_info.manufacture_date
    print "Country code: ",sys1.onie_info.country_code
    print "Diag Version: ",sys1.onie_info.diag_version
    print "ONIE Version: ",sys1.onie_info.onie_version
    syslist=[]
    syslist.append(sys1)
    return syslist
