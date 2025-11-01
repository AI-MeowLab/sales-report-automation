import pandas as pd
import random
import os
from datetime import datetime, timedelta

# 고객 데이터 생성
def generate_customers(num_customers = 300):
    # 저장 폴더 생성
    output_dir = "../output"
    os.makedirs(output_dir, exist_ok=True)

    # 기본 설정값
    regions = ["서울", "경기", "인천", "부산", "대구", "광주", "대전", "울산"]
    gender = ["F", "M"]
    membership_tiers = ["Bronze", "Silver", "Gold", "VIP"]

    # 가입일은 "오늘 기준 2년 이내" 랜덤 날짜로
    today = datetime.today()
    days_range = 365*2  # 2년

    customers = []

    for i in range(1, num_customers + 1):
        customer_id = f"C{str(i).zfill(4)}"
        # 지역 및 주문자 성별 랜덤
        region = random.choice(regions)
        gender = random.choice(gender)

        # 반려묘 체중은 2.5 ~ 8.5kg 사이로 랜덤 (소수 1자리)
        cat_weight = round(random.uniform(2.5, 8.5), 1)

        # 다묘가정 여부 (30% 정도만 1로)
        has_multiple_cats = 1 if random.random() < 0.3 else 0

        # 가입일 랜덤 생성
        random_days = random.randint(0, days_range)
        register_date = (today - timedelta(days = random_days)).strftime("%Y-%m-%d")

        # 회원 등급 랜덤
        membership_tier = random.choice(membership_tiers)

        # 이메일 랜덤
        email = f"{customer_id.lower()}@hillsmall.com"

        customers.append({
            "customer_id": customer_id,
            "region": region,
            "cat_weight": cat_weight,
            "register_date": register_date,
            "gender": gender,
            "has_multiple_cats": has_multiple_cats,
            "membership_tier": membership_tier,
            "email": email,
        })

    # DataFrame으로 변환
    df = pd.DataFrame(customers)

    # CSV로 저장
    output_path = os.path.join(output_dir, "customers.csv")
    df.to_csv(output_path, index=False, encoding="utf-8-sig")

    print(f"✅ 고객 데이터 {len(df)}건 생성 완료 → {output_path}")
    return df

if __name__ == "__main__":
    generate_customers()