#coding-utf8
from math import*
import os
from modula import*
rep="oui"
while rep=="oui":
	try:
		
		Tuple={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
		print("|...Convertisseur de nombre dans toutes les bases...|\n\n")
		choix=int(input('1-Utiliser les nombres à virgule\n2-Quitter la base 10\n3-Quitter la base 16 \n4-Quitter la base 8 \n5-Quitter la base 2\nVotre choix: '))
		
		if choix==1:
			a=int(input('Entrez le nombre'))
		elif choix==2:
			n1=input('\n\nENTREZ LE NOMBRE N= ')
			p=[]
			a=int(input('Vous pouvez specifier sa base de destination\n1-2\n2-8\n3-16\n4-Toute les autres\n'))
			p.append('\nBase 2:'+n1+' = ('+dix_vers(n1,2,Tuple)+')\n')
			p.append('\nBase 8:'+n1+' = ('+dix_vers(n1,8,Tuple)+')\n')
			p.append('\nBase 16:'+n1+' = ('+dix_vers(n1,16,Tuple)+')\n')
			if a==1:
				print(p[0])
			elif a==2:
				print(p[1])
			elif a==3:
				print(p[2])
			elif a==4:
				for t in p:
					print(t)
			else:
				print('veuillez bien choisir entre 1 2 et 3')
			os.system("pause")
		elif choix==3:
			p=[]
			n1=input('\n\nENTREZ LE NOMBRE N= ')
			l=n1
			resultat=seize_10(list(n1),Tuple)
			k='\nBase 10:'+l+' = '+str(resultat)+'\n'
			p.append(k)
			p.append('Base 2:'+n1+' = ('+dix_vers(resultat,2,Tuple)+')\n')
			p.append('Base 8:'+n1+' = ('+dix_vers(resultat,8,Tuple)+')\n')
			a=int(input('Vous pouvez specifier sa base de destination\n1-2\n2-8\n3-10\n4-Toutes les autres\n'))
			if a==1:
				print(p[1])
			elif a==2:
				print(p[2])
			elif a==3:
				print(p[0])
			elif a==4:
				for t in p:
					print(t)
			else:
				print('veuillez bien choisir entre 1 2 et 3')
			os.system("pause")


			
		elif choix==4:
			n1=input('\n\nENTREZ LE NOMBRE N= ')
			p=[]
			resultat=vers_dix(8,n1)
			p.append('Base 10:'+n1+' = '+str(vers_dix(8,n1))+'\n')
			p.append('Base 2:'+n1+' = '+dix_vers(resultat,2,Tuple)+'\n')
			p.append('Base 16:'+n1+' = '+dix_vers(resultat,16,Tuple)+'\n')
			a=int(input('Vous pouvez specifier sa base de destination\n1-2\n2-16\n3-10\n4-Toutes les autres\n'))
			if a==1:
				print(p[1])
			elif a==2:
				print(p[2])
			elif a==3:
				print(p[0])
			elif a==4:
				for t in p:
					print(t)
			else:
				print('veuillez bien choisir entre 1 2 et 3')
			os.system("pause")


		elif choix==5:
			p=[]
			n1=input('\n\nENTREZ LE NOMBRE N= ')
			resultat=str(vers_dix(2,n1))
			p.append('Base 10: '+n1+' = '+resultat+'\n')
			p.append('\nBase 8: '+n1+' = '+dix_vers(resultat,8,Tuple)+'\n')
			p.append('\nBase 16: '+n1+' = '+dix_vers(resultat,16,Tuple)+'\n')
			a=int(input('Vous pouvez specifier sa base de destination\n1-10\n2-8\n3-16\n4-Toutes les autres\n'))
			if a==1:
				print(p[0])
			elif a==2:
				print(p[1])
			elif a==3:
				print(p[2])
			elif a==4:
				for t in p:
					print(t)
			else:
				print('veuillez bien choisir entre 1 2 et 3')
			os.system("pause")

		else:
			print('\nMerci d\'avoir visiter nos services\n')
		rep=input("\nvoulez vous recommencer? (oui ou non) ")
		if rep=="non":
			print('\nMerci de vous formez vous meme plutard histoire de performiser le code qui me régit\n')
			os.system("pause")
			break
		elif rep!="oui":
			print('Bye...')
			os.system("pause")
			break
		if rep=="oui":
			os.system('cls')
		
	except:
		print('\nVous avez mal renseigner un champ')
		if rep=="non":
			print('\nMerci de vous formez vous meme plutard histoire de performiser le code qui me régit\n')
			break
		elif rep!="oui":
			print('Bye...')
			break
		if rep=="oui":
			os.system('cls')
		os.system("pause")
        
		
				
				
			
				
				
			
				
		



