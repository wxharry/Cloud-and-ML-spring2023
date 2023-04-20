#!/bin/bash

ncu --profile-from-start off --metrics  smsp__sass_thread_inst_executed_op_fadd_pred_on,smsp__sass_thread_inst_executed_op_fmul_pred_on,smsp__sass_thread_inst_executed_op_ffma_pred_on --target-processes all python3 main.py --batch-size=64 --dry-run --epochs 1 2>&1 | tee ncu.out
