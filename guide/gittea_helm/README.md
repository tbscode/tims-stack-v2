# Gittea on Microk8s

Check out the [script](./install_gittea_microk8s.sh) for details, it performs followin steps:

- create namespace
- helm install gittea-helm
with ingress and max package size configured ( configured cause we need to push larger packages as well; [see](https://github.com/kubernetes/ingress-nginx/issues/4825) [and](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/#custom-max-body-size) ).


### Install

```
./install_gittea_microk8s.sh \
  K8_NAMESPACE="<installation-namespace>" \
  RELEASE_NAME="<release-name>" \
  ADMIN_USERNAME="<...>" \
  ADMIN_PASSWORD="<...>" \ 
  INGRESS_HOST="<host-url>" \
  RELEASE_NAME="<...>" \
```

### Uninstall

```
microk8s helm uninstall $RELEASE_NAME
```