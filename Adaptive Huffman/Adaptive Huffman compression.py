from pathlib import Path
import os
import json
import heapq
from Tree_Node import TreeNode


class AdaptiveHuffmanCoding:
    def __init__(self):
        self.path = Path(os.path.dirname(os.path.realpath(__file__)))
        self.parent = None
        self.count = 1
        self.encoded_text = ''
        self.decoded_text = ''
        self.concat = ''
        self.curNode = None
        self.cmdict = {'a': '00', 'b': '01', 'c': '10', 'd': '11'}
        self.dedict = {'00': 'a', '01': 'b', '10': 'c', '11': 'd'}

    def _encode_text(self, x):
        node = self._symbol_exists(x)
        if (node == None):
            txt = self._assign_nyt_code() + self.cmdict[x]
            self.encoded_text += txt
            print(txt)
            self._add_to_tree(x)
        else:
            txt = self._assign_code(x)
            self.encoded_text += txt
            print(txt)
            self._increment_tree(node)

    # return node containing symbol
    def _symbol_exists(self, x):
        node = self.parent
        if (node.right and node.right.symbol == 'nyt'):
            if (node.left.symbol == x):
                return node.left
            node = node.right
        while (node.right != None):
            if (node.right.symbol == x):
                return node.right
            node = node.left
        return None

    # add new symbol to tree
    def _add_to_tree(self, x):
        node = self.parent
        while (node.left != None):
            node = node.left
        self.count += 1
        node.right = TreeNode(x, self.count, node)
        node.right.increment()
        self.count += 1
        node.left = TreeNode('nyt', self.count, node)
        self._increment_tree(node)
    # increment counter of existing node

    def _increment_tree(self, node):
        if (node.parent == None):
            node.increment()
            return
        self._handle_swap(node)
        node.increment()
        self._increment_tree(node.parent)

    # check swap conditions
    def _handle_swap(self, node):
        p = self.parent
        if (p.left == node and p.right.count <= node.count and p.right.number < node.number):
            self._swap(node, p.right)
            return
        elif (p.right == node and p.left.count <= node.count and p.left.number > node.number):
            self._swap(node, p.left)
            return
        if (p.right and p.right.symbol == 'nyt'):
            if (p.left.count <= node.count and p.left.number < node.number):
                self._swap(node, p.left)
                return
        while (p.right and p.right != node):
            if (p.right.count <= node.count and p.right.number < node.number):
                self._swap(node, p.right)
                return
            p = p.left

    # swap nodes
    def _swap(self, node1, node2):
        p1 = node1.parent
        p2 = node2.parent

        num1 = node1.number
        num2 = node2.number

        if (p1.right == node1):
            p1.right = node2
        else:
            p1.left = node2

        if (p2.right == node2):
            p2.right = node1
        else:
            p2.left = node1

        node1.parent = p2
        node2.parent = p1

        node1.number = num2
        node2.number = num1

    def _decode_text(self, x):
        if (x == '0'):
            if (self.curNode.left != None):
                self.curNode = self.curNode.left
                if (self.curNode.symbol != 'nyt'):
                    self.decoded_text += self.curNode.symbol
                    print(self.curNode.symbol)
                    self._increment_tree(self.curNode)
                    self.curNode = self.parent
                return
        elif (x == '1'):
            if (self.curNode.right != None):
                self.curNode = self.curNode.right
                if (self.curNode.symbol != 'nyt'):
                    self.decoded_text += self.curNode.symbol
                    print(self.curNode.symbol)
                    self._increment_tree(self.curNode)
                    self.curNode = self.parent
                return

        # if node is nyt or first node
        self.concat += x
        if (self.concat in self.dedict):
            symbol = self.dedict[self.concat]
            self.decoded_text += symbol
            self.concat = ''
            self.curNode = self.parent
            print(symbol)
            self._add_to_tree(symbol)

    def _assign_nyt_code(self):
        node = self.parent
        symbol = ''
        if (not node.left and not node.right):
            return symbol
        if (node.right.symbol == 'nyt'):
            symbol += '1'
            node = node.right
        while (node.left != None):
            symbol += '0'
            node = node.left
        return symbol

    def _assign_code(self, x):
        node = self.parent
        symbol = ''
        if (node.right.symbol == 'nyt'):
            if (node.left.symbol == x):
                return '0'
            symbol += '1'
            node = node.right

        while (node.right != None):
            if (node.right.symbol == x):
                symbol += '1'
                return symbol
            symbol += '0'
            node = node.left
        return symbol

    def adaptive_hauffman_compress(self):
        self.parent = TreeNode('parent', 1)
        x = input('enter text: ')
        while (x != '0'):
            self._encode_text(x)
            x = input()
        print("_________compressed successfully_________")
        print(h.encoded_text)

    def adaptive_hauffman_decompress(self):
        self.parent = TreeNode('parent', 1)
        self.curNode = self.parent
        x = input('enter text: ')
        while (x != 'c'):
            self._decode_text(x)
            x = input()
        print("_________decompressed successfully_________")
        print(h.decoded_text)


h = AdaptiveHuffmanCoding()
h.adaptive_hauffman_compress()
h.adaptive_hauffman_decompress()
