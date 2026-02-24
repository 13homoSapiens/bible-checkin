import pandas as pd

def merge_today_into_existing(
    file_path: str,
    today_list: list[str],   # 今天已读名单
    day_key: str             # 例如 "太1-2"
):
    # 1️⃣ 读取已有文件
    df_old = pd.read_excel(file_path, sheet_name='Sheet1')

    # 2️⃣ 构造今天的 DataFrame
    df_today = pd.DataFrame({
        "姓名": today_list,
        day_key: "(^_^)",
    })

    # 3️⃣ outer merge（两边都保留）
    df = pd.merge(df_old, df_today, on="姓名", how="outer")

    # 5️⃣ 更新统计列
    schedule_cols = [c for c in df.columns if c not in ["姓名","已读","等待"]]

    df["已读"] = df[schedule_cols].apply(
        lambda row: sum(cell == "(^_^)" for cell in row),
        axis=1
    )

    df["等待"] = len(schedule_cols) - df["已读"]

    # 4️⃣ 没出现的人填等待
    df[day_key] = df[day_key].fillna("(~~)")

    schedule_cols = [c for c in df.columns if c not in ["姓名", "已读", "等待"]]
    total_days = len(schedule_cols)
    df["已读"] = pd.to_numeric(df["已读"], errors="coerce")
    df["等待"] = pd.to_numeric(df["等待"], errors="coerce")
    mask = (df["已读"] == 0) & (df["等待"] == total_days)
    df.loc[mask, ["已读", "等待"]] = pd.NA

    # 6️⃣ 保存回去
    df.to_excel(file_path, index=False)

    return df

