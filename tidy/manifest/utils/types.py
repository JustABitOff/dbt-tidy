from typing import Union, TYPE_CHECKING

if TYPE_CHECKING:
    from tidy.manifest.v10.manifest import ManifestV10
    from tidy.manifest.v11.manifest import ManifestV11
    from tidy.manifest.v12.manifest import ManifestV12

ManifestType = Union[
    "ManifestV10",
    "ManifestV11",
    "ManifestV12",
]
