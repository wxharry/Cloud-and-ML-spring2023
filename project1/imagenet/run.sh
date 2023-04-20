# Define the default value for the parameter
DEFAULT_PARAM_VALUE="resnet18"

# Use the first command line argument as the parameter value, or use the default value if none is provided
PARAM_VALUE=${1:-$DEFAULT_PARAM_VALUE}
ncu --profile-from-start off \
	--metrics smsp__sass_thread_inst_executed_op_fadd_pred_on.sum,smsp__sass_thread_inst_executed_op_fmul_pred_on.sum,smsp__sass_thread_inst_executed_op_ffma_pred_on.sum,dram__sectors_write.sum,dram__sectors_read.sum,smsp__cycles_elapsed.sum,smsp__cycles_elapsed.sum.per_second,dram__bytes_read.sum.per_second,dram__bytes_write.sum.per_second \
    --target-processes all python3 main.py /imagenet/ --epochs 1 --gpu 0 -a $PARAM_VALUE 2>&1 | tee ncu-$PARAM_VALUE.out \
    && python3 helper.py $PARAM_VALUE
