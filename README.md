A lightweight RESTful API for taking screenshots of web sites.
It is simple and has a minimal feature set by design.

```
$ python run.py 
$ curl 127.0.0.1:5000/generate?url=http://google.com

{
  "path": "shots/1405200668_httpgooglecom.jpg",
  "success": true
}
```

## Installation

### Automated Installation

If you are using Mac, Linux or other Unix system, run ```install.sh``` which will complete the steps described bellow.

### Manual Installation

Dependencies  can be installed using pip:

```
pip install -r requirements.txt
```

Also, make sure that `shots` directory is writeable:

```
chmod u+x shots/
```

## Roadmap

For v1.0, the following features are planned:

* Saving to Amazon S3
* Documentation
