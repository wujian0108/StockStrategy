import time
import akshare as ak
import pandas as pd


def get_stock_data() -> None:
    stock_codes = ak.stock_zh_a_spot_em()['代码']
    data_frames = []
    count = 0
    for stock_code in stock_codes:
        try:
            stock_data = ak.stock_zh_a_hist(
                symbol=stock_code, period="daily", start_date="20240605", end_date='20240607', adjust="")
            data_frames.append(stock_data)
        except Exception as e:
            print(f"Error fetching data for {stock_code}: {e}")
        if count % 10 == 0:
            time.sleep(0.1)
        count += 1
    all_stock_data = pd.concat(data_frames)
    all_stock_data.to_csv('./stockdata01.csv', sep=',', index=False)


stock_df = pd.read_csv('./stockdata01.csv')
filtered_stock_df = stock_df[stock_df['A'] > 10]
