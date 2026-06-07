import pandas as pd
from prophet import Prophet
import warnings

warnings.filterwarnings("ignore")

print("[*] Loading historical server data...")
df = pd.read_csv('server_logs.csv')
prophet_df = df[['timestamp', 'hourly_cost_usd']].rename(columns={'timestamp': 'ds', 'hourly_cost_usd': 'y'})

print("[*] Training AI Forecasting Model (Prophet)...")
model = Prophet(yearly_seasonality=False, weekly_seasonality=True, daily_seasonality=True)
model.fit(prophet_df)

print("[+] AI Model trained successfully!")
print("[*] Predicting future costs for the next 7 days...")
future = model.make_future_dataframe(periods=168, freq='h')
forecast = model.predict(future)
future_forecast = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(168)
future_forecast.to_csv('forecast_results.csv', index=False)

print("[+] Future predictions saved to 'forecast_results.csv'!")
print(f"[*] Estimated total cost for next 7 days: ${future_forecast['yhat'].sum():.2f}")