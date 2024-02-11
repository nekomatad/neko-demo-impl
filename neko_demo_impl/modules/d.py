from neko_demo_std import DemoInterface


class RDemoInterface(DemoInterface):
    @staticmethod
    def some_very_useful_method(very_important_arg: str = "h") -> None:
        """
        It can be some adapter for internal logic
        """
        print(very_important_arg)


DemoInterface = RDemoInterface

__all__ = ['DemoInterface']
