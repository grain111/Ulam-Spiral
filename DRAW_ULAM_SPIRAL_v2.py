from PIL import Image

def ifprime(x):
	y,c = 1,1
	while y < x**0.5:
		y = y+1
		if x%y == 0:
			c = c+1
			if c>1:
				return False
	if c == 1:
		return True

def cmatr():
	zakres = int(input("Prosze wprowadzic rozmiar tablicy: "))
	Matrix = [[0 for x in range(zakres+1)] for y in range(zakres+1)]
	a = int(zakres*0.5)
	b = a
	mnoznik = 2
	k = 2
	Value = 1
	Matrix[a][b] = Value
	while Value < zakres**2:
		w = (-1)**mnoznik
		for c in range(1,k):
			a = a
			b = b + w
			Value = Value + 1
			print "Value= %s\r"%Value,
			Matrix[a][b] = Value
		for c in range(1,k):
			a = a + w
			b = b
			Value = Value + 1
			print "Value= %s\r"%Value,
			Matrix[a][b] = Value
		k = k + 1
		mnoznik = mnoznik +1
	return Matrix

print("Generowanie tablicy z danymi")
Matrix = cmatr()
zakres = len(Matrix) - 1
print("Macierz z danymi zostala wygenerowana")
# count = float(0)
# Value = Matrix[0][0]

img = Image.new( 'RGB', (zakres+1,zakres+1), "white") # create a new black image
pixels = img.load() # create the pixel map

for q in range(zakres+1):
	for w in range(zakres+1):
		# print "%.2f  percent\r" %((count/(Value))*100),
		# count = count + 1
		if ifprime(Matrix[q][w]) == True:
			pixels[q,w] = (0,0,0)
		else:
			Matrix[q][w] = " "

img.save("ULAM_SPIRAL.png")
