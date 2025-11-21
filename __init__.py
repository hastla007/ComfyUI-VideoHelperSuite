from .videourlhelpersuite.nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
import folder_paths
from .videourlhelpersuite.server import server
from .videourlhelpersuite import documentation
from .videourlhelpersuite import latent_preview

WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
documentation.format_descriptions(NODE_CLASS_MAPPINGS)
