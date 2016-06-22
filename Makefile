#!/usr/bin/env make

deploy:
	gcloud -q preview app deploy py-default/app.yaml py-svc/app.yaml

dispatch:
	gcloud -q preview app deploy dispatch.yaml 

dev:
	# run all services locally
	$(DEVSRV) -A $(APPID) --port=9999 py-default/app.yaml py-svc/app.yaml dispatch.yaml 
