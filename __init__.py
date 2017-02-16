# encoding:utf-8
from urllib import urlopen
import urllib2
import time
import sys 
import requests 
import json

jibing_write =open('/Users/imac/Downloads/惠每云诊所系统/疾病.txt','a+')
# jibing_write_all =open('/Users/imac/Downloads/惠每云诊所系统/症状所有的.txt','a+')
# jibing_list_writ =open('/Users/imac/Downloads/惠每云诊所系统/症状.txt','r')

def writ_txt(text):
    jibing_write.write(text+'\n')
    print ''

def encode2str(encodeN):
    return encodeN.encode('utf8')
#网络请求
def get_html(site,values):
    hdr = {'Host':'api.huimei.com',
           'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Content-Type':'application/json;charset=UTF-8',
           'Huimei_id':'B212C14993',
           'api-extend-params':'%7B%22hospitalGuid%22%3A1544%2C%22userGuid%22%3A383738%2C%22doctorGuid%22%3A2094%2C%22serialNumber%22%3A420561%2C%22authKey%22%3A%22B212C14993%22%2C%22i18n%22%3A%22cn%22%7D',
           'Content-Length':659,
           'Host':'apollo2.huimeionline.com',
           'Accept':'*/*',
           'Accept-Encoding':'gzip, deflate',
           'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
           'Set-Cookie':'SESSION=68d3047a-a433-41d1-927f-d0f8f299d259; Path=/apollo/; HttpOnly'
        
         }
    values ='{"symptom":"%s","confirmDiagnosis":"","confirmDiagnosisMap":[],"examItems":[{"id":1,"value":""},{"id":2,"value":""},{"id":3,"value":""},{"id":4,"value":""},{"id":5,"value":""},{"id":6,"value":""},{"id":7,"value":""},{"id":8,"value":""},{"id":9,"value":""},{"id":10,"value":""},{"id":11,"value":""},{"id":12,"value":""},{"id":13,"value":""},{"id":14,"value":""},{"id":15,"value":""},{"id":16,"value":""},{"id":17,"value":""},{"id":18,"value":""}]}' % (values)
    if 'common_all' not in site:  
        r = requests.post('http://apollo2.huimeionline.com/v_2_2/diagnose_through_interrogation',headers=hdr, data=values)
        text =r.content
        print text
    else:
        r = requests.post('http://apollo2.huimeionline.com/v_2_2/common_all',headers=hdr, data=values)
        text =r.content
    return json.loads(text)




def txt_2_json_1(txt_content,bodyPart,one):
    json_content =txt_content
    body_json =json_content['body']
    if len(body_json) and  body_json['suspectedDiseases'] >0:
        body_json =body_json['suspectedDiseases']
        for one_body in body_json :
            diseaseName =one_body['diseaseName']  #疾病名称
#             print diseaseName
            symptom =one_body['symptomTypes']
           
#             one_more =fri_name+'_'+diseaseName.encode('utf8')
            chatibiaoxian =''
            if symptom is None:
                writ_txt(bodyPart+'__'+one+'__'+encode2str(diseaseName)+'__'+'暂无')
                continue 
            for one_symptom in symptom:
#                 print one_symptom
                namecahqu  = one_symptom['title']
                if(one_symptom.has_key('unmatchSymptom')):   
                    unmatchSymptom  = one_symptom['unmatchSymptom'] #表现或者查体
                    symptomName =''
                    for one_unmatchSymptom in unmatchSymptom:
                        symptomName =symptomName+','+ one_unmatchSymptom ['symptomName']
                else:
                    symptomName =u'暂无'
                chatibiaoxian = chatibiaoxian+'__'+namecahqu+'__'+symptomName
            writ_txt(bodyPart+'__'+one+'__'+encode2str(diseaseName)+encode2str(chatibiaoxian))
            
#             writ_txt(one_more.decode('utf8').encode('utf-8'))


def txt_2_json(txt_content):
#     json_content =json.loads(txt_content)
    json_content =txt_content
    body_json =json_content['body']
    if len(body_json) >0:
        body_json =body_json['commonSymptomMore']
        for one_body in body_json :
            bodyPart =one_body['bodyPart'] #部位
            symptom =one_body['symptom']
            bodyPart =bodyPart.encode('utf8');
            for one in symptom:
                print  one 
                one_str =one.encode('utf8');
                txt_all_info = txt_2_json_1(get_html('部位', one_str),bodyPart,one_str)
