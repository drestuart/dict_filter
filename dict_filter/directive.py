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


class GetChildDirective(Directive):
    """
    Directive to path into an element's children and extract a value
    """

    def __init__(self, *args):
        self.path = args


    def do_directive(self, element : dict, base : dict):

        # Start with the passed-in dictionary element
        node = element

        # Descend into the element's children as specified by self.path
        for step in self.path:
            node = node[step]

        return node

class GetFromBaseDirective(Directive):
    """
    Similar to the GetChildDirective, but retrieves a value by path 
    starting from the root of the whole dictionary
    """
    
    def __init__(self, *args):
        self.path = args


    def do_directive(self, element : dict, base : dict):

        # Start with the passed-in dictionary element
        node = base

        # Descend into the element's children as specified by self.path
        for step in self.path:
            node = node[step]

        return node