#!C:\Users\kryst\Documents\Django-habits-reminder\Django-habits-reminder\Django-habits-reminder\django-habits\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'libsass==0.19.4','console_scripts','pysassc'
__requires__ = 'libsass==0.19.4'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('libsass==0.19.4', 'console_scripts', 'pysassc')()
    )
