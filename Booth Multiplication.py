# 9 * 13
# BR * QR
# BR = "00001001"
# QR = "00001101"
# 63
BR = "01000000"
QR = "01000000"
def pri(ACQR,Qn1,sc):
	print()
	print(ACQR[:8],end="    ")
	print(ACQR[8:],end="    ")
	print(Qn1,end="    ")
	print(sc,end="    ")
	print()

def comp(BR):
	BR1 = []
	for i in BR:
		if i == "0":BR1.append("1")
		else:BR1.append("0")
	twos = list(BR1)
	for i in range(len(BR1) - 1, -1, -1):
		if (BR1[i] == '1'):twos[i] = '0'
		else:
			twos[i] = '1'
			break
	return "".join(twos)

def add(a,b):
	c,a,b = a[8:],a[:8],b
	sum = bin(int(a, 2) + int(b, 2))
	sum = sum[2:]
	# print(sum)
	while(True):
		if len(sum) > 8:sum = sum[1:]
		if len(sum) < 8:sum = "0"+sum
		if len(sum) == 8:return sum+c

def shiftR(a):
	a = a[1] + a
	return(a[:-1],a[-1])

def BOOTH(BR,QR):
	print("AC      ",end="    ")
	print("QR      ",end="    ")
	print("Qn1 ",end="")
	print("sc",end="  ")
	AC = "00000000"
	QR = QR
	BR = BR
	BR1 = comp(BR)
	Qn1 = "0"
	sc= 8
	ACQR = AC+QR

	while(sc):
		pri(ACQR,Qn1,sc)
		if ACQR[-1]+Qn1 == "10":
			ACQR = add(ACQR,BR1)
			print("AC + BR bar + 1")
			pri(ACQR,Qn1,sc)
		if ACQR[-1]+Qn1 == "01":
			ACQR = add(ACQR,BR)
			print("AC + BR")
			pri(ACQR,Qn1,sc)
		if ACQR[-1]+Qn1 == "00" or ACQR[-1]+Qn1 == "11":pass
		ACQR,Qn1 = shiftR(ACQR)
		print("shift right")
		sc-=1
		pri(ACQR,Qn1,sc)
		print("=================================================================")
	
	print("==============================DONE==============================")
	return ACQR
	# print("Binary value = ",end="")
	# print(ACQR)
	# print("decimal value = ",end="")
	# print(int(ACQR, 2))


# BOOTH(BR,QR)

def checkbin(a):
	s = {"0","1"}
	temp = set(a)
	if temp == s or temp == {"0"} or temp == {"1"}:pass
	else:exit("should be in binary form")

def eight(a):
	checkbin(a)
	if len(a)>6:exit("should be in 0 to 111111 or 0 to 63")
	if len(a)==6:return ("00"+a)
	if len(a)<6:
		while(len(a)<6):a = "0"+a
		return ("00"+a)

sign1 = sign2 = "+ve"
print("0: decimal \n1: binary")
n = int(input())
if n == 0:
	QR = input("ENTER QR")
	if int(QR)<0:
		sign1="-ve"
		QR = abs(int(QR))
	QR = bin(int(QR)).replace("0b", "")
	QR = eight(QR)
	BR = input("ENTER BR")
	if int(BR)<0:
		sign2="-ve"
		BR = abs(int(BR))
	BR = bin(int(BR)).replace("0b", "")
	BR = eight(BR)
elif n == 1:
	QR = input("ENTER QR")
	QR = eight(QR)
	BR = input("ENTER BR")
	BR = eight(BR)
else:
	exit("invalid input")

if sign1 == "+ve" and sign2 == "+ve":inp = 0
elif sign1 == "-ve" and sign2 == "-ve":inp = 0
elif sign1 == "+ve" and sign2 == "-ve":inp = 1
elif sign1 == "-ve" and sign2 == "+ve":inp = 1

ans = BOOTH(BR,QR)
if inp == 0:
	print("decimal value = ",end="")
	print(int(ans, 2))
	print("Binary value = ",end="")
	print(ans)
else:
	print("decimal value = ",end="")
	print("-"+str(int(ans, 2)))
	ans = comp(ans)
	print("Binary value = ",end="")
	print(ans)