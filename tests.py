import unittest
import dice


class TestDiceMethods(unittest.TestCase):

    def test_dice_is_instance_of_Die_class(self):
        d20 = dice.Die(20)
        d6 = dice.D6()
        self.assertIsInstance(d20, dice.Die)
        self.assertIsInstance(d6, dice.D6)

    def test_D6_is_subclass_of_Die(self):
        self.assertTrue(issubclass(dice.D6, dice.Die))


if __name__ == '__main__':
    unittest.main()