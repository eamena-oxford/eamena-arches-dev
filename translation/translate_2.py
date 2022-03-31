#!/usr/bin/python3

# translate a PO file

import os, re, csv, polib, sys
from deep_translator import GoogleTranslator
from deep_translator.exceptions import NotValidPayload

target_language = 'fr'
input_file = 'for_translation_arches-70_djangopo_fr.po'
output_file = 'translated_out.po'
path_fold = os.getcwd()

# read PO
print("Read source file")
po = polib.pofile(os.path.join(path_fold, input_file))
print("  " + str(len(po)) + " lines to write")

l = 0
for item in po:

	if item.msgstr != '':
		continue
	try:
		item.msgstr = GoogleTranslator(source='en', target=target_language).translate(item.msgid)
	except NotValidPayload:
		item.msgstr = ''

	if l % 5 == 0:
		print("    write " + "line " + str(l) + "/" + str(len(po)))
	l = l + 1

# write PO/TXT
po.save(os.path.join(path_fold, output_file))

