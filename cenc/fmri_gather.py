#!/usr/bin/env python3
"""
    Gathers fMRI data for CENC study and creates a tarball.  Tarball is uploaded to the
    CENC FTP server
"""

import sys
import os  # system functions
import re
import tarfile
import glob

import argparse
import _utilities as util
import cenc

#
# Main Function
#

if __name__ == "__main__":

    ## Parsing Arguments
    #
    #

    usage = "usage: %prog [options] arg1 arg2"

    parser.add_argument("--in_dir", help="Participant directory", default=os.getcwd())
    parser = argparse.ArgumentParser(prog='cenc_fmri_gather')
    parser.add_argument("--cenc_dir", help="CENC data directory", default=os.getenv('CENC_MRI_DATA'))
    parser.add_argument("--nifti_dir", help="NIFTI data directory", default='./data/nifti')
    parser.add_argument("--dicom_dir", help="NIFTI data directory", default='./data/dicom')
    parser.add_argument("--out_dir", help="NIFTI data directory", default='./data/fmri')
    parser.add_argument("--tarball", help="tarball name", default=None)

    inArgs = parser.parse_args()

    #
    #
    #

    cenc_dirs = cenc.directories(inArgs.in_dir)

    id = cenc_dirs['id']

    participant_dir = cenc_dirs['root']
    nifti_dir = cenc_dirs['nifti']
    dicom_dir = cenc_dirs['dicom']
    out_dir = cenc_dirs['fmri']

    if not inArgs.tarball == None:
        tarball_filename = inArgs.tarball
    else:
        tarball_filename = id + '_fmri.tar.gz'

    if os.path.isfile(os.path.join(out_dir, tarball_filename)):
        sys.exit('fMRI tarball already exists for ' + id + '.')

    # Create Output Directory if it doesn't exist

    files = [os.path.abspath(os.path.join(dicom_dir, 'dcmConvertAll.cfg')),
             os.path.abspath(os.path.join(dicom_dir, 'dcmConvert_cenc.cfg')),
             os.path.abspath(os.path.join(nifti_dir, 'rest.nii.gz'))
             ]

    util.mkcd_dir(out_dir)
    util.link_inputs(files, out_dir)

    files_to_be_tarred = glob.glob('*')

    # Create TarBall

    tarball = tarfile.open(tarball_filename, 'w:gz')

    for f in files_to_be_tarred:
        tarball.add(f)

    tarball.close()

    # Clean Directory

    for ii in files_to_be_tarred:
        os.remove(ii)
