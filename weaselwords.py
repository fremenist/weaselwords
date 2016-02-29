#!/usr/bin/python

import sys, json

with open ("weaselwords.json") as wordsfile:
	parsed_json = json.load (wordsfile)

	for line in sys.stdin:

		if line.lower().strip() in parsed_json:
			print parsed_json[line.lower().strip()]
		else:
			sys.exit(1)
