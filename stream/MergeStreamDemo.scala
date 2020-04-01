import org.apache.spark.sql._
import io.delta.tables._


object MergeStreamDemo { 

  def main(args: Array[String]){ 

      // Reset the output aggregates table
      Seq.empty[(Long, Long)].toDF("key", "count").write
        .format("delta").mode("overwrite").saveAsTable("aggregates")

      val deltaTable = DeltaTable.forName("aggregates")

      // Function to upsert `microBatchOutputDF` into Delta table using MERGE
      def upsertToDelta(microBatchOutputDF: DataFrame, batchId: Long) {
        // ===================================================
        // For DBR 6.0 and above, you can use Merge Scala APIs
        // ===================================================
        deltaTable.as("t")
          .merge(
            microBatchOutputDF.as("s"), 
            "s.key = t.key")
          .whenMatched().updateAll()
          .whenNotMatched().insertAll()
          .execute()
        
        
        /*
        // For DBR 5.5 and below you can use Merge SQL command. 
        
        // Set the dataframe to view name
        microBatchOutputDF.createOrReplaceTempView("updates")
        
        // Use the view name to apply MERGE
        // NOTE: You have to use the SparkSession that has been used to define the `updates` dataframe
        microBatchOutputDF.sparkSession.sql(s"""
          MERGE INTO aggregates t
          USING updates s
          ON s.key = t.key
          WHEN MATCHED THEN UPDATE SET *
          WHEN NOT MATCHED THEN INSERT *
        """)  
        */
      }

      // Setting # partitions to 1 only to make this demo faster.
      // Not recommended for actual workloads.
      spark.conf.set("spark.sql.shuffle.partitions", "1")

      // Define the aggregation
      val aggregatesDF = spark.readStream
        .format("rate")
        .option("rowsPerSecond", "1000")
        .load()
        .select('value % 100 as("key"))
        .groupBy("key")
        .count()

      // Start the query to continuously upsert into aggregates tables in update mode
      aggregatesDF.writeStream
        .format("delta")
        .foreachBatch(upsertToDelta _)
        .outputMode("update")
        .start()

      }

} 
