{\rtf1\ansi\ansicpg1254\cocoartf2818
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import yfinance as yf\
import pandas as pd\
symbols = ["PLTR", "BAC", "DNLI", "PFE", "AAPL"]\
start_date = "2022-01-01"\
end_date = "2024-10-11"\
output_path = "/Users//Library/yolunuz/kendi sisteminiz/\'85/compared_stocks_data.xlsx"\
with pd.ExcelWriter(output_path) as writer:\
    for symbol in symbols:\
        data = yf.download(symbol, start=start_date, end=end_date)\
        data.to_excel(writer, sheet_name=symbol)\
\
print(f"Veriler ba\uc0\u351 ar\u305 yla '\{output_path\}' konumuna kaydedildi.")\
}