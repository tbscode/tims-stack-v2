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

### Branch Structure

- **production**: Holds the current production code ( always push protected )
- **main**: Holds the current staging code ( make a PR here for adding new features )
- **feature-..**: Any feature branch that should be staged with an epherial evironment

### Infrastucture

This setup requires two private VPS's setup with microk8s ( or access to a managed k8s cluster ).

- **Staging Server**: Hosts empherial enviroments and the staging server
- **Production Server**: Host production deployments