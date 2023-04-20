# Homework – Performance study of (a small part of ) Neural Network

## Instruction
* Estimate time (computation) and space (memory) complexity of a convolution layer (Conv2d-2) of MNIST CNN 
    * Code: https://github.com/pytorch/examples/tree/master/mnist
* Image data will be downloaded automatically
    1. Pen and paper method to estimate the complexity
    2. Run and measure the complexity
    3. Try diff batch sizes, draw a chart (x axis: batch size, y axis: flops and/or mem)
    4. Discuss the difference between estimated and measured results
    5. Bonus: try with diff shape/dimension of Conv2d-2 layer and report the results

## Steps
1. run `main.py` to get the summary info
2. run `sh run-w-ncu.sh` to get the profiling data from ncu
3. calculate the output from step 2
4. repeat from step 2 with different parameters

## My report
[Performance study of (a small part of) Neural Network](https://docs.google.com/document/d/1ShEA3ymjcTHogRragjAD1FtlzCPoVG0h2EN179nXhKg/edit)
