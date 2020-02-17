from typing import Dict, Optional
from detectron2.modeling import build_model
from detectron2.utils.registry import Registry
META_ARCH_REGISTRY = Registry("META_ARCH")
def bm_practice(cfg):
    meta_arch = cfg.MODEL.META_ARCHITECTURE
    return META_ARCH_REGISTRY.get(meta_arch)(cfg)
    
