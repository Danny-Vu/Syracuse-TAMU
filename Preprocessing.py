"""
preprocessing the all_plate_signals dataset -saved as csv for easier storage
df [File, Drugname, Dose, Well, Donor, Plate, Group, 0:799 (signal)]
Python
"""
#Removing noisy baseline signals, only using 400 timepoints for our model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/all_plate_signals.csv')

X = df.iloc[:, 207:607].to_numpy()  # Only signal portion

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

delta_values = X_scaled.max(axis=1) - X_scaled.min(axis=1)

baseline_deltas = delta_values[df['Group'] == 'baseline']
plt.hist(baseline_deltas, bins=50, color='skyblue', edgecolor='black')
plt.xlabel("Delta Value")
plt.ylabel("Frequency")
plt.title("Delta Distribution of 'Baseline' Signals")
plt.grid(True)
plt.show()

for p in [1, 5, 10, 20]:
    val = np.percentile(baseline_deltas, p)
    print(f"{p}th percentile delta: {val:.4f}")

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/all_plate_signals_plate16.csv')

# Extract signal (columns 307 to 506 inclusive)
X = df.iloc[:, 207:607].to_numpy()
X = X.reshape(X.shape[0], -1)

# Extract group labels
y = df['Group'].to_numpy()

# Scale the signals using Min-Max scaling
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Filter out noisy 'baseline' rows based on delta threshold
noise = []
for i, row in enumerate(X_scaled):
    delta = max(row) - min(row)
    if delta <= 0.0515 and y[i] == 'baseline':  # 10th percentile threshold
        noise.append(i)

print(f"Number of noisy baseline signals removed: {len(noise)}")

# Drop noisy rows and reset index
df = df.drop(noise).reset_index(drop=True)

#donor correcting the baseline signals to remove donor-specifc effects
import pandas as pd
!pip install scanpy
import scanpy as sc  # works

baseline_df = df[df['Group'] == 'baseline'].copy()
treated_df = df[df['Group'] == 'treated'].copy()

baseline_features = baseline_df.iloc[:, 8:808]
treated_features = treated_df.iloc[:, 8:808]

baseline_donors = baseline_df['Donor'].values.astype(int)

adata = sc.AnnData(baseline_features)
adata.obs['batch'] = baseline_donors

sc.pp.combat(adata, key='batch')

baseline_corrected = pd.DataFrame(adata.X, columns=baseline_features.columns, index=baseline_df.index)

treated_features_df = treated_features.copy()

filtered_df = pd.concat([baseline_corrected, treated_features_df], axis=0)

filtered_df['Donor'] = pd.concat([baseline_df['Donor'], treated_df['Donor']]).astype(int)
filtered_df['Group'] = pd.concat([baseline_df['Group'], treated_df['Group']])
filtered_df['Drugname'] = pd.concat([baseline_df['Drugname'], treated_df['Drugname']])
filtered_df['Dose'] = pd.concat([baseline_df['Dose'], treated_df['Dose']])
filtered_df['Plate'] = pd.concat([baseline_df['Plate'], treated_df['Plate']])
filtered_df['File'] = pd.concat([baseline_df['File'], treated_df['File']])

filtered_df.reset_index(drop=True, inplace=True)

filtered_df
