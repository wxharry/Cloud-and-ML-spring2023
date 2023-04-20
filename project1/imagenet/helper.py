import sys
metrics = {
    "fadd": {
        "name": "smsp__sass_thread_inst_executed_op_fadd_pred_on.sum",
        "total": 0
    },
    "ffma": {
        "name": "smsp__sass_thread_inst_executed_op_ffma_pred_on.sum",
        "total": 0
    },
    "fmul": {
        "name": "smsp__sass_thread_inst_executed_op_fmul_pred_on.sum",
        "total": 0
    },
    "dram_write": {
        "name": "dram__sectors_write.sum",
        "total": 0
    },
    "dram_read": {
        "name": "dram__sectors_read.sum",
        "total": 0
    },
    "cycle_sum": {
        "name": "smsp__cycles_elapsed.sum",
        "total": 0
    },
    "cycle_per_sec": {
        "name": "smsp__cycles_elapsed.sum.per_second",
        "total": 0
    },
    "dram_read_per_sec":{
        "name": "dram__bytes_read.sum.per_second",
        "total": 0
    },
    "dram_write_per_sec":{
        "name": "dram__bytes_write.sum.per_second",
        "total": 0
    }
}
# smsp__cycles_elapsed.sum,
# smsp__cycles_elapsed.sum.per_second,
# smsp__pipe_tensor_op_hmma_cycles_active.sum,
# smsp__pipe_tensor_op_hmma_cycles_active.sum.per_second

with open(f'ncu-{sys.argv[-1]}.out') as f:
    for line in f.readlines():
        line = line.split()
        for metric in metrics.values():
            if metric["name"] in line:
                metric["total"] += float(line[-1])
                metric['value'] = float(line[-1])

with open(f"helper-{sys.argv[-1]}.out", 'w', encoding='utf-8') as f:
    for name, metric in metrics.items():
        f.write(f"{name} = {metric['total']}\n")

    FLOPs = metrics["fadd"]["total"] + metrics["fmul"]["total"]  + metrics["ffma"]["total"]  * 2 
    f.write(f"FLOPs = {FLOPs :.2g}\n")

    mem = (metrics["dram_write"]["total"] + metrics["dram_read"]["total"])*32
    f.write(f"memory = {round(mem / 1024 ** 1, 2):.2g} MB\n")

    timeCycle = metrics['cycle_sum']['total'] / metrics['cycle_per_sec']['value']
    time = timeCycle
    f.write(f"time = {time:.2g} ns\n")

    ai = FLOPs / mem
    f.write(f"AI = {round(ai, 2)} FLOP/byte\n")

    perf = FLOPs / time
    f.write(f"perf = {round(perf, 2)} GFLOP/s\n")

