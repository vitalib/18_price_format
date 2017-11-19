import unittest
import format_price


class TestFormatPrice(unittest.TestCase):
    known_values = (
        ('0', '0'),
        ('01', '1'),
        ('1.00', '1'),
        ('3245', '3 245'),
        ('3245.000000', '3 245'),
        ('3454,00', '3454,00'),
        ('99999', '99 999'),
        ('333 333 33333.', '333 333 33333.'),
        ('incorrect value', 'incorrect value'),
        ('', ''),
                   )

    def test_known_values(self):
        '''format_price should correctly format known values'''
        for price, formatted_price in self.known_values:
            self.assertEqual(
                          format_price.format_price(price),
                          formatted_price
                             )


if __name__ == '__main__':
    unittest.main()
