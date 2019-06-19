aws s3 cp $1 s3://bepro1 > output
aws rekognition index-faces \
--image "{\"S3Object\":{\"Bucket\":\"bepro1\",\"Name\":\"$1\"}}" --collection-id "friends" --detection-attributes "ALL" --external-image-id "abhishek" --region us-east-1