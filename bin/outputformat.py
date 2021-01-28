# Python edgegrid module
""" Copyright 2015 Akamai Technologies, Inc. All Rights Reserved.

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.

 You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
************************************************************************
*  Media Services CLI module by Achuthananda M P (apadmana@akamai.com) & Suhas Bharadwaj (sbharadw@akamai.com)*
************************************************************************
"""
import sys
import os
import requests
import logging
import json
import texttable as tt


from akamai.edgegrid import EdgeGridAuth, EdgeRc
from config import EdgeGridConfig
if sys.version_info[0] >= 3:
    # python3
    from urllib import parse
else:
    # python2.7
    import urlparse as parse

logger = logging.getLogger(__name__)

def formatOutputStreamList(streamList, output_type):
    """ Formats the output on a given format (json or text) """
    if output_type == "json":
        # Let's print the JSON
        print(json.dumps(streamList, indent=2))

    if output_type == "text":
        # Iterate over the dictionary and print the selected information
        ParentTable = tt.Texttable()
        ParentTable.set_cols_width([15, 30, 15, 15, 40])
        ParentTable.set_cols_align(['c', 'c', 'c', 'c', 'c'])
        ParentTable.set_cols_valign(['m', 'm', 'm', 'm', 'm'])
        Parentheader = ['ID', 'Name', 'Format', 'CPcode', 'Origin']
        ParentTable.header(Parentheader)
        for my_item in streamList['streams']:
            Parentrow = [my_item["id"], my_item["name"], my_item["format"], my_item['cpcode'],
                         my_item['originHostName']]
            ParentTable.add_row(Parentrow)
        MainParentTable = ParentTable.draw()
        print(MainParentTable)


def formatOutputLiveOriginList(liveOriginList, output_type):
    """ Formats the output on a given format (json or text) """
    if output_type == "json":
        # Let's print the JSON
        print(json.dumps(liveOriginList, indent=2))

    if output_type == "text":
        # Iterate over the dictionary and print the selected information
        ParentTable = tt.Texttable()
        ParentTable.set_cols_width([45,10, 10, 15, 12])
        ParentTable.set_cols_align(['c','c','c', 'c', 'c'])
        ParentTable.set_cols_valign(['m','m','m', 'm', 'm'])
        Parentheader = ['HostName','Id','CPCode', 'Encoder', 'Status']
        ParentTable.header(Parentheader)
        for my_item in liveOriginList:
            Parentrow = [my_item["hostName"],my_item["id"], my_item["cpcode"], my_item["location"], my_item['status']]
            ParentTable.add_row(Parentrow)
        MainParentTable = ParentTable.draw()
        print(MainParentTable)

def formatOutputGetStream(streamInfo, output_type):
    """ Formats the output on a given format (json or text) """
    if output_type == "json":
        # Let's print the JSON
        print(json.dumps(streamInfo, indent=2))

    if output_type == "text":
        # Iterate over the dictionary and print the selected information
        ParentTable = tt.Texttable()
        ParentTable.set_cols_width([15, 60])
        ParentTable.set_cols_align(['c', 'c'])
        ParentTable.set_cols_valign(['m', 'm'])
        headerList = ['id', 'name', 'format', 'cpcode', 'origin',
                        'createdDate', 'modifiedDate', 'storagecpcode', 'encoderZone', 'primaryPublishingUrl', 'backupPublishingUrl', 'allowedIps']
        for key in headerList:
            if key == 'origin':
                Parentrow = [key, streamInfo[key]['hostName']]
            elif key == 'storagecpcode':
                Parentrow = [key, streamInfo['storageGroup']['cpcode']]
            else:
                Parentrow = [key,streamInfo[key]]
            ParentTable.add_row(Parentrow)

        MainParentTable = ParentTable.draw()
        print(MainParentTable)

def formatOutputOrigin(originInfo, output_type):
    """ Formats the output on a given format (json or text) """
    if output_type == "json":
        # Let's print the JSON
        print(json.dumps(originInfo, indent=2))

    if output_type == "text":
        # Iterate over the dictionary and print the selected information
        ParentTable = tt.Texttable()
        ParentTable.set_cols_width([15, 60])
        ParentTable.set_cols_align(['c', 'c'])
        ParentTable.set_cols_valign(['m', 'm'])
        headerList = ['id', 'type', 'cpcode', 'encoderZone',
                        'backupEncoderZone', 'hostName', 'backupHostName', 'status', 'activeVersion', 'amdProperties','modifiedDate','activeVersion']
        for key in headerList:
            Parentrow = [key,originInfo[key]]
            ParentTable.add_row(Parentrow)

        MainParentTable = ParentTable.draw()
        print(MainParentTable)


