import pandas as pd

df = pd.read_csv("data/egrid2016.csv")
print(df.describe())

import matplotlib.pyplot as plt

plt.scatter(df["CAPFAC"], df["PLNGENAN"])
plt.xlabel("CAPFAC")
plt.ylabel("PLNGENAN")
plt.title("Scatter Plot of CAPFAC and PLNGENAN")
plt.show()
plt.savefig("egrid.png")

from ydata_profiling import ProfileReport
profile = ProfileReport(df, title="profile report")
profile.to_notebook_iframe()
profile.to_file("egrid_data.html")
