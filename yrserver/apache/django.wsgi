import os,sys
import site


apache_configuration = os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace)
sys.path.append(project)

from ConfigParser import RawConfigParser

config = RawConfigParser()
configFile = os.path.join(workspace, 'config','config.ini')
config.read(configFile)

SITE_PACKAGES_DIRECTORY = config.get('wsgi', 'SITE_PACKAGES_DIRECTORY')

site.addsitedir(SITE_PACKAGES_DIRECTORY)

os.environ['DJANGO_SETTINGS_MODULE'] = 'yrserver.settings'

import django.core.wsgi
application = django.core.wsgi.get_wsgi_application()
