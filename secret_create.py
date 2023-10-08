"""
Creates a Secret using AppsV1Api from file server-secret.yaml.
"""

from os import path

import yaml

from kubernetes import client, config


def main():
    # Configs
    config.load_kube_config()

    with open(path.join(path.dirname(__file__), "yaml_manifests/secret.yaml")) as f:
        dep = yaml.safe_load(f)
        k8s_apps_v1 = client.CoreV1Api()
        resp = k8s_apps_v1.create_namespaced_secret(
            body=dep, namespace="default")
        print(f"Secret created. Status='{resp.metadata.name}'")


if __name__ == '__main__':
    main()
