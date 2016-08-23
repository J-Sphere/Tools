#!/usr/bin/env python
import os, argparse,time, sys
parser=argparse.ArgumentParser()
parser.add_argument('-dir', default='./', type=str, help='give path for tree')
parser.add_argument('-showfiles', action='store_true', default=False, help='display files')
parser.add_argument('-runtime', type=float, default=86400., help='maximal runtime, default is one day')
args=parser.parse_args()
start=args.dir
showfiles=args.showfiles
mrt=args.runtime
indentcounter=0
def list_dir1(direc, indentcounter, showfiles, starttime,  mrt):
    if indentcounter==0: tabs=''
    else: tabs='\t'*(indentcounter-1)+'|______ '
    if os.listdir(direc)==[]:
        if showfiles: print(tabs+'empty')
    else:
        for el in sorted(os.listdir(direc)):
            if os.path.isfile(direc+el):
                if showfiles: print(tabs+el)
            else:
                print(tabs+el+':')
                try:
                    if time.time()-starttime>mrt:
                        raise RuntimeError
                    else:
                        list_dir2(direc+el+'/', indentcounter+1, showfiles, starttime, mrt)
                except:
                    pass

# to avoid self iterations change list_dir1(direc+el+'/', indentcounter+1, showfiles) to list_dir2(direc+el+'/', indentcounter+1, showfiles, starttime, mrt)

def list_dir2(direc_2, indentcounter_2, showfiles_2,starttime, mrt):
    if indentcounter_2==0: tabs_2=''
    else: tabs_2='\t'*(indentcounter_2-1)+'|______ '
    if os.listdir(direc_2)==[]:
        if showfiles_2: print(tabs_2+'empty')
    else:
        for le in sorted(os.listdir(direc_2)):
            if os.path.isfile(direc_2+le):
                if showfiles_2: print(tabs_2+le)
            else:
                print(tabs_2+le+':')
                try:
                    if time.time()-starttime>mrt: 
                        raise RuntimeError
                    else:
                        list_dir1(direc_2+le+'/', indentcounter_2+1, showfiles_2, starttime, mrt)
                except:
                    pass

try:
    starttime=time.time()
    list_dir1(start, indentcounter, showfiles, starttime, mrt)
except RuntimeError:
    print('Too many iterations, out of memory')
    


