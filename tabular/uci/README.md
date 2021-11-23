# UCI Datasets

## `bank_marketing1.csv`

Bank Marketing

### Citation Request
  This dataset is public available for research. The details are described in [Moro et al., 2011]. 
  Please include this citation if you plan to use this database:

>  [Moro et al., 2011] S. Moro, R. Laureano and P. Cortez. Using Data Mining for Bank Direct Marketing: An Application of the CRISP-DM Methodology. 
>  In P. Novais et al. (Eds.), Proceedings of the European Simulation and Modelling Conference - ESM'2011, pp. 117-121, Guimarães, Portugal, October, 2011. EUROSIS.
>
>  Available at:
>  - [pdf](http://hdl.handle.net/1822/14838)
>  - [bib](http://www3.dsi.uminho.pt/pcortez/bib/2011-esm-1.txt)

### Sources
   Created by: Paulo Cortez (Univ. Minho) and Sérgio Moro (ISCTE-IUL) @ 2012
   
### Past Usage

  The full dataset was described and analyzed in:

  S. Moro, R. Laureano and P. Cortez. Using Data Mining for Bank Direct Marketing: An Application of the CRISP-DM Methodology. 
  In P. Novais et al. (Eds.), Proceedings of the European Simulation and Modelling Conference - ESM'2011, pp. 117-121, Guimarães, 
  Portugal, October, 2011. EUROSIS.

### Relevant Information

   The data is related with direct marketing campaigns of a Portuguese banking institution. 
   The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, 
   in order to access if the product (bank term deposit) would be (or not) subscribed. 

   There are two datasets: 
   
   1. bank-full.csv with all examples, ordered by date (from May 2008 to November 2010).
   2. bank.csv with 10% of the examples (4521), randomly selected from bank-full.csv.
   
   The smallest dataset is provided to test more computationally demanding machine learning algorithms (e.g. SVM).

   The classification goal is to predict if the client will subscribe a term deposit (variable y).

### Number of Instances
45211 for bank-full.csv (4521 for bank.csv)

### Number of Attributes
16 + output attribute.

### Attribute information

For more information, read [Moro et al., 2011].

Input variables:

- bank client data:
  - 1 - age (numeric)
  - 2 - job : type of job (categorical: "admin.","unknown","unemployed","management","housemaid","entrepreneur","student","blue-collar","self-employed","retired","technician","services") 
  - 3 - marital : marital status (categorical: "married","divorced","single"; note: "divorced" means divorced or widowed)
  - 4 - education (categorical: "unknown","secondary","primary","tertiary")
  - 5 - default: has credit in default? (binary: "yes","no")
  - 6 - balance: average yearly balance, in euros (numeric) 
  - 7 - housing: has housing loan? (binary: "yes","no")
  - 8 - loan: has personal loan? (binary: "yes","no")
- related with the last contact of the current campaign:
  - 9 - contact: contact communication type (categorical: "unknown","telephone","cellular") 
  - 10 - day: last contact day of the month (numeric)
  - 11 - month: last contact month of year (categorical: "jan", "feb", "mar", ..., "nov", "dec")
  - 12 - duration: last contact duration, in seconds (numeric)
- other attributes:
  - 13 - campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)
  - 14 - pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric, -1 means client was not previously contacted)
  - 15 - previous: number of contacts performed before this campaign and for this client (numeric)
  - 16 - poutcome: outcome of the previous marketing campaign (categorical: "unknown","other","failure","success")
- Output variable (desired target):
  - 17 - y: has the client subscribed a term deposit? (binary: "yes","no")

### Missing Attribute Values
None

## `bank_marketing2.csv`

Bank Marketing (with social/economic context)

### Citation Request

This dataset is publicly available for research. The details are described in [Moro et al., 2014]. 
Please include this citation if you plan to use this database:

