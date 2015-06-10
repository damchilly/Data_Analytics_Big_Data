---
title: "PREDICTION MODEL DEV"
author: "Chilly Amador"
date: "June 10, 2015"
output: html_document
---

PREDICTION MODELS DEVELOPMENT

Steps to develop a Sentiment Analysis Predictor:


1.  Import Small Data Matrix data into WEKA to use its Explorer graphical user interface and perform exploratory visualization analysis on the classes.

2.	Perform data cleaning and filtering. Change iphonesentiment data and samsunggalaxysentiment to be seen by WEKA as nominal labels rather than continuous numeric values. Change format to ARFF (WEKA native). Sentiment was manually scored for the training set.

3.	Select attributes (features) that predict overall sentiment toward the iPhone and Galaxy. See “Attribute Selection Report”.

4.	Train a model to predict the overall sentiment toward the iPhone or Samsung Galaxy. See “Galaxy Attribute-Training Model Selection” and “Galaxy Attribute-Training Model Selection”.

5.	Tune the classifier you Selected to Predict Sentiment toward Iphone and Samsung Galaxy

6.	Optionally Experiment with other Attribute Selection Methods

