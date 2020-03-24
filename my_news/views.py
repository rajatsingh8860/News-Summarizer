from django.shortcuts import render,redirect
from bs4 import BeautifulSoup
import string
from gtts import gTTS
import requests
import os
from .models import Entry,Entry_sport
from .forms import EntryForm,EntryForm_sport
import webbrowser as wb
from django.utils.safestring import mark_safe
from django.template import Library
import threading
import json
import itertools
import speech_recognition as sr
from gensim.summarization import summarize

#new
hin_news=[]
hin_head=[]
image=[]
new=[]
head=[]
total=[]
url_main = "http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=0ac8f3782ae04c508c4643776513602b"
response = requests.get(url_main)
output=response.json()
articles=output["articles"]

for ar in articles: 
    hin_news.append(ar["url"])

for vr in articles: 
    hin_head.append(vr["title"])  

for i in articles: 
    image.append(i["urlToImage"])       
#urls    
a=hin_news[0]
b=hin_news[1]
c=hin_news[2]
d=hin_news[3]
e=hin_news[4]
f=hin_news[5]
g=hin_news[6]
h=hin_news[7]
i=hin_news[8]
j=hin_news[9]
k=hin_news[10]
l=hin_news[11]
m=hin_news[12]
n=hin_news[13]
o=hin_news[14]
p=hin_news[15]
q=hin_news[16]
r=hin_news[17]
s=hin_news[18]
t=hin_news[19]

#headings

a_h=hin_head[0]
b_h=hin_head[1]
c_h=hin_head[2]
d_h=hin_head[3]
e_h=hin_head[4]
f_h=hin_head[5]
g_h=hin_head[6]
h_h=hin_head[7]
i_h=hin_head[8]
j_h=hin_head[9]
k_h=hin_head[10]
l_h=hin_head[11]
m_h=hin_head[12]
n_h=hin_head[13]
o_h=hin_head[14]
p_h=hin_head[15]
q_h=hin_head[16]
r_h=hin_head[17]
s_h=hin_head[18]
t_h=hin_head[19]

#image

a_img=image[0]
b_img=image[1]
c_img=image[2]
d_img=image[3]
e_img=image[4]
f_img=image[5]
g_img=image[6]
h_img=image[7]
i_img=image[8]
j_img=image[9]
k_img=image[10]
l_img=image[11]
m_img=image[12]
n_img=image[13]
o_img=image[14]
p_img=image[15]
q_img=image[16]
r_img=image[17]
s_img=image[18]
t_img=image[19]


#first item

for i in hin_news:
    fetch_a = requests.get(i)
    soup_a = BeautifulSoup(fetch_a.text, 'html.parser')

    para_a = soup_a.find_all('p')
    #hin_headings =hin_headings[0:-13]
    url_a = []

    for ht in para_a:
        url_a.append(ht.text)

    string_a=list(url_a)
    count_a=len(string_a)
    lop=count_a-2
    for x, y in enumerate([0]):
        string_a.insert(x + y, ',')
        new_a=''.join(string_a) 

    n_a=new_a.split(',')

    hj_a="""
    {}
    """.format("\n".join(n_a[0:]))

    new_string_a=list(hj_a)
    count=len(hj_a)
    for x, y in enumerate([0,count]):
        new_string_a.insert(x + y, '"""')
        
    new_name_ab=''.join(new_string_a)
   # new_name_ab_a=new_name_ab.split(',')
    sum_ab=summarize(new_name_ab,word_count=80)
    new.append(sum_ab)
    c_ab=len(sum_ab) 
    head.append(c_ab) 
    total.append(new_name_ab)


sum_a=new[0]
sum_b=new[1]
sum_c=new[2]
sum_d=new[3]   
sum_e=new[4] 
sum_f=new[5]
sum_g=new[6]
sum_h=new[7]
sum_i=new[8]
sum_j=new[9]
sum_k=new[10]
sum_l=new[11]
sum_m=new[12]
sum_n=new[13]
sum_o=new[14]
sum_p=new[15]
sum_q=new[16]
sum_r=new[17]
sum_s=new[18]
sum_t=new[19]

c_a=head[0]
c_b=head[1]
c_c=head[2]
c_d=head[3]
c_e=head[4]
c_f=head[5]
c_g=head[6]
c_h=head[7]
c_i=head[8]
c_j=head[9]
c_k=head[10]
c_l=head[11]
c_m=head[12]
c_n=head[13]
c_o=head[14]
c_p=head[15]
c_q=head[16]
c_r=head[17]
c_s=head[18]
c_t=head[19]

