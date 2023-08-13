Certainly! Here are 10 AWK-related challenges that vary in difficulty and cover different concepts. These challenges will help you practice AWK for processing the given CSV data.

**Challenge 1: Count the number of trades**
Print the total number of trades (excluding the header).
awk '{SUM+=1} END {print SUM}' sample_data.csv

**Challenge 2: Calculate the average price**
Calculate and print the average price of all trades.
awk -F ',' '{SUM += $4} {COUNT+=1} END {print SUM, COUNT, "Average: ", SUM/COUNT}' sample_data.csv

awk -F',' 'NR > 1 { sum += $4 } END { avg = sum / (NR - 1); print "Average price:", avg }' input.csv



**Challenge 3: Find the highest price**
Determine and print the highest price among all trades.
 awk -F','  'BEGIN {high = 0} NR>1 {if (high<$4) { high=$4; record=$0 }} END {print high, fields= split(record,","); print fields[2]}' sample_data.csv

 awk -F',' 'NR > 1 && $4 > max { max = $4 } END { print "Highest price:", max }' input.csv


**Challenge 4: Extract trade details**
Print the details of all trades where the Symbol is "AAPL".
 awk -F',' '/AAPL/ {print $0}' sample_data.csv
awk -F',' '$2 == "AAPL" { print }' input.csv

 
**Challenge 5: Total quantity for each symbol**
Calculate and print the total quantity for each unique Symbol.
 awk -F',' 'NR> 1 {quantity[$2] += $3} END {for(symbol in quantity) print symbol, quantity[symbol]}' sample_data.csv
 awk -F',' 'NR > 1 { quantities[$2] += $3 } END { for (symbol in quantities) print symbol, quantities[symbol] }' input.csv


**Challenge 6: Group trades by month**
Print the trade details grouped by month, along with the total number of trades in each month.
 awk -F',' 'FNR>1 {split($5,fields,"-");month[fields[2]]+=1} END {for(item in month) print item,":", month[item]}' sample_data.csv
awk -F',' 'NR > 1 { split($5, date, "-"); month = date[2]; trades[month]++; } END { for (m in trades) print "Month", m, "Total trades:", trades[m] }' input.csv

 
**Challenge 7: Find the most traded Symbol**
Determine and print the Symbol that appears the most times in the dataset.
 awk -F',' 'FNR>1 {trade[$2]+=1} END {high = 0; for (sym in trade) {if (trade[sym]> high) {high = trade[sym]; symbol= sym}}; print symbol,high}' sample_data.csv
awk -F',' 'NR > 1 { symbols[$2]++ } END { max = 0; for (symbol in symbols) if (symbols[symbol] > max) { max = symbols[symbol]; most_traded = symbol; } print "Most traded symbol:", most_traded }' input.csv

 
**Challenge 8: Date-based summary**
Print a summary for each month, including the total trades, total quantity, and average price.
awk -F',' 'NR > 1 { split($5, date, "-"); month = date[2]; trades[month]++; quantities[month] += $3; prices[month] += $4; } END { for (m in trades) print "Month", m, "Total trades:", trades[m], "Total quantity:", quantities[m], "Average price:", prices[m] / trades[m] }' input.csv


**Challenge 9: Calculate the moving average**
Calculate and print the 3-day moving average price for each trade.
awk -F',' 'NR > 1 { prices[NR-1] = $4 } NR > 3 { sum = prices[NR-1] + prices[NR-2] + prices[NR-3]; print "Moving average for trade", NR-1, ":", sum / 3 }' input.csv



**Challenge 10: Complex calculations**
Calculate and print the average trade quantity and average trade price for each Symbol separately. Additionally, find the Symbol with the highest total trade value (quantity * price).

These challenges cover a range of AWK concepts, from basic calculations and filtering to more complex tasks involving grouping, summarization, and advanced calculations. You can start with the easier challenges and gradually move towards the more challenging ones to improve your AWK skills.
