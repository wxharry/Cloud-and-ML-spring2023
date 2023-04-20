# Roofline modeling with ResNet models on ImageNet dataset

## Instruction
* Design the experiment to show the difference
    * 2-3 Environment – Cloud vs Baremetal, different GPU flavors, etc.
    * 2-3 Neural Network models
* Short representative runs – no need to finish training as the accuracy does not matter.
* Report
    * Experiment design (10%) – what are you trying to show and what is the hypothesis
    * Complexity estimation (10%) and measurement (20%)
    * Roofline modeling (40%)
    * Discussion (20%)

## How to run
```
sh run.sh   # run ncu profiler with pytorch codes and helper.py program
```
The output from the ncu profiler with be recorded at ncu-$PARAM_VALUE.out
The helper.py calculates the ncu output to create a result at helper-$PARAM_VALUE.out

## My report
https://docs.google.com/document/d/1jF6JnxiFpqQgT6Y197nEVYh-A6_KEv0EY7DvdoJ4wxM/edit#heading=h.c5tti7rpkphd
