import requests                 # for making HTTP requests
import json                     # library for handling JSON data
import time                     # module for sleep operation

from boltiot import Bolt        # importing Bolt from boltiot module
import conf                     # config file

mybolt = Bolt(conf.bolt_api_key, conf.device_id)

