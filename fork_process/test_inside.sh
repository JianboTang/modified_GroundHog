. ../config.init
. ./localConfig.init
export PYTHONPATH=$PYTHONPATH:$root_path:$root_path/$process_id
data_path=./dataPreprocess/used/train
tool_path=./experiments/nmt
test_path=./dataPreprocess/used/test

post_filename=post_inside.txt
resp_filename=cmnt_inside.txt
out_filename=encdec_trans_inside.txt
#echo "Score with RNNencdec"
#python experiments/nmt/score.py --mode=batch --src=$test_path/$post_filename --trg=$test_path/$resp_filename --allow-unk \
# --state $data_path/encdec-50_state.pkl $data_path/encdec-50_model.npz
python ./experiments/nmt/sample.py --source=$test_path/$post_filename --beam-search --beam-size 10 \
 --trans $test_path/$out_filename  --state $data_path/encdec-50_state.pkl $data_path/encdec-50_model.npz 
