
import stocker
from stocker import Stocker

stock_name = 'AAPL'
s = Stocker(stock_name)
#stock_data = stocker.get_data.main(stock_name, years=1)

#stock_history = s.stock
#print(stock_history.tail())
s.plot_stock()

prediction = stocker.predict.tomorrow('AAPL')

