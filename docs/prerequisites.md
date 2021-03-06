
# Prerequisites and requirements
Inference Model Manager has several requirements and dependencies which needs to be present before the installation 
process can be completed. Below is the list including details and guidelines on how to meet the conditions.


## Kubernetes
Inference Model Menager is meant to be installed on top of a Kubernetes cluster so it has to be installed and available upfront.
In the [security recommendations](security_recommendations.md) are described best practices about configuration so here
will be mentioned the mandatory settings. 
Cluster has to be configured with RBAC feature which is needed to protect all the resources and establish permissions
for all the roles in the Inference Model Manager. The testing was done for versions 1.8 and above. In order to setup
authentication mechanism based on external Identity provider in the platform, k8s cluster should be configured with
OpenID token authentication using DEX as the oauth2 server which should be integrated with an IdP like LDAP, Keystone, 
GitHub or other supported by DEX.
Kubernetes can be hosted on-premise or in the cloud. Because OID authentication requires updating kube-apiserver 
parameters you cannot use GKE service.
The easiest method to install Kubernetes is using kubeadm on premise or using Kops in the cloud providers. 
Generally, any installation mechanism can be applied as long as:
- the version is 1.8 or above 
- cluster has RBAC enabled
- there is an option to add OID authentication parameter in kube-apiserver

## Minio
Inference Model Manager is relying on Minio service or other S3 compatible storage. 
Kubernetes cluster needs connectivity with the Minio storage.
You can install Minio server outside of the cluster, deploy it as Kubernetes service inside the cluster or 
use a cloud provider for S3 compliant service. There is no need to enable connectivity between the users and 
the Minio service as it is expected that the users would connect to the storage only using Inference Model Manager Management API.
For testing purposes you can deploy Minio using provided [example deployment automation](../helm-deployment/minio-subchart). 

## Nginx ingress controller
Inference Model Manager requires nginx ingress controller to expose the gRPC inference endpoints and 
other platform services like Management API and DEX. The recommended version is 0.17.1. 
You can install it using the deployment procedure described on [automation scripts](../helm-deployment/ing-subchart)

If you need to use version 0.20.0 or above it can still work but you would need to adjust manually the template for inference 
ingress record in the 'server controller' [code](../server-controller/resources/ingress.tmpl) and update 
nginx records template in the [config map](../helm-deployment/ing-subchart/nginx.tmpl). 
Versions below 0.13.0 are not supported as they do not support gRPC traffic
load-balancing. 

Typically between the clients and the ingress controller service in Kubernetes should be employed also 
[L3/L4 load-balancer](https://www.nginx.com/resources/glossary/layer-4-load-balancing/)
pointing the traffic to nginx controller nodes.
Make sure it support gRPC traffic and http2 protocol.
An example of such load-balancer in `baremetal` Kubernetes cluster and nginx-ingress controller exposed as a NodePort
might be nginx service with the following configuration:
```bash
user www-data;
worker_processes auto;
pid /run/nginx.pid;

events {
	worker_connections 768;
	# multi_accept on;
}

stream {
    upstream stream_backend {
        server node1.domain.com:<ingress service node port>;
        server node2.domain.com:<ingress service node port>;
    }

    server {
        listen     443;
        proxy_pass stream_backend;
    }
}
```

Another alternative to consider for on-premise installation might be with [MetalLB](https://metallb.universe.tf/concepts/layer2/)(currently in beta).

Read more about the options on [ingress-nginx baremetal considerations](https://github.com/kubernetes/ingress-nginx/blob/master/docs/deploy/baremetal.md).


## Docker registry
You can use prebuilt public docker images or optionally, build platform components’ docker images on your own. In that case push them to a docker registry accessible
for the Kubernetes cluster. Docker Registry credentials should be stored in Kubernetes secrets so the platform deployment 
could pull all needed images. It is strongly recommended to use secure connection with Docker registry with TLS encryption
and authorization enabled.

*Note:* In the included deployment scripts several components are being pulled from public Docker repositories. 
Those are: management-api, server-controller, DEX, nginx-controller, OVMS and TensorFlow Serving. If Kubernetes cluster can’t access public Docker repositories
 from Internet, their images should be pushed to a private registry and deployment templates adjusted accordingly.

## Identity provider supported by DEX connectors
Management API just like Kubernetes API will use user authentication based on JWT tokens generated by oauth2 server DEX. 
It acts as a mediator between the users and external Identity Providers. 
DEX supports several IdPs via included set of connectors. All of them are documented on
 [DEX link](https://github.com/dexidp/dex). 
Integration process has been tested and documented for LDAP (Keystone is TBD soon).
For testing purposes you can deploy LDAP component inside the K8S cluster using the procedure documented 
on [LDAP deployment scripts](../tests/deployment/deployment_imm_ldap.sh).

## DNS records for Management API, oauth2 server and Inference Endpoints
It will be required to configure several DNS CNAME records pointing to nginx-controller Kubernetes service. 
They will be used to connect to platform Management API endpoints, oauth2 server and for inference gRPC endpoints. 
Inference endpoints might be created on the platform in big volumes and every endpoint requires a separate 
target host name for ingress to route the requests to appropriate inference backed services. 
For that reason it is recommended to use DNS CNAME record with wildcard character like *.grpc.domain.com. 

Alternatively there could be used just one name for gRPC endpoints or even IP address however that would require to 
include on the gRPC clients side additional header overriding the target server name. 
Refer to the [example grpc client](../examples/grpc_client).
