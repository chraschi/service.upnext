# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dag Wieers (@dagwieers) <dag@wieers.com>
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
''' This file implements the Kodi xbmc module, either using stubs or alternative functionality '''

# pylint: disable=invalid-name,no-self-use

from __future__ import absolute_import, division, print_function, unicode_literals
import os
import array
import json
import random
import sys
import threading
import time
from weakref import WeakValueDictionary
from xbmcextra import global_settings, import_language, __KODI_MATRIX__
from dummydata import LIBRARY
from statichelper import to_unicode


if __KODI_MATRIX__:
    LOGDEBUG = 0
    LOGINFO = 1
    LOGWARNING = 2
    LOGERROR = 3
    LOGFATAL = 4
    LOGNONE = 5
else:
    LOGDEBUG = 0
    LOGINFO = 1
    LOGNOTICE = 2
    LOGWARNING = 3
    LOGERROR = 4
    LOGSEVERE = 5
    LOGFATAL = 6
    LOGNONE = 7

INFO_LABELS = {
    'System.BuildVersion': '18.9' if __KODI_MATRIX__ else '19.0',
    'Player.Process(VideoWidth)': 1920,
    'Player.Process(VideoHeight)': 1080,
    'Player.Process(VideoDAR)': 1.78
}

REGIONS = {
    'datelong': '%A, %e %B %Y' if random.randint(0, 1) else '%C',
    'dateshort': '%Y-%m-%d' if random.randint(0, 1) else '%x',
    'time': '%I:%M %p' if random.randint(0, 1) else '%X'
}

GLOBAL_SETTINGS = global_settings()
PO = import_language(language=GLOBAL_SETTINGS.get('locale.language'))

PLAYLIST_MUSIC = 0
PLAYLIST_VIDEO = 1


class Keyboard:
    ''' A stub implementation of the xbmc Keyboard class '''

    def __init__(self, line='', heading=''):
        ''' A stub constructor for the xbmc Keyboard class '''

    def doModal(self, autoclose=0):
        ''' A stub implementation for the xbmc Keyboard class doModal() method '''

    def isConfirmed(self):
        ''' A stub implementation for the xbmc Keyboard class isConfirmed() method '''
        return True

    def getText(self):
        ''' A stub implementation for the xbmc Keyboard class getText() method '''
        return 'test'


class Monitor:
    ''' A stub implementation of the xbmc Monitor class '''
    _instances = WeakValueDictionary()
    _instance_number = 0
    _aborted = False

    def __init__(self):
        ''' A stub constructor for the xbmc Monitor class '''
        if not Monitor._instance_number:
            abort_timer = threading.Thread(target=self._timer)
            abort_timer.daemon = True
            abort_timer.start()

        Monitor._instances[Monitor._instance_number] = self
        Monitor._instance_number += 1

    def _timer(self):
        abort_times = [10, 30, 60]
        abort_time = abort_times[random.randint(0, len(abort_times) - 1)]

        time.sleep(abort_time)
        Monitor._aborted = True
        sys.exit()

    def abortRequested(self):
        ''' A stub implementation for the xbmc Monitor class abortRequested() method '''
        return Monitor._aborted

    def waitForAbort(self, timeout=None):
        ''' A stub implementation for the xbmc Monitor class waitForAbort() method '''
        sleep_time = timeout if timeout else 1
        timed_out = False

        try:
            while not timed_out and not Monitor._aborted:
                time.sleep(sleep_time)
                if timeout:
                    timed_out = True
        except (KeyboardInterrupt, SystemExit, Exception):  # pylint: disable=broad-except
            pass

        return Monitor._aborted


