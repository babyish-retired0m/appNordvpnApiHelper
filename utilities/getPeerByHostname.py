#!/usr/bin/env python3
__version__ = "1.1"

# from utilities.splitPeersByGroups import utilitiesPath

"""To recieve the result run the function getPeerByHostname() with attribute host. Available attributes are:
dataJSON, host, iPrint.

Example:
getPeerByHostname(host = 'pl145.nordvpn.com')
>>>return 1 variable Array

TODOs and release notes and changelog are below, at the bottom of the file."""
import json
import sys
import pathlib

functionsPath = pathlib.Path(__file__)
appPath = functionsPath.parents[1]
utilitiesPath = pathlib.PurePath(appPath, 'utilities')
sys.path.append(utilitiesPath)
import jsonHelper

resultsPath = pathlib.PurePath(appPath, 'results')

serversFilePath = jsonHelper.lastFile()
arrJ = json.load(open(serversFilePath))
# arrJ = sorted(arrJ.keys())
# arrJ = sorted(arrJ.items(), key=lambda x: x[0])


def getPeerByHostname(dataJSON = arrJ, hostname = 'pl128.nordvpn.com', iPrint = False):
	for (enum, peer) in enumerate(dataJSON, start = 0):
		if (peer['hostname'] == hostname):
			if iPrint: print('result id:', enum);
			return peer


def storeResults(host, data, iPrint = True):
	import time
	def write_text(path, text):
		with open(path, 'w') as myfile: myfile.write(text)
	def write_text_as_json(path, text):
		import json
		json.dump(text, fp=open(path, 'w'), indent=4)
	def check_file(path):
		import pathlib
		if pathlib.Path(path).is_file():
			print('file', path, 'exists')
			return True
		else:
			print('there is no existing file (and therefore no existing file path) ', path)
			return False
	# time_local = time.strftime("%Y-%m-%d", time.localtime())
	pathRsc = pathlib.PurePath(resultsPath, 'user_interaction', host).with_suffix('.json')
	write_text_as_json(pathRsc, data)
	if iPrint:
		check_file(pathRsc)
		print('store results completed')


if __name__ == '__main__':
	import sys
	import pprint
	defaultHost = 'pl128.nordvpn.com'


	def usage():
		print('usage:\n type hostname of Peer to be showned, hostnames of Peers are:')
		for (enum, peer) in enumerate(arrJ, start = 0):
			print('\t' + str(enum)+' => ' + peer['hostname'])
		print('OR', defaultHost, 'will be showned')
		print('Example of usage:\n$python3 %s %s' % (sys.argv[0], defaultHost))

	def askSave(dialogHost, dialogData):
		class messagebox:
			yes = 'Yes'
			no = 'No'
		print('Do you want to store the results in file?')
		print('Type:', messagebox.yes, 'or', messagebox.no)
		try:
			messagebox.askyesno = input()
			if messagebox.askyesno == 'Yes' or messagebox.askyesno == 'yes' or messagebox.askyesno == 'y' or messagebox.askyesno == 'Y':
				storeResults(dialogHost, dialogData)
		except KeyboardInterrupt:
			print('keyboard interrupted')
			sys.exit(1)
		except Exception as e:
			print(e)
			raise e
		else:
			sys.exit(1)

	def userInteraction():
		if len(sys.argv) == 1:
			usage()
			host = defaultHost
			# data = getPeerByHostname(hostname = defaultHost)
			data = getPeerByHostname(hostname = host)
			pprint.pprint(data)
			print('list length:', len(data))
		elif len(sys.argv) == 2:
			host  = str(sys.argv[1])
			# data = getPeerByHostname(hostname = str(sys.argv[1]))
			try:
				data = getPeerByHostname(hostname = host)
			except Exception as e:
				print(e)
			else:
				print('None object with hostname:', host)
			finally:
				if data:
					pprint.pprint(data)
					print('list length:', len(data))
					askSave(host,data)
		else:
			sys.exit(1)
		return host,data


	userInteraction()


"""release notes:
1.0 rewrite paths
1.1 added jsonHelper
TODO:
2.0 store results"""
"""changelog"""