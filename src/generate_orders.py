import pandas as pd
import random
from datetime import datetime, timedelta
import os

def generate_orders(num_orders=500):

    # 기본 경로/폴더 설정
    output_dir = os.path.join("..", "output")
    os.makedirs(output_dir, exist_ok=True)

    # 고객 데이터 읽기
    customers_path = os.path.join(output_dir, "customers.csv")
    customers_df = pd.read_csv(customers_path)

    # 제품 목록 읽기
    products_path = os.path.join(output_dir, "hills_cat_products.csv")
    products_df = pd.read_csv(products_path)

    # 주문 날짜 범위 설정
    end_date = datetime.now()
    start_date = end_date - timedelta(days=120) # 최근 120일

    payment_methods = ["Card", "BankTransfer", "KakaoPay", "TossPay"]
    statuses = ["paid", "shipped", "delivered", "cancelled", "refunded"]
    status_weights = [0.25, 0.2, 0.4, 0.1, 0.05]

    orders = []

    # 랜덤한 주문 생성
    for i in range(num_orders):
        # 랜덤 주문 날짜
        order_date = start_date + timedelta(
            seconds=random.randint(
                0,
                int((end_date - start_date).total_seconds())
            )
        )

        # 랜덤 제품
        product = products_df.sample(1).iloc[0]

        quantity = random.randint(1, 4)
        unit_price = int(product["price"])
        total_amount = unit_price * quantity

        # 고객 하나 랜덤 선택
        customer = customers_df.sample(1).iloc[0]

        # 랜덤 상태
        status = random.choices(statuses, weights=status_weights, k=1)[0]

        # 주문 생성
        order = {
            "order_id": f"ORD-{10000+i}",
            "order_date": order_date.strftime("%Y-%m-%d %H:%M:%S"),
            "product_name": product["name"],
            "category": product.get("category", None),
            "life_stage": product.get("life_stage", None),
            "main_type": product.get("main_type", None),
            "unit_price": unit_price,
            "quantity": quantity,
            "total_amount": total_amount,
            "payment_method": random.choice(payment_methods),
            "status": status,
            "customer_id": customer["customer_id"],
            "region": customer["region"],
            "gender": customer["gender"],
            "has_multiple_cats": customer["has_multiple_cats"],
            "membership_tier": customer["membership_tier"],
            "register_date": customer["register_date"],
            "cat_weight": customer["cat_weight"],
            "email": customer["email"]
        }

        orders.append(order)

    # DataFrame으로 변환
    orders_df = pd.DataFrame(orders)

    # CSV로 저장
    output_path = os.path.join(output_dir, "orders.csv")
    orders_df.to_csv(output_path, index=False, encoding="utf-8-sig")

    print(f"주문 {len(orders_df)}건 생성 완료 → {output_path}")

if __name__ == "__main__":
    generate_orders()