#                 print txt_all_info
#                 if txt_all_info:
#                     writ_txt(txt_all_info)

# 常见症状
def txt_2_json_3(txt_content):
    json_content =json.loads(txt_content)
    body_json =json_content['body']
    body_json =body_json['commonSymptom']
    if len(body_json) >0:
        for one_body in body_json :
            name =one_body['name']    
            writ_txt(name.encode('utf-8'))




txt_2_json(get_html('common_all','发热'));

jibing_write.close()
# list_write_all =open('/Users/imac/Downloads/惠每云诊所系统/不重复疾病.txt','r')
# for one_jibing in list_write_all.readlines():
#     print one_jibing[0]
#     list_one_list =one_jibing.split('__')
#     txt_content =get_html('http://api.huimei.com/v_2_0/suspected_diagnosis',list_one_list[1])
#     txt_2_json_1(txt_content,list_one_list[0])
    
# txt_content =get_html('http://api.huimei.com/v_2_0/common_diseases')
# txt_content =get_html('http://api.huimei.com/v_2_0/common_symptom_obj') #常见症状

# txt_content =get_html('http://api.huimei.com/v_2_0/diagnose_through_interrogation',)
# txt_2_json_3(txt_content)

 
 
 

































 
 
''' 
list_all =jibing_list_writ.readlines();
for one_jibing in list_all:
# for one_jibing in ['呼吸困难']:
    one_jibing =one_jibing.replace('\n','')
    jibing_write_all_zhengzhaung =open('/Users/imac/Downloads/惠每云诊所系统/%s.txt' % one_jibing,'a+')
    txt_content =get_html('http://api.huimei.com/v_2_0/diagnose_through_interrogation',one_jibing) #获取疾病
 
    text_zhengzhaung =txt_content['body']['symptomClassification']
    if  text_zhengzhaung is not None and len(text_zhengzhaung)>0:
        print '含有症状'
        list_zhengzhuang =text_zhengzhaung[0]['classificationSymptom']['unmatchSymptom']  #症状
        for one_zhengzhaung in list_zhengzhuang:
            txt_content =get_html('http://api.huimei.com/v_2_0/diagnose_through_interrogation',"%s,%s" %(one_jibing,one_zhengzhaung.encode('utf-8'))) #症状 分部 获取疾病
            list_jibing = txt_content['body']['accompanyingSymptom']
            if list_jibing is None or len(text_zhengzhaung) ==0 :
                continue
                
            list_jibing =list_jibing['unmatchSymptom']
            for one_jibing_xiao in list_jibing:
                txt_content =get_html('http://api.huimei.com/v_2_0/diagnose_through_interrogation',"%s,%s,%s" %(one_jibing,one_zhengzhaung.encode('utf-8'),one_jibing_xiao.encode('utf-8'))) #症状 分部 获取疾病
                list_youyin =txt_content['body']['inducement']
                if list_youyin is None  or len(list_youyin) ==0 :
                    continue 
                list_youyin =list_youyin['unmatchSymptom']
                for one_youyin in list_youyin:
                    txt_content =get_html('http://api.huimei.com/v_2_0/diagnose_through_interrogation',"%s,%s,%s,%s" %(one_jibing,one_zhengzhaung.encode('utf-8'),one_jibing_xiao.encode('utf-8'),one_youyin.encode('utf-8'))) #症状 分部 获取疾病
                    list_physical =txt_content['body']['physical']
                    one_unmatchSymptom_list_line_line =''
                    for one_physical in list_physical:
                        bodyPart_name =one_physical['bodyPart']
                        print bodyPart_name #检查名称
                        unmatchSymptom_list =one_physical['partSymptom']['unmatchSymptom']
                        one_unmatchSymptom_list_line =''
                        for one_unmatchSymptom_list in unmatchSymptom_list:
                            one_unmatchSymptom_list_line=one_unmatchSymptom_list_line+'_'+one_unmatchSymptom_list
                             
                        one_unmatchSymptom_list_line_line =one_unmatchSymptom_list_line_line+'__' +bodyPart_name+'_'+one_unmatchSymptom_list_line  #检查小项目
                     
                    print one_unmatchSymptom_list_line_line #检查项目
                    jibing_write_all_zhengzhaung.write("%s__%s__%s__%s%s\n" %(one_jibing,one_zhengzhaung.encode('utf-8'),one_jibing_xiao.encode('utf-8'),one_youyin.encode('utf-8'),one_unmatchSymptom_list_line_line.encode('utf8')))
                       
                    list_jibing_xiao =txt_content['body']['suspectedDiseases']
                    for one_list_jibing_xiao in list_jibing_xiao:
                        uuid =one_list_jibing_xiao['uuid']
                        print 'uuid== '+uuid
                        diseaseName =one_list_jibing_xiao['diseaseName']
                        matchSymptomObj_list =one_list_jibing_xiao['matchSymptom']
                        symptomName=diseaseName+'__'+uuid
                        for one_matchSymptomObj_list in matchSymptomObj_list:
                            symptomName =symptomName+'__'+one_matchSymptomObj_list
                             
                        matchSymptomObj_list =one_list_jibing_xiao['unmatchSymptom']
                        for one_matchSymptomObj_list in matchSymptomObj_list:
                            symptomName =symptomName+'__'+one_matchSymptomObj_list
                        print symptomName
                        jibing_write_all.write(symptomName.encode('utf-8')+'\n')
    else:
            print '不含有症状'  
#         for  one_jibing in ['吸气性呼吸困难','呼气性呼吸困难','夜间阵发性呼吸困难','进行性加重的呼吸困难','活动后气短']:    
            txt_content =get_html('http://api.huimei.com/v_2_0/diagnose_through_interrogation',"%s" %(one_jibing)) #症状 分部 获取疾病
            list_jibing = txt_content['body']['accompanyingSymptom']['unmatchSymptom']
            for one_jibing_xiao in list_jibing:
                txt_content =get_html('http://api.huimei.com/v_2_0/diagnose_through_interrogation',"%s,%s" %(one_jibing,one_jibing_xiao.encode('utf-8'))) #症状 分部 获取疾病
                list_youyin =txt_content['body']['inducement']['unmatchSymptom']
                for one_youyin in list_youyin:
                    txt_content =get_html('http://api.huimei.com/v_2_0/diagnose_through_interrogation',"%s,%s,%s" %(one_jibing,one_jibing_xiao.encode('utf-8'),one_youyin.encode('utf-8'))) #症状 分部 获取疾病
                    list_physical =txt_content['body']['physical']
                    one_unmatchSymptom_list_line_line =''
                    for one_physical in list_physical:
                        bodyPart_name =one_physical['bodyPart']
                        print bodyPart_name #检查名称
                        unmatchSymptom_list =one_physical['partSymptom']['unmatchSymptom']
                        one_unmatchSymptom_list_line =''
                        for one_unmatchSymptom_list in unmatchSymptom_list:
                            one_unmatchSymptom_list_line=one_unmatchSymptom_list_line+'_'+one_unmatchSymptom_list
                             
                        one_unmatchSymptom_list_line_line =one_unmatchSymptom_list_line_line+'__'+ bodyPart_name+'_'+one_unmatchSymptom_list_line  #检查小项目
                    
                    print one_unmatchSymptom_list_line_line   #检查
                    jibing_write_all_zhengzhaung.write("%s__暂无__%s__%s%s\n" %(one_jibing,one_jibing_xiao.encode('utf-8'),one_youyin.encode('utf-8'),one_unmatchSymptom_list_line_line.encode('utf8')))
                    list_jibing_xiao =txt_content['body']['suspectedDiseases']
                    for one_list_jibing_xiao in list_jibing_xiao:
                        uuid =one_list_jibing_xiao['uuid']
                        print 'uuid== '+uuid
                        diseaseName =one_list_jibing_xiao['diseaseName']
                        matchSymptomObj_list =one_list_jibing_xiao['matchSymptom']
                        symptomName=diseaseName+'__'+uuid
                        for one_matchSymptomObj_list in matchSymptomObj_list:
                            symptomName =symptomName+'__'+one_matchSymptomObj_list
                             
                        matchSymptomObj_list =one_list_jibing_xiao['unmatchSymptom']
                        for one_matchSymptomObj_list in matchSymptomObj_list:
                            symptomName =symptomName+'__'+one_matchSymptomObj_list
                        print symptomName #疾病史
                        jibing_write_all.write(symptomName.encode('utf-8')+'\n')
 
    jibing_write_all_zhengzhaung.close()
 
jibing_write_all.close()
print '=====================写入完成==================='
'''









