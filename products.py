products = []
while True:
	name = input('請輸入您的商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入您的商品價格： ')
	#p = [name, price]
	#p.append(name)
	#p.append(price)
	products.append([name, price])

print(products)

for p in products:
	print(p[0], ' 的價格為 ', p[1], ' 元')
