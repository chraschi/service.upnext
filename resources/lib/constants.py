# -*- coding: utf-8 -*-
# GNU General Public License v2.0 (see COPYING or https://www.gnu.org/licenses/gpl-2.0.txt)

from __future__ import absolute_import, division, unicode_literals


ADDON_ID = 'service.upnext'

UNKNOWN_DATA = -1

WINDOW_HOME = 10000

PLAY_CONTROL_ID = 3012
CLOSE_CONTROL_ID = 3013
PROGRESS_CONTROL_ID = 3014
SHUFFLE_CONTROL_ID = 3015

STOP_STRING_ID = 30033
CLOSE_STRING_ID = 30034
NEXT_STRING_ID = 30049

BOOL_STRING_VALUES = {
    'false': False,
    'true': True
}

LOG_ENABLE_DISABLED = 0
LOG_ENABLE_INFO = 1
LOG_ENABLE_DEBUG = 2

ADDON_MISSING_DATA = 1
ADDON_PLAY_URL = 2
ADDON_PLAY_INFO = 3

SETTING_DISABLED = 0
SETTING_FORCED_ON = 1
SETTING_FORCED_OFF = 2

TRACKER_MODE_LOOP = 0
TRACKER_MODE_THREAD = 1
TRACKER_MODE_TIMER = 2
