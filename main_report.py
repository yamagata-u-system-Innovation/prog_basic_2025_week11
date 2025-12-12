# 第10週 課題 模範解答
# main_report.py
# Atsumi2025_airtemp_7days.csv から 2025-08-24 の 24点の温度データを読み込み、
# 1行のレポートを出力するプログラム

import csv

def mean(nums):
    """リストの平均値を返す。空リストのときは None。"""
    if len(nums) == 0:
        return None
    total = 0.0
    for n in nums:
        total += n
    return total / len(nums)


def hottest_hour(nums):
    """
    最大値とそのインデックス(時間=0..23)をタプルで返す。
    空リストなら (None, None)
    """
    if len(nums) == 0:
        return (None, None)
    max_val = nums[0]
    max_idx = 0
    for idx in range(1, len(nums)):
        if nums[idx] > max_val:
            max_val = nums[idx]
            max_idx = idx
    return (max_val, max_idx)


def count_alerts(nums, threshold):
    """threshold（しきい値）以上の時間数を数える。"""
    count = 0
    for t in nums:
        if t >= threshold:
            count += 1
    return count


def make_report_line(day_label, nums, threshold):
    """
    1行のレポート文字列を作成する。
    例:
      "Day-20250824 | avg=28.0°C | max=35.0°C at h=12 | alerts(>=28.0)=11"
    """
    avg = mean(nums)
    mx, h = hottest_hour(nums)
    alerts = count_alerts(nums, threshold)
    return (
        f"{day_label} | avg={avg:.1f}°C | "
        f"max={mx:.1f}°C at h={h} | alerts(>={threshold})={alerts}"
    )


if __name__ == "__main__":
    CSV_PATH = "Atsumi2025_airtemp_7days.csv"
    TARGET_DATE = "2025-08-24"          # 今回レポートを作る日付
    THRESHOLD = 28.0                    # しきい値（アラート温度）

    # CSV から TARGET_DATE の 24件の温度データを読み込む
    temps = []
    with open(CSV_PATH, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Date"] == TARGET_DATE:
                temps.append(float(row["Air Temp (°C)"]))

    # 日付ラベル（例：Day-20250824）を作る
    day_label = f"Day-{TARGET_DATE.replace('-', '')}"

    # レポート1行を作成して表示
    report_line = make_report_line(day_label, temps, THRESHOLD)
    print(report_line)
