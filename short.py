# a= [11, 3, 7, 5, 2]
# a.sort()
# print(a)


# vowels = ['e', 'a', 'u', 'o', 'i']
# vowels.sort()
# print('Sorted list:', vowels)



# dict = {6:'George' ,2:'John' ,1:'Potter' ,9:'Micheal' ,7:'Robert' ,8:'Gayle' }  
# b = sorted(dict.keys())
# print("Sorted keys",b)    
# c = sorted(dict.items())
# print("Sorted Values",c)  


# a = {1:2 ,2:1 ,4:3 ,3:4 ,6:5 ,5:6 }
# print(sorted(a.values()))


# a = {1:2 ,2:1 ,4:3 ,3:4 ,6:5 ,5:6 }
# print(sorted(a.keys()))


# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_d = sorted(d.items())
# print('Dictionary in ascending order by value : ',sorted_d)


# d={2:4,1:3,3:5,6:8}
# a=sorted(d.items())
# print(a)



# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_d = dict( sorted(d.items(),reverse=True))
# print('Dictionary in descending order by value : ',sorted_d)



# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# s= sorted(d.items())
# print('ascending order : ',s)
# s1= dict( sorted(d.items(),reverse=True))
# print('descending order : ',s1)




#  Duplicate values will overwrite existing values:

# thisdict =	{"brand": "Ford","model": "Mustang", "year": 1964,"year": 2020}
# print(thisdict) 


# Print the "brand" value of the dictionary

# thisdict =	{"brand": "Ford","model": "Mustang","year": 1964}
# print(thisdict["brand"])





# String, int, boolean, and list data types:

# thisdict =	{"brand": "Ford","electric": False,"year": 1964,"colors": ["red", "white", "blue"]} 
# print(thisdict)



# get th value

# thisdict =	{"brand": "Ford","model": "Mustang","year": 1964}
# print(thisdict["model"])
















 






# sorted methodes


# dic={}
# a = {9:2 ,2:1 ,4:3 ,3:4 ,6:5 ,5:7 }
# for i in a:
#     if i == 2:
#         dic[i]=a[i]
# print(dic)
# b= sorted(a.keys())
# print(b)
# i=0
# while i<len(a):
#     if b[i]==2:
#         dic=(b[i])
#     i+=1
# print(dic)




# list= [1,36,3,6,4,9]
# new_list = []

# while list:
#     min = list[0]  
#     for x in list: 
#         if x < min:
#             min = x
#     new_list.append(min)
#     list.remove(min)    

# print(new_list)



# s = [ 5, 0, 23, 23,8,3,6, 67]
# b= []
# for i in range(len(s)):
#     a = max(s)
#     b.append(a)
#     s.remove(a)
# print (b)



# a = {'john':'1','alice':'90','rook':'45','emma':'22','roz':'11'}
# b= sorted(a.items())
# print(dict(b))


# a= [4, 2, 3, 9, 5, 0, 1]
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):

#         if a[i] > a[j]:
#             a[i],a[j] = a[j], a[i]

# print(a)




