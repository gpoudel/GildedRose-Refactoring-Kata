# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    # default items

    def test_default(self):
        items = [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7)
        ]

        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()  # Day 1
        self.assertEqual(9, gilded_rose.items[0].sell_in)
        self.assertEqual(19, gilded_rose.items[0].quality)
        self.assertEqual(4, gilded_rose.items[1].sell_in)
        self.assertEqual(6, gilded_rose.items[1].quality)

        gilded_rose.update_quality()  # Day 2
        self.assertEqual(8, gilded_rose.items[0].sell_in)
        self.assertEqual(18, gilded_rose.items[0].quality)
        self.assertEqual(3, gilded_rose.items[1].sell_in)
        self.assertEqual(5, gilded_rose.items[1].quality)

        gilded_rose.update_quality()  # Day 3
        self.assertEqual(7, gilded_rose.items[0].sell_in)
        self.assertEqual(17, gilded_rose.items[0].quality)
        self.assertEqual(2, gilded_rose.items[1].sell_in)
        self.assertEqual(4, gilded_rose.items[1].quality)

    # Aged Brie
    def test_aged_brie(self):
        items = [
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Aged Brie", sell_in=5, quality=48),
            Item(name="Aged Brie", sell_in=-2, quality=46),
        ]

        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()  # Day 1
        self.assertEqual(1, gilded_rose.items[0].sell_in)
        self.assertEqual(1, gilded_rose.items[0].quality)
        self.assertEqual(4, gilded_rose.items[1].sell_in)
        self.assertEqual(49, gilded_rose.items[1].quality)
        self.assertEqual(-3, gilded_rose.items[2].sell_in)
        self.assertEqual(48, gilded_rose.items[2].quality)

        gilded_rose.update_quality()  # Day 2
        self.assertEqual(0, gilded_rose.items[0].sell_in)
        self.assertEqual(2, gilded_rose.items[0].quality)
        self.assertEqual(3, gilded_rose.items[1].sell_in)
        self.assertEqual(50, gilded_rose.items[1].quality)
        self.assertEqual(-4, gilded_rose.items[2].sell_in)
        self.assertEqual(50, gilded_rose.items[2].quality)

        gilded_rose.update_quality()  # Day 3
        self.assertEqual(-1, gilded_rose.items[0].sell_in)
        self.assertEqual(4, gilded_rose.items[0].quality)
        self.assertEqual(2, gilded_rose.items[1].sell_in)
        self.assertEqual(50, gilded_rose.items[1].quality)
        self.assertEqual(-5, gilded_rose.items[2].sell_in)
        self.assertEqual(50, gilded_rose.items[2].quality)

        gilded_rose.update_quality()  # Day 4
        self.assertEqual(-2, gilded_rose.items[0].sell_in)
        self.assertEqual(6, gilded_rose.items[0].quality)
        self.assertEqual(1, gilded_rose.items[1].sell_in)
        self.assertEqual(50, gilded_rose.items[1].quality)
        self.assertEqual(-6, gilded_rose.items[2].sell_in)
        self.assertEqual(50, gilded_rose.items[2].quality)


if __name__ == '__main__':
    unittest.main()
