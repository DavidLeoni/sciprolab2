#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Ports old algolab notebooks to Jupman format: https://github.com/DavidLeoni/jupman

# 0.1  Nov 2017  David Leoni


import argparse
import os

parser = argparse.ArgumentParser(description='Ports old algolab notebooks to Jupman format')
parser.add_argument('input', metavar='INPUT', type=str,
                    help='an integer for the accumulator')
parser.add_argument('output',metavar='OUTPUT',type=str)

args = vars(parser.parse_args())

inpath = args['input']
if not os.path.isfile(inpath):
    raise Exception("Non existing file : " + inpath)

outpath = args['output']
if os.path.isfile(outpath):
    raise Exception("Alread existing output file : " + outpath)

with open(outpath, 'w', encoding='utf-8') as outf:
    
    with open(inpath, encoding='utf-8') as inf:
        s = inf.read()  
        new_s = (s
                 .replace('%%HTML', '')
                 .replace('<p class=', '<div class=')
                 .replace('<code>', '`')
                 .replace('</code>', '`')
                 .replace('<i>', '_')
                 .replace('</i>', '_')
                 .replace('<b>', '**')
                 .replace('</b>', '**')                 
                 .replace('jupman-info','alert alert-info')
                 .replace('jupman-important','alert alert-info')
                 .replace('jupman-warn','alert alert-warning')
                 .replace('WARNING:', '**WARNING:**')
                 .replace('</p>','</div>')
                 )
        outf.write(new_s)

print('  Wrote ' + outpath)
print('')

print('')
print('  DONE.')
print('')
