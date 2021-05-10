# Argo workflow - Example

# Installation

This example was implemented using Minikube and Argo-workflow v3.

1) Install kubectl using this [link](https://kubernetes.io/docs/tasks/tools/).

2) Install minikube using this [link](https://minikube.sigs.k8s.io/docs/start/).

3) Install argo workflow using this 

```
kubectl create ns argo
kubectl apply -n argo -f https://raw.githubusercontent.com/argoproj/argo-workflows/stable/manifests/quick-start-minimal.yaml
```

Next, Download the latest Argo CLI (v3.x) from the [releases page](https://github.com/argoproj/argo-workflows/releases).

Finally, submit an example workflow: 

```
argo submit -n argo --watch https://raw.githubusercontent.com/argoproj/argo-workflows/master/examples/hello-world.yaml
argo list -n argo
argo get -n argo @latest
argo logs -n argo @latest
```

Based on this [link](https://argoproj.github.io/argo-workflows/quick-start/).

Check the workflows using GUI. In a different terminal, execute 


```
argo server
```

and access http://localhost:2746 (check workflow in namespace argo)

To uninstall argo, use:
 ```
kubectl delete -n argo -f https://raw.githubusercontent.com/argoproj/argo-workflows/stable/manifests/quick-start-minimal.yaml
kubectl delete ns argo
```

4) install MinIO using this [link](https://argoproj.github.io/argo-workflows/configure-artifact-repository/)

# Submitting a job
```
argo submit -n argo Pipelines/ToyExample/toy_example.yaml
```

# References

https://argoproj.github.io/argo-workflows/examples/