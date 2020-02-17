from typing import Dict, Optional
from detectron2.modeling import build_model

class RG(object):
        def __init__(self, name: str) -> None:
                self._name = name
                self._obj_map : Dict[str, object] = {}
                        
        def get(self, name: str) -> object:
                ret = self._obj_map.get(name)
                if ret is None:
                    raise KeyError(
                        "No object named '{}' found in '{}' registry!".format(
                            name, "ABCD"
                        )
                    )
                return ret


print("Registry")
print(Registry)
def build_model(cfg):
    meta_arch = cfg.MODEL.META_ARCHITECTURE
    return META_ARCH_REGISTRY.get(meta_arch)(cfg)
    
