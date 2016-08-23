#!/usr/bin/env python
import os, argparse
parser=argparse.ArgumentParser()
parser.add_argument('-dir', default='./', type=str, help='give path for hmi')
args=parser.parse_args()
indir=args.dir
if len(os.listdir(indir))==1: print ('There is only one thing in %s'%(indir))
elif len(os.listdir(indir))==0: print ('There are no things in %s'%(indir))
else: print ('There are %i things in %s'%(len(os.listdir(indir)), indir))
