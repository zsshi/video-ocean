#!/bin/bash

ANACONDA_HOME=$(pwd)/../../anaconda38-slowfast
ANACONDA_PYPATH=${ANACONDA_HOME}/lib/python3.8/site-packages
SLOWFAST_PYPATH=$(pwd)/slowfast

export PATH=${ANACONDA_HOME}/bin:$PATH
export PYTHONPATH=${ANACONDA_PYPATH}:${SLOWFAST_PYPATH}:$PYTHONPATH

ROOT_PATH=../../video-multimodal-workspace
PRETRAIN_PATH=${ROOT_PATH}/pretrained_models
DATA_PATH=${ROOT_PATH}/annotations/mmit
MMIT_VERSION=v1-mini
M3A_MODE=GRAPH
M3A_MODAL_TYPE=AUDIO
M3A_MODAL_JOINT_TYPE=NONE
M3A_NLAYERS=2
M3A_HIDDEN_LAYER=1024
RESULT_PATH=${ROOT_PATH}/results/mmit/run_mmit_${MMIT_VERSION}_mvit_b_8x2
RESULT_LINK=results

if [[ ${M3A_MODE} == 'GRAPH' ]] || [[ ${M3A_MODE} == 'MLP' ]]; then
    RESULT_PATH=${RESULT_PATH}_M3A_${M3A_MODE}_${M3A_MODAL_TYPE}_${M3A_MODAL_JOINT_TYPE}_${M3A_NLAYERS}-LAYER
else
    RESULT_PATH=${RESULT_PATH}
fi

if [ -d ${RESULT_PATH} ]; then
    echo "results path exists, exit..."
    exit 0
fi

rm ${RESULT_LINK}
mkdir ${RESULT_PATH}
ln -s ${RESULT_PATH} ${RESULT_LINK}

python tools/run_net.py \
--cfg configs/Mmit/MVIT_${M3A_MODE}_8x2.yaml \
DATA.PATH_TO_DATA_DIR ${DATA_PATH} \
DATA.MMIT_VERSION ${MMIT_VERSION} \
TRAIN.CHECKPOINT_FILE_PATH ${PRETRAIN_PATH}/MVIT_B_32x3_pretrained_8f.pyth \
M3A.MODE ${M3A_MODE} \
M3A.MODAL_TYPE ${M3A_MODAL_TYPE} \
M3A.MODAL_JOINT_TYPE ${M3A_MODAL_JOINT_TYPE} \
M3A.NLAYERS ${M3A_NLAYERS} \
M3A.HIDDEN_LAYER ${M3A_HIDDEN_LAYER} \
2>&1 | tee ${RESULT_PATH}/log.txt
