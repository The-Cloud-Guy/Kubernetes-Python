from kubernetes import client, config

def delete_deployment(api_instance, deployment_name, namespace):
    # Delete Deployment
    api_response = api_instance.delete_namespaced_deployment(
        name=deployment_name,
        namespace=namespace,
        body=client.V1DeleteOptions(propagation_policy="Foreground", grace_period_seconds=5)
    )
    print("Deployment deleted")

def main():
    config.load_kube_config()
    apps_v1 = client.AppsV1Api()

    namespace = "default"
    deployment_name = "nginx-deployment"
    delete_deployment(apps_v1, deployment_name, namespace)

if __name__ == '__main__':
    main()