---
title: "README"
author: "Chilly Amador"
date: "June 10, 2015"
output: html_document
---

This repository contains a Sentiment Analaysis Project on a big data  for  a smart phone and tablet app developer. This developer is working with a government health agency to create a suite of smart phone medical apps for use by aid workers in developing countries. The government agency will be providing workers with technical support services, but they need to limit the support to a single model of smart phone and operating system. This will also help to limit purchase costs and ensure uniformity when training aid workers to use the device. After completing an initial investigation, the developer has created a short list of devices that are all capable of executing the app suite's functions.

To narrow this list down to one device, I was in charge of conducting a broad-based web sentiment analysis to gain insight into the attitudes toward the devices. 

First, I set up and become familiar with the Amazon Web Services (AWS) computing environment. Next, I used the AWS Elastic Map Reduce (EMR) platform to run a series of Hadoop Streaming jobs that collected large amounts of smart phone-related web pages from a massive repository of web data called Common Crawl. Once this data has been gathered, I compiled it into a Small Data Matrix where I used a machine learning package called WEKA to develop a predictive model that will label the data with the web sites' sentiment toward the devices. I applied the prediction model to the data using Java. 

The files explaining step by step the process are:

1. Big Data / Web Mining: BIGDATA-WEB MINING.md
2. Prediction Model Development: Prediction-Model-Dev.md
3. Sentiment Analysis Prediction: Sentiment-Analysis-Prediction.md

All the other references can be found in PDF files.

This project was completed as part of the Data Analytics/Big Data Certificate at the University of Texas at Austin.
