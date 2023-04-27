# Homework 5 - ML w/ K8S

## Instruction
* Application containers
  * Training: training program, container definition file (dockerfile), training job yaml file
  * Inference: inference program, dockerfile, service yaml file, deployment yaml file
    * Training and inference program need to store and load the trained model
    persistently.
    * Host a URL to allow interaction with User.
* User interaction
  * Give any input to the inference engine (a number, a space bar, image file, image id in
the data set)
* Persistent storage
  * PVC from IBM Cloud Block Stoarge

## Step
1. run mnist training program

``` bash
cd mnist

docker build -t wxharry/mnist-train .

docker run -v /workspace/Cloud-and-ML-spring2023/hw5/model:/model wxharry/mnist-train python main.py --epochs=2 --save-model
```

2. run mnist app service

``` bash
cd app

docker build -t wxharry/mnist-app .

docker run -v /workspace/Cloud-and-ML-spring2023/hw5/model:/model -v /workspace/Cloud-and-ML-spring2023/hw5/app:/app -p 8080:5000 wxharry/mnist-app
```


## My report
[Machine Learning with Kubernetes](https://docs.google.com/document/d/1oeruiQitNUhe6qJCOL0sFITZT4slLYrfsggDgEF94PY/edit#)

## References
[mnist | TensorFlow](https://www.tensorflow.org/datasets/catalog/mnist)

[Pytorch | saving-loading-model-for-inference](https://pytorch.org/tutorials/beginner/saving_loading_models.html#saving-loading-model-for-inference)

[Setting up Ingress | IBM Cloud docs](https://cloud.ibm.com/docs/containers?topic=containers-managed-ingress-setup)
