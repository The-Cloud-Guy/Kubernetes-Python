from kubernetes import client, config

def list_deployments(api_instance, namespace):
    # List Deployments
    deployments = api_instance.list_namespaced_deployment(namespace)
    for deployment in deployments.items:
        print("Name: %s, Replicas: %s" % (deployment.metadata.name, deployment.spec.replicas))

def main():
    config.load_kube_config()
    apps_v1 = client.AppsV1Api()
    namespace = "default"
    list_deployments(apps_v1, namespace)

if __name__ == '__main__':
    main()