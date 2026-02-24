import pandas as pd

people = ['Anna', 'Binbin', 'Bo', 'HomoSapiens', 'Jenny', 'Kai GONG', 'Kali', 'Kim',
          'Michael', 'Monica', 'Purple', 'Qiqi', 'Sandy', 'Simon', 'Yuanbo', '东岩',
          '光宇', '威威', '宏珊', '少平', '少鹏', '岩松', '张乃川', '晓丹', '李莹莹', '李静',
          '燕珊', '王淑娟', '玮彤', '美盈', '育青', '蓝蓝大海', '韩姐', '飞鸟', '香香', '高蓝']

df = pd.read_excel("result.xlsx")
df = pd.DataFrame({"姓名": people})
# 覆盖写入
df.to_excel("result.xlsx", index=False)