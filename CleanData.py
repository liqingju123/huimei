# encoding:utf-8

before_all_data =open('/Users/imac/Downloads/惠每云诊所系统/真正不重复症状.txt','r')
after_all_data =open('/Users/imac/Downloads/惠每云诊所系统/真正不重复症状tmep.txt','w')
 
list_name =[]
list_after_data =[]
for one_before_all_data in before_all_data:
    list_one_before_all_data =one_before_all_data.split('__')
    if list_one_before_all_data[0] not in list_name:
        list_name.append(list_one_before_all_data[0])
        after_all_data.write(one_before_all_data)

before_all_data.close()
after_all_data.close()




