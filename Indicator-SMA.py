//@version=5

// Creating Simple Moving Average
indicator(title = 'MA', overlay = true)

sma20 = ta.sma(close, 20)
sma50 = ta.sma(close, 50)
sma200 = ta.sma(close, 200)

plot(sma20, color = color.lime)
plot(sma50, color = color.yellow)
plot(sma200, color = color.purple)
