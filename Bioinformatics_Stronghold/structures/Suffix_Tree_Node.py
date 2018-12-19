from Suffix_Tree import Suffix_Tree
import sys

class Suffix_Tree_Node():

    def __init__(self, index=-1, parent_node=None, depth=-1):
        self._suffix_link = None
        self.transition_links = list()
        self.index = index
        self.depth = depth
        self.parent_node = parent_node
        self.generalized_indices = dict()

    def __str__(self):
        return "SUFFIX NODE:\n\n> Index: {}\n> Depth: {}\n> Transitions: {}".format(self.index, self.depth, self.transition_links)

    def is_leaf(self):
        return self.transition_links == list()

    def __add_suffix_link(self, suffix_node):
        self._suffix_link = suffix_node
    
    def __get_suffix_link(self):
        if self._suffix_link:
            return self._suffix_link
        else:
            return False

    def __get_transition_link(self, suffix_node, suffix=""):
        for node, sfx in self.transition_links:
            if sfx == "__@__" or suffix == sfx:
                return node
        return False

    def __add_transition_link(self, suffix_node, suffix=""):
        transition_link = self.__get_transition_link(suffix)
        if transition_link:
            self.transition_links.remove((transition_link, suffix))
        self.transition_links.append((suffix_node, suffix))

    def __has_transition(self, suffix):
        for _, sfx in self.transition_links:
            if sfx == "__@__" or suffix == sfx:
                return True
        return False

    def __traverse(self, target):
        for (node, _) in self.transition_links:
            node.__traverse(target)
        target(self)

    def __get_leaves(self):
        if self.is_leaf():
            return [self]
        else:
            return [leaf for (node, _) in self.transition_links for leaf in node.__get_leaves()]
            