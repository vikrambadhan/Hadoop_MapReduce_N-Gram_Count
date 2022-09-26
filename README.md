# MapReduce_N-Gram_Count
Hadoop map reduce to compute n gram counts


The submission was programmed in python and tested on NYU Dataproc Hadoop Cluster.


To run the code:
    mapred streaming -input hw1.txt -output <outputfile> -mapper "python mapper.py" -reducer "python reducer.py" -file mapper.py -file reducer.py

    This will run and output will be stored as <outputfile>


use this <outputfile> file and run:
    mapred streaming -input <outputfile> -output <finalfile> -mapper "python mapper2.py" -reducer "python reducer2.py" -file mapper2.py -file reducer2.py
    
The <finalfile> will be stored as a .txt file and we can parse it to check the output


We parse using the command, 

hdfs dfs -cat <finalfile>.txt/par*

