#!/usr/bin/env python3
__version__ = "1.0"
"""
# release notes
1.0 get peer by id from JSON file
"""
import json
import pprint
import os
import sys
import pathlib

functionsPath = pathlib.Path(__file__)
appPath = functionsPath.parents[1]
utilitiesPath = pathlib.PurePath(appPath, 'utilities')
# utilitiesPath = pathlib.Path(__file__)
sys.path.append(utilitiesPath)
import jsonHelper

resultsPath = pathlib.PurePath(appPath, 'results')
assetsPath = pathlib.PurePath(appPath, 'assets')
# serversJsonFile = 'servers_2024-08-11_full_limit1000000.json'
# serversFilePath = pathlib.PurePath(assetsPath, serversJsonFile)
serversFilePath = jsonHelper.lastFile()
arrJ = json.load(open(serversFilePath))


def getPeerById(dataJSON = arrJ, peerId = int(929966), iPrint = False):
    for (enum,peer) in enumerate(dataJSON, start=0):
        if (peer['id'] == peerId):
            # array={'id':peer['id'],peer['name'],peer['station'],peer['hostname'],peer['load'],peer['status'],peer['locations']['country']['id'],peer['locations']['country']['name'],peer['locations']['country']['code'],peer[],peer[],peer[]}
            # array.extend(['','',''])
            array={peer['id']}
            if iPrint: print('result id:', enum)
            return peer


if __name__ == '__main__':
    import sys
    defaultNumber = 929966
    print('usage:\n type ID number of server to be showned, Numbers of server types are:')
    for peer in arrJ: 
        print('\t' + 'hostname: ' + str(peer['hostname']) + '\t' + 'peer id' + '=>' + str(peer['id']))
    print('OR', defaultNumber, 'will be showned')
    print('Example of usage:\n%s %s' % (sys.argv[0], defaultNumber))
    if len(sys.argv) == 1:
        data = getPeerById()
        print(data)
        print('list length:', len(data))
    elif len(sys.argv) == 2:
        data = (getPeerById(peerId=int(sys.argv[1])))
        print(data)
        print('list length:', len(data))
    else:
        sys.exit(1)