# 🧪 ERP System — Test Automation Suite

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?style=flat-square&logo=selenium&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-8.x-0A9EDC?style=flat-square&logo=pytest&logoColor=white)
![Faker](https://img.shields.io/badge/Faker-Data%20Dummy-FF6B6B?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

> End-to-end automation testing suite for an ERP system, covering Authentication and Master Data modules using Selenium WebDriver + Pytest.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Test Coverage](#test-coverage)
- [Getting Started](#getting-started)
- [Running Tests](#running-tests)
- [Environment Variables](#environment-variables)
- [Test Reports](#test-reports)

---

## 🔍 Overview

This project is a **manual & automation testing portfolio** for an ERP (Enterprise Resource Planning) system. It demonstrates real-world QA Engineering practices including:

- 🔐 **Authentication testing** — positive & negative scenarios
- 🗂️ **Master data testing** — Item creation, validation
- 🤖 **Data-driven testing** using Faker for realistic dummy data
- 🔒 **Secure config management** via `.env` and `python-dotenv`

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3.10+** | Primary language |
| **Selenium WebDriver** | Browser automation |
| **Pytest** | Test framework & runner |
| **Faker** | Generate realistic dummy test data |
| **python-dotenv** | Manage environment variables securely |
| **pytest-html** | HTML test report generation |

---

## 📁 Project Structure

```
erp-automation-testing/
│
├── tests/
│
├── pages/                          # Page Object Model (POM)
│
├── utils/
│   ├── driver_setup.py             # WebDriver initialization
│   ├── generator.py                # Faker data generators
│   └── helpers.py                  # Reusable helper functions
│
├── reports/                        # Auto-generated HTML test reports
├── .env.example                    # Environment variable template
├── conftest.py                     # Pytest fixtures & setup
├── requirements.txt
└── README.md
```

---

## ✅ Test Coverage

### 🔐 Authentication (`tests/auth/`)

| Test Case | Type | Status |
|-----------|------|--------|
| Login with valid email & password | Positive | ✅ |
| Login with wrong password | Negative | ✅ |
| Login with wrong email | Negative | ✅ |
| Login with unregistered email | Negative | ✅ |
| Login without email (empty) | Negative | ✅ |
| Login without password (empty) | Negative | ✅ |
| Login without email & password | Negative | ✅ |

### 🗂️ Data (`tests/`)

| Test Case | Type | Status |
|-----------|------|--------|
| Create new data | Positive | ✅ |
| Create record with empty fields | Negative | ✅ |
| Edit existing record | Positive | ✅ |
| Delete record | Positive | ✅ |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Google Chrome + matching [ChromeDriver](https://chromedriver.chromium.org/)

### Installation

```bash
# Clone the repository
git clone https://github.com/username/erp-automation-testing.git
cd erp-automation-testing

# Create virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt
```

### Setup Environment Variables

```bash
# Copy the example env file
cp .env.example .env
```

Edit `.env` with your actual credentials:

```env
BASE_URL=http://your-erp-app.com
VALID_EMAIL=youruser@email.com
VALID_PASSWORD=yourpassword
```

---

## ▶️ Running Tests

```bash
# Run all tests
pytest

# Run specific module
pytest tests/auth/
pytest tests/inventory/
pytest tests/master/

# Run with detailed output
pytest -v

# Run and generate HTML report
pytest -v --html=reports/report.html --self-contained-html --capture=tee-sys
```

---

## 🔐 Environment Variables

Credentials and config are stored in `.env` (never committed to Git).

| Variable | Description |
|----------|-------------|
| `BASE_URL` | URL of the ERP application |
| `VALID_EMAIL` | Valid login email for positive tests |
| `VALID_PASSWORD` | Valid login password for positive tests |

See `.env.example` for the full template.

---

## 📊 Test Reports

After running tests with `--html`, open the generated report:

```
reports/report.html
```

The report includes:
- ✅ Pass / ❌ Fail / ⚠️ Skip summary
- Detailed error logs and tracebacks
- Test duration per case

---

## 👤 Author

**[Agung Perdana]**
QA Engineer | Manual & Automation Testing

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=flat-square&logo=linkedin)](https://linkedin.com/in/agung-perdana-it)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat-square&logo=github)](https://github.com/AgungPerdana-IT)

---

> 💡 *This project is part of my QA Engineering portfolio, demonstrating real-world automation testing practices on an ERP system.*