from typing import Optional, Dict, Any

from jinja2 import Environment, nodes
from jinja2.nodes import Impossible


def get_config_block(raw_code: str) -> Optional[Dict[str, Any]]:
    env = Environment(extensions=["jinja2.ext.do"])
    ast = env.parse(raw_code)

    def find_config_call(node):
        if (
            isinstance(node, nodes.Call)
            and isinstance(node.node, nodes.Name)
            and node.node.name == "config"
        ):
            config_values = {}
            for kw in node.kwargs:
                try:
                    config_values[kw.key] = kw.value.as_const()
                except Impossible:
                    config_values[kw.key] = None
            return config_values

        for child in node.iter_child_nodes():
            result = find_config_call(child)
            if result:
                return result

        return None

    return find_config_call(ast)