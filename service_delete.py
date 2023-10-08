from kubernetes import client, config

def delete_service(api_instance, service_name, namespace):
    # Delete Service
    api_response = api_instance.delete_namespaced_service(
        name=service_name,
        namespace=namespace,
        body=client.V1DeleteOptions()
    )
    print("Service deleted")

def main():
    config.load_kube_config()
    core_v1 = client.CoreV1Api()

    namespace = "default"
    service_name = "nginx-service"
    delete_service(core_v1, service_name, namespace)

if __name__ == '__main__':
    main()