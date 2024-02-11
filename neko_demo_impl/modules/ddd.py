from neko_demo_std.neko.types import SomeOtherDemoClass


class FirstMixin:
    first = 'first'

    def first_method(self):
        print(self.first)


class SecondMixin:
    second = 'second'

    def second_method(self):
        print(self.second)


class RSomeOtherDemoClass(FirstMixin, SecondMixin, SomeOtherDemoClass):
    """
    Original SomeOtherDemoClass does not involve implementation with mixins,
    but it is possible
    """


SomeOtherDemoClass = RSomeOtherDemoClass

__all__ = ['SomeOtherDemoClass']
