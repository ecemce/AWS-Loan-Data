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

## Reports
* 1- Given this yearly income ranges, <40k, 40-60k, 60-80k, 80-100k and >100k. Generate a report that contains average loan amount and average term of loan in months based on these 5 income ranges. Result file should be like “income range, avg amount, avg term”
* 2- In loans which are fully funded and loan amounts greater than $1000, what is the fully paid amount rate for every loan grade of the borrowers.Result file should be like “credit grade,fully paid amount rate”, eg.“A,%95”

