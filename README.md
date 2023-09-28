## Tims Stack V2

Clean rewrite of Tims Stack

### What for?

This is an opionated framework for hyper dynamic cross plattform progressive app and web-apps.
With full build and development progress automation trough CI / CD automatic build and empherial enviroments.

### Local Development

As easy as it gets:

```
docker-compose build
docker-compose up
```

Same for any service just `cd` into the service ( e.g.: `./backend`, `./frontend` ).

### Default Actions

deploy_production.yaml: on push to **production** branch. -> deploys the default production url
create_builds.yaml: on push to **production** branch --> creates build apps and apks

deploy_staging.yaml: on push to **main** branch -> deploys the default staging url
deploy_feature.yaml: on pull request (or update) to the **main** branch. -> deploys a feature env to a feature-url

build_tests.yaml: any push or commit -> runs builds and tests

#### Action secrets

- `BOT_PAT`: Bot private access token
- `PROD_KUBECONFIG_BASE64_ENCRYPTED`: `kubeconfig.yaml` of the staging server encrypted
  `PROD_KUBECONFIG_PASSWORD`
- `STAGE_KUBECONFIG_BASE64_ENCRYPTED`
  `STAGE_KUBECONFIG_PASSWORD`
- `STAGE_ENV_BASE64_ENCRYPTED`
  `STAGE_ENV_PASSWORD`
- `PRO_ENV_BASE64_ENCRYPTED`
  `PRO_ENV_PASSWORD`

### Branch Structure

- **production**: Holds the current production code ( always push protected )
- **main**: Holds the current staging code ( make a PR here for adding new features )
- **feature-..**: Any feature branch that should be staged with an epherial evironment

### Infrastucture

This setup requires two private VPS's setup with microk8s ( or access to a managed k8s cluster ).

- **Staging Server**: Hosts empherial enviroments and the staging server
- **Production Server**: Host production deployments

## Services

The setup configures services:

- django backend: Hosts rest api, manages backends
- nextjs frontend:
- redis db: used by websockets and celery tasks
- matomo: used for basic page analytics

For the local setup including all these services:

```
docker-compose -f docker-compose.metrics.yaml build
docker-compose -f docker-compose.metrics.yaml up
```

## Expernal Services

These serices are recommended to be kept external, but they are emulated in any of the development environments.

- postgresdb (backend)
- mariadb (matomo)

### Backend

`localhost:8000`

Automat



### Matomo

`localhost:9090`

Development credentials:

superuser login: admin
Admin123
benjamin.tim@gmx.de

```
<!-- Matomo -->
<script>
  var _paq = window._paq = window._paq || [];
  /* tracker methods like "setCustomDimension" should be called before "trackPageView" */
  _paq.push(['trackPageView']);
  _paq.push(['enableLinkTracking']);
  (function() {
    var u="//172.20.0.7/";
    _paq.push(['setTrackerUrl', u+'matomo.php']);
    _paq.push(['setSiteId', '1']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.async=true; g.src=u+'matomo.js'; s.parentNode.insertBefore(g,s);
  })();
</script>
<!-- End Matomo Code -->
```

### MariaDB

All development files containing the setup are in `./matomo/mariadb`.