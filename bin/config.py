# Python edgegrid module - CONFIG for ImgMan CLI module
""" Copyright 2017 Akamai Technologies, Inc. All Rights Reserved.

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

import sys
import os
import argparse
import logging

if sys.version_info[0] >= 3:
    # python3
    from configparser import ConfigParser
    import http.client as http_client
else:
    # python2.7
    from ConfigParser import ConfigParser
    import httplib as http_client

PACKAGE_VERSION = "0.1.8"

logger = logging.getLogger(__name__)


class EdgeGridConfig():

    parser = argparse.ArgumentParser(description='Process command line options.')

    def __init__(self, config_values, configuration, flags=None):
        parser = self.parser
        parser.add_argument('--verbose', '-v', default=False, action='count', help=' Verbose mode')
        parser.add_argument('--debug', '-d', default=False, action='count',
                            help=' Debug mode (prints HTTP headers)')
        parser.add_argument('--edgerc', '-e', default='~/.edgerc', metavar='credentials_file',
                            help=' Location of the credentials file (default is ~/.edgerc)')
        parser.add_argument('--section', '-c', default='mediaservices', metavar='credentials_file_section',
                            action='store', help=' Credentials file Section\'s name to use')
        parser.add_argument('--accountSwitchKey', '-a', metavar='Account Switch Key',
                            action='store', help=' Switch key to different account')

        subparsers = parser.add_subparsers(help='commands', dest="command")

        list_streams_parser = subparsers.add_parser(
            "streams", help="List all MSL Streams.")
        list_streams_parser.add_argument('--output-type', '-t', default='text', choices=[
                                             'json', 'text'], metavar='json/text', help=' Output type {json, text}. Default is text')

        get_stream_parser = subparsers.add_parser(
            "get-stream", help="Get details of a MSL Stream.")
        get_stream_parser.add_argument('streamid', help="Stream Id", action='store')
        get_stream_parser.add_argument('--output-type', '-t', default='text', choices=[
            'json', 'text'], metavar='json/text', help=' Output type {json, text}. Default is text')

        list_liveorigin_parser = subparsers.add_parser(
            "live-origins", help="List all Live Origins.")
        list_liveorigin_parser.add_argument('--output-type', '-t', default='text', choices=[
                                             'json', 'text'], metavar='json/text', help=' Output type {json, text}. Default is text')

        get_origin_parser = subparsers.add_parser(
            "get-liveorigin", help="Get details of a MSL Live Origin")
        get_origin_parser.add_argument('originid', help="Origin Id", action='store')
        get_origin_parser.add_argument('--output-type', '-t', default='text', choices=[
            'json', 'text'], metavar='json/text', help=' Output type {json, text}. Default is text')

        get_encoderLocations_parser = subparsers.add_parser("encoderlocations", help="Get list of All Encoder Locations")
        get_encoderLocations_parser.add_argument('--output-type', '-t', default='text', choices=[
            'json', 'text'], metavar='json/text', help=' Output type {json, text}. Default is text')

        get_key_parser = subparsers.add_parser("generate-key", help="Generate the Key")
        get_key_parser.add_argument('--key-type', '-k', default='AKAMAI', choices=[
            'AKAMAI', 'THIRD_PARTY'], metavar='AKAMAI/THIRD_PARTY', help=' Key Type {AKAMAI,THIRD_PARTY}. Default is AKAMAI')


        list_vod_origin_parser = subparsers.add_parser(
            "vod-origins", help="Get list of VOD Origins.")
        list_vod_origin_parser.add_argument('encoderLocation', help="Location of the Encoder", action='store')
        list_vod_origin_parser.add_argument('--output-type', '-t', default='text', choices=[
            'json', 'text'], metavar='json/text', help=' Output type {json, text}. Default is text')


        create_live_origin_parser = subparsers.add_parser(
            "create-origin", help="Create live origin.")
        create_live_origin_parser.add_argument('originjsonFile', help="Location of the json", action='store')
        create_live_origin_parser.add_argument('--output-type', '-t', default='text', choices=[
            'json', 'text'], metavar='json/text', help=' Output type {json, text}. Default is text')

        createstream_parser = subparsers.add_parser(
            "create-stream", help="Create live stream.")
        createstream_parser.add_argument('streamjsonFile', help="Location of the json", action='store')
        createstream_parser.add_argument('--output-type', '-t', default='text', choices=[
            'json', 'text'], metavar='json/text', help=' Output type {json, text}. Default is text')


        update_live_origin_parser = subparsers.add_parser(
            "update-origin", help="Update live origin.")
        update_live_origin_parser.add_argument('originId', help="Origin Id", action='store')
        update_live_origin_parser.add_argument('originjsonFile', help="Location of the json", action='store')
        update_live_origin_parser.add_argument('--output-type', '-t', default='text', choices=[
            'json', 'text'], metavar='json/text', help=' Output type {json, text}. Default is text')

        updatestream_parser = subparsers.add_parser(
            "update-stream", help="Update live stream.")
        updatestream_parser.add_argument('streamId', help="Stream Id", action='store')
        updatestream_parser.add_argument('streamjsonFile', help="Location of the json", action='store')
        updatestream_parser.add_argument('--output-type', '-t', default='text', choices=[
            'json', 'text'], metavar='json/text', help=' Output type {json, text}. Default is text')

        createcpcode_parser = subparsers.add_parser(
            "create-cpcode", help="Create a CP Code.")
        createcpcode_parser.add_argument('--contract', '-m', help='Contract')
        createcpcode_parser.add_argument('--cpcodeName', '-n', help='CP Code Name')


        get_cpcode_list_parser = subparsers.add_parser("cpcodes", help="Get list of CPcodes")
        get_cpcode_list_parser.add_argument('--type', default='INGEST', choices=[
            'INGEST', 'STORAGE', 'DELIVERY'], help='Identify the cpcode type')
        get_cpcode_list_parser.add_argument('--unused', default='true', choices=[
            'true', 'false'], help=' lists only CP codes that have not already been used to provision an origin')
        get_cpcode_list_parser.add_argument('--output-type', '-t', default='text', choices=[
            'json', 'text'], metavar='json/text', help=' Output type {json, text}. Default is text')


        get_cdn_list_parser = subparsers.add_parser("cdns", help="Get list of CDNs")
        get_cdn_list_parser.add_argument('--output-type', '-t', default='text', choices=[
            'json', 'text'], metavar='json/text', help=' Output type {json, text}. Default is text')


        get_cpcodeorigin_parser = subparsers.add_parser(
            "cpcodes-liveorigin", help="Get Available CP Codes For Live Origin.")
        get_cpcodeorigin_parser.add_argument('--output-type', '-t', default='text', choices=[
            'json', 'text'], metavar='json/text', help=' Output type {json, text}. Default is text')

        get_contracts_parser = subparsers.add_parser(
            "contracts", help="Fetch MSL Contracts")
        get_contracts_parser.add_argument('--output-type', '-t', default='text', choices=[
            'json', 'text'], metavar='json/text', help=' Output type {json, text}. Default is text')

        delete_stream_parser = subparsers.add_parser(
            "delete-stream", help="Delete a MSL Stream")
        delete_stream_parser.add_argument('streamid', help="Stream Id", action='store')
        delete_stream_parser.add_argument('--purge', '-p', default='false', choices=[
            'true', 'false'], metavar='true/false', help=' Purge Archived Content on Netstorage')

        delete_origin_parser = subparsers.add_parser(
            "delete-origin", help="Delete a MSL Origin")
        delete_origin_parser.add_argument('originid', help="Stream Id", action='store')


        if flags:
            for argument in flags.keys():
                parser.add_argument('--' + argument, action=flags[argument])

        arguments = {}
        for argument in config_values:
            if config_values[argument]:
                if config_values[argument] == "False" or config_values[argument] == "True":
                    parser.add_argument('--' + argument, action='count')
                parser.add_argument('--' + argument)
                arguments[argument] = config_values[argument]

        try:
            args = parser.parse_args()
        except:
            sys.exit()

        arguments = vars(args)

        if arguments['debug']:
            http_client.HTTPConnection.debuglevel = 1
            logging.basicConfig()
            logging.getLogger().setLevel(logging.DEBUG)
            requests_log = logging.getLogger("requests.packages.urllib3")
            requests_log.setLevel(logging.DEBUG)
            requests_log.propagate = True

        if "section" in arguments and arguments["section"]:
            configuration = arguments["section"]

        arguments["edgerc"] = os.path.expanduser(arguments["edgerc"])

        if os.path.isfile(arguments["edgerc"]):
            config = ConfigParser()
            config.readfp(open(arguments["edgerc"]))
            if not config.has_section(configuration):
                err_msg = "ERROR: No section named %s was found in your %s file\n" % (
                    configuration, arguments["edgerc"])
                err_msg += "ERROR: Please generate credentials for the script functionality\n"
                err_msg += "ERROR: and run 'python gen_edgerc.py %s' to generate the credential file\n" % configuration
                sys.exit(err_msg)
            for key, value in config.items(configuration):
                # ConfigParser lowercases magically
                if key not in arguments or arguments[key] is None:
                    arguments[key] = value
                else:
                    print("Missing configuration file.  Run python gen_edgerc.py to get your credentials file set up once you've provisioned credentials in LUNA.")
                    return None

        for option in arguments:
            setattr(self, option, arguments[option])

        self.create_base_url()

    def create_base_url(self):
        self.base_url = "https://%s" % self.host
