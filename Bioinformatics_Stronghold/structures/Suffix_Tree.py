from Suffix_Tree_Node import Suffix_Tree_Node
import sys

class Suffix_Tree():

    def __init__(self, str_input=""):
        self.root = Suffix_Tree_Node()
        self.root.depth = 0
        self.root.index = 0
        self.root.parent = self.root
        self.root.__add_suffix_link(self.root)

        if not str_input == "":
            self.construct_tree_by_input(str_input)

    def __verify_input(self, str_input):
        if isinstance(str_input, str):
            return "st"
        elif isinstance(str_input, list):
            if all(isinstance(item, str) for item in str_input):
                return "gst"

        raise ValueError("Argument should be 'STRING' or [LIST OF STRINGS].")

    def construct_tree_by_input(self, str_params):
        param_type = self.__verify_input(str_params)

        if param_type == "st":
            str_params += next(self.__generate_terminal_symbols())
            self.__constructor_helper(str_params)
        if param_type == "gst":
            self.__construct_generalized_suffix_tree(str_params)

    def determine_lcs(self, str_index=-1):
        if str_index == -1 or not isinstance(str_index, list):
            str_index = set(range(len(self.word_starts)))
        else:
            str_index = set(str_index)

        deepest_node = self.__find_lcs(self.root, str_index)
        start_pos, end_pos = deepest_node.index, deepest_node.index + deepest_node.depth
        return self.word[start_pos:end_pos]

    def find_substr(self, substr):
        node = self.root
        while True:
            edge = self.__get_edge_label(node, node.parent_node)
            if edge.startswith(substr):
                return node.index

            iterator = 0
            while (iterator < len(edge) and edge[iterator] == substr[0]):
                substr = substr[1:]
                iterator += 1

            if iterator != 0:
                if iterator == len(edge) and substr != "":
                    pass
                else:
                    return -1

            node = node.__get_transition_link(substr[0])
            if not node:
                return -1

    def find_all_substr(self, substr):
        node = self.root
        while True:
            edge = self.__get_edge_label(node, node.parent_node)
            if edge.startswith(substr):
                break

            iterator = 0
            while (iterator < len(edge) and edge[iterator] == substr[0]):
                substr = substr[1:]
                iterator += 1

            if iterator != 0:
                if iterator == len(edge) and substr != "":
                    pass
                else:
                    return []
            
            node = node.__get_transition_link(substr[0])
            if not node:
                return []

        leaves = node.__get_leaves()
        return [N.index for N in leaves]

    def __constructor_helper(self, str_params):
        self.word = str_params
        self.__constructor_algorithm(str_params)

    def __constructor_algorithm(self, str_params):
        current_node, distance = self.root, 0
        for iterator in range(len(str_params)):
            while current_node.depth == distance and current_node.__has_transition(str_params[distance+iterator]):
                current_node = current_node.__get_transition_link(str_params[distance+iterator])
                distance += 1
                while distance < current_node.depth and str_params[current_node.index+distance] == str_params[iterator+distance]:
                    distance += 1
            if distance < current_node.depth:
                current_node = self.__create_node(str_params, current_node, distance)
            self.__create_leaf(str_params, iterator, current_node, distance)
            if not current_node.__get_suffix_link():
                self.__determine_suffix_link(str_params, current_node)
            current_node = current_node.__get_suffix_link()
            distance -= 1
            if distance < 0:
                distance = 0
    
    def __create_node(self, str_params, current_node, distance):
        index = current_node.index
        parent_node = current_node.parent_node
        curr_sfx_node = Suffix_Tree_Node(index=index, depth=distance)
        curr_sfx_node.__add_transition_link(current_node, str_params[index+distance])
        current_node.parent_node = curr_sfx_node
        parent_node.__add_transition_link(curr_sfx_node, str_params[index+parent_node.depth])
        curr_sfx_node.parent_node = parent_node
        return curr_sfx_node

    def __create_leaf(self, str_params, index, current_node, distance):
        sfx_node = Suffix_Tree_Node()
        sfx_node.index = index
        sfx_node.depth = len(str_params) - index
        current_node.__add_transition_link(sfx_node, str_params[index+distance])
        sfx_node.parent_node = current_node
        return sfx_node

    def __determine_suffix_link(self, str_params, current_node):
        distance = current_node.depth
        par_sfx_node = current_node.parent_node.__get_suffix_link()
        while par_sfx_node.depth < distance - 1:
            par_sfx_node = par_sfx_node.__get_transition_link(str_params[current_node.index+par_sfx_node.depth+1])
        if par_sfx_node.depth > distance - 1:
            par_sfx_node = self.__create_node(str_params, par_sfx_node, distance - 1)
        current_node.__add_suffix_link(par_sfx_node)

    def __construct_generalized_suffix_tree(self, str_params):
        terminal_symbols = self.__generate_terminal_symbols()

        mod_str_params = "".join([param + next(terminal_symbols) for param in str_params])
        self.word = mod_str_params
        self.__get_generalized_word_start_indices(str_params)
        self.__constructor_helper(mod_str_params)
        self.root.__traverse(self.__label_generalized_suffix_nodes)

    def __label_generalized_suffix_nodes(self, suffix_node):
        if suffix_node.is_leaf():
            indices = {self.__get_start_index_of_word(suffix_node.index)}
        else:
            indices = {node for nodes in suffix_node.transition_links for node in nodes[0].generalized_indices}
        suffix_node.generalized_indices = indices

    def __get_start_index_of_word(self, index):
        iterator = 0
        for idx in self.word_starts[1:]:
            if index < idx:
                return iterator
            else:
                iterator += 1
        return iterator

    def __find_lcs(self, node, str_index):
        nodes = [self.__find_lcs(N, str_index) for (N, _) in node.transition_links if N.generalized_indices.issuperset(str_index)]
        if nodes == []:
            return node
        
        deepest_node = max(nodes, key=lambda N: N.depth)
        return deepest_node

    def __get_generalized_word_start_indices(self, str_params):
        self.word_starts, iterator = list(), 0
        for param_index in range(len(str_params)):
            self.word_starts.append(iterator)
            iterator += len(str_params[param_index]) + 1

    def __get_edge_label(self, current_node, parent_node):
        return self.word[current_node.index+parent_node.depth:current_node.index+current_node.depth]

    def __generate_terminal_symbols(self):
        UPPAs = list(list(range(0xE000,0xF8FF+1)) + list(range(0xF0000,0xFFFFD+1)) + list(range(0x100000, 0x10FFFD+1)))
        for iterator in UPPAs:
            yield(chr(iterator))

def main():
    stree = Suffix_Tree("abcdefghab")
    print(stree.find_substr("abc"))
    print(stree.find_all_substr("ab"))

if __name__ == "__main__":
    main()