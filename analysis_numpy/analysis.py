import numpy as np

def revenue_per_year(data):
	# extract header and data seperately
	header = data[0] # col names
	data = np.array(data[1:], dtype=object) # excluding header keep all as obj
	
	# find indicies of year_id and sales col
	year_index = header.index('YEAR_ID')
	sales_index = header.index('SALES')
	
	# convert the data col to numbers
	years = data[:, year_index].astype(int) # takes all years
	sales = data[:, sales_index].astype(float)
	
	# filter unique years
	unique_years = np.unique(years)
	
	# calc total revenue per year
	for year in unique_years:
		total_revenue = sales[years == year].sum() # years == year → Creates a boolean mask for filtering This technique is called Boolean Indexing and is super efficient in NumPy! 🚀
		print(f"Total revenue in {year}: ${total_revenue:,.2f}")

