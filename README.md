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
