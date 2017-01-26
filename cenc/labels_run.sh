#!/usr/bin/env bash

matlab  -softwareopengl -nosplash -nodesktop -noFigureWindows -run "cenc_lst_lpa('t2flair_Affine_nu__t2flair_Warped.nii.gz', 'nu.nii.gz', 0)"