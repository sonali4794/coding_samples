import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#we download data on number of unemployed, number of unemployed for less than 5 weeks and number of employed monthly data from CPS from 1996-2022
#calculate outflow and inflow rate for each entry
#plot actual unemployment and flow steady state unemployment for 3 different scenarios
#basic data cleaning
merged = pd.read_csv("Merged.csv")
merged['Time'] = pd.to_datetime(merged['Year'].astype(str)  + merged['Month'], format='%Y%b')
merged['unemp_next_period'] = merged["Unemp_level"].shift(-1)
merged['unemp__less5_next_period'] = merged["Unemp_less_than_5_weeks"].shift(-1)
merged['Unemp_rate'] = merged['Unemp_rate']/100 

#calculate outlow probability
merged['F_t'] = 1 - ((merged['unemp_next_period'] - merged['unemp__less5_next_period'])/merged["Unemp_level"])
merged['F_t'] = merged['F_t'].apply(lambda x: 0 if x < 0 else x)

#calculate outflow rate
merged['f_t'] = -np.log(1 - merged['F_t'])
merged['f_t'] = merged['f_t'].apply(lambda x: 0 if x < 0 else x)
merged['var1'] = 1 - (merged['f_t']/2)
merged['var2'] = merged['Emp_level'] * merged['var1'] 
#calculate inflow rate
merged['s_t'] = merged['unemp__less5_next_period']/merged['var2']
s_bar = merged['s_t'].mean(skipna = True)
f_bar = merged['f_t'].mean(skipna = True)

#calculate flow steady-state unemployment rate
merged['u_t^ss_c'] = merged['s_t']/(merged['s_t'] + merged['f_t'])

#calculate flow steady-state unemployment rate when inflow rate does not vary
merged['u_t^ss_d'] = s_bar/(s_bar + merged['f_t'])

#calculate flow steady-state unemployment rate when outflow rate does not vary
merged['u_t^ss_e'] = merged['s_t']/(merged['s_t'] + f_bar)

#plot outflow rate
fig, ax = plt.subplots(figsize=(12,5))
ax.set_title('Outflow Rate')
ax.set_xlabel('Time')
ax.set_ylabel('f_t')
ax.plot(merged['Time'], merged['f_t'])
ax.yaxis.grid(color='lightgray', linestyle='dashed')
plt.tight_layout()
plt.show()
fig.savefig("part_a.png")

#plot inflow rate
fig, ax = plt.subplots(figsize=(12,5))
ax.set_title('Inflow Rate')
ax.set_xlabel('Time')
ax.set_ylabel('s_t')
ax.plot(merged['Time'], merged['s_t'])
ax.yaxis.grid(color='lightgray', linestyle='dashed')
plt.tight_layout()
plt.show()
fig.savefig("part_b.png")

#plot Actual Unemployment Rate V/S Flow Steady State Unemployment Rate
fig, ax = plt.subplots(figsize=(12,5))
ax.set_title('Actual Unemployment Rate V/S Flow Steady State Unemployment Rate')
ax.set_xlabel('Time')
ax.set_ylabel('Unemployment Rate')
ax.plot(merged['Time'], merged['Unemp_rate'], label = "Actual u")
ax.plot(merged['Time'], merged['u_t^ss_c'], label = "Flow Steady State u")
ax.yaxis.grid(color='lightgray', linestyle='dashed')
ax.legend()
plt.tight_layout()
plt.show()
fig.savefig("part_c.png")

#plot Actual Unemployment Rate V/S Flow Steady State Unemployment Rate with s constant over time
fig, ax = plt.subplots(figsize=(12,5))
ax.set_title('Actual Unemployment Rate V/S Flow Steady State Unemployment Rate with s constant over time')
ax.set_xlabel('Time')
ax.set_ylabel('Unemployment Rate')
ax.plot(merged['Time'], merged['Unemp_rate'], label = "Actual u ")
ax.plot(merged['Time'], merged['u_t^ss_d'], label = "Flow Steady State u {s constant}")
ax.yaxis.grid(color='lightgray', linestyle='dashed')
ax.legend()
plt.tight_layout()
plt.show()
fig.savefig("part_d.png")

#plot Actual Unemployment Rate V/S Flow Steady State Unemployment Rate with f constant over time
fig, ax = plt.subplots(figsize=(12,5))
ax.set_title('Actual Unemployment Rate V/S Flow Steady State Unemployment Rate with f constant over time')
ax.set_xlabel('Time')
ax.set_ylabel('Unemployment Rate')
ax.plot(merged['Time'], merged['Unemp_rate'], label = "Actual u ")
ax.plot(merged['Time'], merged['u_t^ss_e'], label = "Flow Steady State u {f constant}")
ax.yaxis.grid(color='lightgray', linestyle='dashed')
ax.legend()
plt.tight_layout()
plt.show()
fig.savefig("part_e.png")