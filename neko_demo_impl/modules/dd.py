from neko_demo_std.__internal.some_internal_logic_mixins import (
    FirstAbstractMixin,
    SecondAbstractMixin
)
from neko_demo_std.neko.types import SomeDemoClass


class FirstMixin(FirstAbstractMixin):
    def first_method(self):
        print('first')


class SecondMixin(SecondAbstractMixin):
    def second_method(self):
        print('second')


class RSomeDemoClass(FirstMixin, SecondMixin, SomeDemoClass):
    pass


SomeDemoClass = RSomeDemoClass

__all__ = ['SomeDemoClass']
