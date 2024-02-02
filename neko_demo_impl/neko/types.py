from ..modules.dd import SomeDemoClass
from ..modules.ddd import SomeOtherDemoClass


__all__ = ['SomeDemoClass', 'SomeOtherDemoClass']

"""
Here, modules can be imported from internals of implementation, but they must be 
present in the scope of the same (as in standard) file
"""