#full news

new_name_a=total[0]
new_name_b=total[1]
new_name_c=total[2]
new_name_d=total[3]
new_name_e=total[4]
new_name_f=total[5]
new_name_g=total[6]
new_name_h=total[7]
new_name_i=total[8]
new_name_j=total[9]
new_name_k=total[10]
new_name_l=total[11]
new_name_m=total[12]
new_name_n=total[13]
new_name_o=total[14]
new_name_p=total[15]
new_name_q=total[16]
new_name_r=total[17]
new_name_s=total[18]
new_name_t=total[19]




# audio
def first_speech(requests,id):

    if id==0:
        output=gTTS(text=sum_a,lang='en',slow=False)
        output.save("first_output.mp3")
        os.system("start first_output.mp3")

    elif id==1:
        output=gTTS(text=sum_a,lang='en',slow=False)
        output.save("second_output.mp3")
        os.system("start second_output.mp3")

    elif id==2:
        output=gTTS(text=sum_c,lang='en',slow=False)
        output.save("third_output.mp3")
        os.system("start third_output.mp3")

    elif id==3:
        output=gTTS(text=sum_d,lang='en',slow=False)
        output.save("fourth_output.mp3")
        os.system("start fourth_output.mp3")

    elif id==4:
        output=gTTS(text=sum_e,lang='en',slow=False)
        output.save("fifth_output.mp3")
        os.system("start fifth_output.mp3")

    elif id==5:
        output=gTTS(text=sum_f,lang='en',slow=False)
        output.save("sixth_output.mp3")
        os.system("start sixth_output.mp3")

    elif id==6:
        output=gTTS(text=sum_g,lang='en',slow=False)
        output.save("seventh_output.mp3")
        os.system("start seventh_output.mp3")

    elif id==7:
        output=gTTS(text=sum_h,lang='en',slow=False)
        output.save("eighth_output.mp3")
        os.system("start eighth_output.mp3")

    elif id==8:
        output=gTTS(text=sum_i,lang='en',slow=False)
        output.save("nineth_output.mp3")
        os.system("start nineth_output.mp3")

    elif id==9:
        output=gTTS(text=sum_j,lang='en',slow=False)
        output.save("tenth_output.mp3")
        os.system("start tenth_output.mp3")

    elif id==10:
        output=gTTS(text=sum_k,lang='en',slow=False)
        output.save("eleventh_output.mp3")
        os.system("start eleventh_output.mp3")

    elif id==11:
        output=gTTS(text=sum_l,lang='en',slow=False)
        output.save("twelth_output.mp3")
        os.system("start twelth_output.mp3")

    elif id==12:
        output=gTTS(text=sum_m,lang='en',slow=False)
        output.save("thirteenth_output.mp3")
        os.system("start thirteenth_output.mp3")

    elif id==13:
        output=gTTS(text=sum_n,lang='en',slow=False)
        output.save("fourteenth_output.mp3")
        os.system("start fourteenth_output.mp3")

    elif id==14:
        output=gTTS(text=sum_o,lang='en',slow=False)
        output.save("fifteenth_output.mp3")
        os.system("start fifteenth_output.mp3")

    elif id==15:
        output.save("sixteenth_output.mp3")
        os.system("start sixteenth_output.mp3")
        return render(requests,'my_news/basic.html')

    elif id==16:
        output=gTTS(text=sum_q,lang='en',slow=False)
        output.save("seventeenth_output.mp3")
        os.system("start seventeenth_output.mp3")

    elif id==17:
        output=gTTS(text=sum_r,lang='en',slow=False)
        output.save("eighteenth_output.mp3")
        os.system("start eighteenth_output.mp3")

    elif id==18:
        output=gTTS(text=sum_s,lang='en',slow=False)
        output.save("nineteenth_output.mp3")
        os.system("start nineteenth_output.mp3")

    else:
        output=gTTS(text=sum_t,lang='en',slow=False)
        output.save("twentieth_output.mp3")
        os.system("start twentieth_output.mp3")

    return render(requests,'my_news/basic.html')


