# README

A simple bunch of scripts to:

1. Take a picture from a raspberry pi camera
2. Upload to S3
3. Transform


## Future Enhancement

- Move from AWS CLI through to AWS Python SDK
- Create IAM user in cloudformation
- Rekognition on image
  - Store metadata back in S3
- CloudWatch event/Trigger lambda on S3 PutObject

## In AWS

  - create pi user
    - no permission
  - download api creds
  - run cft to create permissions
  AWS_PROFILE=tomellis aws cloudformation create-stack --stack-name pi-iam --region eu-west-1 --template-body file:////home/trellis/src/pi-lapse/cloudformation/iam.yaml --capabilities CAPABILITY_IAM
  - create s3 bucket
  - test access
  AWS_PROFILE=raspberrypi aws s3 --region eu-west-1 sync /home/trellis/pi-images/ s3://picamera-images/

## On your PI

- Using default raspbian image
- Enable ssh and setup your environment:
```
AWS_ACCESS_KEY=123456
AWS_SECRET_ACCESS_KEY=123456
AWS_REGION=eu-west-1

touch /boot/ssh

cat <<EOF >> /boot/config.txt
# Disable camera light
disable_camera_led=1
EOF

sudo sed /boot/config.txt -i -e "s/^startx/#startx/"

sudo apt-get install python-dev -y

mkdir -p ~/.aws

cat <<EOF >> ~/.aws/credentials
[raspberrypi]
aws_access_key_id = ${AWS_ACCESS_KEY}
aws_secret_access_key = ${AWS_SECRET_ACCESS_KEY}
EOF

cat <<EOF >> ~/.aws/config
[raspberrypi]
output = text
region = ${AWS_REGION}
EOF
```

- Test that you can upload some files via AWS CLI from your pi
```
mkdir -p ~/pi-lapse/images
touch ~/pi-lapse/images/test
AWS_PROFILE=raspberrypi aws s3 --region eu-west-1 sync ~/pi-lapse/images/ s3://picamera-images/
```

