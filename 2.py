print('введите время, часы')
time= int(input())
sec= time//3600
minut= (time//60)%60
chas= time%60
print(str(chas)+':'+str(minut)+':'+str(sec))
