import unittest
from client3 import getDataPoint,getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEquals(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],(quote['top_ask']['price']+ quote['top_bid']['price'])/2 ))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEquals(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],(quote['top_ask']['price']+ quote['top_bid']['price'])/2 ))


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_priceBZero(self):
    price_a = 120
    price_b = 0
    self.assertIsNone(getRatio(price_a, price_b))
  
  def test_getRatio_priceAZero(self):
    price_a = 0
    price_b = 200
    self.assertEqual(getRatio(price_a, price_b), 0)
  
  def test_getRatio_greaterThan1(self):
    price_a = 400
    price_b = 200
    self.assertGreater(getRatio(price_a, price_b), 1)
  
  def test_getRatio_LessThan1(self):
    price_a = 200
    price_b = 400
    self.assertLess(getRatio(price_a, price_b), 1)

  def test_getRatio_exactlyOne(self):
    price_a = 500
    price_b = 500
    self.assertEqual(getRatio(price_a, price_b), 1)



if __name__ == '__main__':
    unittest.main()
