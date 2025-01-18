# HFT Trading Analysis

## 📅 Week 1: Dataset Collection & Preprocessing
**Goal**: Find and prepare the dataset(s) for analysis.

### Day 1–2: Dataset Identification

#### Centralized Dataset:
- [HFT Trading MAP (1-minute data of the most famous stocks)](https://github.com/hank08819/HFTTradingMAP)
- [High-Frequency Futures Data (China - 1-minute data of famous Chinese stocks)](https://www.kaggle.com/datasets/wentinglu/highfrequency-futures-data-china)
- [FirstRateData (1-minute data for SPY and EEM ETFs, only for 2 weeks)](https://firstratedata.com/free-intraday-data)
- [ETSin (1-minute data)](https://etsin.fairdata.fi/dataset/73eb48d7-4dbc-4a10-a52a-da745b47a649/data)

#### Decentralized Dataset:
- [Etherscan API](https://etherscan.io) (Check the main.py for an example usage). You can pick 1000 ETH addresses (both HFT investors and passive investors) and estimate their returns in USD based on buy and sell transactions.
- [Uniswap](https://uniswap.org) is another option to check different cryptocurrencies (not just ETH).

**Example Etherscan Address**:  
`144ae532d7d413daf0c7d44361efbb790c0dca51`

### Deliverables:
- Links to selected datasets (all grouped) [Here](https://mega.nz/folder/AOcCAS4Q#whnWw3j81doBSmpBWAWDxw)
- Initial inspection of datasets (data types, size, structure) - Available in the EDA Notebook file.

### Day 3–5: Data Preprocessing
- **Standardize Data**: Align columns (`timestamp`, `open`, `high`, `low`, `close`, `volume`, `Centralized/Decentralized`).
- **Merge Data**: Combine all dataset data with a column for `Dataset_name`, a binary column for `Centralized/Decentralized`, and the file name.
- **Active vs Passive Labels**: Define thresholds for active and passive trades.

### Deliverables:
- Cleaned dataset(s) ready for analysis.
- Data preprocessing script.

---

## 📅 Week 2: Analysis & Modeling
**Goal**: Conduct statistical analysis, build regression models, and simulate scenarios.

### Day 6–8: Statistical Analysis
- **Regression Analysis**: Analyze trade frequency, commission rates, and net returns.
- **Performance Metrics**: Calculate Sharpe Ratio and Net Returns.
- **Epps Effect**: Examine return correlations over time.

### Deliverables:
- Statistical summary and key relationships identified.
- Visualizations (scatter plots, regression lines).

### Day 9–11: Simulation & Scenario Modeling
- Build simulations for varying:
  - Trade frequency
  - Investment size
  - Commission fees
- Compare outcomes across centralized vs decentralized exchanges.

### Deliverables:
- Simulation outputs and visualizations.
- Key insights documented.

### Day 12–14: Theoretical Model Integration
- **Bouchaud's Response Function**: Model price impact across exchanges.
- **Volatility Clustering (GARCH Model)**: Assess risk-adjusted returns.
- **Epps Effect**: Validate theoretical predictions with data.

### Deliverables:
- Results from Bouchaud's model and GARCH analysis.
- Final visualizations showing trade-offs.

---

## 📅 Week 3: Results & Write-Up
**Goal**: Organize results and draft the paper.

### Day 15–17: Write-Up Drafting
- Already on Overleaf (10 pages of text, max 15 images).

### Deliverables:
- First full draft of the paper.
- Clear figures and tables.

### Day 18: Code Cleanup
- Create a `main.py` file that:
  - Runs the full analysis.
  - Has a Boolean switch for demo mode (subset of data).
- Organize folders:
  - `/data` (demo data + README for full dataset link).
  - `/scripts` (preprocessing, analysis, simulation).
  - `/outputs` (graphs, tables).

### Deliverables:
- Main code file (`main.py`) with demo switch.
- README file explaining the folder structure and dependencies.

### Day 19: Final Submission
- Double-check:
  - Write-up is clean and formatted.
  - Code runs without errors in demo mode.
  - Dataset links are clearly provided.

---

## Folder Structure
```bash
/data
    - demo_data.csv
    - full_dataset_link.txt
/scripts
    - data_preprocessing.py
    - analysis.py
    - simulation.py
/outputs
    - graphs
    - tables