def index(request):
    
    return render(request,'my_news/index.html',{'sum_a':sum_a,'c_a':c_a,'a_h':a_h,'a_img':a_img,
    'sum_b':sum_b,'c_b':c_b,'b_h':b_h,'b_img':b_img,
    'sum_c':sum_c,'c_c':c_c,'c_h':c_h,'c_img':c_img,
    'sum_d':sum_d,'c_d':c_d,'d_h':d_h,'d_img':d_img,
    'sum_e':sum_e,'c_e':c_e,'e_h':e_h,'e_img':e_img,
    'sum_f':sum_f,'c_f':c_f,'f_h':f_h,'f_img':f_img,
    'sum_g':sum_g,'c_g':c_g,'g_h':g_h,'g_img':g_img,
    'sum_h':sum_h,'c_h':c_h,'h_h':h_h,'h_img':h_img,
    'sum_i':sum_i,'c_i':c_i,'i_h':i_h,'i_img':i_img,
    'sum_j':sum_j,'c_j':c_j,'j_h':j_h,'j_img':j_img,
    'sum_k':sum_k,'c_k':c_k,'k_h':k_h,'k_img':k_img,
  #  'sum_l':sum_l,'c_l':c_l,'l_h':l_h,'l_img':l_img,
    'sum_m':sum_m,'c_m':c_m,'m_h':m_h,'m_img':m_img,
    'sum_n':sum_n,'c_n':c_n,'n_h':n_h,'n_img':n_img,
    'sum_o':sum_o,'c_o':c_o,'o_h':o_h,'o_img':o_img,
    'sum_p':sum_p,'c_p':c_p,'p_h':p_h,'p_img':p_img,
    'sum_q':sum_q,'c_q':c_q,'q_h':q_h,'q_img':q_img,
    'sum_r':sum_r,'c_r':c_r,'r_h':r_h,'r_img':r_img,
    'sum_s':sum_s,'c_s':c_s,'s_h':s_h,'s_img':s_img,
    'sum_t':sum_t,'c_t':c_t,'t_h':t_h,'t_img':t_img,

    })

def basic(request):
    return render(request,'my_news/basic.html')    


