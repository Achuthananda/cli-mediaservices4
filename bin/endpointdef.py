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
"""

from __future__ import print_function
import sys
import os
import logging
import random
import re
import requests
import json
import urllib
import texttable as tt
from future import standard_library
from future.builtins import next
from future.builtins import object
from http_calls import EdgeGridHttpCaller
from akamai.edgegrid import EdgeGridAuth, EdgeRc
from config import EdgeGridConfig
from subprocess import call
standard_library.install_aliases()
if sys.version_info[0] >= 3:
    # python3
    from urllib import parse
else:
    # python2.7
    import urlparse as parse

logger = logging.getLogger(__name__)

session = requests.Session()
debug = False
verbose = False
cache = False
format = "json"
section_name = "default"

# If all parameters are set already, use them.  Otherwise
# use the config
config = EdgeGridConfig({"verbose": False}, section_name)

if hasattr(config, "debug") and config.debug:
    debug = True

if hasattr(config, "verbose") and config.verbose:
    verbose = True

if hasattr(config, "cache") and config.cache:
    cache = True


# Set the config options
session.auth = EdgeGridAuth(
    client_token=config.client_token,
    client_secret=config.client_secret,
    access_token=config.access_token
)

if hasattr(config, 'headers'):
    session.headers.update(config.headers)

session.headers.update({'User-Agent': "AkamaiCLI"})

baseurl_prd = '%s://%s/' % ('https', config.host)
prdHttpCaller = EdgeGridHttpCaller(session, debug, verbose, baseurl_prd)


def listStreams(accountSwitchKey=None):
    """ Get list of MSL streams"""
    listStreamsEndpoint = '/config-media-live/v2/msl-origin/streams'
    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey,
                  'sortKey': 'createdDate',
                  'sortOrder': 'DESC'
                  }
        streamList = prdHttpCaller.getResult(listStreamsEndpoint, params)
    else:
        params = {'sortKey': 'createdDate',
                  'sortOrder': 'DESC'
                  }
        streamList = prdHttpCaller.getResult(listStreamsEndpoint,params)
    return streamList

def listLiveOrigins(accountSwitchKey=None):
    """ Get list of MSL streams"""
    listLiveOriginsEndpoint = '/config-media-live/v2/msl-origin/origins'
    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey}
        liveOriginList = prdHttpCaller.getResult(listLiveOriginsEndpoint, params)
    else:
        liveOriginList = prdHttpCaller.getResult(listLiveOriginsEndpoint)
    return liveOriginList


def getStream(accountSwitchKey, streamid):
    "Get a stream details"
    getStreamsEndpoint = '/config-media-live/v2/msl-origin/streams/{streamId}'.format(
        streamId=streamid)
    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey
                  }
        streaminfo = prdHttpCaller.getResult(getStreamsEndpoint, params)
    else:
        streaminfo = prdHttpCaller.getResult(getStreamsEndpoint)
    return streaminfo

def getOrigin(accountSwitchKey, originId):
    "Get origin details"
    getoriginEndpoint = '/config-media-live/v2/msl-origin/origins/{originId}'.format(originId=originId)
    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey}
        originInfo = prdHttpCaller.getResult(getoriginEndpoint, params)
    else:
        originInfo = prdHttpCaller.getResult(getoriginEndpoint)
    return originInfo

def listCDNs(accountSwitchKey=None):
    """ Get list of CDN's """
    listcdnsEndpoint = '/config-media-live/v2/msl-origin/cdns'
    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey
                  }
        cdnList = prdHttpCaller.getResult(listcdnsEndpoint, params)
    else:
        cdnList = prdHttpCaller.getResult(listcdnsEndpoint)
    return cdnList

def getCpCodeLO(accountSwitchKey=None):
    """ Get list of CDN's """
    cpCodeLOEndpoint = '/config-media-live/v2/msl-origin/origins/cpcodes'
    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey
                  }
        cpCodeLOList = prdHttpCaller.getResult(cpCodeLOEndpoint, params)
    else:
        cpCodeLOList = prdHttpCaller.getResult(cpCodeLOEndpoint)
    return cpCodeLOList

def getContracts(accountSwitchKey=None):
    """ Get list of CDN's """
    contractsEndpoint = '/config-media-live/v2/msl-origin/contracts'
    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey
                  }
        contractList = prdHttpCaller.getResult(contractsEndpoint, params)
    else:
        contractList = prdHttpCaller.getResult(contractsEndpoint)
    return contractList

def generateKey(accountSwitchKey=None,keytype=None):
    """ Generate Key"""
    genKeyEndpoint = '/config-media-live/v2/msl-origin/generate-key'
    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey}
        params["type"] = keytype
        key = prdHttpCaller.getResult(genKeyEndpoint, params)
    else:
        parms = {'type':keytype}
        key = prdHttpCaller.getResult(genKeyEndpoint,params)
    return key

