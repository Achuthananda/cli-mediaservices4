# Akamai CLI: Media Services 4

This module enables the use of MSL4 in the Akamai CLI tool

## API Permissions

Please ensure your API client has access to the "Media Streaming" API.

## Install

To install, use [Akamai CLI](https://github.com/akamai/cli):

```
$akamai install https://github.com/Achuthananda/cli-mediaservices4.git
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
- `update-origin` - Update live origin.
- `update-stream` - Update live stream.
- `cpcodes` — Get list of CPcodes.
- `cdns` —   Get list of CDNs
- `create-stream` — Create live stream.
- `cpcodes-liveorigin` —   Get Available CP Codes For Live Origin.
- `contracts` — Fetch MSL Contracts
- `delete-stream` - Delete a MSL Stream
- `delete-origin` - Delete a MSL Origin

## Examples

#### Help
This displays the usage of MediaServices4 Akamai CLI.
```
$akamai msl4 --help
usage: akamai msl4 [-h] [--verbose] [--debug] [--edgerc credentials_file]
                   [--section credentials_file_section]
                   [--accountSwitchKey Account Switch Key]
                   {streams,get-stream,live-origins,get-liveorigin,encoderlocations,generate-key,vod-origins,create-origin,create-stream,update-origin,update-stream,create-cpcode,cpcodes,cdns,cpcodes-liveorigin,contracts,delete-stream,delete-origin}
                   ...

Process command line options.

positional arguments:
  {streams,get-stream,live-origins,get-liveorigin,encoderlocations,generate-key,vod-origins,create-origin,create-stream,update-origin,update-stream,create-cpcode,cpcodes,cdns,cpcodes-liveorigin,contracts,delete-stream,delete-origin}
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
    update-origin       Update live origin.
    update-stream       Update live stream.
    create-cpcode       Create a CP Code.
    cpcodes             Get list of CPcodes
    cdns                Get list of CDNs
    cpcodes-liveorigin  Get Available CP Codes For Live Origin.
    contracts           Fetch MSL Contracts
    delete-stream       Delete a MSL Stream
    delete-origin       Delete a MSL Origin

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

#### Get list of all available encoder locations.
This shows the list of all available encoder locations.
```
$akamai msl4 encoderlocations
+---------------------------+
|         Locations         |
+===========================+
|          EUROPE           |
+---------------------------+
|       NORTH_AMERICA       |
+---------------------------+
|       LATIN_AMERICA       |
+---------------------------+
|       SOUTH_AMERICA       |
+---------------------------+
|          NORDICS          |
+---------------------------+
|       ASIA_PACIFIC        |
+---------------------------+
|      OTHER_AMERICAS       |
+---------------------------+
|         OTHER_APJ         |
+---------------------------+
|        OTHER_EMEA         |
+---------------------------+
|          GERMANY          |
+---------------------------+
|           INDIA           |
+---------------------------+
|           ITALY           |
+---------------------------+
|           JAPAN           |
+---------------------------+
|          MEXICO           |
+---------------------------+
|          TAIWAN           |
+---------------------------+
|      UNITED_KINGDOM       |
+---------------------------+
|          US_EAST          |
+---------------------------+
|        US_CENTRAL         |
+---------------------------+
|          US_WEST          |
+---------------------------+
|         AUSTRALIA         |
+---------------------------+
```

#### Generate the key in both Akamai and Third Party format.
This shows the list of all available encoder locations.
```
$ akamai msl4 generate-key --h
usage: akamai-msl4 generate-key [-h] [--key-type AKAMAI/THIRD_PARTY]

optional arguments:
  -h, --help            show this help message and exit
  --key-type AKAMAI/THIRD_PARTY, -k AKAMAI/THIRD_PARTY
                        Key Type {AKAMAI,THIRD_PARTY}. Default is AKAMAI

```
```
$akamai msl4 generate-key -k AKAMAI
{
  "key": "d3956c487sa63ba8842"
}
```

#### Create the Stream
This CLI creates the stream. It takes the stream settings as input in json file.
Sample input can be found [here](https://github.com/Achuthananda/cli-msl4/blob/master/stream.json)
```
$akamai msl4 create-stream --h
usage: akamai-msl4 create-stream [-h] [--output-type json/text] streamjsonFile

positional arguments:
  streamjsonFile        Location of the json

optional arguments:
  -h, --help            show this help message and exit
  --output-type json/text, -t json/text
                        Output type {json, text}. Default is text
```
```
akamai msl4 create-stream '/Users/apadmana/Desktop/temp/stream.json'
Stream Creation Request Accepted
```

#### Create the Live Origin
This CLI creates the Live Origin. It takes the origin settings as input in json file.
Sample input can be found [here](https://github.com/Achuthananda/cli-msl4/blob/master/origin.json)
```
$:akamai msl4 create-origin --h
usage: akamai msl4 create-origin [-h] [--output-type json/text] originjsonFile

positional arguments:
  originjsonFile        Location of the json

optional arguments:
  -h, --help            show this help message and exit
  --output-type json/text, -t json/text
                        Output type {json, text}. Default is text

```
```
$akamai msl4 create-origin '/Users/apadmana/Desktop/temp/origin.json'
Origin Creation Request Accepted
```


#### Update a Stream
```
$akamai -msl4 -c gss-mediaservices update-stream 2024066 '/Users/apadmana/temp/cli-msl4/udpatestream.json'
Stream Updation Request Accepted
```
#### Update a Origin
```
$akamai msl4 -c gss-mediaservices update-origin 41991 '/Users/apadmana/temp/cli-msl4/updateorigin.json'
Origin Updation  Request Accepted
```

#### Create the CP Code
This CLI creates the CP Code to use.
```
$akamai msl4 create-cpcode --h
usage: akamai msl4 create-cpcode [-h] [--contract CONTRACT]
                                [--cpcodeName CPCODENAME]

optional arguments:
 -h, --help            show this help message and exit
 --contract CONTRACT, -m CONTRACT
                       Contract
 --cpcodeName CPCODENAME, -n CPCODENAME
                       CP Code Name
```
```
$akamai msl4 -c gss-mediaservices create-cpcode -m C-1IE2XHM -n streamcpcode1
{
  "id": 1142464,
  "name": "streamcpcode1",
  "contractId": "C-1IE2OHM"
}
```

#### Get the list of CP Codes
```
$akamai msl4 -c gss-mediaservices cpcodes
+-----------------+------------------------------+----------------------+
|     CPcode      |             Name             |      ContractId      |
+=================+==============================+======================+
|     926793      |            509887            |    ['C-1IE2OHM']     |
+-----------------+------------------------------+----------------------+
|     940507      |             vebr             |    ['C-1IE2OHM']     |
+-----------------+------------------------------+----------------------+
|     940856      |           hgurudat           |    ['C-1IE2OHM']     |
+-----------------+------------------------------+----------------------+
|     954899      |  dk-livestream--lab-cpcode   |    ['C-1IE2OHM']     |
+-----------------+------------------------------+----------------------+
|     955302      |            858687            |    ['C-1IE2OHM']     |
+-----------------+------------------------------+----------------------+
|     955303      |           sabtest            |    ['C-1IE2OHM']     |
+-----------------+------------------------------+----------------------+
|     956550      |         adsilva-msl          |    ['C-1IE2OHM']     |
+-----------------+------------------------------+----------------------+
|     1049749     |           mguheMSL           |    ['C-1IE2OHM']     |
+-----------------+------------------------------+----------------------+
|     1057047     |           rysuzuk            |    ['C-1IE2OHM']     |
+-----------------+------------------------------+----------------------+
```

#### Get the list of CP Codes available for Live Origin
```
$akamai msl4 -c gss-mediaservices cpcodes-liveorigin
[
  {
    "id": 933248,
    "name": "jcl MSL4 lab",
    "contracts": [
      {
        "contractId": "C-1IE2OHM"
      }
    ],
    "contractIds": [
      "C-1IE2OHM"
    ]
  }
]
```
```
$akamai msl4 -c gss-mediaservices cpcodes-liveorigin
+-----------------+----------------------+
|     CPCode      |         Name         |
+=================+======================+
|     933248      |     jcl MSL4 lab     |
+-----------------+----------------------+

```

#### Get the details of contracts in the account
```
$akamai msl4 -c gss-mediaservices contracts
+--------------------------------+-----------------+-----------------+
|         Contract Name          |   Contract ID   |   Account ID    |
+================================+=================+=================+
|   Top-Level Group: C-1IE2OHM   |    C-1IE2OHM    |   B-C-1IE2OH8   |
+--------------------------------+-----------------+-----------------+
```

#### Delete a Stream
```
$akamai msl4 -c gss-mediaservices delete-stream 2024791
Stream Succesfully Deleted
```

#### Delete an Origin
```
$akamai msl4 -c gss-mediaservices delete-origin 41988
Origin Deletion Request Accepted
```
