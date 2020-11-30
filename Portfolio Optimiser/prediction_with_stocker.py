
import stocker
from stocker import Stocker

stock_name = 'AAPL'
s = Stocker(stock_name)
#s.plot_stock()
#stock_data = stocker.get_data.main(stock_name, years=1)

#stock_history = s.stock
#print(stock_history.tail())

prediction, a, model = stocker.predict.tomorrow('GOOG', plot=True)
#E = [17.95, 40.85, 1.88, 11.92, 177.70, 24.11]
#p = model.predict(E)
#print(prediction)
#stock_names = ['GAZP.ME', 'TSLA', 'BP', 'AAPL', 'GOOG', 'SBER.ME']
#E = [17.95, 40.85, 1.88, 11.92, 177.70, 24.11]

