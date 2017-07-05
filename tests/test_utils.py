import pandas as pd
from minimaldsproject import utils
from pandas.testing import assert_frame_equal
import unittest

class TestMyPackage(unittest.TestCase):

    def setUp(self):
        self.s = pd.Series([1,1,2,3])

    def test_my_foo(self):
        assert_frame_equal(
            utils.my_foo(self.s),
            pd.DataFrame(
                {
                    "count": [2,1,1],
                    "ratio": [0.5, .25, .25]
                },
                index=[1,3,2]
            )
        )
