# Microk8s on VPS

First we get a simple ubuntu 22.04 vps with a public IP address.

## 1. Create a base user

Create a user, and add it to the sudoers.

```
adduser <user-name>
usermod -aG sudo <user-name>
```

## 2. Create ssh keys

```
ssh-keygen -b 2048 -t rsa
chmod 600 <key-file> <key-file>.pub
```

Copy the content of `<key-name>.pub` to your VPS `/home/<user-name>/authorized_keys`

## 3. setup and enable the firewall

```
ufw allow ssh
ufw allow http
ufw allow https
ufw allow 16433
ufw enable
```

> We also allow access to 16433 for the cube api server

Now disconnect from your server and connect again as the new user:

```
ssh -i "<private-server-key> <user-name>@<server-IP>
```

## 4. Install and setup microk8s

```
sudo snap install microk8s --classic --channel=1.28
sudo microk8s start
mirok8s enable ingress hostpath certmanager
```

Now edit `/var/snap/microk8s/current/certs/csr.conf.template`

```
[ alt_names ]
DNS.1 = kubernetes
DNS.2 = kubernetes.default
DNS.3 = kubernetes.default.svc
DNS.4 = kubernetes.default.svc.cluster
DNS.5 = kubernetes.default.svc.cluster.local
DNS.6 = k8s.<your-domain>
```

Refresh the server certificate:

```
sudo microk8s refresh-certs --cert server.crt
```

View the updated client certificate: `microk8s config > kubeconfig.yaml`
Open the `kubeconfig.yaml`

```
...
- cluster:
    certificate-authority-data: XXXXXXXXCENSOREDXXXXXXX
    server: <pub-IP> <---- put k8s.<domain> here
...
```

Now you can connect to the kubernetes cluster from your local machine:

```
KUBECONFIG="./kubeconfig.yaml" kubectl get pods --all-namespaces
```

## 5. Setting up Matallb