class Player:
    ''' A stub implementation of the xbmc Player class '''

    def __init__(self):
        ''' A stub constructor for the xbmc Player class '''
        self._count = 0

    def play(self, item='', listitem=None, windowed=False, startpos=-1):  # pylint: disable=unused-argument
        ''' A stub implementation for the xbmc Player class play() method '''
        return

    def playnext(self):
        ''' A stub implementation for the xbmc Player class playnext() method '''
        return

    def stop(self):
        ''' A stub implementation for the xbmc Player class stop() method '''
        return

    def isExternalPlayer(self):
        ''' A stub implementation for the xbmc Player class isExternalPlayer() method '''
        return False

    def getPlayingFile(self):
        ''' A stub implementation for the xbmc Player class getPlayingFile() method '''
        return '/foo/bar'

    def isPlaying(self):
        ''' A stub implementation for the xbmc Player class isPlaying() method '''
        # Return True four times out of five
        self._count += 1
        return bool(self._count % 5 != 0)

    def seekTime(self, seekTime):  # pylint: disable=unused-argument
        ''' A stub implementation for the xbmc Player class seekTime() method '''
        return

    def showSubtitles(self, bVisible):  # pylint: disable=unused-argument
        ''' A stub implementation for the xbmc Player class showSubtitles() method '''
        return

    def getTotalTime(self):
        ''' A stub implementation for the xbmc Player class getTotalTime() method '''
        return 0

    def getTime(self):
        ''' A stub implementation for the xbmc Player class getTime() method '''
        return 0

    def getVideoInfoTag(self):
        ''' A stub implementation for the xbmc Player class getVideoInfoTag() method '''
        return InfoTagVideo()


class PlayList:
    ''' A stub implementation of the xbmc PlayList class '''

    def __init__(self, playList):
        ''' A stub constructor for the xbmc PlayList class '''

    def getposition(self):
        ''' A stub implementation for the xbmc PlayList class getposition() method '''
        return 0

    def size(self):
        ''' A stub implementation for the xbmc PlayList class size() method '''
        return 1


class InfoTagVideo:
    ''' A stub implementation of the xbmc InfoTagVideo class '''

    def __init__(self):
        ''' A stub constructor for the xbmc InfoTagVideo class '''

    def getSeason(self):
        ''' A stub implementation for the xbmc InfoTagVideo class getSeason() method '''
        return 0

    def getEpisode(self):
        ''' A stub implementation for the xbmc InfoTagVideo class getEpisode() method '''
        return 0

    def getTVShowTitle(self):
        ''' A stub implementation for the xbmc InfoTagVideo class getTVShowTitle() method '''
        return ''

    def getPlayCount(self):
        ''' A stub implementation for the xbmc InfoTagVideo class getPlayCount() method '''
        return 0

    def getRating(self):
        ''' A stub implementation for the xbmc InfoTagVideo class getRating() method '''
        return 0

    def getMediaType(self):
        ''' A stub implementation for the xbmc InfoTagVideo class getMediaType() method '''
        return ''


class RenderCapture:
    ''' A stub implementation of the xbmc RenderCapture class '''

    def __init__(self):
        ''' A stub constructor for the xbmc RenderCapture class '''
        self._width = 0
        self._height = 0

    def capture(self, width, height):
        ''' A stub implementation for the xbmc RenderCapture class capture() method '''
        self._width = width
        self._height = height

    def getImage(self):
        ''' A stub implementation for the xbmc RenderCapture class getImage() method '''
        return array.array('B', [
            random.randint(0, 255) if i % 4 != 3 else 255
            for i in range(self._width * self._height * 4)
        ])


def executebuiltin(string, wait=False):  # pylint: disable=unused-argument
    ''' A stub implementation of the xbmc executebuiltin() function '''
    return


