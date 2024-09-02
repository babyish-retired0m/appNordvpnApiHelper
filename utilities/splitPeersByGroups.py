#!/usr/bin/env python3
__version__ = "1.2"
#release notes
#1.2 added jsonHelper
#1.1 rewrite paths with pathlib
#1.0 Split JSON file by groups
import json
import pprint
import pathlib

utilitiesPath = pathlib.Path(__file__)
appPath = utilitiesPath.parents[1]
resultsPath = pathlib.PurePath(appPath, 'results')

import sys
sys.path.append(str(utilitiesPath))
import jsonHelper

serversFilePath = jsonHelper.lastFile()

arrJ = json.load(open(serversFilePath))


def fillArrayTypesPeers(dataJSON = arrJ, iPrint = False):
	counterP = 0
	arrPeersTypes = {}
	listPeersTypes = arrPeersTypes.values()
	for (enum, peer) in enumerate(dataJSON, start = 0):
		serverType = peer['groups'][0]['title']
		if (serverType not in listPeersTypes):
			arrPeersTypes[counterP] = serverType
			counterP += 1
	return arrPeersTypes


arrSrvTypes = fillArrayTypesPeers()


def explodeByGroups(dataJSON = arrJ, srvType = arrSrvTypes[4], iPrint = False):
	array = []
	for (enum, srv) in enumerate(dataJSON, start = 0):
		if (srv['groups'][0]['title'] == srvType):
			array.append(srv['hostname'])
			# array.extend(['','',''])
		if iPrint:
			print('result id:', enum)
	return array


if __name__ == '__main__':
	import sys
	defaultNumber = 4
	print('usage:\n type number of server type to be showed, Numbers of server types are:')
	for srvType in arrSrvTypes:
		print('\t' + str(srvType) + '=>' + arrSrvTypes[srvType], end = '\n')
	print('OR', arrSrvTypes[defaultNumber], 'will be showed')
	print('Example of usage:\n%s %s' % (sys.argv[0], defaultNumber))
	if len(sys.argv) == 1:
		data = explodeByGroups()
		# print(data)
		pprint.pprint(data)
		print('Quantity of servers:', len(data))
	elif len(sys.argv) == 2:
		data = (explodeByGroups(srvType = arrSrvTypes[int (sys.argv[1])]))
		print(data)
		print('Quantity of servers:', len(data))
	else:
		sys.exit(1)