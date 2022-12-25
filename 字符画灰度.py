import os 
import time
import shutil
import subprocess
from tqdm import tqdm
from PIL import Image

pix =''' .'`^",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@'''
pix2= lambda p: pix[(255 - p) * 68 //255]
path='/storage/emulated/0/termux_py_字符画'
##################
def initialize() :
    if not os.path.exists(path) :
        os.makedirs(path)
    a='----------'*3
    os.system('clear')
    print('请依据下方横线确定屏幕宽度,输入"Q"完成,回车继续')
    while True :
        print(a)
        print(len(a))
        b=input().upper()
        if b == 'Q' :
            if len(a) % 2 == 0 :
                c=len(a)
            else :
                c=len(a)-1
            with open('/storage/emulated/0/termux_py_字符画/width.txt','w') as f :
                f.write(str(c))
            break
        else :
            a+='-'
            
##################          
def ffmpeg_thumbnail() :
    if not os.path.exists('/storage/emulated/0/termux_py_字符画/width.txt') :
        width=100
    else :
        with open('/storage/emulated/0/termux_py_字符画/width.txt','r') as f :
            width=int(f.read())
    a=input('请输入需要处理的文件路径:')
    if not os.path.exists(path+'/new') :
        os.makedirs(path+'/new')
        ffm='ffmpeg -i "'+a+'"'+' -r 24 -f image2 '+path+'/new/'+'%d.png'
        print(ffm)
        os.system(ffm)
    b=len(os.listdir(path+'/new'))
    c=input('重命名:')
    path_1=path+'/'+c
    path_2=path+'/'+'list'
    if not os.path.exists(path_1) :
        os.makedirs(path_1)
    if not os.path.exists(path_2) :
        os.makedirs(path_2)
    with open(path_2+'/'+c+'.txt','w') as f :
        f.write(c+'\n'+str(b)+'\n'+str(width))
    for i in tqdm(range(1,b+1)) :
        im = Image.open(path+'/new/'+str(i)+'.png')
        im.thumbnail((width/2,1000))
        im = im.convert("L")
        px = im.getdata()
        txt=''
        d=0
        for b in px :
            e=pix2(b)
            txt+=(e*2)
            d+=1
            if d == width/2 :
                txt+='\n'
                d=0
        with open(path_1+'/'+str(i)+'.txt','w') as f :
            f.write(txt)
    print('正在删除多余文件，用时较长…')
    shutil.rmtree('/storage/emulated/0/termux_py_字符画/new')  
    print('---完成---')

##################          
def player() :
    path_1=path+'/list'
    a=os.listdir(path_1)
    for i in range(0,len(a)):
        print(i,'----',a[i][:-4])
    b=input('请选择序号')
    c=a[int(b)]
    with open(path_1+'/'+c,'r') as f :
        d=f.readlines()
    name=d[0][:-1]
    suma=d[1][:-1]
    path_2=path+'/'+name+'/'
    txt=[]
    for i in tqdm(range(1,int(suma)+1)) :
        with open(path_2+str(i)+'.txt','r') as f :
            txt.append(f.read())
    os.system('clear')
    t=time.time()
    for i in txt :
        os.system('clear')
        print(i)
        T=time.time()-t
        print(T)
        time.sleep(0.014)
    
    
    
##################
    
while True :
    IN=input('''
1.初始化
2.制作字符画
3.播放字符画
>>>''')

    if IN == '1' :
        initialize()
        break
    elif IN == '2' :
        ffmpeg_thumbnail()
        break
    elif IN == '3' :
        player()
        break
    else :
        print('输入错误')
    


#ffmpeg -i 1.mp4 -r 24 -f image2 .\output\1_frame_%05d.png
#ffmpeg -i "/storage/emulated/0/termux_py_字符画/video.mp4" -r 24 -f image2 /storage/emulated/0/termux_py_字符画/new/1_frame_%05d.png