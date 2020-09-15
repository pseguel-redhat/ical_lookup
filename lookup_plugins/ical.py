from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

#DOCUMENTATION = '''
#  lookup: ical
#  author: Paulo Seguel <pseguel@gmail.com>
#  short_description: Checks if date is in an ical calendar. Returns boolean.
#  description:
#      - This lookup returns true if an event exists in an iCal calendar in a particular
#      date. If the date is not defined, it will assume current timestamp:
#  options:
#      _date:
#        description: Date to check
#'''
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase
from ansible.utils.display import Display
import ansible.utils as utils

from ics import Calendar
import requests, arrow

display = Display()

class LookupModule(LookupBase):

    def __init__(self, basedir=None, **kwargs):
        self.basedir = basedir

    def run(self, url, instant=None, variables=None, **kwargs):
        # Get iCal from URL
        url = url[0]
        c = Calendar(requests.get(url).text)
        if instant==None: 
            instant = arrow.utcnow()
        else:
            instant = arrow.get(instant)

        display.debug("iCal lookup instant: %s" % instant)
        matching_events = list(c.timeline.at(instant))

        if len(matching_events) == 0:
            return [False]
        else:
            return [True]
