############################################################################
# Copyright ESIEE Paris (2018)                                             #
#                                                                          #
# Contributor(s) : Benjamin Perret                                         #
#                                                                          #
# Distributed under the terms of the CECILL-B License.                     #
#                                                                          #
# The full license is in the file LICENSE, distributed with this software. #
############################################################################

import unittest
import numpy as np
import higra as hg


class TestLCAFast(unittest.TestCase):

    @staticmethod
    def getTree():
        parent_relation = np.asarray((5, 5, 6, 6, 6, 7, 7, 7), dtype=np.uint64)
        return hg.Tree(parent_relation)

    def test_LCAFast(self):
        t = TestLCAFast.getTree()
        lca = hg.LCAFast(t)

        self.assertTrue(lca.lca(0, 0) == 0)
        self.assertTrue(lca.lca(3, 3) == 3)
        self.assertTrue(lca.lca(5, 5) == 5)
        self.assertTrue(lca.lca(7, 7) == 7)
        self.assertTrue(lca.lca(0, 1) == 5)
        self.assertTrue(lca.lca(1, 0) == 5)
        self.assertTrue(lca.lca(2, 3) == 6)
        self.assertTrue(lca.lca(2, 4) == 6)
        self.assertTrue(lca.lca(3, 4) == 6)
        self.assertTrue(lca.lca(5, 6) == 7)
        self.assertTrue(lca.lca(0, 2) == 7)
        self.assertTrue(lca.lca(1, 4) == 7)
        self.assertTrue(lca.lca(2, 6) == 6)

    def test_LCAFastV(self):
        g = hg.get_4_adjacency_graph((2, 2))
        t = hg.Tree((4, 4, 5, 5, 6, 6, 6))
        lca = hg.LCAFast(t)

        ref = (4, 6, 6, 5)
        res = lca.lca(g)
        self.assertTrue(np.all(ref == res))

    def test_LCAFastVertices(self):
        t = hg.Tree((4, 4, 5, 5, 6, 6, 6))
        lca = hg.LCAFast(t)
        res = lca.lca((0, 0, 1, 3), (0, 3, 0, 0))
        self.assertTrue(np.all(res == (0, 6, 4, 6)))


if __name__ == '__main__':
    unittest.main()
