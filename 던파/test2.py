import csv
import random

# 헤더 생성
header = ["가맹점", "정산금액"]

# 레코드 생성
data = []
for _ in range(100):
    가맹점 = f"가맹점_{random.randint(1, 1000)}"
    정산금액 = round(random.uniform(1000, 10000), 2)
    data.append([가맹점, 정산금액])

# CSV 파일 작성
file_path = "가맹점데이터.csv"
with open(file_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # 헤더 작성
    writer.writerow(header)
    
    # 데이터 작성
    writer.writerows(data)

print(f"CSV 파일이 성공적으로 생성되었습니다. 파일 경로: {file_path}")