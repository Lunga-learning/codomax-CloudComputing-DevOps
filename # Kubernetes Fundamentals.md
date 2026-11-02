# Kubernetes Fundamentals — Practical Learning Notes

**Environment**

* Operating System: Windows 11 Home
* Linux environment: Ubuntu 26.04.1 LTS (WSL2)
* Container platform: Docker Desktop
* Kubernetes tool: Kind
* Kubernetes client: kubectl v1.37.2
* Kubernetes cluster: devops-learning
* Kubernetes node version: v1.35.0

## 1. Kubernetes Cluster Setup and Verification

Create a local Kubernetes cluster:

```bash
kind create cluster --name devops-learning
```

Check cluster information:

```bash
kubectl cluster-info
```

Check cluster nodes:

```bash
kubectl get nodes
```

**Observed result:** The `devops-learning-control-plane` node reached `Ready` status.

## 2. Pods

Create an Nginx Pod:

```bash
kubectl run nginx-pod --image=nginx:latest
```

Check Pods:

```bash
kubectl get pods
```

Get detailed Pod information:

```bash
kubectl describe pod nginx-pod
```

View application logs:

```bash
kubectl logs nginx-pod
```

Inspect Pod IP addresses:

```bash
kubectl get pods -o wide
```

Access Nginx through port forwarding:

```bash
kubectl port-forward pod/nginx-pod 8080:80
```

Open `http://localhost:8080` in a browser.

**Observed result:** The Nginx welcome page appeared successfully.

The logs confirmed a successful HTTP request with status code `200`.

**Key learning:** A Pod is the smallest deployable unit in Kubernetes. It provides an environment for running one or more containers.

## 3. Deployments

Create a Deployment with two replicas:

```bash
kubectl create deployment nginx-deployment --image=nginx:latest --replicas=2
```

Inspect Deployments:

```bash
kubectl get deployments
```

Inspect the Pods:

```bash
kubectl get pods -o wide
```

**Observed result:**

* Desired replicas: 2
* Ready replicas: 2
* Available replicas: 2

### Testing Kubernetes self-healing

Delete one Deployment-managed Pod:

```bash
kubectl delete pod nginx-deployment-74794ff46b-nr5tz
```

Check the Pods again:

```bash
kubectl get pods -o wide
```

**Observed result:** Kubernetes automatically created a replacement Pod with a new name and IP address.

**Key learning:** Deployments manage Pods and maintain the desired number of replicas. If a managed Pod is deleted, Kubernetes works to replace it.

## 4. Services

Expose the Deployment:

```bash
kubectl expose deployment nginx-deployment --name=nginx-service --type=NodePort --port=80 --target-port=80
```

Inspect Services:

```bash
kubectl get services
```

Inspect Service endpoints:

```bash
kubectl get endpoints nginx-service
```

Inspect detailed Service configuration:

```bash
kubectl describe service nginx-service
```

**Observed results:**

* Service name: nginx-service
* Type: NodePort
* ClusterIP: 10.96.125.4
* Service port: 80
* Target port: 80
* NodePort: 30504
* Pod endpoints: 10.244.0.6:80 and 10.244.0.8:80

**Key learning:** A Service provides a stable network endpoint for accessing matching Pods. It can continue directing traffic to replacement Pods even when their IP addresses change.

## 5. ConfigMaps

Create a ConfigMap:

```bash
kubectl create configmap app-config \
  --from-literal=APP_ENV=development \
  --from-literal=APP_NAME=DevOps-Learning-App \
  --from-literal=APP_VERSION=1.0
```

Inspect it:

```bash
kubectl describe configmap app-config
```

Create a test Pod that loads ConfigMap values as environment variables:

```bash
kubectl run config-test-pod \
  --image=busybox:latest \
  --restart=Never \
  --overrides='{"spec":{"containers":[{"name":"config-test-pod","image":"busybox:latest","envFrom":[{"configMapRef":{"name":"app-config"}}],"command":["sh","-c","env | grep ^APP_; sleep 3600"]}]}}'
```

View the container logs:

```bash
kubectl logs config-test-pod
```

**Observed result:**

```text
APP_NAME=DevOps-Learning-App
APP_ENV=development
APP_VERSION=1.0
```

**Key learning:** ConfigMaps store non-sensitive configuration separately from container images and can provide those values to containers as environment variables.

Passwords and other confidential values should be stored using Kubernetes Secrets rather than ConfigMaps.

## 6. Resource Cleanup

Delete the Deployment:

```bash
kubectl delete deployment nginx-deployment
```

Delete the Service:

```bash
kubectl delete service nginx-service
```

Delete the standalone Nginx Pod:

```bash
kubectl delete pod nginx-pod
```

Delete the ConfigMap test Pod:

```bash
kubectl delete pod config-test-pod
```

Delete the ConfigMap:

```bash
kubectl delete configmap app-config
```

Verify cleanup:

```bash
kubectl get all
```

**Final observed result:** Only the built-in `kubernetes` Service remained.

The local Kind cluster was preserved.

## 7. Final Learning Outcomes

I have gained practical introductory experience with:

1. Creating and inspecting Kubernetes Pods.
2. Deploying containerized applications.
3. Managing application replicas with Deployments.
4. Demonstrating Kubernetes self-healing.
5. Exposing applications using Services.
6. Understanding ClusterIP, NodePort and TargetPort.
7. Inspecting Service selectors and endpoints.
8. Creating ConfigMaps.
9. Injecting ConfigMap values into containers.
10. Cleaning up Kubernetes resources safely.

**Practical achievement:** Successfully deployed, accessed, inspected, scaled through replicas, tested recovery, configured and cleaned up a local Nginx application using Kubernetes.

**Environment status:** Local Kind cluster preserved and ready for future Kubernetes exercises.
