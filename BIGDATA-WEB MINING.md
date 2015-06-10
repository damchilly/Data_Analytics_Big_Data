---
title: "Big Data - Web Mining for Sentiment Analysis"
author: "Chilly Amador"
date: "April, 2015"
output: html_document
---

BIG DATA / WEB MINING FOR SENTIMENT ANALYSIS

A. CLIENT ENVIRONMENT SET UP

Create a sample Hadoop Streaming Job using AWS-EMR
1.  Create an AWS account.
2.	 Install Ruby to run the Amazon EMR CLI, which will allow to launch and monitor progress of running job flows, and to create additional custom functionality around job flows (such as sequences with multiple processing steps, scheduling, workflow, or monitoring).
4.	Install Amazon's Command Line Interface.This allows to programmatically launch and monitor progress of running job flows, and to create additional custom functionality around job flows.
5.	Configure Credentials.Your credentials are used to calculate the signature value for every request.
6.	Install Simple Storage Service (S3) Browser. This will allow to easily explore S3 buckets and upload/download multiple files at a time.
7.	Install WinSCP (or other SFTP/FTP/SCP client).This will allow to transfer files to EC2 instances.

B.  AWS (S3-EMR) ENVIRONMENT SET UP

1.	Setup S3 output location bucket.
2.	Create New Job Flow using EMR console.
3.	 Define job flow. Modify and run AWS sample application “Word Count”. 
4.	Specify parameters.Specify the input, output, mapper, and reducer locations in S3.
5.	Configure EC2 instances.
6.	Configure Advanced Options.Entered EC2 key pair, to use VPC, and your job flow debugging options.
7.	Run job. Once a job has started running, monitor the status of the sample Hadoop Streaming job by returning to the EMR console.
8.	Review Job Output.

C. DATA COLLECTION FOR SENTIMENT ANALYSIS ON IPHONE AND SAMSUNG GALAXY USING AWS-EMR JOB FLOWS

Running Mapper and Reducer Scripts on a Common Crawl Segment Using the EMR Console. 

1.	Identify a valid segment of the Common Crawl.There is often variation between 900 and 6000 textData files from one Segment so each segment has to be checked to prevent EMR jobs from failing by trying to process textData files that don't exist.
2.	Set up S3 buckets: A bucket for mapper and reducer script location with logging, a bucket for output location, and a bucket to hold debugging logs.
3.	Upload the mapper and reducer scripts to an S3 bucket:We are using python scripts to process the sentiment analysis (Mapper.py and Reducer.py) 
4.	Use EMR to create a new job flows:We had a restriction and could only run on a maximum 20 node configuration per region. For this task we used the standard configuration of one master and two core nodes. Define the job flows by:
o	Job flow name.
o	Job type (Streaming).
o	Create individual job flow
5.	Specify parameters:
•	Mapper location
•	Reducer location
•	Input location: Common Crawl keeps their web segment data in an S3 bucket on AWS. Provide the URL of the Amazon S3 bucket that contains the Common Crawl segment files you want to access.
•	Output location
•	Extra arguments: For this Hadoop Streaming job we need to specify that the input files are in sequence file format - a file format used by the Common Crawl to store text data in a compressed manner.
•	Master/core/task instance type: A small instance is the cheapest.
•	Core/task instance count: This number you input here defines the size of your Hadoop network. Increase or decrease the number of core instances depending on the amount of resources you anticipate you will need for a particular job. We used one master node and four core nodes for each job. This configuration was set up using the command line interface and JSON job files.
6.	Configure EC2 instances: These options greatly streamline the job and/or to make it more cost effective. You have the option here to configure the following:
7.	 Enter advanced options:This window allows you to enter advanced details about your job flow, such as whether or not you will be using an EC2 key pair, whether you will use Virtual Public Cloud (VPC), job flow debugging options, and several other options. Be sure to enable debugging and specify an S3 location for debugging information to be stored.
8.	Configure bootstrap actions:Here you are given the option to run bootstrap actions, which allow you to pass a reference to a script stored in Amazon S3. This script can contain configuration settings and arguments related to Hadoop or Elastic MapReduce. Bootstrap actions are run before Hadoop starts and before the node begins processing data. We didn’t use these options.
9.	Review the details of your job flow:In this step to review the details of your job flow and edit as necessary. This is the time to look over the details to ensure they are correct, especially the Hadoop Streaming Script Location, Input Location, and Output Location, as this is where the majority of the problems are likely to occur when attempting to run the scripts.
1.	Run job.
2.	Review output:Sentiment Analysis output was stored at the S3 bucket.

C. DATA COLLECTION FOR SENTIMENT ANALYSIS ON IPHONE AND SAMSUNG GALAXY USING AWS CLI

1.	Select the set of segments to run jobs on by looking in the ValidSegments2 folder in the Common Crawl bucket on S3.
2.	Look at each segment on S3 and make note of the number of nodes.
3.	Plan the number of jobs you want to run. AWS allows to run a maximum of 20 nodes at once in any region (e.g. no more the six jobs with three nodes each at once). We set up to process 20 total segments of Common Crawl data before compiling the data into a Large Data Matrix. We configured five jobs, with four nodes each (three worker nodes and one master). Each of the five jobs processed the files from four segments.
4.	Create five .bdf files (JSON). Each file contained a list of S3 references to ranges of files that will cover all of the files in the desired segments. The range covered 100 files so that data loss was limited in case of error.
5.	Store a CreateJSON.py Python script into the folder with the .bdf files and run it from the command line.This script generated a .json file for each .bdf, with all of the appropriate markup. The .json file will contain one step per line (or file range) in the .bdf file. At this point, you would have five .json files.If each .json file is going to cover four segments, and each segment has 1000 files (this is highly variable), then each .json file would have 40 steps that will cover 100 files per step.
6.	Run the .json files one by one, directly from the command prompt. A batch file can be used in case we were working with more volume and it will make it easier to kick off all of the runs at once, and to consistently set parameters that all of the runs have in common.
7.	Monitoring jobs and output:The five job flows finished within 19 hours. Some missing files produced non-fatal errors in two job streams, and the jobs continue processing until they reached the end if the segment. 20,000 files were processed. Output was stored in the S3 output bucket.
D. CONSOLIDATE STREAMING JOBS OUTPUTS
You will need to aggregate the results of the streaming jobs you set up. This involves the following steps:
1.	Download your EMR output. Download all of the folders generated by the EMR jobs to a folder location on your local machine. 
2.	Load the ConcatenateFiles.py to concatenate the output obtained by EMR directly and those generated from the AWS CLI. 
3.	Save the MatrixHeader.csv file in the same local folder with the EMR output folders. Because the data matrices are just numbers, this file helps keep track of which column has what label. It is useful when getting a feel for the data, and when you are creating the report.
Run the ConcatenateFiles.py script from terminal with one parameter, which is the file path to the location of the EMR output. The script generated Concatenated.csv, a file containing all of the EMR results merged together (this is the Large Data Matrix).