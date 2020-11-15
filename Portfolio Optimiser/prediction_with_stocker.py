
import stocker
from stocker import Stocker

stock_name = 'AAPL'
s = Stocker(stock_name)
#stock_data = stocker.get_data.main(stock_name, years=1)

#stock_history = s.stock
#print(stock_history.tail())

prediction, a = stocker.predict.tomorrow('AAPL')
print(prediction)
stock_names = ['GAZP.ME', 'TSLA', 'BP', 'AAPL', 'GOOG', 'SBER.ME']
E = [17.95, 40.85, 1.88, 11.92, 177.70, 24.11]

