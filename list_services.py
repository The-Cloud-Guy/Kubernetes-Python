from kubernetes import client, config

def list_services(api_instance, namespace):
    # List Services
    services = api_instance.list_namespaced_service(namespace)
    for service in services.items:
        print("Name: %s, Cluster IP: %s" % (service.metadata.name, service.spec.cluster_ip))

def main():
    config.load_kube_config()
    namespace = "default"
    core_v1 = client.CoreV1Api()
    list_services(core_v1, namespace)

if __name__ == '__main__':
    main()