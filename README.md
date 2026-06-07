# ☁️ Cloud FinOps AI: Smart Cost Optimizer

An intelligent tool that analyzes server logs and uses Machine Learning (Prophet algorithm) to forecast infrastructure costs and provide actionable optimization recommendations.

## 🚀 Key Features
* **Predictive Analytics:** Forecasts future cloud costs based on historical CPU and RAM usage.
* **Intelligent Recommendations:** Suggests downsizing resources or implementing auto-scaling based on predicted traffic patterns.
* **Interactive Dashboard:** Built with Streamlit to visualize cost trends and resource efficiency.
* **Automated Data Generation:** Simulates realistic cloud server metrics to train the AI model.

## 🛠️ Tech Stack
* **Language:** Python
* **Forecasting:** Prophet (by Meta)
* **Dashboard:** Streamlit
* **Data Processing:** Pandas, NumPy
* **Environment:** VS Code

## ⚙️ How to Run

### 1. Set Up Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install pandas numpy scikit-learn prophet streamlit