def first(request,id):
    if id==0:
        item=new_name_a
        if request.method == 'POST':
            form = EntryForm(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first/0')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm(initial={'text':item_new})
       
    elif id==1:
        item=new_name_b
        if request.method == 'POST':
            form = EntryForm(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first/1')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm(initial={'text':item_new})
       
    elif id==2:
        item=new_name_c
        if request.method == 'POST':
            form = EntryForm(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first/2')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm(initial={'text':item_new})
             
   
    elif id==3:
        item=new_name_d
        if request.method == 'POST':
            form = EntryForm(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first/3')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm(initial={'text':item_new})
        

        
    elif id==4:
        item=new_name_e 
        if request.method == 'POST':
            form = EntryForm(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first/{}'.format(4))

        else:
            item_new=item.replace('\n','')
            form=EntryForm(initial={'text':item_new})
            #return redirect('/first/4')
    elif id==5:
        item=new_name_f
        if request.method == 'POST':
            form = EntryForm(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first/5')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm(initial={'text':item_new})
    elif id==6:
        item=new_name_g
        if request.method == 'POST':
            form = EntryForm(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first/6')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm(initial={'text':item_new})
    elif id==7:
        item=new_name_h
        if request.method == 'POST':
            form = EntryForm(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first/7')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm(initial={'text':item_new})
    elif id==8:
        item=new_name_i
        if request.method == 'POST':
            form = EntryForm(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first/8')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm(initial={'text':item_new})
    elif id==9:
        item=new_name_j
        if request.method == 'POST':
            form = EntryForm(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first/9')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm(initial={'text':item_new})
    elif id==10:
        item=new_name_k
        if request.method == 'POST':
            form = EntryForm(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first/10')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm(initial={'text':item_new})
    elif id==11:
        item=new_name_l
        if request.method == 'POST':
            form = EntryForm(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first/11')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm(initial={'text':item_new})
    elif id==12:
        item=new_name_m
        if request.method == 'POST':
            form = EntryForm(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first/12')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm(initial={'text':item_new})
    elif id==13:
        item=new_name_n  
        if request.method == 'POST':
            form = EntryForm(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first/13')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm(initial={'text':item_new})
    elif id==14:
        item=new_name_o
        if request.method == 'POST':
            form = EntryForm(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first/14')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm(initial={'text':item_new}) 
    elif id==15:
        item=new_name_p
        if request.method == 'POST':
            form = EntryForm(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first/15')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm(initial={'text':item_new})
    elif id==16:
        item=new_name_q
        if request.method == 'POST':
            form = EntryForm(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first/16')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm(initial={'text':item_new})
    elif id==17:
        item=new_name_r
        if request.method == 'POST':
            form = EntryForm(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first/17')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm(initial={'text':item_new})
    elif id==18:
        item=new_name_s 
        if request.method == 'POST':
            form = EntryForm(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first/18')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm(initial={'text':item_new})
    else:
        item=new_name_t  
        if request.method == 'POST':
            form = EntryForm(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first/19')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm(initial={'text':item_new})                                                     

    data={'item':item,'id':id,'form':form}  
    
    return render(request,'my_news/first.html',data)    
      
      


#sports news

hin_news_s=[]
hin_head_s=[]
image_s=[]
new_s=[]
head_s=[]
total_s=[]
url_main_s = (
'http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=0ac8f3782ae04c508c4643776513602b')
response_s = requests.get(url_main_s)
output_s=response_s.json()
articles_s=output_s["articles"]

for ar in articles_s: 
    hin_news_s.append(ar["url"])

for vr in articles_s: 
    hin_head_s.append(vr["title"])  

for i in articles_s: 
    image_s.append(i["urlToImage"])       
#urls    
a_s=hin_news_s[0]
b_s=hin_news_s[1]
c_s=hin_news_s[2]
d_s=hin_news_s[3]
e_s=hin_news_s[4]
f_s=hin_news_s[5]
g_s=hin_news_s[6]
h_s=hin_news_s[7]
i_s=hin_news_s[8]
j_s=hin_news_s[9]
k_s=hin_news_s[10]
l_s=hin_news_s[11]
m_s=hin_news_s[12]
n_s=hin_news_s[13]
o_s=hin_news_s[14]
p_s=hin_news_s[15]
q_s=hin_news_s[16]
r_s=hin_news_s[17]
s_s=hin_news_s[18]
t_s=hin_news_s[19]

#headings

a_h_s=hin_head_s[0]
b_h_s=hin_head_s[1]
c_h_s=hin_head_s[2]
d_h_s=hin_head_s[3]
e_h_s=hin_head_s[4]
f_h_s=hin_head_s[5]
g_h_s=hin_head_s[6]
h_h_s=hin_head_s[7]
i_h_s=hin_head_s[8]
j_h_s=hin_head_s[9]
k_h_s=hin_head_s[10]
l_h_s=hin_head_s[11]
m_h_s=hin_head_s[12]
n_h_s=hin_head_s[13]
o_h_s=hin_head_s[14]
p_h_s=hin_head_s[15]
q_h_s=hin_head_s[16]
r_h_s=hin_head_s[17]
s_h_s=hin_head_s[18]
t_h_s=hin_head_s[19]

#image

a_img_s=image_s[0]
b_img_s=image_s[1]
c_img_s=image_s[2]
d_img_s=image_s[3]
e_img_s=image_s[4]
f_img_s=image_s[5]
g_img_s=image_s[6]
h_img_s=image_s[7]
i_img_s=image_s[8]
j_img_s=image_s[9]
k_img_s=image_s[10]
l_img_s=image_s[11]
m_img_s=image_s[12]
n_img_s=image_s[13]
o_img_s=image_s[14]
p_img_s=image_s[15]
q_img_s=image_s[16]
r_img_s=image_s[17]
s_img_s=image_s[18]
t_img_s=image_s[19]


#first item

for i in hin_news_s:
    fetch_a_s = requests.get(i)
    soup_a_s= BeautifulSoup(fetch_a_s.text, 'html.parser')

    para_a_s = soup_a_s.find_all('p')
    #hin_headings =hin_headings[0:-13]
    url_a_s = []

    for ht in para_a_s:
        url_a_s.append(ht.text)

    string_a_s=list(url_a_s)
    count_a_s=len(string_a_s)
    lop_s=count_a_s-2
    for x, y in enumerate([0]):
        string_a_s.insert(x + y, ',')
        new_a_s=''.join(string_a_s) 

    n_a_s=new_a_s.split(',')

    hj_a_s="""
    {}
    """.format("\n".join(n_a_s[0:]))

    new_string_a_s=list(hj_a_s)
    count_s=len(hj_a_s)
    for x, y in enumerate([0,count_s]):
        new_string_a_s.insert(x + y, '"""')
        
    new_name_ab_s=''.join(new_string_a_s)
    sum_ab_s=summarize(new_name_ab_s,word_count=80)
    new_s.append(sum_ab_s)
    c_ab_s=len(sum_ab_s) 
    head_s.append(c_ab_s) 
    total_s.append(new_name_ab_s)

sum_a_s=new_s[0]
sum_b_s=new_s[1]
sum_c_s=new_s[2]
sum_d_s=new_s[3]   
sum_e_s=new_s[4] 
sum_f_s=new_s[5]
sum_g_s=new_s[6]
sum_h_s=new_s[7]
sum_i_s=new_s[8]
sum_j_s=new_s[9]
sum_k_s=new_s[10]
sum_l_s=new_s[11]
sum_m_s=new_s[12]
sum_n_s=new_s[13]
sum_o_s=new_s[14]
sum_p_s=new_s[15]
sum_q_s=new_s[16]
sum_r_s=new_s[17]
sum_s_s=new_s[18]
sum_t_s=new_s[19]

c_a_s=head_s[0]
c_b_s=head_s[1]
c_c_s=head_s[2]
c_d_s=head_s[3]
c_e_s=head_s[4]
c_f_s=head_s[5]
c_g_s=head_s[6]
c_h_s=head_s[7]
c_i_s=head_s[8]
c_j_s=head_s[9]
c_k_s=head_s[10]
c_l_s=head_s[11]
c_m_s=head_s[12]
c_n_s=head_s[13]
c_o_s=head_s[14]
c_p_s=head_s[15]
c_q_s=head_s[16]
c_r_s=head_s[17]
c_s_s=head_s[18]
c_t_s=head_s[19]

#full news

new_name_a_s=total_s[0]
new_name_b_s=total_s[1]
new_name_c_s=total_s[2]
new_name_d_s=total_s[3]
new_name_e_s=total_s[4]
new_name_f_s=total_s[5]
new_name_g_s=total_s[6]
new_name_h_s=total_s[7]
new_name_i_s=total_s[8]
new_name_j_s=total_s[9]
new_name_k_s=total_s[10]
new_name_l_s=total_s[11]
new_name_m_s=total_s[12]
new_name_n_s=total_s[13]
new_name_o_s=total_s[14]
new_name_p_s=total_s[15]
new_name_q_s=total_s[16]
new_name_r_s=total_s[17]
new_name_s_s=total_s[18]
new_name_t_s=total_s[19]

def first_s(request,id):
    if id==0:
        item=new_name_a_s
        if request.method == 'POST':
            form = EntryForm_sport(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first_s/0')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm_sport(initial={'text_sport':item_new})
       
    elif id==1:
        item=new_name_b_s
        if request.method == 'POST':
            form = EntryForm_sport(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first_s/1')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm_sport(initial={'text_sport':item_new})
       
    elif id==2:
        item=new_name_c_s
        if request.method == 'POST':
            form = EntryForm_sport(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first_s/2')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm_sport(initial={'text_sport':item_new})
             
   
    elif id==3:
        item=new_name_d_s
        if request.method == 'POST':
            form = EntryForm_sport(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first_s/3')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm_sport(initial={'text_sport':item_new})
        

        
    elif id==4:
        item=new_name_e_s 
        if request.method == 'POST':
            form = EntryForm_sport(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first_s/{}'.format(4))

        else:
            item_new=item.replace('\n','')
            form=EntryForm_sport(initial={'text_sport':item_new})
            #return redirect('/first/4')
    elif id==5:
        item=new_name_f_s
        if request.method == 'POST':
            form = EntryForm_sport(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first_s/5')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm_sport(initial={'text_sport':item_new})
    elif id==6:
        item=new_name_g_s
        if request.method == 'POST':
            form = EntryForm_sport(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first_s/6')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm_sport(initial={'text_sport':item_new})
    elif id==7:
        item=new_name_h_s
        if request.method == 'POST':
            form = EntryForm_sport(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first_s/7')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm_sport(initial={'text_sport':item_new})
    elif id==8:
        item=new_name_i_s
        if request.method == 'POST':
            form = EntryForm_sport(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first_s/8')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm_sport(initial={'text_sport':item_new})
    elif id==9:
        item=new_name_j_s
        if request.method == 'POST':
            form = EntryForm_sport(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first_s/9')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm_sport(initial={'text_sport':item_new})
    elif id==10:
        item=new_name_k_s
        if request.method == 'POST':
            form = EntryForm_sport(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first_s/10')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm_sport(initial={'text_sport':item_new})
    elif id==11:
        item=new_name_l_s
        if request.method == 'POST':
            form = EntryForm_sport(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first_s/11')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm_sport(initial={'text_sport':item_new})
    elif id==12:
        item=new_name_m_s
        if request.method == 'POST':
            form = EntryForm_sport(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first_s/12')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm_sport(initial={'text_sport':item_new})
    elif id==13:
        item=new_name_n_s  
        if request.method == 'POST':
            form = EntryForm_sport(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first_s/13')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm_sport(initial={'text_sport':item_new})
    elif id==14:
        item=new_name_o_s
        if request.method == 'POST':
            form = EntryForm_sport(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first_s/14')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm_sport(initial={'text_sport':item_new}) 
    elif id==15:
        item=new_name_p_s
        if request.method == 'POST':
            form = EntryForm_sport(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first_s/15')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm_sport(initial={'text_sport':item_new})
    elif id==16:
        item=new_name_q_s
        if request.method == 'POST':
            form = EntryForm_sport(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first_s/16')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm_sport(initial={'text_sport':item_new})
    elif id==17:
        item=new_name_r_s
        if request.method == 'POST':
            form = EntryForm_sport(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first_s/17')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm_sport(initial={'text_sport':item_new})
    elif id==18:
        item=new_name_s_s 
        if request.method == 'POST':
            form = EntryForm_sport(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first_s/18')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm_sport(initial={'text_sport':item_new})
    else:
        item=new_name_t_s  
        if request.method == 'POST':
            form = EntryForm_sport(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/first_s/19')

        else:
            item_new=item.replace('\n',' ')
            form=EntryForm_sport(initial={'text_sport':item_new})                                                     

    data={'item':item,'id':id,'form':form}  
    
    return render(request,'my_news/first_s.html',data)    
   

#  top news audio
def first_speech(requests,id):

    if id==0:
        output=gTTS(text=sum_a,lang='en',slow=False)
        output.save("first_output.mp3")
        os.system("start first_output.mp3")

    elif id==1:
        output=gTTS(text=sum_b,lang='en',slow=False)
        output.save("second_output.mp3")
        os.system("start second_output.mp3")

    elif id==2:
        output=gTTS(text=sum_c,lang='en',slow=False)
        output.save("third_output.mp3")
        os.system("start third_output.mp3")

    elif id==3:
        output=gTTS(text=sum_d,lang='en',slow=False)
        output.save("fourth_output.mp3")
        os.system("start fourth_output.mp3")

    elif id==4:
        output=gTTS(text=sum_e,lang='en',slow=False)
        output.save("fifth_output.mp3")
        os.system("start fifth_output.mp3")

    elif id==5:
        output=gTTS(text=sum_f,lang='en',slow=False)
        output.save("sixth_output.mp3")
        os.system("start sixth_output.mp3")

    elif id==6:
        output=gTTS(text=sum_g,lang='en',slow=False)
        output.save("seventh_output.mp3")
        os.system("start seventh_output.mp3")

    elif id==7:
        output=gTTS(text=sum_h,lang='en',slow=False)
        output.save("eighth_output.mp3")
        os.system("start eighth_output.mp3")

    elif id==8:
        output=gTTS(text=sum_i,lang='en',slow=False)
        output.save("nineth_output.mp3")
        os.system("start nineth_output.mp3")

    elif id==9:
        output=gTTS(text=sum_j,lang='en',slow=False)
        output.save("tenth_output.mp3")
        os.system("start tenth_output.mp3")

    elif id==10:
        output=gTTS(text=sum_k,lang='en',slow=False)
        output.save("eleventh_output.mp3")
        os.system("start eleventh_output.mp3")

    elif id==11:
        output=gTTS(text=sum_l,lang='en',slow=False)
        output.save("twelth_output.mp3")
        os.system("start twelth_output.mp3")

    elif id==12:
        output=gTTS(text=sum_m,lang='en',slow=False)
        output.save("thirteenth_output.mp3")
        os.system("start thirteenth_output.mp3")

    elif id==13:
        output=gTTS(text=sum_n,lang='en',slow=False)
        output.save("fourteenth_output.mp3")
        os.system("start fourteenth_output.mp3")

    elif id==14:
        output=gTTS(text=sum_o,lang='en',slow=False)
        output.save("fifteenth_output.mp3")
        os.system("start fifteenth_output.mp3")

    elif id==15:
        output=gTTS(text=sum_p,lang='en',slow=False)
        output.save("sixteenth_output.mp3")
        os.system("start sixteenth_output.mp3")
        return render(requests,'my_news/basic.html')

    elif id==16:
        output=gTTS(text=sum_q,lang='en',slow=False)
        output.save("seventeenth_output.mp3")
        os.system("start seventeenth_output.mp3")

    elif id==17:
        output=gTTS(text=sum_r,lang='en',slow=False)
        output.save("eighteenth_output.mp3")
        os.system("start eighteenth_output.mp3")

    elif id==18:
        output=gTTS(text=sum_s,lang='en',slow=False)
        output.save("nineteenth_output.mp3")
        os.system("start nineteenth_output.mp3")

    else:
        output=gTTS(text=sum_t,lang='en',slow=False)
        output.save("twentieth_output.mp3")
        os.system("start twentieth_output.mp3")

    return render(requests,'my_news/basic.html')     


# sports news audio

def second_speech(requests,id):

    if id==0:
        output=gTTS(text=sum_a_s,lang='en',slow=False)
        output.save("first_output.mp3")
        os.system("start first_output.mp3")

    elif id==1:
        output=gTTS(text=sum_b_s,lang='en',slow=False)
        output.save("second_output.mp3")
        os.system("start second_output.mp3")

    elif id==2:
        output=gTTS(text=sum_c_s,lang='en',slow=False)
        output.save("third_output.mp3")
        os.system("start third_output.mp3")

    elif id==3:
        output=gTTS(text=sum_d_s,lang='en',slow=False)
        output.save("fourth_output.mp3")
        os.system("start fourth_output.mp3")

    elif id==4:
        output=gTTS(text=sum_e_s,lang='en',slow=False)
        output.save("fifth_output.mp3")
        os.system("start fifth_output.mp3")

    elif id==5:
        output=gTTS(text=sum_f_s,lang='en',slow=False)
        output.save("sixth_output.mp3")
        os.system("start sixth_output.mp3")

    elif id==6:
        output=gTTS(text=sum_g_s,lang='en',slow=False)
        output.save("seventh_output.mp3")
        os.system("start seventh_output.mp3")

    elif id==7:
        output=gTTS(text=sum_h_s,lang='en',slow=False)
        output.save("eighth_output.mp3")
        os.system("start eighth_output.mp3")

    elif id==8:
        output=gTTS(text=sum_i_s,lang='en',slow=False)
        output.save("nineth_output.mp3")
        os.system("start nineth_output.mp3")

    elif id==9:
        output=gTTS(text=sum_j_s,lang='en',slow=False)
        output.save("tenth_output.mp3")
        os.system("start tenth_output.mp3")

    elif id==10:
        output=gTTS(text=sum_k_s,lang='en',slow=False)
        output.save("eleventh_output.mp3")
        os.system("start eleventh_output.mp3")

    elif id==11:
        output=gTTS(text=sum_l_s,lang='en',slow=False)
        output.save("twelth_output.mp3")
        os.system("start twelth_output.mp3")

    elif id==12:
        output=gTTS(text=sum_m_s,lang='en',slow=False)
        output.save("thirteenth_output.mp3")
        os.system("start thirteenth_output.mp3")

    elif id==13:
        output=gTTS(text=sum_n_s,lang='en',slow=False)
        output.save("fourteenth_output.mp3")
        os.system("start fourteenth_output.mp3")

    elif id==14:
        output=gTTS(text=sum_o_s,lang='en',slow=False)
        output.save("fifteenth_output.mp3")
        os.system("start fifteenth_output.mp3")

    elif id==15:
        output=gTTS(text=sum_p_s,lang='en',slow=False)
        output.save("sixteenth_output.mp3")
        os.system("start sixteenth_output.mp3")
        return render(requests,'my_news/basic.html')

    elif id==16:
        output=gTTS(text=sum_q_s,lang='en',slow=False)
        output.save("seventeenth_output.mp3")
        os.system("start seventeenth_output.mp3")

    elif id==17:
        output=gTTS(text=sum_r_s,lang='en',slow=False)
        output.save("eighteenth_output.mp3")
        os.system("start eighteenth_output.mp3")

    elif id==18:
        output=gTTS(text=sum_s_s,lang='en',slow=False)
        output.save("nineteenth_output.mp3")
        os.system("start nineteenth_output.mp3")

    else:
        output=gTTS(text=sum_t_s,lang='en',slow=False)
        output.save("twentieth_output.mp3")
        os.system("start twentieth_output.mp3")

    return render(requests,'my_news/new_basic.html')






def sports(requests):
    return render(requests,'my_news/sports.html',{'sum_a_s':sum_a_s,'c_a_s':c_a_s,'a_h_s':a_h_s,'a_img_s':a_img_s,
    'sum_b_s':sum_b_s,'c_b_s':c_b_s,'b_h_s':b_h_s,'b_img_s':b_img_s,
    'sum_c_s':sum_c_s,'c_c_s':c_c_s,'c_h_s':c_h_s,'c_img_s':c_img_s,
    'sum_d_s':sum_d_s,'c_d_s':c_d_s,'d_h_s':d_h_s,'d_img_s':d_img_s,
    'sum_e_s':sum_e_s,'c_e_s':c_e_s,'e_h_s':e_h_s,'e_img_s':e_img_s,
    'sum_f_s':sum_f_s,'c_f_s':c_f_s,'f_h_s':f_h_s,'f_img_s':f_img_s,
    'sum_g_s':sum_g_s,'c_g_s':c_g_s,'g_h_s':g_h_s,'g_img_s':g_img_s,
    'sum_h_s':sum_h_s,'c_h_s':c_h_s,'h_h_s':h_h_s,'h_img_s':h_img_s,
    'sum_i_s':sum_i_s,'c_i_s':c_i_s,'i_h_s':i_h_s,'i_img_s':i_img_s,
    'sum_j_s':sum_j_s,'c_j_s':c_j_s,'j_h_s':j_h_s,'j_img_s':j_img_s,
    'sum_k_s':sum_k_s,'c_k_s':c_k_s,'k_h_s':k_h_s,'k_img_s':k_img_s,
  #  'sum_l_s':sum_l_s,'c_l_s':c_l_s,'l_h_s':l_h_s,'l_img_s':l_img_s,
    'sum_m_s':sum_m_s,'c_m_s':c_m_s,'m_h_s':m_h_s,'m_img_s':m_img_s,
    'sum_n_s':sum_n_s,'c_n_s':c_n_s,'n_h_s':n_h_s,'n_img_s':n_img_s,
    'sum_o_s':sum_o_s,'c_o_s':c_o_s,'o_h_s':o_h_s,'o_img_s':o_img_s,
    'sum_p_s':sum_p_s,'c_p_s':c_p_s,'p_h_s':p_h_s,'p_img_s':p_img_s,
    'sum_q_s':sum_q_s,'c_q_s':c_q_s,'q_h_s':q_h_s,'q_img_s':q_img_s,
    'sum_r_s':sum_r_s,'c_r_s':c_r_s,'r_h_s':r_h_s,'r_img_s':r_img_s,
    'sum_s_s':sum_s_s,'c_s_s':c_s_s,'s_h_s':s_h_s,'s_img_s':s_img_s,
    'sum_t_s':sum_t_s,'c_t_s':c_t_s,'t_h_s':t_h_s,'t_img_s':t_img_s,

    })


#Method for My_news page

def My_technology_news(request):
    date=Entry.objects.all().order_by('-date_posted')
    my_news_data=Entry.objects.all().order_by('-date_posted').values('text').distinct()
    feed1={'my_news_data':my_news_data,'date':date}
    combine=zip(my_news_data,date)
    feed2={'combine':combine}
    return render(request,'my_news/My_technology_news.html',feed2)

#method for my_sports_news page

def My_sports_news(request):
    date=Entry_sport.objects.all().order_by('-date_posted_sport')
    my_news_data=Entry_sport.objects.all().order_by('-date_posted_sport').values('text_sport').distinct()
    feed1={'my_news_data':my_news_data,'date':date}
    combine=zip(my_news_data,date)
    feed2={'combine':combine}
    return render(request,'my_news/My_sports_news.html',feed2)    


# Email
'''sum_a_length=len(sum_a)
def printit():
    threading.Timer(5.0,printit).start()
    

printit()'''    


