import django.conf.global_settings as DEFAULT_SETTINGS
from settings import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

ANSWER_FILE_DIR = '/var/lib/vmos/answers'

# Template schema:
# - <container_name>
#     - <group_name>
#         - <section_name>
#             - id: <attribute_id>
#               name: <attribute_name>
#               default: <optional_default_value>
#
# Keep all list items in the order that they should appear in when displayed.
# Each container and group is a heading in the nav menu for the "Prepare" step.
# Keys for the answer file are stored in the "id" attribute of the sections.
# Each section is displayed as a part of the form for its group.
ANSWER_FILE_BASE = 'base.yml'
# TODO: Allow user to choose file.
ANSWER_FILE_DEFAULT = 'default.yml'

VMOS_LOG_DIR = '/var/lib/vmos/logs'

NSX_DEPLOY_LOG = 'nsx-deploy.log'
NSX_CONFIGURE_LOG = 'nsx-configure.log'
SDDC_DEPLOY_LOG = 'sddc-deploy.log'
SDDC_CONFIGURE_LOG = 'sddc-configure.log'

DEBUG_OPTION = '-vvvv'

# List each command and its arguments.
NSX_DEPLOY_VALIDATE = []
NSX_DEPLOY_RUN = []
NSX_CONFIGURE_VALIDATE = []
NSX_CONFIGURE_RUN = []

SDDC_DEPLOY_VALIDATE = []
SDDC_DEPLOY_RUN = []
SDDC_CONFIGURE_VALIDATE = []
SDDC_CONFIGURE_RUN = []