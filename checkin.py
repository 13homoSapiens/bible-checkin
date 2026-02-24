from books import parse_checkin as parse
from writein import merge_today_into_existing as merge
import pandas as pd
import looking

#init
days = ['1Mon.txt', '2Tue.txt', '3Wed.txt', '4Thu.txt', '5Fri.txt', '6Sat.txt', '7Sun.txt']
df = pd.read_excel("result.xlsx")
df = df[["姓名",'已读','等待']]
df.to_excel("result.xlsx", index=False)

for day in days:
    with open(day) as f:
        text = f.read()
    parsed = parse(text)
    date = parsed["date"]
    chapters = parsed["book"] + parsed["chapters"]
    names = parsed["names"]

    merge(file_path = "result.xlsx",
    today_list = names,
    day_key = chapters)
    looking.beauty()



