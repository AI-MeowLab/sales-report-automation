# 🛒 판매 데이터 자동화 (Sales Report Automation)

> Python 기반으로 판매 데이터를 자동 생성하고 정리하는 프로젝트입니다.  
> 실제 사이트(힐스펫)의 제품 정보를 기반으로 가상의 판매 내역을 생성하고,  
> 향후 자동 통계 리포트를 **웹 시각화 형태로 확장하여 GitHub Pages로 배포할 예정입니다.**


## 📘 프로젝트 개요 (Project Overview)

### 🇰🇷 한국어
- HTML에서 제품명, 카테고리, 가격을 추출하여 CSV로 저장
- 고객 및 주문 데이터를 자동으로 생성 (총 300명 고객, 500건 주문)
- 결제 방식·주문 상태·회원 등급 등 무작위 샘플링
- main.py 한 번 실행으로 모든 데이터 자동 생성
- 향후 자동 통계 리포트를 웹 형태로 시각화하여 GitHub Pages를 통해 배포 예정  

### 🌍 English
This project automates the generation and cleaning of simulated sales data using Python.  
- Parses product information from a local HTML file (hills.html)
- Automatically generates 300 sample customers and 500 linked orders
- Randomizes payment methods, order statuses, and customer tiers
- Supports one-click data generation via main.py
- Future goal: visualize automated sales reports and deploy via GitHub Pages


## 🧩 진행 현황 (Current Progress)

### ✅ 완료된 기능 (Completed)
- generate_products.py – HTML 기반 제품 정보 파싱
- generate_customers.py – 고객 데이터 자동 생성
- generate_orders.py – 고객 연동 주문 데이터 생성
- main.py - 전체 자동 실행 통합 (제품 → 고객 → 주문)
- .gitignore 및 폴더 구조 정리

### 🚧 예정된 기능 (Planned)
- 자동 통계 리포트 생성 및 웹 시각화 (`make_report.py`)
- 카테고리·월별 매출 분석
- GitHub Pages 기반 리포트 배포

---

## 🗂️ 프로젝트 구조 (Project Structure)

```
sales-report-automation/
├── data/                    # 원본 HTML 데이터 (예: hills.html)
├── output/                  # 자동 생성 결과 (CSV 등)
│   ├── hills_cat_products.csv
│   ├── customers.csv
│   └── orders.csv
├── src/                     # 데이터 생성 스크립트
│   ├── generate_products.py
│   ├── generate_customers.py
│   └── generate_orders.py
├── main.py                  # 한 번에 전체 데이터 생성
├── .gitignore
└── README.md
```

## ⚙️ 기술 스택 (Tech Stack)

| 항목 | 설명 |
|------|------|
| **Python 3.9+** | 메인 개발 언어 |
| **pandas** | 데이터 프레임 처리 |
| **BeautifulSoup4** | HTML 파싱 |
| **random, datetime** | 데이터 샘플링 및 날짜 생성 |
| **openpyxl, matplotlib** *(planned)* | 리포트 자동화 및 웹 시각화용 데이터 생성 |

## 🚀 실행 방법 (How to Run)

### 1️⃣ 환경 설정

```bash
git clone https://github.com/AI-MeowLab/sales-report-automation.git
cd sales-report-automation

python -m venv venv
source venv/bin/activate   # (Windows: venv\Scripts\activate)
pip install pandas beautifulsoup4
```

### 2️⃣ 데이터 생성
```bash
python main.py
```

### 3️⃣ 개별 실행도 가능
```
cd src
python generate_products.py      # 제품 데이터만 생성
python generate_customers.py     # 고객 데이터만 생성
python generate_orders.py        # 주문 데이터만 생성
```

## 🧠 프로젝트 목적 (Purpose)

### 🇰🇷 한국어
- 데이터 분석 및 자동화 학습용  
- 실제 쇼핑몰 데이터를 모사한 가상 판매 데이터 생성  
- 자동 리포트를 웹 시각화 형태로 배포 (GitHub Pages 활용)

### 🌍 English
- Educational project for data analytics and automation  
- Generates realistic e-commerce datasets  
- Expands to web-based visualized reports via **GitHub Pages**


## 📅 업데이트 로그 (Update Log)

| 날짜 | 내용 |
|------|------|
| 2025-10-31 | 제품 파싱 및 주문 생성 기능 구현 완료 |
| 2025-11-01 | generate_products() 함수화 및 main.py 통합 실행 추가 |
| 예정 | 자동 통계 리포트 기능 및 GitHub Pages 배포 예정 |


## ✨ 작성자 (Author)

| 항목 | 정보 |
|------|------|
| **이름** | Kim Chaeyoon (AI-MeowLab) |
| **분야** | Python · Data Automation · Visualization Projects |
| **연락처** | GitHub Issues or personal profile |


## 💡 한줄 요약 (Summary)

> “Python으로 가상의 판매 데이터를 자동으로 생성하고,  
> 웹 기반 리포트 시각화 및 GitHub Pages 배포로 확장하는 프로젝트입니다.”

## 💬 커밋 및 PR 가이드라인
| 구분 | 예시 |
|------|------|
| **기능 추가** | feat: integrate product generator into main workflow |
| **문서 수정** | docs: update readme for main.py automation |
| **버그 수정** | fix: resolve file path error in order generator |