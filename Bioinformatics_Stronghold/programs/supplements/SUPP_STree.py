"""
NAME: Aakash Sudhakar
DATE: December 27, 2018

A Python 3 implementation of the Suffix text characterization tree. 

Algorithm based on:
McCreight, Edward M. "A space-economical suffix tree construction algorithm." - ACM, 1976.

Implementation based on:
UH CS - 58093 String Processing Algorithms Lecture Notes

Improved upon from Suffix Tree implementation by Github user @ptrun.
"""

import sys


class Suffix_Tree():
    """
    \nSuffix tree class representation.
    """

    def __init__(self, data_input=""):
        self.root = Suffix_Node()
        self.root.depth = 0
        self.root.index = 0
        self.root.parent = self.root
        self.root._add_suffix_link(self.root)
        if not data_input == "":
           self.construct_suffix_tree_type(data_input)

    def __validate_input(self, data_input):
        """
        \nChecks the validity of the input.
        \nThrows ValueError in case of invalid input.

        INPUT:
            [list] data_input
        OUTPUT: 
            [str] "stree"/"gst"
        """
        if isinstance(data_input, str):
            return "stree"
        elif isinstance(data_input, list):
            if all(isinstance(data, str) for data in data_input):
                return "gst"
        raise ValueError("String argument should be of type String or a List of Strings.")

    def construct_suffix_tree_type(self, data_input):
        """
        \nConstructs Suffix tree type based on given input.
        \nIf input is single string, constructed Suffix tree is default (McCreight).
        \nIf input is list of strings, constructed Suffix tree is generalized.

        INPUT:
            [str]/[list] data_input
        OUTPUT: 
            None
        """
        data_type = self.__validate_input(data_input)

        if data_type == "stree":
            data_input += next(self.__generate_terminal_symbols())
            self.__default_tree_constructor(data_input)
        if data_type == "gst":
            self.__generalized_tree_constructor(data_input)

    def __default_tree_constructor(self, data_input):
        """
        \nConstructs default Suffix tree with single string data input.

        INPUT: 
            [str] data_input
        OUTPUT: 
            None
        """
        self.word = data_input
        self.__tree_algorithm_McCreight(data_input)

    def __tree_algorithm_McCreight(self, data_input):
        """
        \nConstructs default Suffix tree using McCreight algorithm.

        INPUT: 
            [str] data_input
        OUTPUT: 
            None
        """
        rel_node_pos, rel_depth = self.root, 0

        for iterator in range(len(data_input)):
            while rel_node_pos.depth == rel_depth and rel_node_pos._has_transition(data_input[rel_depth + iterator]):
                rel_node_pos = rel_node_pos._get_transition_link(data_input[rel_depth + iterator])
                rel_depth = rel_depth + 1
                while rel_depth < rel_node_pos.depth and data_input[rel_node_pos.index + rel_depth] == data_input[iterator + rel_depth]:
                    rel_depth += 1

            if rel_depth < rel_node_pos.depth:
                rel_node_pos = self.__create_suffix_node(data_input, rel_node_pos, rel_depth)

            self.__create_suffix_leaf(data_input, iterator, rel_node_pos, rel_depth)
            if not rel_node_pos._get_suffix_link():
                self.__create_suffix_link(data_input, rel_node_pos)

            rel_node_pos = rel_node_pos._get_suffix_link()
            rel_depth -= 1

            if rel_depth < 0:
                rel_depth = 0

    def __create_suffix_node(self, data_input, current_node, relative_depth):
        """
        \nCreates branch node on Suffix tree with given parameters.

        INPUT: 
            [str] data_input
            [Suffix_Node] current_node
            [int] relative_depth
        OUTPUT: 
            [Suffix_Node] new_suffix_node
        """
        relative_index, parent_node = current_node.index, current_node.parent
        new_suffix_node = Suffix_Node(index=relative_index, depth=relative_depth)

        new_suffix_node._add_transition_link(current_node, data_input[relative_index+relative_depth])
        current_node.parent = new_suffix_node

        parent_node._add_transition_link(new_suffix_node, data_input[relative_index+parent_node.depth])
        new_suffix_node.parent = parent_node
        return new_suffix_node

    def __create_suffix_leaf(self, data_input, relative_iterator, current_node, relative_depth):
        """
        \nCreates leaf node on Suffix tree with given parameters. 

        INPUT:
            [str] data_input
            [int] relative_iterator
            [Suffix_Node] current_node
            [int] relative_depth
        OUTPUT: 
            [Suffix_Node] new_suffix_node
        """
        new_suffix_node = Suffix_Node()
        new_suffix_node.index = relative_iterator
        new_suffix_node.depth = len(data_input) - relative_iterator

        current_node._add_transition_link(new_suffix_node, data_input[relative_iterator + relative_depth])
        new_suffix_node.parent = current_node
        return new_suffix_node

    def __create_suffix_link(self, data_input, current_node):
        """
        \nCreates link across Suffix node with given parameters.

        INPUT:
            [str] data_input
            [Suffix_Node] current_node
        OUTPUT: 
            None
        """
        relative_depth = current_node.depth
        relative_suffix_link = current_node.parent._get_suffix_link()

        while relative_suffix_link.depth < relative_depth - 1:
            relative_suffix_link = relative_suffix_link._get_transition_link(data_input[current_node.index + relative_suffix_link.depth + 1])
        
        if relative_suffix_link.depth > relative_depth - 1:
            relative_suffix_link = self.__create_suffix_node(data_input, relative_suffix_link, relative_depth-1)
        current_node._add_suffix_link(relative_suffix_link)

    def __generalized_tree_constructor(self, data_input_arr):
        """
        \nConstructs generalized Suffix tree (GST) with single string data input.

        INPUT: 
            [list] data_input_arr
        OUTPUT: 
            None
        """
        terminal_symbols = self.__generate_terminal_symbols()

        data_genr_arr = "".join([data + next(terminal_symbols) for data in data_input_arr])
        self.word = data_genr_arr
        self.__get_GST_start_indices(data_input_arr)

        self.__default_tree_constructor(data_genr_arr)
        self.root._traverse(self.__label_GST_nodes)

    def __label_GST_nodes(self, current_node):
        """
        \nLabels nodes of GST with indices of strings found across descendants.

        INPUT:
            [Suffix_Node] current_node
        OUTPUT:
            None
        """
        if current_node.is_leaf():
            word_index = {self.__get_word_index(current_node.index)}
        else:
            word_index = {link for links in current_node.transition_links for link in links[0].generalized_indices}
        current_node.generalized_indices = word_index

    def __get_word_index(self, node_index):
        """
        \nGets index of input string based on node's starting index.

        INPUT:
            [int] node_index
        OUTPUT:
            [int] relative_index
        """
        relative_index = 0
        for word_start_index in self.word_starts[1:]:
            if node_index < word_start_index:
                return relative_index
            else:
                relative_index += 1
        return relative_index

    def determine_LCS(self, string_indices=-1):
        """
        \nDetermines Longest Common Substring (LCS) of strings across Suffix tree.
        \nIf string_indices is provided, those strings are searched.
        \nIf string_indices is not provided, all strings are searched.

        INPUT:
            [int]/[list] string_indices
        OUTPUT:
            None
        """
        if string_indices == -1 or not isinstance(string_indices, list):
            string_indices = set(range(len(self.word_starts)))
        else:
            string_indices = set(string_indices)

        deepest_node = self.__GST_traverser(self.root, string_indices)
        start_index, end_index = deepest_node.index, deepest_node.index + deepest_node.depth
        return self.word[start_index:end_index]

    def __GST_traverser(self, node, string_indices):
        """
        \nTraverses labeled GST using string indices to find LCS.

        INPUT:
            [Suffix_Node] node
            [set] string_indices
        OUTPUT:
            [Suffix_Node] node/deepest_node
        """
        string_nodes = [self.__GST_traverser(node_link, string_indices) for (node_link,_) in node.transition_links if node_link.generalized_indices.issuperset(string_indices)]

        if string_nodes == []:
            return node

        deepest_node = max(string_nodes, key=lambda X: X.depth)
        return deepest_node

    def __get_GST_start_indices(self, data_input):
        """
        \nReturns starting indices of strings across GST.

        INPUT:
            [list] data_input
        OUTPUT:
            None
        """
        self.word_starts, index = list(), 0
        for data_index in range(len(data_input)):
            self.word_starts.append(index)
            index += len(data_input[data_index]) + 1

    def find(self, substring):
        """
        \nFinds starting position of input substring within string(s) used for Suffix tree construction.

        INPUT:
            [str] substring
        OUTPUT:
            [int] node.index/-1
        """
        node = self.root
        while True:
            edge = self.__get_edge_label(node, node.parent)
            if edge.startswith(substring):
                return node.index
            
            iterator = 0
            while(iterator < len(edge) and edge[iterator] == substring[0]):
                substring = substring[1:]
                iterator += 1
            
            if iterator != 0:
                if iterator == len(edge) and substring != "":
                    pass
                else:
                    return -1
            
            node = node._get_transition_link(substring[0])
            if not node:
                return -1

    def find_all(self, substring):
        """
        \nFinds all starting positions of input substring within string(s) used for Suffix tree construction.

        INPUT:
            [str] substring
        OUTPUT:
            [list] []/substr_positions
        """
        node = self.root
        while True:
            edge = self.__get_edge_label(node, node.parent)
            if edge.startswith(substring):
                break

            iterator = 0
            while(iterator < len(edge) and edge[iterator] == substring[0]):
                substring = substring[1:]
                iterator += 1
            
            if iterator != 0:
                if iterator == len(edge) and substring != '':
                    pass
                else:
                    return []

            node = node._get_transition_link(substring[0])
            if not node:
                return []

        substr_positions = sorted([leaf.index for leaf in node._get_leaves()])
        return substr_positions

    def __get_edge_label(self, node, parent):
        """
        \nReturns edge label between node and its parent.

        INPUT:
            [Suffix_Node] node
            [Suffix_Node] parent
        OUTPUT:
            [str] self.word[...]
        """
        start_index, end_index = node.index + parent.depth, node.index + node.depth
        return self.word[start_index:end_index]

    def __generate_terminal_symbols(self):
        """
        \nGenerates unique terminal symbols used for GST construction.
        \nNOTE: Uses UPEA characters to ensure non-string-occurring terminal symbols.

        INPUT:
            None
        OUTPUT:
            [chr] chr(symbol)
        """
        UPEAs = list(list(range(0xE000,0xF8FF+1)) + list(range(0xF0000,0xFFFFD+1)) + list(range(0x100000, 0x10FFFD+1)))
        for symbol in UPEAs:
            yield chr(symbol)
        raise ValueError("Too many input strings.")


