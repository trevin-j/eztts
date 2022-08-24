import sys
import subprocess

import requests

from .adapter_manifest import ADAPTER_MANIFEST


def url_exists(path):
    try:
        r = requests.head(path)
        return r.status_code == requests.codes.ok
    except:
        return False


def install_dependencies_for(package_name: str, branch: str):
    requirements_txt_url = f"https://raw.githubusercontent.com/trevin-j/eztts/{branch}/eztts/adapters/{package_name}/requirements.txt"
    if url_exists(requirements_txt_url):
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_txt_url])
    else:
        print(f"No requirements.txt found for {package_name}. Skipping.")


def install_dependencies(branch: str):
    """
    Ask user for which adapters to install dependencies.
    """
    # Menu
    print("Which adapter(s) would you like to install dependencies for?")

    adapter_pkg_names = []
    for i, adapter in enumerate(ADAPTER_MANIFEST):
        if ADAPTER_MANIFEST[str(adapter)]["remote_requirements_txt"]:
            adapter_pkg_names.append(str(adapter))
            print(f"{len(adapter_pkg_names) - 1}: {str(adapter)}")

    # Get user input
    packages = input("> ")

    packages = packages.split(",")

    # Strip whitespace, and convert to ints
    packages = [int(package.strip()) for package in packages]

    for package in packages:
        install_dependencies_for(adapter_pkg_names[package], branch)
        
