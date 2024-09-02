#!/usr/bin/env python3
__version__ = "2.0"
"""
Code for generation VPN & DNS settings & firewall rules for RouterOS by Mikrotik router.
To recieve the results, run the function getRules(), it accepts data in JSON format with attribute dataJSON = YOURdataARRAY -> getRules(dataJSON = YOURdataARRAY). 
>>> And RETURN with answer of 3 varibles: dns_str, peer_str, address_list_str
"""
"""
TODOs, release notes and changelog are below the code, at the bottom of the file.
"""
import json
import sys
import pathlib

functionsPath = pathlib.Path(__file__)
appPath = functionsPath.parents[1]
assetsPath = pathlib.PurePath(appPath, 'assets')
sys.path.append(assetsPath)


resultsPath = pathlib.PurePath(appPath, 'results')
serversJsonFile = 'servers_2024-08-11_limit1000000.json'
serversFilePath = pathlib.PurePath(assetsPath, serversJsonFile)
arrJ = json.load(open(serversFilePath))

import getPeerByHostname as getPeer

def getRules(dataJSON = arrJ):
	dns_str="/ip dns static\n"
	peer_str="/ip ipsec peer\n"
	address_list_str="/ip firewall address-list\n"
	for (enum, peer) in enumerate(dataJSON):
		dns_str += "add address=\"" + peer['station'] + "\" comment=\"" + str(peer['id']) + "_" + peer['locations'][0]['country']['code'] + "_NordVPNpeer\" name=\"" + peer['hostname'] + "\"\n"
		
		peer_str += "add name=\"" + str(peer['id']) + "_" + peer['locations'][0]['country']['code'] + "\" address=\"" + peer['hostname'] + "\" comment=\"" + peer['locations'][0]['country']['name'] + "\" profile=NordVPN exchange-mode=ike2 send-initial-contact=yes disabled=yes\n"
		
		address_list_str += "add address=\"" + peer['hostname'] + "\" comment=\"" + str(peer['id']) + "_" + peer['locations'][0]['country']['code'] + "\" list=\"NordVPN\"\n"
	return dns_str,peer_str,address_list_str


def storeResults(data, type, comment='', iPrint = True):
	# types = ('dns', 'peer', 'firewall')
	typesDict = {
				'dns':'mikrotik_rule_dns_hosts_nordvpn.com_', 
				'peer':'mikrotik_rule_ipsec_peers_nordvpn.com_', 
				'firewall':'mikrotik_rule_firewall_address-list_'
				}
	types = list(typesDict.keys())
	def write_text(path,text):
		with open(path, 'w') as myfile: myfile.write(text)
	def check_file(path):
		import pathlib
		if pathlib.Path(path).is_file():
			print('file', path, 'exists')
			return True
		else:
			print('there is no existing file (and therefore no existing file path) ' + path);
			return False
	import time
	time_local = time.strftime("%Y-%m-%d", time.localtime())
	mikrotikResultsPath = pathlib.PurePath(resultsPath, 'mikrotik')
	if types[0] == type:
		typePath = typesDict['dns']
	elif types[1] == type:
		typePath = typesDict['peer']
	elif types[2] == type:
		typePath = typesDict['firewall']
	pathRsc = pathlib.PurePath(mikrotikResultsPath, typePath + time_local + comment + '.rsc')
	write_text(pathRsc, data)
	if iPrint:
		check_file(pathRsc)
		print('store results completed')


if __name__ == '__main__':
	import getHostArray as getArrayForHost
	data = ['pl204.nordvpn.com', 'pl205.nordvpn.com', 'pl206.nordvpn.com', 'pl207.nordvpn.com', 'pl208.nordvpn.com', 'pl209.nordvpn.com', 'pl210.nordvpn.com', 'pl211.nordvpn.com', 'pl212.nordvpn.com', 'pl213.nordvpn.com', 'pl214.nordvpn.com', 'pl215.nordvpn.com', 'pl216.nordvpn.com', 'pl217.nordvpn.com', 'pl218.nordvpn.com', 'pl219.nordvpn.com', 'pl220.nordvpn.com', 'pl221.nordvpn.com', 'pl222.nordvpn.com', 'pl223.nordvpn.com', 'pl224.nordvpn.com', 'pl225.nordvpn.com', 'pl226.nordvpn.com', 'pl227.nordvpn.com', 'pl230.nordvpn.com', 'pl231.nordvpn.com', 'pl232.nordvpn.com', 'pl233.nordvpn.com', 'pl234.nordvpn.com', 'pl235.nordvpn.com', 'pl236.nordvpn.com', 'pl237.nordvpn.com', 'pl238.nordvpn.com', 'pl239.nordvpn.com', 'pl240.nordvpn.com', 'pl241.nordvpn.com', 'pl242.nordvpn.com', 'pl243.nordvpn.com']
	#  dataFalse ['pl208.nordvpn.com', 'pl209.nordvpn.com', 'pl210.nordvpn.com', 'pl211.nordvpn.com', 'pl212.nordvpn.com', 'pl213.nordvpn.com', 'pl214.nordvpn.com', 'pl215.nordvpn.com', 'pl216.nordvpn.com', 'pl217.nordvpn.com', 'pl218.nordvpn.com', 'pl219.nordvpn.com', 'pl220.nordvpn.com', 'pl221.nordvpn.com']
	dataResults, dataFalse = getArrayForHost.getArray(data)
	print('dataFalse', dataFalse)

 
	dns_str, peer_str, address_list_str = getRules(dataResults)
	# print(dns_str)
	# print(peer_str)
	# print(address_list_str)
	storeResults(dns_str, type='dns', comment='PL-2024-newPeers')
	storeResults(peer_str, type='peer', comment='PL-2024-newPeers')
	storeResults(address_list_str, type='firewall', comment='PL-2024-newPeers')

	
"""
release notes:
2.0 
	rewrite paths
	added function generateMikrotikRulesIpSec()
TODO:
2.1
	store results
	add function checkPeersByVerbosePing()
"""
