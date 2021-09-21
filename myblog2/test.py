list_person_hobby=[]
dict_person={}
while True:
    name=input('请输入姓名')
    if name=='':
        break
    dict_person={name:[]}
    list_person_hobby.append(dict_person)
    while True:
        hobby=input('请输入爱好')
        if hobby=='':
            break
        dict_person[name].append(hobby)
    
for person in list_person_hobby:
    print('该人的姓名为%s' %person)
    for hobby in dict_person[name]:
        print('该人的兴趣为%s' %hobby)
    print('\n')