#!/bin/bash
echo $PYTHONPATH
export tool_path=./experiments/nmt/preprocess
export train_path=./dataPreprocess/used/train

python $tool_path/preprocess.py -d $train_path/vocab.cn.pkl -v 5946 -b $train_path/binarized_text.cn.pkl -p $train_path/post.txt
python $tool_path/preprocess.py -d $train_path/vocab.en.pkl -v 5369 -b $train_path/binarized_text.en.pkl -p $train_path/cmnt.txt


python $tool_path/invert-dict.py $train_path/vocab.en.pkl $train_path/ivocab.en.pkl
python $tool_path/invert-dict.py $train_path/vocab.cn.pkl $train_path/ivocab.cn.pkl


python $tool_path/convert-pkl2hdf5.py $train_path/binarized_text.en.pkl $train_path/binarized_text.en.h5
python $tool_path/convert-pkl2hdf5.py $train_path/binarized_text.cn.pkl $train_path/binarized_text.cn.h5


python $tool_path/shuffle-hdf5.py $train_path/binarized_text.cn.h5 $train_path/binarized_text.en.h5 $train_path/binarized_text.shuffled.cn.h5 $train_path/binarized_text.shuffled.en.h5

