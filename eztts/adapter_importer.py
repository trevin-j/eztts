from .adapter_manifest import ADAPTER_MANIFEST

valid_adapters = []

IMPORT_TEMPLATE = \
"""
try:
    from {_from} import {_adapter}
    valid_adapters.append({_adapter})
except ImportError:
    pass
"""

def dynamic_safe_adapter_import(_from: str, _adapter: str):
    """
    Dynamically import an adapter class into the module where this was called from.
    Safe in this sense means it will not crash on a failed import. Instead, it will
    continue on with the programming, assuming that the dependencies just aren't
    installed for that adapter.
    """
    exec(IMPORT_TEMPLATE.format(_from=_from, _adapter=_adapter))


def safe_import_all_adapters():
    """
    Dynamically import all adapters found in the manifest using the safe dynamic import
    function.
    """
    for adapter_info in ADAPTER_MANIFEST.values():
        dynamic_safe_adapter_import(adapter_info["import_location"], adapter_info["class_name"])