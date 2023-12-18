# 二維清單的應用

products = []

while True:
	name = input('請輸入商品名稱(輸入q離開)：')
	if name == 'q': # 輸入q離開(quit)
		break
	price = input('請輸入商品價格：')

	# way1
	# item = [] # 存每個品項+價格
	# item.append(name)
	# item.append(price)
	# products.append(item)

	# way2
	# item = [name,price] # 存每個品項+價格
	# products.append(item)

	# way3
	products.append([name, price]) # 存每個品項+價格

for item in products:
	print(item[0], '的價格是', item[1])