def formatOutputContract(contractInfo, output_type):
    """ Formats the output on a given format (json or text) """
    if output_type == "json":
        # Let's print the JSON
        print(json.dumps(contractInfo, indent=2))

    if output_type == "text":
        # Iterate over the dictionary and print the selected information
        ParentTable = tt.Texttable()
        ParentTable.set_cols_width([30,15, 15])
        ParentTable.set_cols_align(['c','c','c'])
        ParentTable.set_cols_valign(['m','m','m'])
        Parentheader = ['Contract Name','Contract ID', 'Account ID']
        ParentTable.header(Parentheader)
        for my_item in contractInfo:
            Parentrow = [my_item["contractName"], my_item["contractId"], my_item["accountId"]]
            ParentTable.add_row(Parentrow)
        MainParentTable = ParentTable.draw()
        print(MainParentTable)


def formatOutputEncoderLocationsList(encoderLocationsList,output_type):
    """ Formats the output on a given format (json or text) """
    if output_type == "json":
        print(json.dumps(encoderLocationsList, indent=2))
    if output_type == "text":
        # Iterate over the dictionary and print the selected information
        ParentTable = tt.Texttable()
        ParentTable.set_cols_width([25])
        ParentTable.set_cols_align(['c'])
        ParentTable.set_cols_valign(['m'])
        Parentheader = ['Locations']
        ParentTable.header(Parentheader)
        for my_item in encoderLocationsList:
            Parentrow = [my_item["location"]]
            ParentTable.add_row(Parentrow)
        MainParentTable = ParentTable.draw()
        print(MainParentTable)

def formatOutputvodOriginsList(vodOriginsList, output_type):
    """ Formats the output on a given format (json or text) """
    if output_type == "json":
        print(json.dumps(vodOriginsList, indent=2))
    if output_type == "text":
        # Iterate over the dictionary and print the selected information
        ParentTable = tt.Texttable()
        ParentTable.set_cols_width([30,10, 10])
        ParentTable.set_cols_align(['c','c','c'])
        ParentTable.set_cols_valign(['m','m','m'])
        Parentheader = ['Name','CPCode', 'StreamCount']
        ParentTable.header(Parentheader)
        for my_item in vodOriginsList:
            Parentrow = [my_item["name"], my_item["cpcode"], my_item["streamCount"]]
            ParentTable.add_row(Parentrow)
        MainParentTable = ParentTable.draw()
        print(MainParentTable)

def formatOutputCPCodeLiveOrigin(cpcodeOriginList, output_type):
    """ Formats the output on a given format (json or text) """
    if output_type == "json":
        print(json.dumps(cpcodeOriginList, indent=2))
    if output_type == "text":
        # Iterate over the dictionary and print the selected information
        ParentTable = tt.Texttable()
        ParentTable.set_cols_width([15,20])
        ParentTable.set_cols_align(['c','c'])
        ParentTable.set_cols_valign(['m','m'])
        Parentheader = ['CPCode','Name']
        ParentTable.header(Parentheader)
        for my_item in cpcodeOriginList:
            Parentrow = [my_item["id"], my_item["name"]]
            ParentTable.add_row(Parentrow)
        MainParentTable = ParentTable.draw()
        print(MainParentTable)

def formatOutputCDNList(cdnList, output_type):
    """ Formats the output on a given format (json or text) """
    if output_type == "json":
        # Let's print the JSON
        print(json.dumps(cdnList, indent=2))

    if output_type == "text":
        # Iterate over the dictionary and print the selected information
        ParentTable = tt.Texttable()
        ParentTable.set_cols_width([15, 15])
        ParentTable.set_cols_align(['c', 'c'])
        ParentTable.set_cols_valign(['m', 'm'])
        Parentheader = ['Code', 'CDN Name']
        ParentTable.header(Parentheader)
        for each_item in cdnList:
            Parentrow = [each_item["code"], each_item["name"]]
            ParentTable.add_row(Parentrow)
        MainParentTable = ParentTable.draw()
        print(MainParentTable)


def formatOutputGeneric(list):
    print(json.dumps(list, indent=2))

def formatOutputCPCodelist(cpcodelist, output_type):
    if output_type == "json":
        # Let's print the JSON
        print(json.dumps(cpcodelist, indent=2))

    if output_type == "text":
        # Iterate over the dictionary and print the selected information
        ParentTable = tt.Texttable()
        ParentTable.set_cols_width([15, 28, 20])
        ParentTable.set_cols_align(['c', 'c', 'c'])
        ParentTable.set_cols_valign(['m', 'm', 'm'])
        Parentheader = ['CPcode', 'Name', 'ContractId']
        ParentTable.header(Parentheader)
        for each_item in cpcodelist:
            Parentrow = [each_item["id"], each_item["name"], str(each_item["contractIds"])]
            ParentTable.add_row(Parentrow)
        MainParentTable = ParentTable.draw()
        print(MainParentTable)
