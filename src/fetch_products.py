from bs4 import BeautifulSoup
import pandas as pd
import random
import os

def guess_price(category, main_type):
    """
    카테고리/사료타입 기준으로 대략적인 가격대를 정하고
    거기에 1~2천원 정도 랜덤으로 얹어서 리얼하게 보이게 하는 함수
    """
    # 1) 기본 베이스 가격
    # 프리스크립션 > 사이언스
    if category and "프리스크립션" in category:
        base = random.randint(48000, 62000)   # 처방식이니까 비싸게
    elif category and "사이언스" in category:
        base = random.randint(32000, 46000)
    else:
        base = random.randint(28000, 42000)   # 기타/태그모호

    # 2) 사료 타입에 따른 보정
    # 건사료가 습식보다 비싸게
    if main_type and "건사료" in main_type:
        base += random.randint(2000, 5000)
    elif main_type and ("습식" in main_type or "캔" in main_type):
        base -= random.randint(1000, 3000)

    # 3) 깔끔하게 100원 단위 정리
    return int(base / 100) * 100

def generate_products(html_path="../data/hills.html", output_path="../output/hills_cat_products.csv"):
    """
    힐스 HTML 파일을 파싱해서 제품 정보를 CSV로 저장
    """
    # 폴더 존재 여부 확인
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # HTML 읽기
    if not os.path.exists(html_path):
        raise FileNotFoundError(f"❌ HTML 파일이 없습니다: {html_path}")

    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

     # BeautifulSoup 파싱
    soup = BeautifulSoup(html, "html.parser")

    # 제품 블록 선택
    products = soup.select("div.articleList-article-wrapper")
    rows = []

    # 반복해서 데이터 추출
    for product in products:
        name_tag = product.select_one("h3.articleList-title a")
        if not name_tag:
            continue

        name = name_tag.get_text(strip=True)
        tags = [li.get_text(strip=True) for li in product.select("ul.articleList-tags li")]

        # 주요 속성 추출 (간단히)
        life_stage = next((t for t in tags if "어덜트" in t or "키튼" in t or "시니어" in t), "전연령용")
        category = next((t for t in tags if "사이언스" in t or "프리스크립션" in t), "기타")
        main_type = next((t for t in tags if "건사료" in t or "습식" in t), "기타")

        price = guess_price(category, main_type)

        rows.append({
            "name": name,
            "category": category,
            "life_stage": life_stage,
            "main_type": main_type,
            "tags": ", ".join(tags),
            "price": price,
        })

    df = pd.DataFrame(rows)
    df.to_csv("../output/hills_cat_products.csv", index=False, encoding="utf-8-sig")
    print(f"{len(df)}개 제품 저장 완료!")
    
    return df

if __name__ == "__main__":
    generate_products()