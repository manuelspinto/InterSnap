__author__ = 'masp'

class Stat:
    def __init__(self, dea = 0, lon = 0, top = 0, dele = 0):
        self.dea = dea
        self.lon = lon
        self.top = top
        self.dele = dele

class Tree:
    def __init__(self, root = None, stat = Stat()):
        self.root = Node(-1)
        self.stat = stat

    def _find_px(self, px, mask):
        lvl = 0
        aux = self.root
        while True:
            if px[lvl] == "0":
                if aux.left is None:
                    aux.left = Node(-1)
                if lvl != mask -1:
                    aux = aux.left
                else: return aux.left
            else:
                if aux.right is None:
                    aux.right = Node(-1)
                if lvl != mask -1:
                    aux = aux.right
                else: return aux.right
            lvl +=1


    def _inorder_spread(self, node):
        if node.left is not None:
            if node.left.adv == 0:
                node.left.asn = node.asn
            else:
                node.left.pasn = node.asn
            self._inorder_spread(node.left)
        if node.right is not None:
            if node.right.adv == 0:
                node.right.asn = node.asn
            else:
                node.right.pasn = node.asn
            self._inorder_spread(node.right)


    def _spread_asn(self):
        root = self.root
        self._inorder_spread(root)

    def insert_px(self, px, mask, asn):
        node = self._find_px(px, mask)
        node.asn = asn
        node.adv = 1

    def _inorder_stat(self, node):
        if node.adv == 1:
            if node.pasn == -1:
                if (node.left is None) and (node.right is None): #no child
                    self.stat.lon += 1
                else:
                    self.stat.top += 1
            else:
                if node.asn == node.pasn:
                    self.stat.dea += 1
                else:
                    self.stat.dele += 1

        if node.left is not None:
            self._inorder_stat(node.left)
        if node.right is not None:
            self._inorder_stat(node.right)

    def _get_type(self):
        root = self.root
        self._inorder_stat(root)


    def get_stat(self):
        self._spread_asn()
        self._get_type()
        #totstr = "Total number of px: {}".format(self.stat.tot)
        #deastr = "Total number of deaggregated pxs: {}".format(self.stat.dea)
        deastr = "{}".format(self.stat.dea)
        fullstr = []
        fullstr.append(deastr)
        return fullstr


class Node:
    def __init__(self, asn, pasn = -1, left = None, right = None, adv = 0):
        self.asn = asn
        self.pasn = pasn
        self.left = left
        self.right = right
        self.adv = adv

    def __str__(self):
        return str(self.asn)

