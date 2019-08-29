'''def rec(n):
	if n==0:
		return 1
	elif n==1:
		return 3
	else:
		value=3*rec(n-1)
		return value




print(rec(5))'''



def recop(n):
	k=int(n/2)
	
	if n==0:
		return 1
	elif n==1:
		return 3
	else:
		#print("3 to power {} multiplied with 3 to power {}".format(k,n-k))
		result1 = recop(k)
		#print( "{} from 3 to power of{}".format(result1,k))
		result2 = recop(n-k)
		#print("{} from 3 to power of{}".format(result2,n-k))
		#print(result1*result2)
		return result1*result2

	'''if l<=0:
		return 1
	elif l==1:
		return 3
	else:
		result2 =(3*recop(l-1))
		#print(result2)
		return result2

	result =result1*result2
	return result'''

print(recop(9))

'''
#3^n = 3^k*3^(n-k)
recop(9)= recop(4)*recop(5)
recop(4)=recop(2)*recop(2)
recop(2)='''





	




