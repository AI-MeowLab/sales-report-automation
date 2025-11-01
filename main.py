"""
Main script to generate all sample datasets for the E-commerce automation project.
1. Generate product list by parsing local Hills HTML file
2. Generates customer master data
3. Generates order data linked to customers
"""

import os
from src.fetch_products import generate_products
from src.generate_customers import generate_customers
from src.generate_orders import generate_orders

def main():
    print("🚀 Starting automated data generation process...\n")

    # 1 제품 데이터 생성
    print("Step 1: Generating product list...")
    products = generate_products(html_path="data/hills.html", output_path="output/hills_cat_products.csv")

    # 2 고객 데이터 생성
    print("\nStep 2: Generating customer data...")
    customers = generate_customers(num_customers=300)

    # 3 주문 데이터 생성
    print("\nStep 3: Generating order data...")
    orders = generate_orders(num_orders=500)

    # 완료 메시지
    print("\nAll data generation completed successfully!")


if __name__ == "__main__":
    main()