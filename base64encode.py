#!/usr/bin/env python

import base64
from optparse import OptionParser
import sys

def get_arguments():

	parser = OptionParser()
	parser.add_option("-d", "--decode", dest="decode", help="Decode your string")
	parser.add_option("-e", "--encode", dest="encode", help="Encode your string")
	(options, arguments) = parser.parse_args()

	if options.decode is None and options.encode is None:

		print("[*] python base64.py -h for help")
		sys.exit()

	return options

crypt = get_arguments()

if crypt.decode is None and crypt.encode is None:
    print("[*] python base64.py -h for help")
    sys.exit()

# Encoding
if crypt.encode is not None:
    encoded_string = base64.b64encode(crypt.encode.encode('utf-8')).decode('utf-8')
    print(encoded_string)

# Decoding
elif crypt.decode is not None:
    try:
        decoded_string = base64.b64decode(crypt.decode.encode('utf-8')).decode('utf-8')
        print(decoded_string)
        
    except base64.binascii.Error as e:
        print(f"Error decoding: {e}")