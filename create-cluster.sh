eksctl create cluster \
--name test \
--version 1.18 \
--region us-east-1 \
--nodegroup-name linux-nodes \
--nodes 1 \
--nodes-min 1 \
--nodes-max 2 \
--with-oidc \
--managed