import pandas as pd

df = pd.read_csv("data/egrid2016.csv")
print(df.describe())

import matplotlib.pyplot as plt

plt.plot(df["PLCO2EQA"], df["PLPRMFL"])
plt.xlabel('PLCO2EQA')
plt.ylabel('PLPRMFL')
plt.title('example plot')
plt.grid(True)
plt.show()

from ydata_profiling import ProfileReport
profile = ProfileReport(df, title="profile report")
profile.to_notebook_ifame()
profile.to_file("egrid_data.pdf")
