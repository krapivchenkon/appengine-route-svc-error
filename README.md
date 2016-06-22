#### Current repo describes steps to reproduce routing error when deploying appengine app with services using GCloud SDK

### What steps will reproduce the problem?
- Create App Engine project
- `git clone https://github.com/krapivchenkon/appengine-route-svc-error.git`
- `gcloud config set project <your-app-id>`
- `gcloud -q preview app deploy py-default/app.yaml py-svc/app.yaml`

After this step we can perform following:

```
$ curl https://<your-app-id>.appspot.com/
Hello, world from Python MAIN:PROD
$ curl https://<your-app-id>.appspot.com/py/
Hello, world from Python MAIN:PROD
$ curl https://py-svc-dot-<your-app-id>.appspot.com
Hello, world from Python SUB SERVICE:PROD
```
As you can see we are able now to invoke microservices using naming convention described in GCP documentation

- Now we update dispatch.yaml configuration:
`gcloud -q preview app deploy dispatch.yaml `

And test again:

```
$ curl https://<your-app-id>.appspot.com
Hello, world from Python MAIN:PROD
$ curl https://<your-app-id>.appspot.com/py/
Hello, world from Python SUB SERVICE:PROD
$ curl https://py-svc-dot-<your-app-id>.appspot.com
Hello, world from Python MAIN:PROD
$ curl http://py-svc.<your-app-id>.appspot.com
Hello, world from Python MAIN:PROD
```

After dispatch.yaml was applied we are able to route according to rules in dispatch.yaml
but unable to reference services using naming convention:

`https://user-service-dot-my-app.appspot.com`


### What is the output of 'gcloud info'?
```
Google Cloud SDK [114.0.0]

Platform: [Mac OS X, x86_64]
Python Version: [2.7.10 (default, Oct 23 2015, 19:19:21)  [GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.5)]]
Python Location: [/System/Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python]
Site Packages: [Disabled]

Installation Root: [/Users/nikolayk/google-cloud-sdk]
Installed Components:
  core: [2016.06.09]
  app-engine-python: [1.9.38]
  core-nix: [2016.03.28]
  gcloud: []
  gsutil-nix: [4.18]
  gsutil: [4.19]
  bq: [2.0.24]
  bq-nix: [2.0.24]
