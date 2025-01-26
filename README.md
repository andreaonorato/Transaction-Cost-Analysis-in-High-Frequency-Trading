# Transaction Cost Analysis in High-Frequency Trading  

## Overview  
This project explores the impact of transaction costs on profitability in high-frequency trading (HFT) and passive investment strategies. Using a dataset of 1-second trading data for Bitcoin (BTC), Ethereum (ETH), and Cardano (ADA) over a 2-week period, the study analyzes market microstructure, network fees, and trading strategy performance in decentralized exchanges (DEXs).

Key insights include:  
- The influence of trading fees, slippage, and network costs on net profitability.  
- A comparative study of active (HFT) vs passive strategies.  
- The role of market microstructure dynamics and the Epps effect in trading decisions.  

---

## Datasets  
The study uses high-frequency cryptocurrency limit order book data sourced from Kaggle (https://www.kaggle.com/datasets/martinsn/high-frequency-crypto-limit-order-book-data)
While regarding fees the dataset has been built starting from these data:
- **Bitcoin (BTC):** [Mempool Fee Data](https://mempool.space/graphs/mempool#4y)  
- **Ethereum (ETH):** [Gas Prices](https://etherscan.io/chart/gasprice)  
- **Cardano (ADA):** [Explorer Fees](https://cexplorer.io/)  

---

## Results  
Key findings:  
- HFT profitability is sensitive to transaction costs, favoring BTC for tighter spreads.  
- Passive strategies perform better under high network congestion due to lower frequency.  
- Correlation insights from the Epps effect can inform portfolio optimization.

---

## How to Use  
1. Clone the repository:  
   ```bash
   git clone https://github.com/andreaonorato/Transaction-Cost-Analysis-in-High-Frequency-Trading.git
   cd Transaction-Cost-Analysis-in-High-Frequency-Trading
   ```
2. Install required libraries:
  ```bash
  pip install -r requirements.txt
  ```

