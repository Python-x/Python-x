import time
list1 = ["马化疼","码云","王贱林","潘长酱"]
for i in list1:
	print("%s来到了饭局"%i)
	time.sleep(1)
for e in list1:
	print("各位大哥们,这位是%s"%e)
	time.sleep(1)
time.sleep(3)
print("马化疼突然感觉一阵肾疼,急忙冲了出去")
time.sleep(2)
print("源哥来到了饭局")
time.sleep(1)
list1[0] = "赵庆元"
for u in list1:
	print("没事没事,%s你先坐,别管他"%u)
	time.sleep(1)
time.sleep(1)
print("哎,那里有个更大的桌子,朋友们,我再叫一些人来嗨")
time.sleep(1)
list1.insert(0,"贾淼浩")
list1.insert(2,"吴金航")
list1.append("王喜亮")
print("一共来了%s个人"%len(list1))
print("%s来到了饭局"%list1[0])
time.sleep(1)
print("%s来到了饭局"%list1[2])
time.sleep(1)
print("%s来到了饭局"%list1[6])
time.sleep(1)
for p in list1:
	print("%s大哥，咱去那个桌子"%p)
	time.sleep(1)
time.sleep(1)
print("唉呀妈呀出事了,桌子没回来,只能在我家小桌子凑合了")
time.sleep(1)
n = 6
for o in range(1,6):
	print("%s,不好意思,只能下次再一起玩了"%list1[n])
	list1.pop(n)
	n-=1
	time.sleep(1)
for l in list1:
	print("%s,走吧,去我家玩"%l)
	time.sleep(1)
del list1[0]
del list1[0]
print(list1)
