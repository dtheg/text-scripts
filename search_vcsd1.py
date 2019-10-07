import os
import io
import re
import argparse
import codecs
import sys

#Checks if a word is already in user-rules and user-dictionary#
parser = argparse.ArgumentParser("")
parser.add_argument('-i', "--input_word", required=True, help="input word",type=str)
args = parser.parse_args()

word = args.input_word
mypath = "/Users/davidgaray/voiceservicescustomdictionaries/es-MX/"

from os import listdir
from os.path import isfile, join
onlyfiles = [mypath+f for f in listdir(mypath) if isfile(join(mypath, f))]

for i in onlyfiles:
	regex1 = r'({})'.format(word)
	with codecs.open(i, 'r', encoding='latin-1') as f:
		read_data = f.read()
		read_data = read_data.replace('\\b', ' ' ).replace('\\s', ' ').split('\n')
		for number, line in enumerate(read_data):
			#regex1 = r'(\b|[b]){}\b'.format(word)
			results = re.findall(regex1, line, re.I)
			for w in results:
				print(number+1, word+"     in"+" ---> "+line, i.split('/')[-1])
