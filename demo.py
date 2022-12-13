if __name__ == '__main__':
	# n = int(input())
	n=117
	res = set()
	str_n = str(n)
	for i in range(len(str_n)):
		in_sum=str_n[i]
		if (int(str_n[i])%2==0):
				res.add(int(str_n[i]))

		for j in range(i+1,len(str_n)):
			in_sum+=str_n[j]
			
			if(int(in_sum)%2==0):
				res.add(int(in_sum))

	print(res,len(res))










#n=3568