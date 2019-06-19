aws s3 cp $1 s3://bepro1 > output
aws rekognition search-faces-by-image --collection-id "friends" --image "{\"S3Object\":{\"Bucket\":\"bepro1\",\"Name\":\"$1\"}}" --region us-east-1