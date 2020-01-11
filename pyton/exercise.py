

s = 'django'
print(s[0])
print(s[-1])
print(s[:4])
print(s[1:4])



l =[3,7,[1,4,'hallo']]
l[2][2] = 'goodbye'
print(l)



d1 = {'simple_key':'hello'}
d1['simple_key']
print(d1)
d2 = {'k1':{'k2':'hello'}}
d2['k1']['k2']
print (d2)
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
d3['k1'][0]['nest_key'][1][0]
print(d3)


mylist = [400,1,1,1,1,2,2,2,2,22,2,400,3,3,3,2,2,2,3,3,2,1,1,1,2,1,2,3,12,312,312,312,1,1,21,2,3,23,]
newelem = set(mylist)
print(newelem)

a = 4
name = "Sammy"
print ("Hello my dog's name is {1} and he is {0} years old".format(a, name))
