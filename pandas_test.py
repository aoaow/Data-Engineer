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
profile.to_file("egrid_summary.html")

import markdownify

with open('egrid_summary.html', 'r') as f:
    html_string = f.read()

markdown_string = markdownify.markdownify(html_string, heading_style='ATX')

with open('egrid_summary.md', 'w') as f:
    f.write(markdown_string)
