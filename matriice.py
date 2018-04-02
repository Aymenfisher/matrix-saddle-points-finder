matrice=[[1,2,3],[0,5,3],[-1,-2,-1],[-1,-2,-1]]
number_of_lines=len(matrice)
number_of_columns=len(matrice[0])
line=0
while line<number_of_lines:
	maximum=max(matrice[line])
	column=0
	while column<number_of_columns:
		suspect=matrice[line][column]
		if suspect==maximum:
			line2=0
			while line2<number_of_lines:
				to_check=matrice[line2][column]
				if suspect==to_check :
				  line2+=1
				  pass
				elif suspect>to_check:
					line2+=1
					break	
				if line2==number_of_lines-1:
					print "point-col found :"
					print "ligne :",line+1
					print "colonne: ",column+1
					print "Valeur: ",maximum
					print '-'*6
					line2+=1
				line2+=1	
					
		column+=1
	line+=1	