def executeJSONRPC(jsonrpccommand):
    ''' A reimplementation of the xbmc executeJSONRPC() function '''
    command = json.loads(jsonrpccommand)
    method = command.get('method') if command else None
    params = command.get('params', {}) if command else {}

    if method == 'Settings.GetSettingValue':
        key = params.get('setting')
        return json.dumps(dict(id=1, jsonrpc='2.0', result=dict(value=GLOBAL_SETTINGS.get(key))))

    if method == 'Addons.GetAddonDetails':
        if params.get('addonid') == 'script.module.inputstreamhelper':
            return json.dumps(dict(id=1, jsonrpc='2.0', result=dict(addon=dict(enabled='true', version='0.3.5'))))
        return json.dumps(dict(id=1, jsonrpc='2.0', result=dict(addon=dict(enabled='true', version='1.2.3'))))

    if method == 'Textures.GetTextures':
        return json.dumps(dict(id=1, jsonrpc='2.0', result=dict(textures=[dict(cachedurl="", imagehash="", lasthashcheck="", textureid=4837, url="")])))

    if method == 'Textures.RemoveTexture':
        return json.dumps(dict(id=1, jsonrpc='2.0', result="OK"))

    if method == 'Player.GetActivePlayers':
        return json.dumps(dict(id=1, jsonrpc='2.0', result=[[dict(type='video', playerid=1)], [dict(type='audio', playerid=0)], []][random.randint(0, 2)]))

    if method == 'Player.GetProperties' and params.get('properties') == ['speed']:
        return json.dumps(dict(id=1, jsonrpc='2.0', result=dict(speed=random.randint(0, 1))))

    if method == 'Player.GetItem':
        return json.dumps(dict(id=1, jsonrpc='2.0', result=dict(item=LIBRARY['episodes'][0])))

    if method == 'VideoLibrary.GetTVShows':
        tvshow_filter = params.get('filter')
        if tvshow_filter:
            filter_field = tvshow_filter.get('field')
            filter_operator = tvshow_filter.get('operator')
            filter_value = tvshow_filter.get('value')
            if filter_field == 'title' and filter_operator == 'is':
                tvshowid = LIBRARY['tvshows'].get(filter_value, {}).get('tvshowid')
                episodes = [episode for episode in LIBRARY['episodes'] if episode['showtitle'] == filter_value]
                for episode in episodes:
                    episode['tvshowid'] = tvshowid
                return json.dumps(dict(id=1, jsonrpc='2.0', result=dict(tvshows=[dict(tvshowid=tvshowid)])))

    if method == 'VideoLibrary.GetEpisodes':
        episode_filter = params.get('filter', {})
        tvshowid = params.get('tvshowid')
        if tvshowid is not None and episode_filter:
            def filter_walker(filter_object, seeking):
                for level in filter_object:
                    if isinstance(filter_object, dict) and filter_object[level] == seeking:
                        return filter_object
                    elif isinstance(level, dict):
                        found = filter_walker(level, seeking)
                        if found:
                            return found
                    elif isinstance(filter_object[level], list):
                        found = filter_walker(filter_object[level], seeking)
                        if found:
                            return found
                    elif isinstance(filter_object[level], dict):
                        found = filter_walker(filter_object[level], seeking)
                        if found:
                            return found

            season = filter_walker(episode_filter, 'season')
            episode_number = filter_walker(episode_filter, 'episode')
            if season and episode_number:
                episodes = [
                    episode for episode in LIBRARY['episodes']
                    if episode['tvshowid'] == tvshowid
                    and episode['season'] == int(season.get('value'))
                    and episode['episode'] >= int(episode_number.get('value'))
                ]
                if episode_number.get('operator') == 'greaterthan':
                    episodes = episodes[1:]
                return json.dumps(dict(id=1, jsonrpc='2.0', result=dict(episodes=episodes)))

    if method == 'VideoLibrary.GetEpisodeDetails':
        episodeid = params.get('episodeid')
        if episodeid is not None:
            episodes = [
                episode for episode in LIBRARY['episodes']
                if episode['episodeid'] == episodeid
            ]
            return json.dumps(dict(id=1, jsonrpc='2.0', result=dict(episodedetails=episodes[0])))

    if method == 'VideoLibrary.GetTVShowDetails':
        tvshowid = params.get('tvshowid')
        if tvshowid is not None:
            tvshows = [
                details for tvshow, details in LIBRARY['tvshows'].items()
                if details['tvshowid'] == tvshowid
            ]
            return json.dumps(dict(id=1, jsonrpc='2.0', result=dict(tvshowdetails=tvshows[0])))

    if method == 'JSONRPC.NotifyAll':
        for ref in Monitor._instances.valuerefs():
            notification_handler = getattr(ref, "onNotification", None)
            if callable(notification_handler):
                notification_handler(ref, params.get('sender'), params.get('message'), params.get('data'))
        return json.dumps(dict(id=1, jsonrpc='2.0', result="OK"))

    if method == 'Player.Open':
        pass

    if method == 'Playlist.Add':
        pass

    if method == 'Playlist.Add':
        pass

    log("executeJSONRPC does not implement method '{method}'".format(**command), LOGERROR)
    return json.dumps(dict(error=dict(code=-1, message='Not implemented'), id=1, jsonrpc='2.0'))


