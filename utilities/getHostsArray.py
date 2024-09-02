#!/usr/bin/env python3
__version__ = "1.0"
"""
# release notes
Split JSON file by groups
"""
import json
import pprint
import os
import pathlib
import sys


functionsPath = pathlib.Path(__file__)
appPath = functionsPath.parents[1]
utilitiesPath = pathlib.PurePath(appPath, 'utilities')
sys.path.append(str(utilitiesPath))

import getPeerByHostname as getPeer

def getArray(dataList=['pl128.nordvpn.com'], iPrint = False):
    dataDict = {}
    data = []
    counterOutcoming = 0
    falseData = []
    for peer in dataList:
        # print('getArrayForHost.getArray() hostname =>', peer)
        resultsArr = getPeer.getPeerByHostname(hostname = peer)
        if resultsArr:
            data.append(resultsArr)
        else:
            falseData.append(peer)
    if iPrint:
        print('total peers incoming', len(data))
        print('total peers outcoming', len(resultsArr)-counterOutcoming)
        print('sum substract(difference) => from incoming to outgoing',len(data)-(len(resultsArr)-counterOutcoming))

    return data, falseData

# data = ['pl204.nordvpn.com', 'pl205.nordvpn.com', 'pl206.nordvpn.com', 'pl207.nordvpn.com', 'pl208.nordvpn.com', 'pl209.nordvpn.com', 'pl210.nordvpn.com', 'pl211.nordvpn.com', 'pl212.nordvpn.com', 'pl213.nordvpn.com', 'pl214.nordvpn.com', 'pl215.nordvpn.com', 'pl216.nordvpn.com', 'pl217.nordvpn.com', 'pl218.nordvpn.com', 'pl219.nordvpn.com', 'pl220.nordvpn.com', 'pl221.nordvpn.com', 'pl222.nordvpn.com', 'pl223.nordvpn.com', 'pl224.nordvpn.com', 'pl225.nordvpn.com', 'pl226.nordvpn.com', 'pl227.nordvpn.com', 'pl230.nordvpn.com', 'pl231.nordvpn.com', 'pl232.nordvpn.com', 'pl233.nordvpn.com', 'pl234.nordvpn.com', 'pl235.nordvpn.com', 'pl236.nordvpn.com', 'pl237.nordvpn.com', 'pl238.nordvpn.com', 'pl239.nordvpn.com', 'pl240.nordvpn.com', 'pl241.nordvpn.com', 'pl242.nordvpn.com', 'pl243.nordvpn.com']


if __name__ == '__main__':
    if len(sys.argv) == 1:
        data = getArray()
        print(data)
        print('list length:', len(data))
    elif len(sys.argv) == 2:
        if isinstance(sys.argv[1], str):
            dataList = sys.argv[1].rsplit(',')
            print('data list:',dataList)
            data, fasleData = getArray(dataList=dataList, iPrint=False)
            if len(data)>=1:
                pprint.pprint(data)
            else:
                print('None object with hostname:', sys.argv[1])
        else:
            print('type list of hostnames (or hostname) of server(s) to be showed')
            sys.exit(1)
    else:
        print('type list of hostnames (or hostname) of server(s) to be showed')
        sys.exit(1)