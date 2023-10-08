from kubernetes import client, config

def update_deployment_replicas(api_instance, deployment_name, new_replicas, namespace):
    # Update Deployment replicas
    body = {
        "spec": {
            "replicas": new_replicas
        }
    }
    api_response = api_instance.patch_namespaced_deployment(
        name=deployment_name,
        namespace=namespace,
        body=body
    )
    print("Deployment updated")

def main():
    config.load_kube_config()
    apps_v1 = client.AppsV1Api()

    namespace = "default"
    deployment_name = "nginx-deployment"
    new_replicas = 5
    update_deployment_replicas(apps_v1, deployment_name, new_replicas, namespace)

if __name__ == '__main__':
    main()