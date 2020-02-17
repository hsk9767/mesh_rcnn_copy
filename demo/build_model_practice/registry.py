from typing import Dict, Optional
from detectron2.utils.registry import Registry

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


META_ARCH_REGISTRY = Registry("META_ARCH")
def bm_practice(cfg):
    meta_arch = cfg.MODEL.META_ARCHITECTURE
    return META_ARCH_REGISTRY.get(meta_arch)(cfg)
    