>  [Moro et al., 2014] S. Moro, P. Cortez and P. Rita. A Data-Driven Approach to Predict the Success of Bank Telemarketing. Decision Support Systems, In press, http://dx.doi.org/10.1016/j.dss.2014.03.001
>
>  Available at:
>  - [pdf](http://dx.doi.org/10.1016/j.dss.2014.03.001)
>  - [bib](http://www3.dsi.uminho.pt/pcortez/bib/2014-dss.txt)

### Sources
   Created by: Sérgio Moro (ISCTE-IUL), Paulo Cortez (Univ. Minho) and Paulo Rita (ISCTE-IUL) @ 2014
   
### Past Usage

  The full dataset (bank-additional-full.csv) was described and analyzed in:

  S. Moro, P. Cortez and P. Rita. A Data-Driven Approach to Predict the Success of Bank Telemarketing. Decision Support Systems (2014), doi:10.1016/j.dss.2014.03.001.
 
### Relevant Information

   This dataset is based on "Bank Marketing" UCI dataset (please check the description at: http://archive.ics.uci.edu/ml/datasets/Bank+Marketing).
   The data is enriched by the addition of five new social and economic features/attributes (national wide indicators from a ~10M population country), published by the Banco de Portugal and publicly available at: https://www.bportugal.pt/estatisticasweb.
   This dataset is almost identical to the one used in [Moro et al., 2014] (it does not include all attributes due to privacy concerns). 
   Using the rminer package and R tool (http://cran.r-project.org/web/packages/rminer/), we found that the addition of the five new social and economic attributes (made available here) lead to substantial improvement in the prediction of a success, even when the duration of the call is not included. Note: the file can be read in R using: d=read.table("bank-additional-full.csv",header=TRUE,sep=";")
   
   The zip file includes two datasets: 
   
   1. bank-additional-full.csv with all examples, ordered by date (from May 2008 to November 2010).
   2. bank-additional.csv with 10% of the examples (4119), randomly selected from bank-additional-full.csv.
   
   The smallest dataset is provided to test more computationally demanding machine learning algorithms (e.g., SVM).

   The binary classification goal is to predict if the client will subscribe a bank term deposit (variable y).

### Number of Instances
41188 for bank-additional-full.csv

### Number of Attributes
20 + output attribute.

### Attribute information

For more information, read [Moro et al., 2014].

Input variables:

- bank client data:
  - 1 - age (numeric)
  - 2 - job : type of job (categorical: "admin.","blue-collar","entrepreneur","housemaid","management","retired","self-employed","services","student","technician","unemployed","unknown")
  - 3 - marital : marital status (categorical: "divorced","married","single","unknown"; note: "divorced" means divorced or widowed)
  - 4 - education (categorical: "basic.4y","basic.6y","basic.9y","high.school","illiterate","professional.course","university.degree","unknown")
  - 5 - default: has credit in default? (categorical: "no","yes","unknown")
  - 6 - housing: has housing loan? (categorical: "no","yes","unknown")
  - 7 - loan: has personal loan? (categorical: "no","yes","unknown")
- related with the last contact of the current campaign:
  - 8 - contact: contact communication type (categorical: "cellular","telephone") 
  - 9 - month: last contact month of year (categorical: "jan", "feb", "mar", ..., "nov", "dec")
  - 10 - day_of_week: last contact day of the week (categorical: "mon","tue","wed","thu","fri")
  - 11 - duration: last contact duration, in seconds (numeric). Important note:  this attribute highly affects the output target (e.g., if duration=0 then y="no"). Yet, the duration is not known before a call is performed. Also, after the end of the call y is obviously known. Thus, this input should only be included for benchmark purposes and should be discarded if the intention is to have a realistic predictive model.
- other attributes:
  - 12 - campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)
  - 13 - pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric; 999 means client was not previously contacted)
  - 14 - previous: number of contacts performed before this campaign and for this client (numeric)
  - 15 - poutcome: outcome of the previous marketing campaign (categorical: "failure","nonexistent","success")
- social and economic context attributes
  - 16 - emp.var.rate: employment variation rate - quarterly indicator (numeric)
  - 17 - cons.price.idx: consumer price index - monthly indicator (numeric)     
  - 18 - cons.conf.idx: consumer confidence index - monthly indicator (numeric)     
  - 19 - euribor3m: euribor 3 month rate - daily indicator (numeric)
  - 20 - nr.employed: number of employees - quarterly indicator (numeric)
- Output variable (desired target):
  - 21 - y: has the client subscribed a term deposit? (binary: "yes","no")

### Missing Attribute Values
There are several missing values in some categorical attributes, all coded with the "unknown" label. These missing values can be treated as a possible class label or using deletion or imputation techniques.


## `creditcard_default.csv`

Predicting Credit Defaults

### Citation Request

> Yeh, I. C., & Lien, C. H. (2009). The comparisons of data mining techniques for the predictive accuracy of probability of default of credit card clients. Expert Systems with Applications, 36(2), 2473-2480.


### Source

Name: I-Cheng Yeh 
email addresses: (1) icyeh '@' chu.edu.tw (2) 140910 '@' mail.tku.edu.tw 
institutions: (1) Department of Information Management, Chung Hua University, Taiwan. (2) Department of Civil Engineering, Tamkang University, Taiwan. 
other contact information: 886-2-26215656 ext. 3181 


### Data Set Information

This research aimed at the case of customers' default payments in Taiwan and compares the predictive accuracy of probability of default among six data mining methods. From the perspective of risk management, the result of predictive accuracy of the estimated probability of default will be more valuable than the binary result of classification - credible or not credible clients. Because the real probability of default is unknown, this study presented the novel â€œSorting Smoothing Methodâ€ to estimate the real probability of default. With the real probability of default as the response variable (Y), and the predictive probability of default as the independent variable (X), the simple linear regression result (Y = A + BX) shows that the forecasting model produced by artificial neural network has the highest coefficient of determination; its regression intercept (A) is close to zero, and regression coefficient (B) to one. Therefore, among the six data mining techniques, artificial neural network is the only one that can accurately estimate the real probability of default.


### Attribute Information

This research employed a binary variable, default payment (Yes = 1, No = 0), as the response variable. This study reviewed the literature and used the following 23 variables as explanatory variables: 
ID: Identifier.
LIMIT_BAL: Amount of the given credit (NT dollar): it includes both the individual consumer credit and his/her family (supplementary) credit. 
SEX: Gender (1 = male; 2 = female). 
EDUCATION: Education (1 = graduate school; 2 = university; 3 = high school; 4 = others). 
MARRIAGE: Marital status (1 = married; 2 = single; 3 = others). 
AGE: Age (year). 
PAY_1,PAY_2,PAY_3,PAY_4,PAY_5,PAY_6: History of past payment. We tracked the past monthly payment records (from April to September, 2005) as follows: X6 = the repayment status in September, 2005; X7 = the repayment status in August, 2005; . . .;X11 = the repayment status in April, 2005. The measurement scale for the repayment status is: -1 = pay duly; 1 = payment delay for one month; 2 = payment delay for two months; . . .; 8 = payment delay for eight months; 9 = payment delay for nine months and above. 
BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6: Amount of bill statement (NT dollar). X12 = amount of bill statement in September, 2005; X13 = amount of bill statement in August, 2005; . . .; X17 = amount of bill statement in April, 2005. 
PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6: Amount of previous payment (NT dollar). X18 = amount paid in September, 2005; X19 = amount paid in August, 2005; . . .;X23 = amount paid in April, 2005.
default payment next month: Target.

## `onlinenews_popularity.csv`

Online News Popularity

### Citation Request
 
 Please include this citation if you plan to use this database: 
 
>    K. Fernandes, P. Vinagre and P. Cortez. A Proactive Intelligent Decision
>    Support System for Predicting the Popularity of Online News. Proceedings
>    of the 17th EPIA 2015 - Portuguese Conference on Artificial Intelligence,
>    September, Coimbra, Portugal.

### Source Information
- Creators: 
  - Kelwin Fernandes (kafc ‘@’ inesctec.pt, kelwinfc ’@’ gmail.com)
  - Pedro Vinagre (pedro.vinagre.sousa ’@’ gmail.com)
  - Pedro Sernadela
- Donor: Kelwin Fernandes (kafc ’@’ inesctec.pt, kelwinfc '@' gmail.com)
- Date: May, 2015

### Past Usage
1. K. Fernandes, P. Vinagre and P. Cortez. A Proactive Intelligent Decision Support System for Predicting the Popularity of Online News. Proceedings of the 17th EPIA 2015 - Portuguese Conference on Artificial Intelligence, September, Coimbra, Portugal.

Results: 
- Binary classification as popular vs unpopular using a decision threshold of 1400 social interactions.
  - Experiments with different models: Random Forest (best model), Adaboost, SVM, KNN and Naïve Bayes.
  - Recorded 67% of accuracy and 0.73 of AUC.
- Predicted attribute: online news popularity (boolean)

### Relevant Information
- The articles were published by Mashable (www.mashable.com) and their content as the rights to reproduce it belongs to them. Hence, this dataset does not share the original content but some statistics associated with it. The original content be publicly accessed and retrieved using the provided urls.
- Acquisition date: January 8, 2015
- The estimated relative performance values were estimated by the authors using a Random Forest classifier and a rolling windows as assessment method.  See their article for more details on how the relative performance values were set.

### Number of Instances
39797 

### Attribute Information

Number of Attributes: 61 (58 predictive attributes, 2 non-predictive, 1 goal field)

| Number | Attribute                 | Description |
| :----: | :---                      | :---        |
| 0 | url                            | URL of the article |
| 1 | timedelta                      | Days between the article publication and the dataset acquisition |
| 2 | n_tokens_title                 | Number of words in the title |
| 3 | n_tokens_content               | Number of words in the content |
| 4 | n_unique_tokens                | Rate of unique words in the content |
| 5 | n_non_stop_words               | Rate of non-stop words in the content |
| 6 | n_non_stop_unique_tokens       | Rate of unique non-stop words in the content |
| 7 | num_hrefs                      | Number of links |
| 8 | num_self_hrefs                 | Number of links to other articles published by Mashable |
| 9 | num_imgs                       | Number of images |
| 10 | num_videos                    | Number of videos |
| 11 | average_token_length          | Average length of the words in the content |
| 12 | num_keywords                  | Number of keywords in the metadata |
| 13 | data_channel_is_lifestyle     | Is data channel 'Lifestyle'? |
| 14 | data_channel_is_entertainment | Is data channel 'Entertainment'? |
| 15 | data_channel_is_bus           | Is data channel 'Business'? |
| 16 | data_channel_is_socmed        | Is data channel 'Social Media'? |
| 17 | data_channel_is_tech          | Is data channel 'Tech'? |
| 18 | data_channel_is_world         | Is data channel 'World'? |
| 19 | kw_min_min                    | Worst keyword (min. shares) |
| 20 | kw_max_min                    | Worst keyword (max. shares) |
| 21 | kw_avg_min                    | Worst keyword (avg. shares) |
| 22 | kw_min_max                    | Best keyword (min. shares) |
| 23 | kw_max_max                    | Best keyword (max. shares) |
| 24 | kw_avg_max                    | Best keyword (avg. shares) |
| 25 | kw_min_avg                    | Avg. keyword (min. shares) |
| 26 | kw_max_avg                    | Avg. keyword (max. shares) |
| 27 | kw_avg_avg                    | Avg. keyword (avg. shares) |
| 28 | self_reference_min_shares     | Min. shares of referenced articles in Mashable |
| 29 | self_reference_max_shares     | Max. shares of referenced articles in Mashable |
| 30 | self_reference_avg_sharess    | Avg. shares of referenced articles in Mashable |
| 31 | weekday_is_monday             | Was the article published on a Monday? |
| 32 | weekday_is_tuesday            | Was the article published on a Tuesday? |
| 33 | weekday_is_wednesday          | Was the article published on a Wednesday? |
| 34 | weekday_is_thursday           | Was the article published on a Thursday? |
| 35 | weekday_is_friday             | Was the article published on a Friday? |
| 36 | weekday_is_saturday           | Was the article published on a Saturday? |
| 37 | weekday_is_sunday             | Was the article published on a Sunday? |
| 38 | is_weekend                    | Was the article published on the weekend? |
| 39 | LDA_00                        | Closeness to LDA topic 0 |
| 40 | LDA_01                        | Closeness to LDA topic 1 |
| 41 | LDA_02                        | Closeness to LDA topic 2 |
| 42 | LDA_03                        | Closeness to LDA topic 3 |
| 43 | LDA_04                        | Closeness to LDA topic 4 |
| 44 | global_subjectivity           | Text subjectivity |
| 45 | global_sentiment_polarity     | Text sentiment polarity |
| 46 | global_rate_positive_words    | Rate of positive words in the content |
| 47 | global_rate_negative_words    | Rate of negative words in the content |
| 48 | rate_positive_words           | Rate of positive words among non-neutral tokens |
| 49 | rate_negative_words           | Rate of negative words among non-neutral tokens |
| 50 | avg_positive_polarity         | Avg. polarity of positive words |
| 51 | min_positive_polarity         | Min. polarity of positive words |
| 52 | max_positive_polarity         | Max. polarity of positive words |
| 53 | avg_negative_polarity         | Avg. polarity of negative  words |
| 54 | min_negative_polarity         | Min. polarity of negative  words |
| 55 | max_negative_polarity         | Max. polarity of negative  words |
| 56 | title_subjectivity            | Title subjectivity |
| 57 | title_sentiment_polarity      | Title polarity |
| 58 | abs_title_subjectivity        | Absolute subjectivity level |
| 59 | abs_title_sentiment_polarity  | Absolute polarity level |
| 60 | shares                        | Number of shares (target) |

### Missing Attribute Values
None

### Class Distribution

The class value (shares) is continuously valued. We transformed the task into a binary task using a decision threshold of 1400.

| Shares Value Range | Number of Instances in Range |
| :----------------: | :--------------------------: |
| <  1400            | 18490                        |
| >= 1400            | 21154                        |


## `wine_quality-red.csv` & `wine_quality-white.csv`

Wine Quality

### Citation Request
  This dataset is public available for research. The details are described in [Cortez et al., 2009]. 
  Please include this citation if you plan to use this database:

>  P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis. 
>  Modeling wine preferences by data mining from physicochemical properties.
>  In Decision Support Systems, Elsevier, 47(4):547-553. ISSN: 0167-9236.
>
>  Available at: 
>  - [@Elsevier](http://dx.doi.org/10.1016/j.dss.2009.05.016)
>  - [Pre-press (pdf)](http://www3.dsi.uminho.pt/pcortez/winequality09.pdf)
>  - [bib](http://www3.dsi.uminho.pt/pcortez/dss09.bib)

### Sources
Created by: Paulo Cortez (Univ. Minho), Antonio Cerdeira, Fernando Almeida, Telmo Matos and Jose Reis (CVRVV) @ 2009
   
### Past Usage

  P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis. 
  Modeling wine preferences by data mining from physicochemical properties.
  In Decision Support Systems, Elsevier, 47(4):547-553. ISSN: 0167-9236.

  In the above reference, two datasets were created, using red and white wine samples.
  The inputs include objective tests (e.g. PH values) and the output is based on sensory data
  (median of at least 3 evaluations made by wine experts). Each expert graded the wine quality 
  between 0 (very bad) and 10 (very excellent). Several data mining methods were applied to model
  these datasets under a regression approach. The support vector machine model achieved the
  best results. Several metrics were computed: MAD, confusion matrix for a fixed error tolerance (T),
  etc. Also, we plot the relative importances of the input variables (as measured by a sensitivity
  analysis procedure).
 
### Relevant Information

   The two datasets are related to red and white variants of the Portuguese "Vinho Verde" wine.
   For more details, consult: http://www.vinhoverde.pt/en/ or the reference [Cortez et al., 2009].
   Due to privacy and logistic issues, only physicochemical (inputs) and sensory (the output) variables 
   are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.).

   These datasets can be viewed as classification or regression tasks.
   The classes are ordered and not balanced (e.g. there are munch more normal wines than
   excellent or poor ones). Outlier detection algorithms could be used to detect the few excellent
   or poor wines. Also, we are not sure if all input variables are relevant. So
   it could be interesting to test feature selection methods. 

### Number of Instances
red wine - 1599; white wine - 4898. 

### Attribute information

Number of Attributes: 11 + output attribute

Note: several of the attributes may be correlated, thus it makes sense to apply some sort of
feature selection.

For more information, read [Cortez et al., 2009].

- Input variables (based on physicochemical tests):
  - 1 - fixed acidity
  - 2 - volatile acidity
  - 3 - citric acid
  - 4 - residual sugar
  - 5 - chlorides
  - 6 - free sulfur dioxide
  - 7 - total sulfur dioxide
  - 8 - density
  - 9 - pH
  - 10 - sulphates
  - 11 - alcohol
- Output variable (based on sensory data): 
  - 12 - quality (score between 0 and 10)

###  Missing Attribute Values
None
