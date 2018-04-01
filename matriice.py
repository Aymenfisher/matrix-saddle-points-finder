matrice=[[1,2,3],[0,5,3],[-1,-2,-1],[50,-55,3]]
for n in matrice:
	line_number=matrice.index(n)
	maximum=max(n)
	index_of_max=n.index(maximum)
	for i in matrice:
		minimum=i[index_of_max]
		if maximum==minimum:
			pass
		elif maximum>minimum:
			break
	else:
		print 'point col found!!! :'
		print "ligne: ",line_number+1
		print "colonne: ",index_of_max+1
		print "Valeur: ",maximum


			
			
