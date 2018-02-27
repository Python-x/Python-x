import time
p = "欢迎来到召唤师峡谷\n"
print(p)
first_name ="潘"
last_name ="志伟"
full_name = first_name+last_name
print(full_name)
age = int(input("输入你的年龄"))
if age <11:
	print("你只能玩一个小时哦")
else:
	print("正在进入游戏...")
q = 2
print("尊敬的召唤师，您在这局游戏中的的综合排名是%d,继续努力哦\n"%q)
list1 = ["安其拉","孙悟空","杨戬","貂蝉","扁鹊"]
print(list1)
print(list1[3])
print(list1[1])
time.sleep(2)
print("马化腾你的安其拉太菜了，换个吧")
list1[0]="狄仁杰"
print(list1)
time.sleep(2)
del list1[2]
print("杨戬的哮天犬叫他回去撒狗粮了....\n杨戬退出了组队")
time.sleep(2)
print(list1)
list1.insert(0,"兰陵王")
print(list1,"\n准备好,游戏开始")
list1.pop()
time.sleep(2)
print("您的队友扁鹊退出了游戏")
print(list1)
list1.append("扁鹊")
time.sleep(2)
print(list1)
print("第二局开始,换队长")
list1.sort()
time.sleep(2)
print(list1)
print("妈卖批,不行,还得换,他太菜")
list1.sort(reverse = True)
time.sleep(2)
print(list1)
print(sorted(list1))
list1.reverse()
print(list1)
print("就这样吧")
print(len(list1))
for i in list1:
	if i == "貂蝉":
		print("忍奥义之瞎JB秀--%s"%i)
	else:
		print("%s是一个优秀的英雄"%i)







