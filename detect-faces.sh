aws s3 cp $1 s3://bepro1 > output
aws rekognition detect-faces --attributes "ALL" --image "{\"S3Object\":{\"Bucket\":\"bepro1\",\"Name\":\"$1\"}}" --region us-east-1