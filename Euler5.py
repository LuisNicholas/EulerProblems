def SmallestOneToTwenty():
	i = 0
	while i < 10000000:	
		j = 0
		i = i + 1
		for x in range(1 , 21):
			if i % x == 0:
				j = j + 1
			if j >= 20:
				print i

SmallestOneToTwenty()
		
				
