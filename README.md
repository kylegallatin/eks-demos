Create a cluster

```
docker build -t eksctl-cli .
docker run -it eksctl-cli bash
aws configure
./create-cluster.sh
```