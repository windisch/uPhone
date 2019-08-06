# boot.py -- run on boot-up
# can run arbitrary Python, but best to keep it minimal

import machine
import pyb
pyb.main('main.py') # main script to run after this one
pyb.country('US') # ISO 3166-1 Alpha-2 code, eg US, GB, DE, AU
