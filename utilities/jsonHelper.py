#!/usr/bin/env python3
__version__ = "1.0"
# """
# TODOs, release notes and changelog are below the code, at the bottom of the file.
# """
import sys
import pathlib
# from retry import retry
import datetime

# Current folder path
functionsPath = pathlib.Path(__file__)
# Project folder path, ancestor folder
appPath = functionsPath.parents[1]
# Assets folder path with JSON files from API nordvpn.com
assetsPath = pathlib.PurePath(appPath, 'assets')
# Adding assets path to sys paths for importing modules as built-in(native)
sys.path.append(assetsPath)


def getListFolder(path = None, file_extension = "*"):
    p = pathlib.Path(path)
    #print(list(p.glob('**/*.*')))
    return list(p.glob('**/*.'+file_extension))


def getServersJsonFiles(pathsList):
    serversList = []
    for pathJ in pathsList:
        # if pathJ.name.startswith('servers'):
        # if pathJ.stem.match('servers.*'):
        if pathJ.stem.startswith('servers_'):
            serversList.append(pathJ)
    return serversList


def isActualFileDate(fileModifiedTime, delta = 30):
    month_ago = datetime.datetime.now() - datetime.timedelta(delta)
    modification_date = datetime.datetime.fromtimestamp(fileModifiedTime)
    need_update = month_ago > modification_date
    if need_update:
        print("** The servers JSON API data file hasn't been update in the last month", file = sys.stderr)
    return need_update


# class NordVpnApiError(Exception):
#     """Exception raised for errors in the API request """
#     def __init__(self, params,  msg):
#         self.message = f"Received an error during the API process with the following params: {params}. The API message: {msg}"
#         super().__init__(self.message)
#
#
# @retry((NordVpnApiError, Exception), tries=3, delay=2)
# def nordvpnApiQuery():
#     import http.client
#     import urllib
#     host = 'api.nordvpn.com'
#     conn = http.client.HTTPSConnection(host)
#     """
#     # urllib.parse.urlparse('https://api.nordvpn.com/v1/servers?limit=10000000')
#     # params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
#     """
#     payload = urllib.parse.urlencode({'limit':1000000})
#     # headers = {'Host' : host,
#     #             'Content-type': 'application/x-www-form-urlencoded',
#     #             'Accept': 'text/plain'}
#     headers = {
#         # 'Authorization': 'Bearer YOUR_API_TOKEN',
#         'Content-Type': 'application/json',
#         'Accept': 'application/json'
#         }
#     conn.request('GET', '/v1/servers?', payload, headers)
#     response = conn.getresponse()
#     data = response.read()
#     #data.decode("utf-8")
#     if response.status == 200:
#         print(response.status, response.reason)
#         return json.loads(data)
#     else:
#         print(response.status, response.reason)
#         msg = ""
#         if "message" in json.loads(data).keys():
#             msg = json.loads(data)["message"]
#         raise NordVpnApiError(params, msg)

def lastFile():
    pathsListAllJsonFiles = getListFolder(path = assetsPath, file_extension = 'json')
    pathsListServersJsonFiles = getServersJsonFiles(pathsListAllJsonFiles)
    # lastFile = list(reversed(pathsListServersJsonFiles))[0]
    lastFile = sorted(pathsListServersJsonFiles, reverse=True)[0]
    return lastFile


# if lastFileNeedUpdate:
#     nordvpnApiQuery()

if __name__ == '__main__':
    lastFileNeedUpdate = isActualFileDate(pathlib.Path(lastFile()).stat().st_mtime, delta=11)
    print('Last file:', lastFile())
    print('File need update:', lastFileNeedUpdate)
