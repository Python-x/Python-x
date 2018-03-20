class Kao_di_gua:
    def __init__(self):
        self.sheng_shu = 0
        self.sheng_shu_str = '生的鸡'
        self.add_tiao_liaos = []

    def Kao(self, times):
        self.sheng_shu += times
        if self.sheng_shu > 8:
            self.sheng_shu_str = '烤糊了'
        elif self.sheng_shu > 5:
            self.sheng_shu_str = '烤熟了'
            self.add_tiao_liaos.append('苹果酱料')
        elif self.sheng_shu > 3:
            self.sheng_shu_str = '半生不熟'
        else:
            self.add_tiao_liaos.append('橄榄油')
            self.sheng_shu_str = '生鸡'

kdg = Kao_di_gua()
kdg.Kao(3)
print(kdg.sheng_shu_str)
kdg.Kao(3)
print(kdg.sheng_shu_str)
print(kdg.add_tiao_liaos)
