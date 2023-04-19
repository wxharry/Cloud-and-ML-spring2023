# Homework 3 - Docker MNIST HW

## Instruction
* Work: Run MNIST inside a Docker container
  * MNIST can be based on PyTorch or TenserFlow.
  * We provided a example code set.
* Submission:
  * Source code, files containing your own work or being modified by you (35 points)
    * Vagrantfile (If need to use Vagrant for your experiment)
    * Dockerfile (must include one or a few changes to the example, i.e. mnist/main.py command line options)
    * On screen output (partial capture) of the ‘docker run’.
    * Other downloaded files with you modifications
  * Report (55 points)
    * Document your steps so we can reproduce them. These should include a workflow, observations with attention to details, map to learnt concepts, code comment or explanation, and brief comparative discuss.
    * The purpose of the report is show that you can not only do the operation, but have conceptual build-up of container technologies.
* Extra credit (10 points):
  * Run MNIST inside a Singularity container (inside a Vagrant VM if need)
  * Compare Docker and Singularity in your report.

## Steps
1. build Dockerfile

``` bash
docker build -t pytorch-mnist .
```

2. run docker container

```
docker run pytorch-mnist
```