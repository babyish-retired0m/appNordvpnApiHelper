#!/usr/bin/env python3
__version__ = "1.1"
"""
# release notes
1.1 rewrite paths with pathlib
1.0 Split JSON file by countries

# todo
Store results
"""
import json
import pprint
import pathlib

utilitiesPath = pathlib.Path(__file__)
appPath = utilitiesPath.parents[1]
resultsPath = pathlib.PurePath(appPath, 'results')
assetsPath = pathlib.PurePath(appPath, 'assets')
serversJsonFile = 'servers_2024-08-11_full_limit1000000.json'
serversFilePath = pathlib.PurePath(assetsPath, serversJsonFile)
arrJ = json.load(open(serversFilePath))


def fillCountriesArray(dataJSON=arrJ):
    counterP = 0
    arrCountries = {}
    listCountries = arrCountries.values()
    for (enum,peer) in enumerate(dataJSON,start=0):
        country=peer['locations'][0]['country']['name']
        # listCountries.append(country)
        if (country not in listCountries):
            arrCountries[counterP]=country
            counterP+=1
            # print('peer number:',enum)
    return arrCountries

def splitByCountries(dataJSON = arrJ, country = 'Poland', iPrint = False):
    counterP = 0
    listPeers = []
    for (enum,peer) in enumerate(dataJSON,start=0):
        if (peer['locations'][0]['country']['name'] == country):
            listPeers.append(peer['hostname'])
            counterP+=1
        if iPrint: print('result number:', enum)
    return listPeers

if __name__ == '__main__':
    import sys

    listCountries = fillCountriesArray()
    defaultNumber = 94

    def usage():
        print('usage:\n type number of Country to be shown, Numbers of Countries are:')
        for country in listCountries:
            print('\t' + str(country) + ' => ' + listCountries[country])
        print('OR', listCountries[defaultNumber], 'will be shown')


    def userInteraction():
        import sys

        if len(sys.argv) == 1:
            usage()
            print('Example of usage:\n$python3 %s %s' % (sys.argv[0], defaultNumber))
            data = splitByCountries(country = listCountries[defaultNumber])
        elif len(sys.argv) == 2:
            data = splitByCountries(country = listCountries[int(sys.argv[1])])
        else:
            sys.exit(1)
        print(data)
        print('Quantity of servers:', len(data))

    userInteraction()