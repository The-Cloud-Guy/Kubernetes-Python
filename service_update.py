from kubernetes import client, config

def update_service_type(api_instance, service_name, new_type, namespace):
    # Update Service type
    body = {
        "spec": {
            "type": new_type
        }
    }
    api_response = api_instance.patch_namespaced_service(
        name=service_name,
        namespace=namespace,
        body=body
    )
    print("Service updated")

def main():
    config.load_kube_config()
    core_v1 = client.CoreV1Api()

    namespace = "default"
    service_name = "nginx-service"
    new_type = "NodePort"
    update_service_type(core_v1, service_name, new_type, namespace)

if __name__ == '__main__':
    main()