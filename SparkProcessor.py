
from pyspark.sql.functions import *
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.appName("LoanProcessor").getOrCreate()


main_df =spark.read.format("csv").option("header","true").option("inferSchema","true").load("s3://loans3bucket/loan.csv")
main_df.createOrReplaceTempView("main_df")
loan_df = spark.sql("select annual_inc , loan_amnt , term from main_df")
loan_df = loan_df.na.drop()
loan_df.createOrReplaceTempView("loan_df")
loan_df_2 = loan_df.withColumn('term', split(loan_df['term'], ' ').getItem(1))
loan_df_2.createOrReplaceTempView("loan_df_2")
report_1=loan_df_2.withColumn("inc_range",when(col("annual_inc")< 40000, lit(1))
                            .when((col("annual_inc") >40000 ) & (col("annual_inc") <= 60000),lit(2))
                            .when((col("annual_inc") >60000 ) & (col("annual_inc") <= 80000),lit(3))
                            .when((col("annual_inc") >80000 ) & (col("annual_inc") <= 100000),lit(4))
                            .otherwise(lit(5)))                            
report=report_1.groupBy("inc_range").agg(avg("term"), avg("loan_amnt")).sort("inc_range")
report.coalesce(1).write.option("header",True).csv("s3://loans3bucket/report_one/report_one.csv") 

df = spark.sql("select loan_amnt,loan_status, funded_amnt, grade  from main_df")
df=df.filter("loan_amnt > 1000 and loan_amnt=funded_amnt")
df.createOrReplaceTempView('df')
gradeCountsDF=df.groupBy("grade").agg(count("grade").alias('grade_count')).sort("grade")
fpCountsDF=df.filter(df.loan_status == "Fully Paid").groupBy("grade").agg(count("grade").alias('fp_count')).sort("grade")
gradeCountsDF.createOrReplaceTempView("gradeCountsDF")
fpCountsDF.createOrReplaceTempView("fpCountsDF")
joinDF = spark.sql("select g.grade , g.grade_count , f.fp_count from gradeCountsDF g, fpCountsDF f where g.grade == f.grade order by g.grade asc")
joinDF.createOrReplaceTempView("joinDF")
report = spark.sql("select *,  ROUND((fp_count)/(grade_count)*100 , 2)  as fully_paid_amount_rate from joinDF ")
report.createOrReplaceTempView("report")
report_2=spark.sql("select grade , fully_paid_amount_rate from report")
report_2.coalesce(1).write.option("header",True).csv("s3://loans3bucket/report_two/report_two.csv")


spark.stop()
