# Report Loan Data with AWS
## Introduction
The applicant  deliver a system built on Amazon Web Services using PySpark , Python. The system completes objectives  with given data to generate loan reports.

### Steps To Complete:

* 1.Using firehose client application , throw the data in s3 bucket gzip format.
* 2.The spark process should produce 2 report outputs that will meet the desired conditions.
* 3.Spark code should read data from S3 , run on EMR and the cluster should be configured to auto terminate after Spark application finished.
* 4.Finally, the outputs should be written on the s3 bucket.

## Architecture Pipeline
![github-small](https://github.com/ecemce/AWS-Loan-Data/blob/main/docs/aws-loan-data-pipeline.png)

## Important Notes
* Please make sure that you provide the right AWS credentials and permissions.
* Please note that almost all services you will use have free-tier and will not occur any cost for the new AWS users. Only EMR does not have the free-tier.
* Shut it down when not using (don't forget)
* Use small machine types (m4.large etc.)
* Use single node cluster (1 master, 0 worker)

## Reports
* 1- Given this yearly income ranges, <40k, 40-60k, 60-80k, 80-100k and >100k. Generate a report that contains average loan amount and average term of loan in months based on these 5 income ranges. Result file should be like “income range, avg amount, avg term”
* 2- In loans which are fully funded and loan amounts greater than $1000, what is the fully paid amount rate for every loan grade of the borrowers.Result file should be like “credit grade,fully paid amount rate”, eg.“A,%95”

## SparkProcessor.py
Spark application code that fulfills the required conditions in the report.

## Transfer_data.py
Writes csv data in gzip format to s3 bucket using firehose client.


## All Steps
* Bucket name:loanS3bucket , AWS Region:eu-central-1 and then create a bucket
![github-small](https://github.com/ecemce/AWS-Loan-Data/blob/main/docs/s3bucket.png)

* Kinesis > Data streams > Create data stream 
Delivery Stream Name : LoanStream , Source: Direct put or other source
![github-small](https://github.com/ecemce/AWS-Loan-Data/blob/main/docs/kinesis.png)


* Destination:AmazonS3 , S3 bucket:loanS3bucket
![github-small](https://github.com/ecemce/AWS-Loan-Data/blob/main/docs/kinesis2.png)

* s3 compression:GZIP 
![github-small](https://github.com/ecemce/AWS-Loan-Data/blob/main/docs/kinesis3.png)

* Release:emr-5.33.0 , Instance type:m4.large , number of instances:1
![github-small](https://github.com/ecemce/AWS-Loan-Data/blob/main/docs/emr1.png)

* The bucket should look like this after the code runs
![github-small](https://github.com/ecemce/AWS-Loan-Data/blob/main/docs/loans3bucket.png)

