#!/usr/bin/env python
# reducer.py

import sys
import re
import os

items = os.listdir(".")
        
for fileName in items:
    if(fileName.endswith(".bdf")):
        with open("./" + fileName) as infile:
            with open("./" + fileName[:-4] + '.json', 'w+') as outfile:
                # Print the JSON file header markup
                outfile.write("[\n")
                for line in infile:
                    # Parse the elements out of the line
                    linesplit=line.split("/")

                    segmentnumber = linesplit[6]
                    filerange = linesplit[7].rstrip()

                    # Print the markup for each line
                    outfile.write ("{\n")
                    outfile.write ("\"Name\": \"BM_2_" + segmentnumber + "_" + filerange + "\",\n")
                    outfile.write ("\"ActionOnFailure\": \"CONTINUE\",\n")
                    outfile.write ("\"HadoopJarStep\":\n")
                    outfile.write ("{\n")
                    outfile.write ("\"Jar\": \"/home/hadoop/contrib/streaming/hadoop-streaming.jar\",\n")
                    outfile.write ("\"Args\":\n")
                    outfile.write ("[\n")
                    outfile.write ("\"-input\", \"s3://aws-publicdatasets/common-crawl/parse-output/segment/" + segmentnumber + "/" + filerange + "\",\n")
                    outfile.write ("\"-output\", \"s3://da-charles-test-bucket/ScriptOutput/RR_1_" + segmentnumber + "_" + filerange + "\",\n")
                    outfile.write ("\"-mapper\", \"s3://da-charles-test-bucket/PythonScripts/Mapper.py\",\n")
                    outfile.write ("\"-reducer\", \"s3://da-charles-test-bucket/PythonScripts/Reducer.py\",\n")
                    outfile.write ("\"-inputformat\", \"SequenceFileAsTextInputFormat\"\n")
                    outfile.write ("]\n")
                    outfile.write ("}\n")
                    outfile.write ("},\n") 
                # Print the JSON file footer markup
                outfile.write("]\n")

