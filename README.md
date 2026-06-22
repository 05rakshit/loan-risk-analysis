# loan-risk-analysis

**The Problem**
Lenders commonly take raw defaults into consideration to assess loan risk — but this metric is misleading. A loan purpose with the highest number of defaults (600+) can actually be safer than one with lower defaults if its total loan volume is much higher. This analysis identifies which loan purpose carries the true risk of default using default rate rather than raw count.

**Key Findings**
  1. Debt Consolidation has the highest number of defaults (603) but only a 15.2% default rate — close to average
  2. Small Business loans have the highest default rate at 27% — nearly double the dataset average — despite not having the highest raw default count
  3. Small Business loans also carry the highest average interest rate at 14%, confirming that lenders already price in some risk but possibly not enough

**Tools Used**
  1. Python — main language
  2. Pandas — data cleaning and analysis
  3. Tableau — interactive dashboard

**Dashboard**
Live Link -> https://public.tableau.com/views/LoanDataDashboard_17821383468270/LoanRiskAnalysisbyPurpose
