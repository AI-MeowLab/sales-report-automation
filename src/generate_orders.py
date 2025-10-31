import pandas as pd
import random
from datetime import datetime, timedelta
import os

# 2. 주문내역 만들기

# 2.1 제품 목록 읽기
products_path = os.path.join("..", "output", "hills_cat_products.csv")
products_df = pd.read_csv(products_path)

# 2.2 주문 건 수 설정
NUM_ORDERS = 500

# 2.3 주문 날짜 범위 설정
end_date = datetime.now()
start_date = end_date - timedelta(days=120)

payment_methods = ["Card", "BankTransfer", "KakaoPay", "TossPay"]
statuses = ["paid", "shipped", "delivered", "cancelled", "refunded"]
status_weights = [0.25, 0.2, 0.4, 0.1, 0.05]

orders = []

# 2.4 랜덤한 주문 생성
for i in range(NUM_ORDERS):
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
        "customer_id": f"CUST-{random.randint(1, 120)}",
    }

    orders.append(order)

orders_df = pd.DataFrame(orders)

output_path = os.path.join("..", "output", "orders.csv")
orders_df.to_csv(output_path, index=False, encoding="utf-8-sig")

print(f"주문 {len(orders_df)}건 생성 완료 → {output_path}")