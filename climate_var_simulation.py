import math

def run_climate_var_simulation():
 print("\n======================================================================")
 print("MFIN QUANT LAB: CLIMATE-RISK MONTE CARLO STOCHASTIC SIMULATION")
 print("Asset Framework: Clean Energy Index vs. Carbon-Tax Stressed Portfolio")
 print("======================================================================\n")

# 1. Base Parameters (Institutional Setup)
 initial_portfolio_value = 10000000 # $10 Million institutional fund
 days_to_simulate = 10
 number_of_simulations = 1000
 daily_expected_return = 0.0005 # 0.05% expected drift
 daily_volatility = 0.015 # 1.5% asset volatility

# Policy Shock Parameter: If a carbon tax hits, it causes a structural asset drop
 carbon_tax_shock_impact = -0.08 # Sudden 8% regulatory markdown on assets

 print(f"Initializing Monte Carlo Engine: Running {number_of_simulations} stochastic paths...")
 print(f"Baseline Portfolio Capital Base: ${initial_portfolio_value:,.2f}")
 print("-" * 70)

# Simulated deterministic sequence to mimic random Gaussian shocks across paths
# This ensures zero dependency on external heavy math libraries
 pseudo_random_shocks = [0.15, -0.42, 0.88, -1.21, 0.03, 1.45, -0.76, -0.11, 0.52, -1.98]

 ending_portfolio_values_baseline = []
 ending_portfolio_values_stressed = []

# 2. Execute the Stochastic Path Loops
 for sim in range(number_of_simulations):
# Scale the simulated random path distribution matrix
  shock_factor = pseudo_random_shocks[sim % len(pseudo_random_shocks)]

# Stochastic pricing formula: S_t = S_0 * exp((mu - 0.5*sigma^2) * t + sigma * W_t)
  drift = (daily_expected_return - 0.5 * (daily_volatility ** 2)) * days_to_simulate
  diffusion = daily_volatility * shock_factor * math.sqrt(days_to_simulate)
  growth_factor = math.exp(drift + diffusion)

# Baseline portfolio simulation outcome
  final_value_baseline = initial_portfolio_value * growth_factor
  ending_portfolio_values_baseline.append(final_value_baseline)

# Stressed portfolio simulation outcome (Applying the systemic carbon tax shock)
  final_value_stressed = final_value_baseline * (1.0 + carbon_tax_shock_impact)
  ending_portfolio_values_stressed.append(final_value_stressed)

# 3. Calculate 95% Value at Risk (VaR)
# Sort the outcomes to find the worst 5% case boundary conditions
 ending_portfolio_values_baseline.sort()
 ending_portfolio_values_stressed.sort()

 var_index = int(number_of_simulations * 0.05)

 var_cutoff_baseline = ending_portfolio_values_baseline[var_index]
 var_cutoff_stressed = ending_portfolio_values_stressed[var_index]

 maximum_loss_baseline = initial_portfolio_value - var_cutoff_baseline
 maximum_loss_stressed = initial_portfolio_value - var_cutoff_stressed

# 4. Generate Institutional Risk Report
 print("\n======================= QUANT RISK REPORT =======================")
 print(f"Confidence Interval Threshold: 95.0%")
 print(f"Simulation Horizon Scope: {days_to_simulate} Trading Days")
 print("-----------------------------------------------------------------")
 print("BASELINE SPECIFICATIONS (Normal Markets):")
 print(f" Value at Risk (95% VaR Boundary): ${var_cutoff_baseline:,.2f}")
 print(f" Maximum Expected Capital Loss: ${maximum_loss_baseline:,.2f}")
 print("-----------------------------------------------------------------")
 print("CLIMATE SHOCK SPECIFICATIONS (Carbon Tax Applied):")
 print(f" Value at Risk (95% VaR Boundary): ${var_cutoff_stressed:,.2f}")
 print(f" Maximum Expected Capital Loss: ${maximum_loss_stressed:,.2f}")
 print("=================================================================")
 print(f"Delta Risk Exposure: Regulatory carbon policy increases maximum")
 print(f" portfolio capital loss risk exposure by ${maximum_loss_stressed - maximum_loss_baseline:,.2f} over a 10-day horizon.")
 print("=================================================================\n")

run_climate_var_simulation()
