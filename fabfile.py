from fabric.api import *

# the user to use for the remote commands
env.user = 'root'
env.password = 'helloworld'
# the servers where the commands are executed
env.hosts = ['162.243.249.136']

def pack():
    # create a new source distribution as tarball
    local('python setup.py sdist --formats=gztar', capture=False)

def deploy():
    # figure out the release name and version
    dist = local('python setup.py --fullname', capture=True).strip()
    # upload the source tarball to the temporary folder on the server
    put('dist/%s.tar.gz' % dist, '/tmp/lightshot.tar.gz')
    # create a place where we can unzip the tarball, then enter
    # that directory and unzip it
    run('mkdir -p /tmp/lightshot')
    with cd('/tmp/lightshot'):
        run('tar xzf /tmp/lightshot.tar.gz')

    with cd('/tmp/lightshot/{dist}'.format(dist=dist)):
        # now setup the package with our virtual environment's
        # python interpreter
        run('/var/www/lightshot/env/bin/python setup.py install')
    # now that all is set up, delete the folder again
    run('rm -rf /tmp/lightshot /tmp/lightshot.tar.gz')
    # and finally touch the .wsgi file so that mod_wsgi triggers
    # a reload of the application
    run('touch /var/www/lightshot.wsgi')