# **Netzence Backend Technical Task**
#### **Candidate:** Bello Shehu Ango

---

## **Task 1: Simple API with AWS Lambda, API Gateway, and DynamoDB**

### **Deployment Steps**

1. **Build and Publish the Docker Image to ECR**
   - Log in to your AWS account and navigate to the ECR page. Create a new repository; in this example, it's named `netzence/assessment`.  
     ![alt text](static/images/static/img/image.png)  
   - Copy the URI of the repository for use in the following steps.

   - Open your terminal in the project directory and run:  
     ```bash
     docker build -t netzence_assessment .
     ```
   - Tag the image with the URI of the ECR repository:  
     ```bash
     docker tag netzence_assessment:latest <ECR_REPOSITORY_URI>
     ```
   - Log in to your ECR repository:  
     ```bash
     aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <ECR_REPOSITORY_URI>
     ```
     ![alt text](static/images/image-22.png)  

   - Push the image to your ECR repository:  
     ```bash
     docker push <ECR_REPOSITORY_URI>
     ```
     Verify the image is uploaded by navigating to the ECR repository's details page.  
     ![alt text](static/images/image-1.png)

2. **Create IAM Policy and Role**
   - Go to the IAM console and create a new policy.  
     ![alt text](static/images/image-3.png)  
   - Switch to the **JSON** tab and paste the following policy:  
     ```json
     {
         "Version": "2012-10-17",
         "Statement": [
             {
                 "Sid": "ReadWriteTable",
                 "Effect": "Allow",
                 "Action": [
                     "dynamodb:BatchGetItem",
                     "dynamodb:GetItem",
                     "dynamodb:Query",
                     "dynamodb:Scan",
                     "dynamodb:BatchWriteItem",
                     "dynamodb:PutItem",
                     "dynamodb:UpdateItem",
                     "dynamodb:DescribeTable"
                 ],
                 "Resource": "arn:aws:dynamodb:*:*:table/items"
             },
             {
                 "Sid": "WriteLogStreamsAndGroups",
                 "Effect": "Allow",
                 "Action": [
                     "logs:CreateLogStream",
                     "logs:PutLogEvents"
                 ],
                 "Resource": "*"
             }
         ]
     }
     ```
     ![alt text](static/images/image-4.png)  
   - Name the policy `NetzenceAssessmentLambdaPolicy`.  
     ![alt text](static/images/image-7.png)

   - Create a new role:  
     ![alt text](static/images/image-6.png)  
     Select **Lambda** as the trusted entity and attach the policy `NetzenceAssessmentLambdaPolicy`.  
     ![alt text](static/images/image-8.png)  
     Name the role `NetzenceAssessmentLambdaRole`.  
     ![alt text](static/images/image-10.png)

3. **Set Up S3 Bucket**
   - Navigate to the S3 service and create a bucket named `netzence-assessment-bucket`.  
     Disable "Block all public access" (not recommended for production).  
     ![alt text](static/images/image-14.png)  
     ![alt text](static/images/image-16.png)  
   - Add the following bucket policy under **Permissions > Bucket Policy**:  
     ```json
     {
         "Version": "2012-10-17",
         "Statement": [
             {
                 "Sid": "PublicReadGetObject",
                 "Effect": "Allow",
                 "Principal": "*",
                 "Action": "s3:GetObject",
                 "Resource": "arn:aws:s3:::netzence-assessment-bucket/*"
             }
         ]
     }
     ```
     ![alt text](static/images/image-19.png)

4. **Create the Lambda Function**
   - Go to the Lambda service and create a function using a container image. Name it `NetzenceAssessmentLambda1`.  
     ![alt text](static/images/image.png)  
   - Select the ECR repository with your Docker image and set the architecture to `x86_64`.  
   - Choose the execution role `NetzenceAssessmentLambdaRole`.  
     ![alt text](static/images/image-12.png)

   - Add environment variables under **Configuration > Environment Variables**. Replace placeholder values with your live AWS credentials.  
     ![alt text](static/images/image-13.png)

5. **Set Up API Gateway**
   - Navigate to the API Gateway service and create a REST API named `NetzenceAssessmentAPI`.  
     ![alt text](static/images/image-25.png)  
   - Create a resource and enable proxy integration for `{endpoints+}`.  
     ![alt text](static/images/image-28.png)  
   - Link the resource to the Lambda function. Configure methods for `GET`, `POST`, `PUT`, and `DELETE`.  
     ![alt text](static/images/image-31.png)  
   - Deploy the API to a stage named `dev` and copy the Invoke URL for testing.  
     ![alt text](static/images/image-37.png)

---

## **Task 2: Lambda Function for Scheduled Data Archiving**

1. **Create the Lambda Function**
   - Name the function `itemArchiver` and set the runtime to Python 3.13.  
     ![alt text](static/images/image-39.png)  
   - Use the same role `NetzenceAssessmentLambdaRole`.  
     ![alt text](static/images/image-40.png)  
   - Upload the code from `archiver.py` and set the environment variable `S3_BUCKET` to `netzence-assessment-bucket`.  
     ![alt text](static/images/image-42.png)

2. **Schedule the Function**
   - Use Amazon EventBridge to create a daily recurring schedule.  
     ![alt text](static/images/image-44.png)  
   - Set the target to invoke the `itemArchiver` Lambda function.  
     ![alt text](static/images/image-47.png)

---

## **Testing the API**
- Import the provided Postman collection (`API Docs.postman_collection.json`) and set the `BASE_URL` to the Invoke URL of your API Gateway.

---

## **Assumptions**
- The DynamoDB table can be created within the application itself rather than through the AWS Console.

---

This improved version maintains structure, clarity, and readability while keeping the original images in place. Let me know if you'd like further edits!