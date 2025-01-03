try:
    from .nodes import NODE_CLASS_MAPPINGS
    from .nodes import NODE_DISPLAY_NAME_MAPPINGS
    
    __all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
except ImportError:
    import traceback
    print("Unable to import nodes.py")
    traceback.print_exc()
    NODE_CLASS_MAPPINGS = {}
    NODE_DISPLAY_NAME_MAPPINGS = {} 