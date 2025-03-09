import matplotlib.pyplot as plt
from scipy import stats

house_sizes = [750, 800, 850, 900, 950, 1000, 1100, 1200, 1300, 1400, 1500]
house_prices = [150, 160, 165, 170, 175, 180, 200, 220, 240, 260, 280]

slope, intercept, r, p, std_err = stats.linregress(house_sizes,house_prices)

def predict(x):
	return round(slope,2) * x + intercept

predicted_price = predict(1050)

print(f'predicted price for 1050sqft. house = {predicted_price:.2f}K')

regression_line = list(map(predict, house_sizes))

plt.scatter(house_sizes, house_prices, color='green', label='Actual data')
plt.plot(house_sizes, regression_line, color='red', label='regression line')
plt.xlabel("House Size (sq. ft.)")
plt.ylabel("House Price ($1000s)")
plt.title("House Size vs. Price Regression")
plt.legend()
plt.show()

print(f'equation: {slope:.2f} * size + {intercept:.2f}')
print(f'correlation coefficient: {r:.2f}')
