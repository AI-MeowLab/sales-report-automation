# 🛒 판매 데이터 자동화 (Sales Report Automation)

> Python 기반으로 판매 데이터를 자동 생성하고 정리하는 프로젝트입니다.  
> 실제 사이트(힐스펫)의 제품 정보를 기반으로 가상의 판매 내역을 생성하고,  
> 향후 자동 통계 리포트를 **웹 시각화 형태로 확장하여 GitHub Pages로 배포할 예정입니다.**


## 📘 프로젝트 개요 (Project Overview)

### 🇰🇷 한국어
- HTML에서 제품명, 카테고리, 가격을 추출하여 CSV로 저장  
- 제품 정보를 기반으로 500건의 주문 내역 자동 생성  
- 결제 방식, 주문 상태, 고객 ID 등을 무작위로 생성  
- 향후 자동 통계 리포트를 웹 형태로 시각화하여 GitHub Pages를 통해 배포 예정  

### 🌍 English
This project automates the generation and cleaning of simulated sales data using Python.  
- Parses product information from a sample HTML (Hills Pet Cat Food)  
- Generates 500 random order records  
- Includes random payment methods, statuses, and customer IDs  
- Future work: visualize automated sales reports and deploy them via **GitHub Pages**


## 🧩 진행 현황 (Current Progress)

### ✅ 완료된 기능 (Completed)
- 제품 정보 파싱 스크립트 (`fetch_products.py`)
- 주문 내역 자동 생성 스크립트 (`generate_orders.py`)
- `.gitignore` 구성 및 프로젝트 구조 정리

### 🚧 예정된 기능 (Planned)
- 자동 통계 리포트 생성 및 웹 시각화 (`make_report.py`)
- 카테고리·월별 매출 분석
- GitHub Pages 기반 리포트 배포

---

## 🗂️ 프로젝트 구조 (Project Structure)

```plaintext
sales-report-automation/
├── data/               # 원본 HTML 데이터 (예: hills.html)
├── src/                # 데이터 생성 스크립트
│   ├── fetch_products.py
│   └── generate_orders.py
├── output/             # 실행 시 자동 생성되는 결과 (Git에서 제외됨)
├── venv/               # 가상환경 (Git에서 제외됨)
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
source venv/bin/activate
pip install pandas beautifulsoup4
```

### 2️⃣ 데이터 생성
```bash
cd src
python fetch_products.py   # 제품 정보 CSV 생성
python generate_orders.py    # 주문 내역 CSV 생성
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