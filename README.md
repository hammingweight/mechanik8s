# Mechanik8s

A Kubernetes daemonset for retrieving pod and host metrics. The goal is to expose metrics via a Model Context Protocol server.
Currently only a host's `/sys/fs/cgroup` directory is mounted in the daemonset pod.

To run what we have so far

```
helm install mechanik8s helm/
kubectl get pods -w | grep ^mechanik8s
```

When the pod(s) is (are) running, you can examine the host's cgroup virtual filesystem

```
kubectl exec -it $(kubectl get pods | grep ^mechanik8s | head -n 1 | awk '{print $1}') -- bash
cd /hostcgroups/
ls
```
