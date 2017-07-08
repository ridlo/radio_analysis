import os
import sys
import glob

for ifile in glob.glob("*.fits"): # for safety reason
    print "Fits file:", ifile
    cmd = "sextractor "+ifile+" -CHECKIMAGE_NAME check_"+ifile[:-5]+".fits > "+ifile[:-5]+".cat"
    print "Running sextractor: "+cmd
    os.system(cmd)