def listVODOrigins(accountSwitchKey, encoderLocation):
    "Get List of VOD Origins"
    listVODOriginsEndpoint = '/config-media-live/v2/msl-origin/vod-origin?encoderLocation={}'.format(encoderLocation)
    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey}
        vodOriginList = prdHttpCaller.getResult(listVODOriginsEndpoint, params)
    else:
        vodOriginList = prdHttpCaller.getResult(listVODOriginsEndpoint)
    return vodOriginList

def listEncoderLocations(accountSwitchKey):
    listEncoderLocationEndPoint = '/config-media-live/v2/msl-origin/publishing-locations'
    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey}
        encoderLocationList = prdHttpCaller.getResult(listEncoderLocationEndPoint, params)
    else:
        encoderLocationList = prdHttpCaller.getResult(listEncoderLocationEndPoint)
    return encoderLocationList

def createLiveOrigin(accountSwitchKey, jsonLocation):
    createOriginEndPoint = '/config-media-live/v2/msl-origin/origins'
    file = open(jsonLocation,'r')
    originData = json.load(file)
    originData = json.dumps(originData)
    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey}
        status,createOriginResp = prdHttpCaller.postResult(createOriginEndPoint, originData,params)
    else:
        status,createOriginResp = prdHttpCaller.postResult(createOriginEndPoint,originData)
    return status,createOriginResp

def createStream(accountSwitchKey, jsonLocation):
    createStreamEndPoint = '/config-media-live/v2/msl-origin/streams'
    file = open(jsonLocation,'r')
    streamData = json.load(file)
    streamData = json.dumps(streamData)
    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey}
        status,createStreamResp = prdHttpCaller.postResult(createStreamEndPoint,streamData,params)
    else:
        status,createStreamResp = prdHttpCaller.postResult(createStreamEndPoint,streamData)
    return status,createStreamResp


def updateLiveOrigin(accountSwitchKey,originId,jsonLocation):
    updateOriginEndPoint = '/config-media-live/v2/msl-origin/origins/{originId}'.format(originId=originId)
    file = open(jsonLocation,'r')
    originData = json.load(file)
    originData = json.dumps(originData)
    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey}
        status,updateOriginResp = prdHttpCaller.putResult(updateOriginEndPoint,originData,params)
    else:
        status,updateOriginResp = prdHttpCaller.putResult(updateOriginEndPoint,originData)
    return status,updateOriginResp

def updateStream(accountSwitchKey,streamId,jsonLocation):
    updateStreamEndPoint = '/config-media-live/v2/msl-origin/streams/{streamId}'.format(streamId=streamId)
    file = open(jsonLocation,'r')
    streamData = json.load(file)
    streamData = json.dumps(streamData)
    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey}
        status,updateStreamResp = prdHttpCaller.putResult(updateStreamEndPoint,streamData,params)
    else:
        status,updateStreamResp = prdHttpCaller.putResult(updateStreamEndPoint,streamData)
    return status,updateStreamResp

def createCPCode(accountSwitchKey,contract,cpcodeName):
    createCPCodePoint = '/config-media-live/v2/msl-origin/cpcodes'

    cpCodeData = {}
    cpCodeData["name"] = cpcodeName
    cpCodeData["contractId"] = contract
    cpCodeData= json.dumps(cpCodeData)

    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey}
        status,createCPCodeResp = prdHttpCaller.postResult(createCPCodePoint,cpCodeData,params)
    else:
        status,createCPCodeResp = prdHttpCaller.postResult(createCPCodePoint,cpCodeData)
    return status,createCPCodeResp

def listCPCodes(accountSwitchKey=None, type="INGEST", unused="true"):
    """ Get list of cpcodes """
    listcpcodeEndpoint = '/config-media-live/v2/msl-origin/cpcodes'
    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey,
                  'type': type,
                  'unused': unused

                  }
        cpcodeList = prdHttpCaller.getResult(listcpcodeEndpoint, params)
    else:
        params = {
            'type': type,
            'unused': unused
        }
        cpcodeList = prdHttpCaller.getResult(listcpcodeEndpoint, params)
    return cpcodeList

def deleteStream(accountSwitchKey,streamId,purge):
    deleteStreamEndPoint = '/config-media-live/v2/msl-origin/streams/{streamId}'.format(streamId=streamId)
    params = {}
    params["purgeContent"] = purge.lower()
    if accountSwitchKey:
        params['accountSwitchKey'] =  accountSwitchKey

    status,deleteResp = prdHttpCaller.deleteResult(deleteStreamEndPoint,params)
    return status

def deleteOrigin(accountSwitchKey,originId):
    deleteoriginEndPoint = '/config-media-live/v2/msl-origin/origins/{originId}'.format(originId=originId)

    if accountSwitchKey:
        params = {'accountSwitchKey': accountSwitchKey}
        status,deleteOriginResp = prdHttpCaller.deleteResult(deleteoriginEndPoint,params)
    else:
        status,deleteOriginResp = prdHttpCaller.deleteResult(deleteoriginEndPoint)
    return status