class Suffix_Node():
    """
    \nSuffix tree node class representation.
    """

    def __init__(self, index=-1, parent_node=None, depth=-1):
        # Links
        self.suffix_link = None
        self.transition_links = []
        # Properties
        self.index = index
        self.depth = depth
        self.parent = parent_node
        self.generalized_indices = {}

    def __str__(self):
        return "SUFFIX_NODE: \n> Index: {} \n> Depth: {} \n> Transitions: {}".format(str(self.index), str(self.depth), str(self.transition_links))

    def _add_suffix_link(self, suffix_node):
        self.suffix_link = suffix_node

    def _get_suffix_link(self):
        if self.suffix_link:
            return self.suffix_link
        else:
            return False

    def _get_transition_link(self, suffix_actual):
        for node, suffix_expected in self.transition_links:
            if suffix_expected == "__@__" or suffix_actual == suffix_expected:
                return node
        return False

    def _add_transition_link(self, suffix_node, suffix=""):
        transition_link = self._get_transition_link(suffix)
        if transition_link:
            self.transition_links.remove((transition_link, suffix))
        self.transition_links.append((suffix_node, suffix))

    def _has_transition(self, suffix_actual):
        for _, suffix_expected in self.transition_links:
            if suffix_expected == "__@__" or suffix_actual == suffix_expected:
                return True
        return False

    def is_leaf(self):
        return self.transition_links == []

    def _traverse(self, labeler):
        for (node, _) in self.transition_links:
            node._traverse(labeler)
        labeler(self)

    def _get_leaves(self):
        if self.is_leaf():
            return [self]
        else:
            return [leaf for (node, _) in self.transition_links for leaf in node._get_leaves()]