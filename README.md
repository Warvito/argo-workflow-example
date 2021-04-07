# Argo workflow - Example

# Installation

This example was implemented using Minikube and Argo-workflow v3.

1) Install kubectl using this [link](https://kubernetes.io/docs/tasks/tools/).

2) Install minikube using this link [link](https://minikube.sigs.k8s.io/docs/start/).

3) Install argo workflow using this 

```
kubectl create ns argo
kubectl apply -n argo -f https://raw.githubusercontent.com/argoproj/argo-workflows/stable/manifests/quick-start-minimal.yaml
```

Based on this [link](https://argoproj.github.io/argo-workflows/quick-start/). Make sure to select a version 3.x in the release page.

Try to check the workflow using argo server and accessing http://localhost:2746 (check workflow in namespace argo)

To remove use 
 ```
kubectl delete -n argo -f https://raw.githubusercontent.com/argoproj/argo-workflows/stable/manifests/quick-start-minimal.yaml
kubectl delete ns argo
```

4) install MinIO using this (link)[https://argoproj.github.io/argo-workflows/configure-artifact-repository/]

5) Submit job

```
argo submit -n argo Pipelines/ToyExample/toy_example.yaml
```
