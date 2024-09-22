mport polars as pl

df = pl.read_csv("data/egrid2016.csv", ignore_errors=True)

print("Mean for the feature CAPFAC is {}".format(df.select(pl.mean("CAPFAC"))))
print("Median for the feature CAPFAC is {}".format(df.select(pl.median("CAPFAC"))))
print("Std for the feature CAPFAC is {}".format(df.select(pl.std("CAPFAC"))))

# provide visualizations

import matplotlib.pyplot as plt

plt.scatter(df["CAPFAC"], df["PLNGENAN"])
plt.xlabel("CAPFAC")
plt.ylabel("PLNGENAN")
plt.title("Scatter Plot of CAPFAC and PLNGENAN")
plt.show()
plt.savefig("egrid.png")

from ydata_profiling import ProfileReport
# convert pl df to pd df
import pandas as pd
df = df.to_pandas()
profile = ProfileReport(df, title="profile report")
profile.to_notebook_iframe()
profile.to_file("egrid_summary.html")

import markdownify

with open('egrid_summary.html', 'r', encoding="utf-8") as f:
    html_string = f.read()

markdown_string = markdownify.markdownify(html_string, heading_style='ATX')

with open('egrid_summary.md', 'w', encoding="utf-8") as f:
    f.write(markdown_string)