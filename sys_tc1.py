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
 Description: Get the System status
"""
DEBUG = True

from libonlp import sys
from libonlp import get_sys
from time import sleep

sysobj = get_sys() #System object
count = len(sysobj)
print "The count is ",count

if DEBUG:
    if count != 0:
        print "Test case passed"
    else:
        print "Test case failed"
