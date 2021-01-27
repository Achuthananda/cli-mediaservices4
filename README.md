# Akamai CLI: Media Services 4

This module enables the use of MSL4 in the Akamai CLI tool

## API Permissions

Please ensure your API client has access to the "Media Streaming" API.

## Install

To install, use [Akamai CLI](https://github.com/akamai/cli):

```
$akamai install https://github.com/Achuthananda/cli-msl4.git
```

You may also use this as a stand-alone command by cloning this repository
and compiling it yourself.

## Usage

```
$akamai msl4 [global flags] Commands
```

## Global Flags
- `--edgerc value` — Location of the credentials file (default: user's directory like "/Users/apadmana") [$AKAMAI_EDGERC]
- `--section value` — Section of the credentials file (default: "mediaservices") [$AKAMAI_EDGERC_SECTION]
- `--debug` - `-d` - prints debug information
- `--verbose` - Print verbose information
- `--version`, `-v` — Print the version
- `--help`, `-h` — Show help

## Commands  
- `streams` —   List all MSL4 streams
- `get-stream ` — Get details of a MSL Stream.
- `live-origins ` —   List all Live Origins.
- `get-liveorigin` — Get details of a MSL Live Origin.
- `encoderlocations ` —   Get list of All Encoder Locations
- `vod-origins` — Get list of VOD Origins..
- `create-origin` —   Create live origin.
- `create-stream` — Create live stream.
- `create-cpcode` —   Create a CP Code..
- `cpcodes` — Get list of CPcodes.
- `cdns` —   Get list of CDNs
- `create-stream` — Create live stream.
- `cpcodes-liveorigin` —   Get Available CP Codes For Live Origin.
- `contracts` — Fetch MSL Contracts

## Examples

#### Help
This displays the usage of MediaServices4 Akamai CLI.
```
$akamai msl4 --help
usage: akamai msl4 [-h] [--verbose] [--debug] [--edgerc credentials_file]
                   [--section credentials_file_section]
                   [--accountSwitchKey Account Switch Key]
                   {streams,get-stream,live-origins,get-liveorigin,encoderlocations,generate-key,vod-origins,create-origin,create-stream,create-cpcode,cpcodes,cdns,cpcodes-liveorigin,contracts}
                   ...

Process command line options.

positional arguments:
  {streams,get-stream,live-origins,get-liveorigin,encoderlocations,generate-key,vod-origins,create-origin,create-stream,create-cpcode,cpcodes,cdns,cpcodes-liveorigin,contracts}
                        commands
    streams             List all MSL Streams.
    get-stream          Get details of a MSL Stream.
    live-origins        List all Live Origins.
    get-liveorigin      Get details of a MSL Live Origin
    encoderlocations    Get list of All Encoder Locations
    generate-key        Generate the Key
    vod-origins         Get list of VOD Origins.
    create-origin       Create live origin.
    create-stream       Create live stream.
    create-cpcode       Create a CP Code.
    cpcodes             Get list of CPcodes
    cdns                Get list of CDN's
    cpcodes-liveorigin  Get Available CP Codes For Live Origin.
    contracts           Fetch MSL Contracts

optional arguments:
  -h, --help            show this help message and exit
  --verbose, -v         Verbose mode
  --debug, -d           Debug mode (prints HTTP headers)
  --edgerc credentials_file, -e credentials_file
                        Location of the credentials file (default is
                        ~/.edgerc)
  --section credentials_file_section, -c credentials_file_section
                        Credentials file Section's name to use
  --accountSwitchKey Account Switch Key, -a Account Switch Key
                        Switch key to different account
```

#### List All the Streams in the Account
This shows all the streams in the Account.
```
$ akamai msl4 streams
+-----------------+--------------------------------+-----------------+-----------------+------------------------------------------+
|       ID        |              Name              |     Format      |     CPcode      |                  Origin                  |
+=================+================================+=================+=================+==========================================+
|     2024123     |       cinnocen-tst-DASH        |      DASH       |     1134561     |   013-dn001-cilivetst.akamaiorigin.net   |
+-----------------+--------------------------------+-----------------+-----------------+------------------------------------------+
|     2024075     |        cinnocen-tst-HLS        |       HLS       |     1134561     |   013-dn001-cilivetst.akamaiorigin.net   |
+-----------------+--------------------------------+-----------------+-----------------+------------------------------------------+
|     2024066     |         ci-livestream          |       HLS       |     1134561     | 013-dn001-ciliveorigin.akamaiorigin.net  |
+-----------------+--------------------------------+-----------------+-----------------+------------------------------------------+
|     2022699     |           TestStream           |      CMAF       |     1108951     | 012-dn001-hgurudliveorigin.akamaiorigin. |
|                 |                                |                 |                 |                   net                    |
+-----------------+--------------------------------+-----------------+-----------------+------------------------------------------+
```

#### List All the Live Origins in the Account.
This shows all the live origins in the Account.
```
$ akamai msl4 list-groups --output-type json
+-----------------------------------------------+------------+------------+-----------------+--------------+
|                   HostName                    |     Id     |   CPCode   |     Encoder     |    Status    |
+===============================================+============+============+=================+==============+
|   002-dn001-parajelestream.akamaiorigin.net   |   39213    |   933248   |  NORTH_AMERICA  | PROVISIONED  |
+-----------------------------------------------+------------+------------+-----------------+--------------+
|    014-dn001-rsliveorigin.akamaiorigin.net    |   32389    |   933248   |      JAPAN      | PROVISIONED  |
+-----------------------------------------------+------------+------------+-----------------+--------------+
|        006-dn001-sab.akamaiorigin.net         |   30183    |   933248   |  ASIA_PACIFIC   | PROVISIONED  |
+-----------------------------------------------+------------+------------+-----------------+--------------+
|  012-dn001-hgurudliveorigin.akamaiorigin.net  |   29184    |   933248   |      INDIA      | PROVISIONED  |
+-----------------------------------------------+------------+------------+-----------------+--------------+
```
#### Get Details of a particular stream.
This shows the details of a stream.
```
$ akamai msl4 -c mediaservices get-stream 2018465
+-----------------+--------------------------------------------------------------+
|       id        |                           2018465                            |
+-----------------+--------------------------------------------------------------+
|      name       |                      achuth-teststream                       |
+-----------------+--------------------------------------------------------------+
|     format      |                             HLS                              |
+-----------------+--------------------------------------------------------------+
|     cpcode      |                            926793                            |
+-----------------+--------------------------------------------------------------+
|     origin      |          008-dn001-acmpteststream1.akamaiorigin.net          |
+-----------------+--------------------------------------------------------------+
|   createdDate   |                   2020-08-05T12:00:53.248Z                   |
+-----------------+--------------------------------------------------------------+
|  modifiedDate   |                   2020-09-24T10:42:42.363Z                   |
+-----------------+--------------------------------------------------------------+
|  storagecpcode  |                            940858                            |
+-----------------+--------------------------------------------------------------+
|   encoderZone   |                          OTHER_APJ                           |
+-----------------+--------------------------------------------------------------+
| primaryPublishi |   p-ep2018465.i.akamaientrypoint.net/2018465/(event_name)    |
|      ngUrl      |                                                              |
+-----------------+--------------------------------------------------------------+
| backupPublishin |  b-ep2018465.i.akamaientrypoint.net/2018465-b/(event_name)   |
|      gUrl       |                                                              |
+-----------------+--------------------------------------------------------------+
|   allowedIps    | ['52.47.171.50/32', '15.236.12.107/32', '15.236.243.99/32']  |
+-----------------+--------------------------------------------------------------+
```

#### Get Details of a particular stream in json format.
This shows the details of a stream in json
```
$akamai msl4 -c mediaservices get-stream 2018465 -t json
{
  "id": 2018465,
  "name": "achuth-teststream",
  "format": "HLS",
  "type": "MSL4",
  "cpcode": 926793,
  "ingestAccelerated": false,
  "allowedIps": [
    "52.47.171.50/32",
    "15.236.12.107/32",
    "15.236.243.99/32"
  ],
  "ingestOptions": {
    "streamId": 2018465
  },
  "encoderZone": "OTHER_APJ",
  "origin": {
    "id": 34983,
    "hostName": "008-dn001-acmpteststream1.akamaiorigin.net",
    "cpcode": 933248
  },
  "primaryPreferredSettings": {
    "preferredEps": [],
    "preferredRegions": [],
    "penalty": null,
    "ignoreRestriction": null
  },
  "backupPreferredSettings": {
    "preferredEps": [],
    "preferredRegions": [],
    "penalty": null,
    "ignoreRestriction": null
  },
  "mapRule": 269,
  "disableDuplicateEviction": false,
  "events": [],
  "createdDate": "2020-08-05T12:00:53.248Z",
  "modifiedDate": "2020-09-24T10:42:42.363Z",
  "createdBy": "apadmana",
  "modifiedBy": "apadmana",
  "provisionDetail": {
    "streamId": 2018465,
    "status": "PROVISIONED",
    "message": "Provisioned"
  },
  "additionalEmailIds": [
    "apadmana@akamai.com"
  ],
  "storageGroup": {
    "cpcode": 940858
  },
  "primaryPublishingUrl": "p-ep2018465.i.akamaientrypoint.net/2018465/(event_name)",
  "backupPublishingUrl": "b-ep2018465.i.akamaientrypoint.net/2018465-b/(event_name)",
  "isDedicatedOrigin": false,
  "tpsSettings": {
    "inactiveOnly": true
  },
  "ingestLimitOverride": {}
}

```
#### Get Details of a Live Origin.
This shows the details of a live origin.
```
$akamai msl4 get-liveorigin --h
usage: akamai msl4 get-liveorigin [-h] [--output-type json/text] originid

positional arguments:
  originid              Stream Id

optional arguments:
  -h, --help            show this help message and exit
  --output-type json/text, -t json/text
                        Output type {json, text}. Default is text
```
```
$akamai msl4 get-liveorigin 33183 -t text
+-----------------+--------------------------------------------------------------+
|       id        |                            33183                             |
+-----------------+--------------------------------------------------------------+
|      type       |                             MSL4                             |
+-----------------+--------------------------------------------------------------+
|     cpcode      |                            933248                            |
+-----------------+--------------------------------------------------------------+
|   encoderZone   |                         ASIA_PACIFIC                         |
+-----------------+--------------------------------------------------------------+
| backupEncoderZo |                          AUSTRALIA                           |
|       ne        |                                                              |
+-----------------+--------------------------------------------------------------+
|    hostName     |           006-dn001-originshield.akamaiorigin.net            |
+-----------------+--------------------------------------------------------------+
| backupHostName  |           010-dn001-originshield.akamaiorigin.net            |
+-----------------+--------------------------------------------------------------+
|     status      |                         PROVISIONED                          |
+-----------------+--------------------------------------------------------------+
|  activeVersion  |                              1                               |
+-----------------+--------------------------------------------------------------+
|  amdProperties  |                              []                              |
+-----------------+--------------------------------------------------------------+
|  modifiedDate   |                   2020-07-01T05:06:02.171Z                   |
+-----------------+--------------------------------------------------------------+
|  activeVersion  |                              1                               |
+-----------------+--------------------------------------------------------------+
```
