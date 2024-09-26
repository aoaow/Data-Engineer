profile reportToggle navigation[profile report](#top)* [Overview](#overview)
* [Variables](#variables-dropdown)
* [Interactions](#interactions)
* [Correlations](#correlations_tab)
* [Missing values](#missing)
* [Sample](#sample)
# Overview

Brought to you by [YData](https://ydata.ai/?utm_source=opensource&utm_medium=ydataprofiling&utm_campaign=report)

* [Overview](#overview-dataset_overview)
* [Alerts 11](#overview-alerts)
* [Reproduction](#overview-reproduction)

Dataset statistics



| Number of variables | 8 |
| --- | --- |
| Number of observations | 9709 |
| Missing cells | 5876 |
| Missing cells (%) | 7\.6% |
| Duplicate rows | 0 |
| Duplicate rows (%) | 0\.0% |
| Total size in memory | 606\.9 KiB |
| Average record size in memory | 64\.0 B |

Variable types



| Numeric | 4 |
| --- | --- |
| Text | 3 |
| Categorical | 1 |



Alerts

| [`CAPFAC`](#pp_var_-8750263118712590403) is highly overall correlated with `PLNGENAN` | High correlation |
| [`NAMEPCAP`](#pp_var_4113971882481861012) is highly overall correlated with `PLNGENAN` | High correlation |
| [`PLNGENAN`](#pp_var_7602518011428172269) is highly overall correlated with `CAPFAC` and 1 other fields | High correlation |
| [`CAPFAC`](#pp_var_-8750263118712590403) has 1671 (17\.2%) missing values | Missing |
| [`NAMEPCAP`](#pp_var_4113971882481861012) has 438 (4\.5%) missing values | Missing |
| [`PLNGENAN`](#pp_var_7602518011428172269) has 1671 (17\.2%) missing values | Missing |
| [`PLCO2EQA`](#pp_var_3351287638996251187) has 2040 (21\.0%) missing values | Missing |
| [`SEQPLT16`](#pp_var_8008548475385040249) is uniformly distributed | Uniform |
| [`SEQPLT16`](#pp_var_8008548475385040249) has unique values | Unique |
| [`CAPFAC`](#pp_var_-8750263118712590403) has 527 (5\.4%) zeros | Zeros |
| [`PLNGENAN`](#pp_var_7602518011428172269) has 323 (3\.3%) zeros | Zeros |

Reproduction



| Analysis started | 2024\-09\-26 15:25:31\.439621 |
| --- | --- |
| Analysis finished | 2024\-09\-26 15:25:34\.675787 |
| Duration | 3\.24 seconds |
| Software version | [ydata\-profiling vv4\.10\.0](https://github.com/ydataai/ydata-profiling) |
| Download configuration | [config.json](data:text/plain;charset=utf-8,%7B%22title%22%3A%20%22profile%20report%22%2C%20%22dataset%22%3A%20%7B%22description%22%3A%20%22%22%2C%20%22creator%22%3A%20%22%22%2C%20%22author%22%3A%20%22%22%2C%20%22copyright_holder%22%3A%20%22%22%2C%20%22copyright_year%22%3A%20%22%22%2C%20%22url%22%3A%20%22%22%7D%2C%20%22variables%22%3A%20%7B%22descriptions%22%3A%20%7B%7D%7D%2C%20%22infer_dtypes%22%3A%20true%2C%20%22show_variable_description%22%3A%20true%2C%20%22pool_size%22%3A%200%2C%20%22progress_bar%22%3A%20true%2C%20%22vars%22%3A%20%7B%22num%22%3A%20%7B%22quantiles%22%3A%20%5B0.05%2C%200.25%2C%200.5%2C%200.75%2C%200.95%5D%2C%20%22skewness_threshold%22%3A%2020%2C%20%22low_categorical_threshold%22%3A%205%2C%20%22chi_squared_threshold%22%3A%200.999%7D%2C%20%22text%22%3A%20%7B%22length%22%3A%20true%2C%20%22words%22%3A%20true%2C%20%22characters%22%3A%20true%2C%20%22redact%22%3A%20false%7D%2C%20%22cat%22%3A%20%7B%22length%22%3A%20true%2C%20%22characters%22%3A%20true%2C%20%22words%22%3A%20true%2C%20%22cardinality_threshold%22%3A%2050%2C%20%22percentage_cat_threshold%22%3A%200.5%2C%20%22imbalance_threshold%22%3A%200.5%2C%20%22n_obs%22%3A%205%2C%20%22chi_squared_threshold%22%3A%200.999%2C%20%22coerce_str_to_date%22%3A%20false%2C%20%22redact%22%3A%20false%2C%20%22histogram_largest%22%3A%2050%2C%20%22stop_words%22%3A%20%5B%5D%7D%2C%20%22image%22%3A%20%7B%22active%22%3A%20false%2C%20%22exif%22%3A%20true%2C%20%22hash%22%3A%20true%7D%2C%20%22bool%22%3A%20%7B%22n_obs%22%3A%203%2C%20%22imbalance_threshold%22%3A%200.5%2C%20%22mappings%22%3A%20%7B%22t%22%3A%20true%2C%20%22f%22%3A%20false%2C%20%22yes%22%3A%20true%2C%20%22no%22%3A%20false%2C%20%22y%22%3A%20true%2C%20%22n%22%3A%20false%2C%20%22true%22%3A%20true%2C%20%22false%22%3A%20false%7D%7D%2C%20%22path%22%3A%20%7B%22active%22%3A%20false%7D%2C%20%22file%22%3A%20%7B%22active%22%3A%20false%7D%2C%20%22url%22%3A%20%7B%22active%22%3A%20false%7D%2C%20%22timeseries%22%3A%20%7B%22active%22%3A%20false%2C%20%22sortby%22%3A%20null%2C%20%22autocorrelation%22%3A%200.7%2C%20%22lags%22%3A%20%5B1%2C%207%2C%2012%2C%2024%2C%2030%5D%2C%20%22significance%22%3A%200.05%2C%20%22pacf_acf_lag%22%3A%20100%7D%7D%2C%20%22sort%22%3A%20null%2C%20%22missing_diagrams%22%3A%20%7B%22bar%22%3A%20true%2C%20%22matrix%22%3A%20true%2C%20%22heatmap%22%3A%20true%7D%2C%20%22correlation_table%22%3A%20true%2C%20%22correlations%22%3A%20%7B%22auto%22%3A%20%7B%22key%22%3A%20%22auto%22%2C%20%22calculate%22%3A%20true%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%2C%20%22spearman%22%3A%20%7B%22key%22%3A%20%22spearman%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%2C%20%22pearson%22%3A%20%7B%22key%22%3A%20%22pearson%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%2C%20%22phi_k%22%3A%20%7B%22key%22%3A%20%22phi_k%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%2C%20%22cramers%22%3A%20%7B%22key%22%3A%20%22cramers%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%2C%20%22kendall%22%3A%20%7B%22key%22%3A%20%22kendall%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%7D%2C%20%22interactions%22%3A%20%7B%22continuous%22%3A%20true%2C%20%22targets%22%3A%20%5B%5D%7D%2C%20%22categorical_maximum_correlation_distinct%22%3A%20100%2C%20%22memory_deep%22%3A%20false%2C%20%22plot%22%3A%20%7B%22missing%22%3A%20%7B%22force_labels%22%3A%20true%2C%20%22cmap%22%3A%20%22RdBu%22%7D%2C%20%22image_format%22%3A%20%22svg%22%2C%20%22correlation%22%3A%20%7B%22cmap%22%3A%20%22RdBu%22%2C%20%22bad%22%3A%20%22%23000000%22%7D%2C%20%22dpi%22%3A%20800%2C%20%22histogram%22%3A%20%7B%22bins%22%3A%2050%2C%20%22max_bins%22%3A%20250%2C%20%22x_axis_labels%22%3A%20true%2C%20%22density%22%3A%20false%7D%2C%20%22scatter_threshold%22%3A%201000%2C%20%22cat_freq%22%3A%20%7B%22show%22%3A%20true%2C%20%22type%22%3A%20%22bar%22%2C%20%22max_unique%22%3A%2010%2C%20%22colors%22%3A%20null%7D%2C%20%22font_path%22%3A%20null%7D%2C%20%22duplicates%22%3A%20%7B%22head%22%3A%2010%2C%20%22key%22%3A%20%22%23%20duplicates%22%7D%2C%20%22samples%22%3A%20%7B%22head%22%3A%2010%2C%20%22tail%22%3A%2010%2C%20%22random%22%3A%200%7D%2C%20%22reject_variables%22%3A%20true%2C%20%22n_obs_unique%22%3A%2010%2C%20%22n_freq_table_max%22%3A%2010%2C%20%22n_extreme_obs%22%3A%2010%2C%20%22report%22%3A%20%7B%22precision%22%3A%208%7D%2C%20%22html%22%3A%20%7B%22style%22%3A%20%7B%22primary_colors%22%3A%20%5B%22%23377eb8%22%2C%20%22%23e41a1c%22%2C%20%22%234daf4a%22%5D%2C%20%22logo%22%3A%20%22%22%2C%20%22theme%22%3A%20null%7D%2C%20%22navbar_show%22%3A%20true%2C%20%22minify_html%22%3A%20true%2C%20%22use_local_assets%22%3A%20true%2C%20%22inline%22%3A%20true%2C%20%22assets_prefix%22%3A%20null%2C%20%22assets_path%22%3A%20null%2C%20%22full_width%22%3A%20false%7D%2C%20%22notebook%22%3A%20%7B%22iframe%22%3A%20%7B%22height%22%3A%20%22800px%22%2C%20%22width%22%3A%20%22100%25%22%2C%20%22attribute%22%3A%20%22srcdoc%22%7D%7D%7D) |

# Variables

Select ColumnsSEQPLT16PSTATABBPNAMEPLPRMFLCAPFACNAMEPCAPPLNGENANPLCO2EQA[SEQPLT16](#pp_var_8008548475385040249)  
Real number (ℝ)

`UNIFORM`  `UNIQUE`  



| Distinct | 9709 |
| --- | --- |
| Distinct (%) | 100\.0% |
| Missing | 0 |
| Missing (%) | 0\.0% |
| Infinite | 0 |
| Infinite (%) | 0\.0% |
| Mean | 4855 |



| Minimum | 1 |
| --- | --- |
| Maximum | 9709 |
| Zeros | 0 |
| Zeros (%) | 0\.0% |
| Negative | 0 |
| Negative (%) | 0\.0% |
| Memory size | 76\.0 KiB |

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:34\.824544image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ More details * [Statistics](#8008548475385040249bottom-8008548475385040249statistics)
* [Histogram](#8008548475385040249bottom-8008548475385040249histogram)
* [Common values](#8008548475385040249bottom-8008548475385040249common_values)
* [Extreme values](#8008548475385040249bottom-8008548475385040249extreme_values)

Quantile statistics



| Minimum | 1 |
| --- | --- |
| 5\-th percentile | 486\.4 |
| Q1 | 2428 |
| median | 4855 |
| Q3 | 7282 |
| 95\-th percentile | 9223\.6 |
| Maximum | 9709 |
| Range | 9708 |
| Interquartile range (IQR) | 4854 |

Descriptive statistics



| Standard deviation | 2802\.8912 |
| --- | --- |
| Coefficient of variation (CV) | 0\.57732054 |
| Kurtosis | \-1\.2 |
| Mean | 4855 |
| Median Absolute Deviation (MAD) | 2427 |
| Skewness | 0 |
| Sum | 47137195 |
| Variance | 7856199\.2 |
| Monotonicity | Strictly increasing |

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:35\.079207image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/**Histogram with fixed size bins** (bins\=50\) 

| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1 | 1 | \< 0\.1% |
| 6468 | 1 | \< 0\.1% |
| 6470 | 1 | \< 0\.1% |
| 6471 | 1 | \< 0\.1% |
| 6472 | 1 | \< 0\.1% |
| 6473 | 1 | \< 0\.1% |
| 6474 | 1 | \< 0\.1% |
| 6475 | 1 | \< 0\.1% |
| 6476 | 1 | \< 0\.1% |
| 6477 | 1 | \< 0\.1% |
| Other values (9699\) | 9699 | 99\.9% |

* [Minimum 10 values](#8008548475385040249extreme_values-8008548475385040249firstn)
* [Maximum 10 values](#8008548475385040249extreme_values-8008548475385040249lastn)



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1 | 1 | \< 0\.1% |
| 2 | 1 | \< 0\.1% |
| 3 | 1 | \< 0\.1% |
| 4 | 1 | \< 0\.1% |
| 5 | 1 | \< 0\.1% |
| 6 | 1 | \< 0\.1% |
| 7 | 1 | \< 0\.1% |
| 8 | 1 | \< 0\.1% |
| 9 | 1 | \< 0\.1% |
| 10 | 1 | \< 0\.1% |



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 9709 | 1 | \< 0\.1% |
| 9708 | 1 | \< 0\.1% |
| 9707 | 1 | \< 0\.1% |
| 9706 | 1 | \< 0\.1% |
| 9705 | 1 | \< 0\.1% |
| 9704 | 1 | \< 0\.1% |
| 9703 | 1 | \< 0\.1% |
| 9702 | 1 | \< 0\.1% |
| 9701 | 1 | \< 0\.1% |
| 9700 | 1 | \< 0\.1% |

[PSTATABB](#pp_var_-3268110645972725649)  
Text



| Distinct | 51 |
| --- | --- |
| Distinct (%) | 0\.5% |
| Missing | 0 |
| Missing (%) | 0\.0% |
| Memory size | 76\.0 KiB |

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:35\.312593image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ More details * [Overview](#-3268110645972725649bottom--3268110645972725649overview)
* [Words](#-3268110645972725649bottom--3268110645972725649word)
* [Characters](#-3268110645972725649bottom--3268110645972725649characters)

Length



| Max length | 2 |
| --- | --- |
| Median length | 2 |
| Mean length | 2 |
| Min length | 2 |

Characters and Unicode



| Total characters | 19418 |
| --- | --- |
| Distinct characters | 24 |
| Distinct categories | 1 [?](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category "Unicode categories (click for more information)") |
| Distinct scripts | 1 [?](https://en.wikipedia.org/wiki/Script_(Unicode)#List_of_scripts_in_Unicode "Unicode scripts (click for more information)") |
| Distinct blocks | 1 [?](https://en.wikipedia.org/wiki/Unicode_block "Unicode blocks (click for more information)") |

 The Unicode Standard assigns character properties to each code point, which can be used to analyse textual variables. Unique



| Unique | 0 ? |
| --- | --- |
| Unique (%) | 0\.0% |

Sample



| 1st row | AK |
| --- | --- |
| 2nd row | AK |
| 3rd row | AK |
| 4th row | AK |
| 5th row | AK |



| Value | Count | Frequency (%) |
| --- | --- | --- |
| ca | 1520 | 15\.7% |
| nc | 763 | 7\.9% |
| tx | 541 | 5\.6% |
| ny | 440 | 4\.5% |
| mn | 383 | 3\.9% |
| ma | 357 | 3\.7% |
| nj | 277 | 2\.9% |
| pa | 261 | 2\.7% |
| ia | 259 | 2\.7% |
| mi | 254 | 2\.6% |
| Other values (41\) | 4654 | 47\.9% |

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:35\.742316image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/* [Characters](#-3268110645972725649unicode--3268110645972725649characters)
* [Categories](#-3268110645972725649unicode--3268110645972725649categories)
* [Scripts](#-3268110645972725649unicode--3268110645972725649scripts)
* [Blocks](#-3268110645972725649unicode--3268110645972725649blocks)

#### Most occurring characters



| Value | Count | Frequency (%) |
| --- | --- | --- |
| A | 3433 | 17\.7% |
| C | 2701 | 13\.9% |
| N | 2556 | 13\.2% |
| M | 1589 | 8\.2% |
| I | 1394 | 7\.2% |
| T | 998 | 5\.1% |
| O | 815 | 4\.2% |
| L | 639 | 3\.3% |
| Y | 575 | 3\.0% |
| X | 541 | 2\.8% |
| Other values (14\) | 4177 | 21\.5% |

#### Most occurring categories



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 19418 | 100\.0% |

#### Most frequent character per category

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| A | 3433 | 17\.7% |
| C | 2701 | 13\.9% |
| N | 2556 | 13\.2% |
| M | 1589 | 8\.2% |
| I | 1394 | 7\.2% |
| T | 998 | 5\.1% |
| O | 815 | 4\.2% |
| L | 639 | 3\.3% |
| Y | 575 | 3\.0% |
| X | 541 | 2\.8% |
| Other values (14\) | 4177 | 21\.5% |

#### Most occurring scripts



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 19418 | 100\.0% |

#### Most frequent character per script

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| A | 3433 | 17\.7% |
| C | 2701 | 13\.9% |
| N | 2556 | 13\.2% |
| M | 1589 | 8\.2% |
| I | 1394 | 7\.2% |
| T | 998 | 5\.1% |
| O | 815 | 4\.2% |
| L | 639 | 3\.3% |
| Y | 575 | 3\.0% |
| X | 541 | 2\.8% |
| Other values (14\) | 4177 | 21\.5% |

#### Most occurring blocks



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 19418 | 100\.0% |

#### Most frequent character per block

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| A | 3433 | 17\.7% |
| C | 2701 | 13\.9% |
| N | 2556 | 13\.2% |
| M | 1589 | 8\.2% |
| I | 1394 | 7\.2% |
| T | 998 | 5\.1% |
| O | 815 | 4\.2% |
| L | 639 | 3\.3% |
| Y | 575 | 3\.0% |
| X | 541 | 2\.8% |
| Other values (14\) | 4177 | 21\.5% |

[PNAME](#pp_var_-8797806405091613723)  
Text



| Distinct | 9682 |
| --- | --- |
| Distinct (%) | 99\.7% |
| Missing | 0 |
| Missing (%) | 0\.0% |
| Memory size | 76\.0 KiB |

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:36\.159451image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ More details * [Overview](#-8797806405091613723bottom--8797806405091613723overview)
* [Words](#-8797806405091613723bottom--8797806405091613723word)
* [Characters](#-8797806405091613723bottom--8797806405091613723characters)

Length



| Max length | 45 |
| --- | --- |
| Median length | 32 |
| Mean length | 18\.618498 |
| Min length | 2 |

Characters and Unicode



| Total characters | 180767 |
| --- | --- |
| Distinct characters | 74 |
| Distinct categories | 1 [?](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category "Unicode categories (click for more information)") |
| Distinct scripts | 1 [?](https://en.wikipedia.org/wiki/Script_(Unicode)#List_of_scripts_in_Unicode "Unicode scripts (click for more information)") |
| Distinct blocks | 1 [?](https://en.wikipedia.org/wiki/Unicode_block "Unicode blocks (click for more information)") |

 The Unicode Standard assigns character properties to each code point, which can be used to analyse textual variables. Unique



| Unique | 9656 ? |
| --- | --- |
| Unique (%) | 99\.5% |

Sample



| 1st row | 7\-Mile Ridge Wind Project |
| --- | --- |
| 2nd row | Agrium Kenai Nitrogen Operations |
| 3rd row | Alakanuk |
| 4th row | Allison Creek Hydro |
| 5th row | Ambler |



| Value | Count | Frequency (%) |
| --- | --- | --- |
| solar | 1540 | 5\.3% |
| llc | 1119 | 3\.9% |
| wind | 798 | 2\.8% |
| energy | 701 | 2\.4% |
| farm | 538 | 1\.9% |
| plant | 526 | 1\.8% |
| power | 504 | 1\.7% |
| station | 422 | 1\.5% |
| project | 394 | 1\.4% |
| center | 391 | 1\.4% |
| Other values (6951\) | 21976 | 76\.0% |

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:36\.826693image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/* [Characters](#-8797806405091613723unicode--8797806405091613723characters)
* [Categories](#-8797806405091613723unicode--8797806405091613723categories)
* [Scripts](#-8797806405091613723unicode--8797806405091613723scripts)
* [Blocks](#-8797806405091613723unicode--8797806405091613723blocks)

#### Most occurring characters



| Value | Count | Frequency (%) |
| --- | --- | --- |
|  | 19217 | 10\.6% |
| e | 14727 | 8\.1% |
| a | 13386 | 7\.4% |
| r | 12563 | 6\.9% |
| n | 11615 | 6\.4% |
| o | 11333 | 6\.3% |
| i | 9343 | 5\.2% |
| t | 9228 | 5\.1% |
| l | 9085 | 5\.0% |
| s | 4574 | 2\.5% |
| Other values (64\) | 65696 | 36\.3% |

#### Most occurring categories



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 180767 | 100\.0% |

#### Most frequent character per category

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
|  | 19217 | 10\.6% |
| e | 14727 | 8\.1% |
| a | 13386 | 7\.4% |
| r | 12563 | 6\.9% |
| n | 11615 | 6\.4% |
| o | 11333 | 6\.3% |
| i | 9343 | 5\.2% |
| t | 9228 | 5\.1% |
| l | 9085 | 5\.0% |
| s | 4574 | 2\.5% |
| Other values (64\) | 65696 | 36\.3% |

#### Most occurring scripts



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 180767 | 100\.0% |

#### Most frequent character per script

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
|  | 19217 | 10\.6% |
| e | 14727 | 8\.1% |
| a | 13386 | 7\.4% |
| r | 12563 | 6\.9% |
| n | 11615 | 6\.4% |
| o | 11333 | 6\.3% |
| i | 9343 | 5\.2% |
| t | 9228 | 5\.1% |
| l | 9085 | 5\.0% |
| s | 4574 | 2\.5% |
| Other values (64\) | 65696 | 36\.3% |

#### Most occurring blocks



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 180767 | 100\.0% |

#### Most frequent character per block

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
|  | 19217 | 10\.6% |
| e | 14727 | 8\.1% |
| a | 13386 | 7\.4% |
| r | 12563 | 6\.9% |
| n | 11615 | 6\.4% |
| o | 11333 | 6\.3% |
| i | 9343 | 5\.2% |
| t | 9228 | 5\.1% |
| l | 9085 | 5\.0% |
| s | 4574 | 2\.5% |
| Other values (64\) | 65696 | 36\.3% |

[PLPRMFL](#pp_var_-6469024893398103229)  
Categorical



| Distinct | 37 |
| --- | --- |
| Distinct (%) | 0\.4% |
| Missing | 56 |
| Missing (%) | 0\.6% |
| Memory size | 76\.0 KiB |



| SUN | 2475 |
| --- | --- |
| NG | 1973 |
| WAT | 1510 |
| WND | 1208 |
| DFO | 838 |
| Other values (32\) | 1649 |

 More details * [Overview](#-6469024893398103229bottom--6469024893398103229overview)
* [Categories](#-6469024893398103229bottom--6469024893398103229string)
* [Words](#-6469024893398103229bottom--6469024893398103229word)
* [Characters](#-6469024893398103229bottom--6469024893398103229characters)

Length



| Max length | 3 |
| --- | --- |
| Median length | 3 |
| Mean length | 2\.7788252 |
| Min length | 2 |

Characters and Unicode



| Total characters | 26824 |
| --- | --- |
| Distinct characters | 22 |
| Distinct categories | 1 [?](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category "Unicode categories (click for more information)") |
| Distinct scripts | 1 [?](https://en.wikipedia.org/wiki/Script_(Unicode)#List_of_scripts_in_Unicode "Unicode scripts (click for more information)") |
| Distinct blocks | 1 [?](https://en.wikipedia.org/wiki/Unicode_block "Unicode blocks (click for more information)") |

 The Unicode Standard assigns character properties to each code point, which can be used to analyse textual variables. Unique



| Unique | 4 ? |
| --- | --- |
| Unique (%) | \< 0\.1% |

Sample



| 1st row | WND |
| --- | --- |
| 2nd row | NG |
| 3rd row | DFO |
| 4th row | WAT |
| 5th row | DFO |

#### Common Values



| Value | Count | Frequency (%) |
| --- | --- | --- |
| SUN | 2475 | 25\.5% |
| NG | 1973 | 20\.3% |
| WAT | 1510 | 15\.6% |
| WND | 1208 | 12\.4% |
| DFO | 838 | 8\.6% |
| LFG | 404 | 4\.2% |
| BIT | 210 | 2\.2% |
| SUB | 155 | 1\.6% |
| WDS | 149 | 1\.5% |
| OBG | 95 | 1\.0% |
| Other values (27\) | 636 | 6\.6% |

#### Length

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:37\.069581image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Histogram of lengths of the category 

| Value | Count | Frequency (%) |
| --- | --- | --- |
| sun | 2475 | 25\.6% |
| ng | 1973 | 20\.4% |
| wat | 1510 | 15\.6% |
| wnd | 1208 | 12\.5% |
| dfo | 838 | 8\.7% |
| lfg | 404 | 4\.2% |
| bit | 210 | 2\.2% |
| sub | 155 | 1\.6% |
| wds | 149 | 1\.5% |
| obg | 95 | 1\.0% |
| Other values (27\) | 636 | 6\.6% |

* [Characters](#-6469024893398103229unicode--6469024893398103229characters)
* [Categories](#-6469024893398103229unicode--6469024893398103229categories)
* [Scripts](#-6469024893398103229unicode--6469024893398103229scripts)
* [Blocks](#-6469024893398103229unicode--6469024893398103229blocks)

#### Most occurring characters



| Value | Count | Frequency (%) |
| --- | --- | --- |
| N | 5721 | 21\.3% |
| W | 3068 | 11\.4% |
| S | 2859 | 10\.7% |
| U | 2703 | 10\.1% |
| G | 2619 | 9\.8% |
| D | 2199 | 8\.2% |
| T | 1730 | 6\.4% |
| A | 1522 | 5\.7% |
| F | 1281 | 4\.8% |
| O | 1093 | 4\.1% |
| Other values (12\) | 2029 | 7\.6% |

#### Most occurring categories



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 26824 | 100\.0% |

#### Most frequent character per category

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| N | 5721 | 21\.3% |
| W | 3068 | 11\.4% |
| S | 2859 | 10\.7% |
| U | 2703 | 10\.1% |
| G | 2619 | 9\.8% |
| D | 2199 | 8\.2% |
| T | 1730 | 6\.4% |
| A | 1522 | 5\.7% |
| F | 1281 | 4\.8% |
| O | 1093 | 4\.1% |
| Other values (12\) | 2029 | 7\.6% |

#### Most occurring scripts



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 26824 | 100\.0% |

#### Most frequent character per script

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| N | 5721 | 21\.3% |
| W | 3068 | 11\.4% |
| S | 2859 | 10\.7% |
| U | 2703 | 10\.1% |
| G | 2619 | 9\.8% |
| D | 2199 | 8\.2% |
| T | 1730 | 6\.4% |
| A | 1522 | 5\.7% |
| F | 1281 | 4\.8% |
| O | 1093 | 4\.1% |
| Other values (12\) | 2029 | 7\.6% |

#### Most occurring blocks



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 26824 | 100\.0% |

#### Most frequent character per block

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| N | 5721 | 21\.3% |
| W | 3068 | 11\.4% |
| S | 2859 | 10\.7% |
| U | 2703 | 10\.1% |
| G | 2619 | 9\.8% |
| D | 2199 | 8\.2% |
| T | 1730 | 6\.4% |
| A | 1522 | 5\.7% |
| F | 1281 | 4\.8% |
| O | 1093 | 4\.1% |
| Other values (12\) | 2029 | 7\.6% |

[CAPFAC](#pp_var_-8750263118712590403)  
Real number (ℝ)

`HIGH CORRELATION`  `MISSING`  `ZEROS`  



| Distinct | 4392 |
| --- | --- |
| Distinct (%) | 54\.6% |
| Missing | 1671 |
| Missing (%) | 17\.2% |
| Infinite | 0 |
| Infinite (%) | 0\.0% |
| Mean | 0\.27465116 |



| Minimum | 0 |
| --- | --- |
| Maximum | 1\.855 |
| Zeros | 527 |
| Zeros (%) | 5\.4% |
| Negative | 0 |
| Negative (%) | 0\.0% |
| Memory size | 76\.0 KiB |

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:37\.298496image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ More details * [Statistics](#-8750263118712590403bottom--8750263118712590403statistics)
* [Histogram](#-8750263118712590403bottom--8750263118712590403histogram)
* [Common values](#-8750263118712590403bottom--8750263118712590403common_values)
* [Extreme values](#-8750263118712590403bottom--8750263118712590403extreme_values)

Quantile statistics



| Minimum | 0 |
| --- | --- |
| 5\-th percentile | 0 |
| Q1 | 0\.064125 |
| median | 0\.2267 |
| Q3 | 0\.4084 |
| 95\-th percentile | 0\.75789 |
| Maximum | 1\.855 |
| Range | 1\.855 |
| Interquartile range (IQR) | 0\.344275 |

Descriptive statistics



| Standard deviation | 0\.23836596 |
| --- | --- |
| Coefficient of variation (CV) | 0\.86788622 |
| Kurtosis | 0\.19538867 |
| Mean | 0\.27465116 |
| Median Absolute Deviation (MAD) | 0\.1719 |
| Skewness | 0\.84937189 |
| Sum | 2207\.646 |
| Variance | 0\.056818329 |
| Monotonicity | Not monotonic |

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:37\.689489image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/**Histogram with fixed size bins** (bins\=50\) 

| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 527 | 5\.4% |
| 0\.0003 | 47 | 0\.5% |
| 0\.0001 | 45 | 0\.5% |
| 0\.0005 | 43 | 0\.4% |
| 0\.0002 | 41 | 0\.4% |
| 0\.0006 | 37 | 0\.4% |
| 0\.0004 | 34 | 0\.4% |
| 0\.0007 | 32 | 0\.3% |
| 0\.0008 | 27 | 0\.3% |
| 0\.0011 | 24 | 0\.2% |
| Other values (4382\) | 7181 | 74\.0% |
| (Missing) | 1671 | 17\.2% |

* [Minimum 10 values](#-8750263118712590403extreme_values--8750263118712590403firstn)
* [Maximum 10 values](#-8750263118712590403extreme_values--8750263118712590403lastn)



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 527 | 5\.4% |
| 0\.0001 | 45 | 0\.5% |
| 0\.0002 | 41 | 0\.4% |
| 0\.0003 | 47 | 0\.5% |
| 0\.0004 | 34 | 0\.4% |
| 0\.0005 | 43 | 0\.4% |
| 0\.0006 | 37 | 0\.4% |
| 0\.0007 | 32 | 0\.3% |
| 0\.0008 | 27 | 0\.3% |
| 0\.0009 | 23 | 0\.2% |



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1\.855 | 1 | \< 0\.1% |
| 1\.1268 | 1 | \< 0\.1% |
| 1\.0708 | 1 | \< 0\.1% |
| 1\.0238 | 1 | \< 0\.1% |
| 0\.9985 | 1 | \< 0\.1% |
| 0\.9907 | 1 | \< 0\.1% |
| 0\.9891 | 1 | \< 0\.1% |
| 0\.984 | 1 | \< 0\.1% |
| 0\.9817 | 1 | \< 0\.1% |
| 0\.9744 | 1 | \< 0\.1% |

[NAMEPCAP](#pp_var_4113971882481861012)  
Real number (ℝ)

`HIGH CORRELATION`  `MISSING`  



| Distinct | 1919 |
| --- | --- |
| Distinct (%) | 20\.7% |
| Missing | 438 |
| Missing (%) | 4\.5% |
| Infinite | 0 |
| Infinite (%) | 0\.0% |
| Mean | 83\.398285 |



| Minimum | 0 |
| --- | --- |
| Maximum | 999\.6 |
| Zeros | 1 |
| Zeros (%) | \< 0\.1% |
| Negative | 0 |
| Negative (%) | 0\.0% |
| Memory size | 76\.0 KiB |

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:37\.954845image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ More details * [Statistics](#4113971882481861012bottom-4113971882481861012statistics)
* [Histogram](#4113971882481861012bottom-4113971882481861012histogram)
* [Common values](#4113971882481861012bottom-4113971882481861012common_values)
* [Extreme values](#4113971882481861012bottom-4113971882481861012extreme_values)

Quantile statistics



| Minimum | 0 |
| --- | --- |
| 5\-th percentile | 1\.2 |
| Q1 | 3\.2 |
| median | 11 |
| Q3 | 73 |
| 95\-th percentile | 510 |
| Maximum | 999\.6 |
| Range | 999\.6 |
| Interquartile range (IQR) | 69\.8 |

Descriptive statistics



| Standard deviation | 170\.79549 |
| --- | --- |
| Coefficient of variation (CV) | 2\.0479497 |
| Kurtosis | 9\.4430056 |
| Mean | 83\.398285 |
| Median Absolute Deviation (MAD) | 9\.5 |
| Skewness | 3\.0508612 |
| Sum | 773185\.5 |
| Variance | 29171\.1 |
| Monotonicity | Not monotonic |

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:38\.208602image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/**Histogram with fixed size bins** (bins\=50\) 

| Value | Count | Frequency (%) |
| --- | --- | --- |
| 5 | 481 | 5\.0% |
| 2 | 325 | 3\.3% |
| 1 | 283 | 2\.9% |
| 3 | 220 | 2\.3% |
| 1\.5 | 212 | 2\.2% |
| 20 | 185 | 1\.9% |
| 4 | 137 | 1\.4% |
| 10 | 121 | 1\.2% |
| 1\.6 | 121 | 1\.2% |
| 1\.8 | 111 | 1\.1% |
| Other values (1909\) | 7075 | 72\.9% |
| (Missing) | 438 | 4\.5% |

* [Minimum 10 values](#4113971882481861012extreme_values-4113971882481861012firstn)
* [Maximum 10 values](#4113971882481861012extreme_values-4113971882481861012lastn)



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 1 | \< 0\.1% |
| 0\.4 | 1 | \< 0\.1% |
| 0\.7 | 1 | \< 0\.1% |
| 1 | 283 | 2\.9% |
| 1\.1 | 106 | 1\.1% |
| 1\.2 | 106 | 1\.1% |
| 1\.3 | 92 | 0\.9% |
| 1\.4 | 81 | 0\.8% |
| 1\.5 | 212 | 2\.2% |
| 1\.6 | 121 | 1\.2% |



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 999\.6 | 1 | \< 0\.1% |
| 994\.5 | 1 | \< 0\.1% |
| 994\.4 | 1 | \< 0\.1% |
| 991\.5 | 1 | \< 0\.1% |
| 990\.5 | 1 | \< 0\.1% |
| 989 | 1 | \< 0\.1% |
| 988 | 1 | \< 0\.1% |
| 987 | 1 | \< 0\.1% |
| 985 | 1 | \< 0\.1% |
| 982 | 1 | \< 0\.1% |

[PLNGENAN](#pp_var_7602518011428172269)  
Real number (ℝ)

`HIGH CORRELATION`  `MISSING`  `ZEROS`  



| Distinct | 6958 |
| --- | --- |
| Distinct (%) | 86\.6% |
| Missing | 1671 |
| Missing (%) | 17\.2% |
| Infinite | 0 |
| Infinite (%) | 0\.0% |
| Mean | 507007\.05 |



| Minimum | \-768620 |
| --- | --- |
| Maximum | 32377477 |
| Zeros | 323 |
| Zeros (%) | 3\.3% |
| Negative | 177 |
| Negative (%) | 1\.8% |
| Memory size | 76\.0 KiB |

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:38\.453765image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ More details * [Statistics](#7602518011428172269bottom-7602518011428172269statistics)
* [Histogram](#7602518011428172269bottom-7602518011428172269histogram)
* [Common values](#7602518011428172269bottom-7602518011428172269common_values)
* [Extreme values](#7602518011428172269bottom-7602518011428172269extreme_values)

Quantile statistics



| Minimum | \-768620 |
| --- | --- |
| 5\-th percentile | 0 |
| Q1 | 2948\.75 |
| median | 17218 |
| Q3 | 156888 |
| 95\-th percentile | 2906099\.1 |
| Maximum | 32377477 |
| Range | 33146097 |
| Interquartile range (IQR) | 153939\.25 |

Descriptive statistics



| Standard deviation | 1880040\.7 |
| --- | --- |
| Coefficient of variation (CV) | 3\.7081154 |
| Kurtosis | 56\.949835 |
| Mean | 507007\.05 |
| Median Absolute Deviation (MAD) | 17198 |
| Skewness | 6\.6634138 |
| Sum | 4\.0753226 × 109 |
| Variance | 3\.5345529 × 1012 |
| Monotonicity | Not monotonic |

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:38\.717171image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/**Histogram with fixed size bins** (bins\=50\) 

| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 323 | 3\.3% |
| 8 | 17 | 0\.2% |
| 3 | 17 | 0\.2% |
| 1 | 11 | 0\.1% |
| 4 | 11 | 0\.1% |
| 14 | 10 | 0\.1% |
| 7 | 10 | 0\.1% |
| 5 | 9 | 0\.1% |
| 30 | 9 | 0\.1% |
| 57 | 7 | 0\.1% |
| Other values (6948\) | 7614 | 78\.4% |
| (Missing) | 1671 | 17\.2% |

* [Minimum 10 values](#7602518011428172269extreme_values-7602518011428172269firstn)
* [Maximum 10 values](#7602518011428172269extreme_values-7602518011428172269lastn)



| Value | Count | Frequency (%) |
| --- | --- | --- |
| \-768620 | 1 | \< 0\.1% |
| \-751650 | 1 | \< 0\.1% |
| \-703946 | 1 | \< 0\.1% |
| \-572652 | 1 | \< 0\.1% |
| \-498562 | 1 | \< 0\.1% |
| \-489099 | 1 | \< 0\.1% |
| \-360845 | 1 | \< 0\.1% |
| \-349056 | 1 | \< 0\.1% |
| \-317173 | 1 | \< 0\.1% |
| \-284770 | 1 | \< 0\.1% |



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 32377477 | 1 | \< 0\.1% |
| 26214623 | 1 | \< 0\.1% |
| 21875435 | 1 | \< 0\.1% |
| 21694303 | 1 | \< 0\.1% |
| 21177103 | 1 | \< 0\.1% |
| 20506630 | 1 | \< 0\.1% |
| 20385142 | 1 | \< 0\.1% |
| 20297460 | 1 | \< 0\.1% |
| 19884289 | 1 | \< 0\.1% |
| 19860229 | 1 | \< 0\.1% |

[PLCO2EQA](#pp_var_3351287638996251187)  
Text

`MISSING`  



| Distinct | 2604 |
| --- | --- |
| Distinct (%) | 34\.0% |
| Missing | 2040 |
| Missing (%) | 21\.0% |
| Memory size | 76\.0 KiB |

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:39\.138074image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ More details * [Overview](#3351287638996251187bottom-3351287638996251187overview)
* [Words](#3351287638996251187bottom-3351287638996251187word)
* [Characters](#3351287638996251187bottom-3351287638996251187characters)

Length



| Max length | 10 |
| --- | --- |
| Median length | 1 |
| Mean length | 2\.7896727 |
| Min length | 1 |

Characters and Unicode



| Total characters | 21394 |
| --- | --- |
| Distinct characters | 11 |
| Distinct categories | 1 [?](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category "Unicode categories (click for more information)") |
| Distinct scripts | 1 [?](https://en.wikipedia.org/wiki/Script_(Unicode)#List_of_scripts_in_Unicode "Unicode scripts (click for more information)") |
| Distinct blocks | 1 [?](https://en.wikipedia.org/wiki/Unicode_block "Unicode blocks (click for more information)") |

 The Unicode Standard assigns character properties to each code point, which can be used to analyse textual variables. Unique



| Unique | 2434 ? |
| --- | --- |
| Unique (%) | 31\.7% |

Sample



| 1st row | 1,050 |
| --- | --- |
| 2nd row | 0 |
| 3rd row | 1,088 |
| 4th row | 31,903 |
| 5th row | 1,430 |



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 4580 | 59\.7% |
| 4 | 21 | 0\.3% |
| 3 | 21 | 0\.3% |
| 6 | 21 | 0\.3% |
| 5 | 18 | 0\.2% |
| 9 | 14 | 0\.2% |
| 16 | 13 | 0\.2% |
| 2 | 13 | 0\.2% |
| 19 | 12 | 0\.2% |
| 10 | 12 | 0\.2% |
| Other values (2594\) | 2944 | 38\.4% |

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:39\.760001image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/* [Characters](#3351287638996251187unicode-3351287638996251187characters)
* [Categories](#3351287638996251187unicode-3351287638996251187categories)
* [Scripts](#3351287638996251187unicode-3351287638996251187scripts)
* [Blocks](#3351287638996251187unicode-3351287638996251187blocks)

#### Most occurring characters



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 5707 | 26\.7% |
| , | 2688 | 12\.6% |
| 1 | 2110 | 9\.9% |
| 2 | 1654 | 7\.7% |
| 3 | 1495 | 7\.0% |
| 4 | 1393 | 6\.5% |
| 5 | 1385 | 6\.5% |
| 7 | 1309 | 6\.1% |
| 6 | 1259 | 5\.9% |
| 8 | 1200 | 5\.6% |

#### Most occurring categories



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 21394 | 100\.0% |

#### Most frequent character per category

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 5707 | 26\.7% |
| , | 2688 | 12\.6% |
| 1 | 2110 | 9\.9% |
| 2 | 1654 | 7\.7% |
| 3 | 1495 | 7\.0% |
| 4 | 1393 | 6\.5% |
| 5 | 1385 | 6\.5% |
| 7 | 1309 | 6\.1% |
| 6 | 1259 | 5\.9% |
| 8 | 1200 | 5\.6% |

#### Most occurring scripts



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 21394 | 100\.0% |

#### Most frequent character per script

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 5707 | 26\.7% |
| , | 2688 | 12\.6% |
| 1 | 2110 | 9\.9% |
| 2 | 1654 | 7\.7% |
| 3 | 1495 | 7\.0% |
| 4 | 1393 | 6\.5% |
| 5 | 1385 | 6\.5% |
| 7 | 1309 | 6\.1% |
| 6 | 1259 | 5\.9% |
| 8 | 1200 | 5\.6% |

#### Most occurring blocks



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 21394 | 100\.0% |

#### Most frequent character per block

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 5707 | 26\.7% |
| , | 2688 | 12\.6% |
| 1 | 2110 | 9\.9% |
| 2 | 1654 | 7\.7% |
| 3 | 1495 | 7\.0% |
| 4 | 1393 | 6\.5% |
| 5 | 1385 | 6\.5% |
| 7 | 1309 | 6\.1% |
| 6 | 1259 | 5\.9% |
| 8 | 1200 | 5\.6% |

# Interactions

* [SEQPLT16](#interactions-interactions_seqplt16)
* [CAPFAC](#interactions-interactions_capfac)
* [NAMEPCAP](#interactions-interactions_namepcap)
* [PLNGENAN](#interactions-interactions_plngenan)

* [PLNGENAN](#interactions_seqplt16-interactions_seqplt16_plngenan)
* [SEQPLT16](#interactions_seqplt16-interactions_seqplt16_seqplt16)
* [CAPFAC](#interactions_seqplt16-interactions_seqplt16_capfac)
* [NAMEPCAP](#interactions_seqplt16-interactions_seqplt16_namepcap)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:33\.552463image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:31\.755284image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:32\.454835image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:33\.076657image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/* [PLNGENAN](#interactions_capfac-interactions_capfac_plngenan)
* [SEQPLT16](#interactions_capfac-interactions_capfac_seqplt16)
* [CAPFAC](#interactions_capfac-interactions_capfac_capfac)
* [NAMEPCAP](#interactions_capfac-interactions_capfac_namepcap)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:33\.670849image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:32\.083516image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:32\.582207image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:33\.191019image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/* [PLNGENAN](#interactions_namepcap-interactions_namepcap_plngenan)
* [SEQPLT16](#interactions_namepcap-interactions_namepcap_seqplt16)
* [CAPFAC](#interactions_namepcap-interactions_namepcap_capfac)
* [NAMEPCAP](#interactions_namepcap-interactions_namepcap_namepcap)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:33\.797726image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:32\.211905image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:32\.710032image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:33\.314812image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/* [PLNGENAN](#interactions_plngenan-interactions_plngenan_plngenan)
* [SEQPLT16](#interactions_plngenan-interactions_plngenan_seqplt16)
* [CAPFAC](#interactions_plngenan-interactions_plngenan_capfac)
* [NAMEPCAP](#interactions_plngenan-interactions_plngenan_namepcap)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:33\.916497image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:32\.328735image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:32\.830372image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:33\.428107image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/# Correlations

* [Auto](#correlations_tab-auto_diagram_table)

* [Heatmap](#auto_diagram_table-auto_diagram)
* [Table](#auto_diagram_table-auto_table)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:39\.931859image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/

|  | CAPFAC | NAMEPCAP | PLNGENAN | PLPRMFL | SEQPLT16 |
| --- | --- | --- | --- | --- | --- |
| CAPFAC | 1\.000 | 0\.081 | 0\.670 | 0\.313 | 0\.046 |
| NAMEPCAP | 0\.081 | 1\.000 | 0\.700 | 0\.209 | 0\.085 |
| PLNGENAN | 0\.670 | 0\.700 | 1\.000 | 0\.280 | 0\.076 |
| PLPRMFL | 0\.313 | 0\.209 | 0\.280 | 1\.000 | 0\.157 |
| SEQPLT16 | 0\.046 | 0\.085 | 0\.076 | 0\.157 | 1\.000 |

# Missing values

* [Count](#missing-bar)
* [Matrix](#missing-matrix)
* [Heatmap](#missing-heatmap)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:34\.104991image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ A simple visualization of nullity by column. xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:34\.345193image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Nullity matrix is a data\-dense display which lets you quickly visually pick out patterns in data completion. xml version\="1\.0" encoding\="utf\-8" standalone\="no"?2024\-09\-26T15:25:34\.562824image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ The correlation heatmap measures nullity correlation: how strongly the presence or absence of one variable affects the presence of another. # Sample

* [First rows](#sample-head)
* [Last rows](#sample-tail)



|  | SEQPLT16 | PSTATABB | PNAME | PLPRMFL | CAPFAC | NAMEPCAP | PLNGENAN | PLCO2EQA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | AK | 7\-Mile Ridge Wind Project | WND | NaN | 1\.8 | NaN | None |
| 1 | 2 | AK | Agrium Kenai Nitrogen Operations | NG | NaN | 21\.6 | NaN | None |
| 2 | 3 | AK | Alakanuk | DFO | 0\.0533 | 2\.6 | 1213\.0 | 1,050 |
| 3 | 4 | AK | Allison Creek Hydro | WAT | 0\.0155 | 6\.5 | 881\.0 | 0 |
| 4 | 5 | AK | Ambler | DFO | 0\.1366 | 1\.1 | 1316\.0 | 1,088 |
| 5 | 6 | AK | Anchorage 1 | NG | 0\.0424 | 121\.4 | 45082\.0 | 31,903 |
| 6 | 7 | AK | Angoon | DFO | 0\.1030 | 1\.9 | 1714\.0 | 1,430 |
| 7 | 8 | AK | Aniak | DFO | 0\.1148 | 2\.6 | 2614\.0 | 2,167 |
| 8 | 9 | AK | Annex Creek | WAT | 0\.7319 | 4\.0 | 25644\.0 | 0 |
| 9 | 10 | AK | Auke Bay | DFO | 0\.0000 | 36\.2 | 8\.0 | 244 |



|  | SEQPLT16 | PSTATABB | PNAME | PLPRMFL | CAPFAC | NAMEPCAP | PLNGENAN | PLCO2EQA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9699 | 9700 | WY | Swift Creek | WAT | 0\.3376 | 2\.5 | 7393\.0 | 0 |
| 9700 | 9701 | WY | Top of the World Windpower Project | WND | 0\.3579 | 200\.0 | 627052\.0 | 0 |
| 9701 | 9702 | WY | TransAlta Wyoming Wind | WND | 0\.2871 | 144\.0 | 362139\.0 | 0 |
| 9702 | 9703 | WY | Tronox | SUB | 0\.7717 | 41\.0 | 277147\.0 | 149,830 |
| 9703 | 9704 | WY | Two Elk Generating Station | WC | NaN | 320\.0 | NaN | None |
| 9704 | 9705 | WY | Western Sugar Coop \- Torrington | NG | 0\.3935 | 2\.0 | 6894\.0 | 2,378 |
| 9705 | 9706 | WY | Wygen I | SUB | 0\.9012 | 90\.0 | 710524\.0 | 926,216 |
| 9706 | 9707 | WY | Wygen II | SUB | 0\.8824 | 95\.0 | 734354\.0 | 909,355 |
| 9707 | 9708 | WY | Wygen III | SUB | 0\.8086 | 116\.0 | 821699\.0 | 975,147 |
| 9708 | 9709 | WY | Wyodak | SUB | 0\.5835 | 402\.3 | 2056358\.0 | 2,708,380 |

Report generated by [YData](https://ydata.ai/?utm_source=opensource&utm_medium=pandasprofiling&utm_campaign=report).