def getCondVisibility(string):
    ''' A reimplementation of the xbmc getCondVisibility() function '''
    if string == 'system.platform.android':
        return False
    return True


def getInfoLabel(key):
    ''' A reimplementation of the xbmc getInfoLabel() function '''
    return INFO_LABELS.get(key, '')


def getLocalizedString(msgctxt):
    ''' A reimplementation of the xbmc getLocalizedString() function '''
    for entry in PO:
        if entry.msgctxt == '#%s' % msgctxt:
            return entry.msgstr or entry.msgid
    if int(msgctxt) >= 30000:
        log('Unable to translate #{msgctxt}'.format(msgctxt=msgctxt), LOGERROR)
    return '<Untranslated>'


def getRegion(key):
    ''' A reimplementation of the xbmc getRegion() function '''
    return REGIONS.get(key)


def log(msg, level):
    ''' A reimplementation of the xbmc log() function '''
    if level in (LOGERROR, LOGFATAL):
        print('\033[31;1m%s: \033[32;0m%s\033[39;0m' % (level, to_unicode(msg)))
        if level == LOGFATAL:
            raise Exception(msg)
    elif level == LOGWARNING or (not __KODI_MATRIX__ and level == LOGINFO + 1):
        print('\033[33;1m%s: \033[32;0m%s\033[39;0m' % (level, to_unicode(msg)))
    elif level == LOGDEBUG:
        print('\033[32;1m%s: \033[30;1m%s\033[39;0m' % (level, to_unicode(msg)))
    else:
        print('\033[32;1m%s: \033[32;0m%s\033[39;0m' % (level, to_unicode(msg)))


def setContent(self, content):  # pylint: disable=unused-argument
    ''' A stub implementation of the xbmc setContent() function '''
    return


def sleep(seconds):
    ''' A reimplementation of the xbmc sleep() function '''
    time.sleep(seconds)


# translatePath and makeLegalFilename have been moved to xbmcvfs in Kodi 19+
# but currently still available in xbmc
if not __KODI_MATRIX__ or True:  # pylint: disable=condition-evals-to-constant
    def translatePath(path):
        ''' A stub implementation of the xbmc translatePath() function '''
        if path.startswith('special://home'):
            return path.replace('special://home', os.path.join(os.getcwd(), 'tests/'))
        if path.startswith('special://masterprofile'):
            return path.replace('special://masterprofile', os.path.join(os.getcwd(), 'tests/userdata/'))
        if path.startswith('special://profile'):
            return path.replace('special://profile', os.path.join(os.getcwd(), 'tests/userdata/'))
        if path.startswith('special://userdata'):
            return path.replace('special://userdata', os.path.join(os.getcwd(), 'tests/userdata/'))
        return path

    def makeLegalFilename(path):
        ''' A stub implementation of the xbmc makeLegalFilename() function '''
        return os.path.normpath(path)
