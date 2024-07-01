# AWS-Lambda
Lambda function to unzip the incoming files in S3
It works fine in default Lambda settings {timeout 3 sec, 512 Mb RAM, 512 Mb storage} only with small archive files (unzipped file size <20MB, archive size ~ 3 MB) 
To get it to work with big Archives sized 200-250 MB you need to increase the RAM and Storage +_ increase timeout (1min)
Tested config: Lambda-heavy-duty {1Gb Memory/ 3Gb Storage / 60 sec timeout}
File DSM25556.gz	261.2 MB was unzipped in around 6-7 sec

