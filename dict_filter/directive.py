from abc import ABC, abstractmethod

class Directive(ABC):
    """
    Abstract base class for directives. Subclasses must override do_directive(element, base).
    """


    @abstractmethod
    def do_directive(self, element, base):
        pass

    def __call__(self, element, base):
        return self.do_directive(element, base)


class ExtractDirective(Directive):

    def __init__(self, *args):
        self.path = args


    def do_directive(self, element : dict, base : dict):

        # Start with the passed-in dictionary element
        node = element

        # Descend into the element's children as specified by self.path
        for step in self.path:
            node = node[step]

        return node
