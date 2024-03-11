'''Question "abc xyz pqr lmn" -> ['abc', 'xyz', 'pqr', 'lmn']'''


string="abc xyz pqr lmn"
result=[]
a = " abc xyz pqr lmn"
s = a.split() #split gives the splitted list ['abc', 'xyz', 'pqr', 'lmn']
print(s)
result = " ".join(i[::-1] for i in s)
print(result)