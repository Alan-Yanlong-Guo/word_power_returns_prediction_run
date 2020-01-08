## Introduction
The previous researches on the sentiment analysis of financial documents concerns the use of pre-specified sentiment dictionaries. However, the sentiment scored derived from researches for other purposes might not be suitable in the financial context. This paper uses machine learning techniques to understand the sentimental structure of a text corpus without relying on pre-existing dictionaries. It has three virtues: a) simplicity b) minimal computing power c) ability to generalize to other datasets. 

The aim of the paper is to study the extent to which business news explains and predicts observed asset price variation. The dataset being used is the Dow Jones Newswires. The model is evaluated using back-testing and is shown to outperform similar strategies based on RavenPack. The paper also studies the impacts of “stale” and “fresh” news and the assimilation of news for different stocks. 

**Procedures**

First: Isolate the most relevant features from a large vocabulary of terms using the bag-of-words representation. 

Second: Assign term-specific sentiment weight for the prediction task and taking into account the skewness in terms of frequencies. 

Third: Use the estimated topic model to assign an article-level sentiment score. 

## Methodology 
To establish notation, we use $d_{ij}$ to denote the number of time word j occur in article i, and denote the subset of columns from D using d_i[S] . Each article is tagged with identifier of stock and we only study articles that correspond to a single stock, we label the return of the stock on the publication date as y_i. 


$$
\begin{aligned}
 AR(p): Y_i &= c + \epsilon_i + \phi_i Y_{i-1} \dots \\
 Y_{i} &= c + \phi_i Y_{i-1} \dots
\end{aligned}
$$

$\frac{1}{2x}$
