import yfinance as yf
import numpy as np

# Fetch Tesla stock price data
def fetch_stock_data(start, end, ticker="TSLA"):
    stock_data = yf.download(ticker, start=start, end=end)
    return stock_data['Close'].tolist()  # Use closing prices


# 1. Buy and Hold Strategy
def buy_and_hold(prices):
    initial_price = prices[0]
    return (prices[-1] - initial_price) / initial_price  # Single return value




# 2. Momentum Strategy
def momentum(prices, window=5):
    if len(prices) < window + 1:
        return 0  # Not enough data for a complete momentum strategy
    if prices[-1] > prices[0]:
        return (prices[-1] - prices[0]) / prices[0]  # Positive momentum return
    else:
        return (prices[0] - prices[-1]) / prices[0]  # Negative momentum return




# 3. Mean Reversion Strategy
def mean_reversion(prices, window=20, transaction_cost=0.001):
    if len(prices) < window + 1:
        return 0  # Not enough data for mean reversion strategy
    moving_avg = sum(prices[-window:]) / window
    if prices[-1] < moving_avg:
        return (prices[-1] - prices[-2]) - transaction_cost
    else:
        return (prices[-2] - prices[-1]) - transaction_cost



# 4. Scalping Strategy
def scalping(prices, threshold=0.001, transaction_cost=0.001):
    if len(prices) < 2:
        return 0  # Not enough data for scalping strategy
    price_diff = prices[-1] - prices[-2]
    if price_diff > threshold:
        return price_diff - transaction_cost
    elif price_diff < -threshold:
        return -price_diff - transaction_cost
    return 0  # No significant movement



# Risk and Performance Metrics
def performance_metrics(returns):
    if len(returns) == 0:
        return {"Annualized Return": 0, "Volatility": 0, "Sharpe Ratio": 0, "Max Drawdown": 0}
    
    # Calculate daily returns
    daily_return_mean = np.mean(returns)
    daily_volatility = np.std(returns)
    
    # Annualized returns (252 trading days per year)
    annualized_return = daily_return_mean * 252
    annualized_volatility = daily_volatility * np.sqrt(252)
    sharpe_ratio = annualized_return / annualized_volatility if annualized_volatility != 0 else 0
    
    # Calculate max drawdown
    cumulative_returns = np.cumsum(returns)
    peak = np.maximum.accumulate(cumulative_returns)
    max_drawdown = np.min(cumulative_returns - peak)  # Drawdown from peak value

    return {
        "Annualized Return": annualized_return,
        "Volatility": annualized_volatility,
        "Sharpe Ratio": sharpe_ratio,
        "Max Drawdown": max_drawdown
    }




# Daily Returns for Each Strategy
def daily_returns(prices, strategy_func, **kwargs):
    returns = []
    for i in range(1, len(prices)):
        # Get the return for the current day using the strategy function
        daily_return = strategy_func(prices[:i+1], **kwargs)  # We need only the return for the i-th day
        returns.append(daily_return)  # Append the daily return directly, no need for normalization
    return returns




# Compare Strategies
def compare_strategies(prices):
    strategies = {
        "Buy and Hold": buy_and_hold,
        "Momentum": momentum,
        "Mean Reversion": mean_reversion,
        "Scalping": scalping
    }

    metrics = {}
    for name, strategy_func in strategies.items():
        strategy_daily_returns = daily_returns(prices, strategy_func)
        metrics[name] = performance_metrics(strategy_daily_returns)
    
    return metrics



# Main Execution
prices = fetch_stock_data(start="2024-01-01", end="2024-01-03")
print(len(prices))
strategy_metrics = compare_strategies(prices)

# Display Results
for strategy, metrics in strategy_metrics.items():
    print(f"\n📈 {strategy} Strategy Metrics:")
    for key, value in metrics.items():
        print(f"{key}: {value:.4f}")


print(prices[-1])
print(prices[0])