#!/bin/bash
. ../config.init
. ./localConfig.init
export PYTHONPATH=$PYTHONPATH:$root_path:$root_path/$process_id
echo $PYTHONPATH
export train_path=./dataPreprocess/used/train
python  ./experiments/nmt/train.py  --proto=prototype_encdec_state "prefix='$train_path/encdec-50_',seqlen=50,sort_k_batches=20"
# python  ./experiments/nmt/train.py --proto=prototype_search_state "prefix='$train_path/search_',seqlen=50,sort_k_batches=20"
