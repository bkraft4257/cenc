#!/usr/bin/env python
"""
SCP copy of CENC partipant ID to local directory for FTP to CENC servers.
"""

import os
import argparse

cenc_local_directory = "/Users/bkraft/cenc/"
cenc_remote_directory = "/cenc/mri/subjects/"
cenc_prefix = "34P1"

usage = "usage: %prog [options] arg1 arg2"

parser = argparse.ArgumentParser(prog='cenc_scp')

parser.add_argument("cenc_id_number", help="CENC ID number", type=int)

inArgs = parser.parse_args()

cenc_acrostic = "%s%03d" % (cenc_prefix, inArgs.cenc_id_number)
cenc_data_directory = os.path.join(cenc_remote_directory, cenc_acrostic, 'data')

cenc_tarballs = (os.path.join(cenc_data_directory, 'dicom', cenc_acrostic + '.tar.gz'),
                 os.path.join(cenc_data_directory, 'fmri', cenc_acrostic + '_fmri.tar.gz')
                 )

for ii in cenc_tarballs:
    os.system("scp {0!s}:{1!s} {2!s}".format('bkraft@aging1a.medeng.wfubmc.edu', ii,
                                             cenc_local_directory))