ncu --profile-from-start off --metrics smsp__sass_thread_inst_executed_op_fadd_pred_on.sum,smsp__sass_thread_inst_executed_op_fmul_pred_on.sum,smsp__sass_thread_inst_executed_op_ffma_pred_on.sum --target-processes all python3 main.py --dummy --epochs 1 --gpu 0 2>&1 | tee ncu.out