# Lightshot

A lightweight RESTful API for taking screenshots of web sites.
Screenshots can be stored locally or uploaded to AWS S3.

Usage example:

```
$ curl 127.0.0.1:5000/generate?url=http://google.com

{
  "path": "shots/1405200668_httpgooglecom.jpg",
  "success": true
}
```

With uploading to S3 enabled:

```
$ curl 127.0.0.1:5000/generate?url=http://google.com

{
  "s3_url": "https://lightshot.s3.amazonaws.com/1419887713_httpgooglecom.jpg",
  "success": true
}
```

## Installation

### Automated Installation

If you are using Mac, Linux or other Unix system, run ```install.sh``` which will complete the steps described bellow.

### Manual Installation

Dependencies  can be installed using pip:

```
pip install --pre -r requirements.txt
```

Also, make sure that `shots` directory is writeable, and logging directory exists and is writable.

## Configuration

The value of an environment variable `LIGHTSHOT_SETTINGS` should be the path to the configuration file. Running
`run.sh` will do that for you.

An example configuration file is included in config/default.config.