from fvcore.common.registry import Registry

META_ARCH_REGISTRY = Registry("META_ARCH")  # noqa F401 isort:skip

def get(self, name: str) -> object:
        ret = self._obj_map.get(name)
        if ret is None:
            raise KeyError(
                "No object named '{}' found in '{}' registry!".format(
                    name, self._name
                )
            )
        return ret
def bm_practice(cfg):
    meta_arch = cfg.MODEL.META_ARCHITECTURE
    return get(meta_arch)(cfg)
    
