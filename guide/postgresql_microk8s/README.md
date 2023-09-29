## Postgresql helm microk8s setup

This creates and setups bitnamis postgresql helm chart with hourly backups to the host system.

### Installation

```
./create_postgresdb.sh \
  RELEASE_NAME="<release-name>" \
  K8_NAMESPACE="<installation-namespace>" \
  DB_USERNAME="<db-username>" \
  DB_PASSWORD="<your-super-secure-password>" \
  DB_NAME="<db-name>" \
  DB_CLUSTER_DOMAIN="<your-custom-domain>" \
  BACKUP_MOUNT_PATH="/some-host-path" \
  TARGET_PORT="30004"
```

### Destruction

```
microk8s kubectl delete <installation-namespace>
```