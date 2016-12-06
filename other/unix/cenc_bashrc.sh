### Cenc bash shell environment
#
#

#
# export CENC_PATH=/gandg/cenc3/cenc/icGit/release/ic/studies/cenc
#

export CENC_SUBJECTS_DIR=/cenc/mri/freesurfer
export CENC_MRI_DATA=/cenc/mri/subjects/
export CENC_MATLAB=${CENC_PATH}/matlab
export CENC_SCRIPTS=${CENC_PATH}/scripts


export PATH=${CENC_PATH}:${CENC_SCRIPTS}:${PATH}	

export CENC_CTF_TEMPLATE="$IMAGEWAKE2_TEMPLATES/ixi/cerebellum_isotropic/ixiIsotropic_t_T1wSkullStripped.nii.gz"

export PYTHONPATH=${CENC_SCRIPTS}:$PYTHONPATH

source ${CENC_PATH}/other/unix/cenc_alias.sh


