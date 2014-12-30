from boto.s3.connection import S3Connection
from boto.s3.key import Key

import ntpath
from urlparse import urlparse

class S3:

    def __init__(self, access_key, secret_key, bucket):
        self.connection = S3Connection(access_key, secret_key)
        self.bucket = self.connection.get_bucket(bucket)

    def upload_file(self, screenshot, public_read=False, s3_path = ""):
        if screenshot.last_used_filename is None:
            raise Exception("No screenshot has been taken")

        file_name = ntpath.basename(screenshot.last_used_filename)
        full_s3_path = s3_path + "/" + file_name

        s3_key = Key(self.bucket)
        s3_key.key = full_s3_path
        s3_key.set_contents_from_filename(screenshot.last_used_filename)

        if public_read:
            s3_key.set_acl('public-read')
            full_url = s3_key.generate_url(expires_in=60)
            # strip out access key, etc since it's public
            parsed_url = urlparse(full_url)
            public_url = parsed_url.scheme + "://" +  parsed_url.netloc + parsed_url.path

            return public_url

