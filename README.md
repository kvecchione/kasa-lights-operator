TP-Link Kasa Lights Operator
---

I was interested in trying out building a Kubernetes Operator using KOPF (Kubernetes Operator Python Framework): https://kopf.readthedocs.io/en/stable/

This operator uses the python-kasa python library to interact with TP-Link Kasa Plugs and Bulbs. https://github.com/python-kasa/python-kasa

## Installation
Install the Custom Resource Definition (CRD) with `kubectl apply -f crd/crd.yml`. This will configure the KasaLight object type in Kubernetes.

We then need to create the controller that will watch for updates to this object type as well as the RBAC objects to give the container permissions to watch for new objects and emit events. To do this, 
run `kubectl apply -f deployment.yml`

## Usage

Once these are created and running, we can apply a KasaLight manifest with a desired IP, state (on/off), and type (plug/bulb). Once you have added the right values here, run `kubectl apply -f example/example.yml` and it should adjust the state of the light.

Note: The `state` value needs to be in quotes because YAML translates on/off to boolean.
