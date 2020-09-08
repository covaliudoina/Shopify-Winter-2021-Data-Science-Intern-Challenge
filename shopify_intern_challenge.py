import sys
import pandas as pd

def main():

	data =  pd.read_csv('orders.csv', header=0)
	df = pd.DataFrame(data)

#Question 1.a.Separate the dataset in D2C AND B2C
	#D2C -customer who order up to 10 items per order
	#B2B-customers who order more than 10 items per order

	D2C=df[df.total_items <= 10]  
	AOV_D2C= D2C.order_amount.mean()
	print('Question 1.a: \n Average Order Value for D2C customers is: $',AOV_D2C)

	B2B=df[df.total_items >10]     
	AOV_B2B= B2B.order_amount.mean()
	print(' Average Order Value for B2B customers is: $',AOV_B2B)

#Question 2.b and c Calculate the Median Order Value for the entire dataset

	Median_Order_Value= df.order_amount.median()
	print('Question 1.b and 1.c: \n Median Order Value is: $',Median_Order_Value)

	#Average basket value for B2B customers
	ABV_B2B= B2B.total_items.mean()
	print(" Average basket value for B2B customers is:",ABV_B2B,'items' )

	#Average basket value for D2C customers
	ABV_D2C= D2C.total_items.mean()
	print(" Average basket value for D2C customers is:",ABV_D2C,'items' )

if __name__ == "__main__":
	main()