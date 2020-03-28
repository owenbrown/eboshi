# eboshi - Hugo CI/CD for AWS
The purpose of the project is to create pretty websites that anyone can update by updates a markdown file in a Git repo.

This allows teams to collaborate. Anyone can view the resultin website. 
![Lady Eboshi](https://vignette.wikia.nocookie.net/studio-ghibli/images/9/9f/Eboshi.png/revision/latest?cb=20181025001610)



## Design
Eboshi runs on Hugo in AWS Lambda.
Although Hugo is written in Go, Eboshi is written in Python. The reason is that Owen knows Python best.

The project is deployed using AWS Chalice. The reason is that it is not expected that other developer will update Eboshi.

Steps
- Create an AWS account
- Deploy a Hello World Lambda function using AWS Chalice.
- Create a Github repo that holds the actual website.
- Subscribe the lambda function to the Github repo.
- Verify that the lambda function executes when pushes are made to the github repo.
- Update the lambda function to git-clone the repo into local storage.
- Add Hugo binary to the lambda function.
- Run Hugo in the lambda function. Walk the directory, verifying that files were created.
- Create two S3 buckets - one for dev and one for prod.
- Change Hugo to in the Lambda function to push to S3 instead of leaving the files locally.
- Change the markdown source repo. Verify that changes propogate through to S3.
- Purchase a domain name.
- Add Cloudfront. Add HTTPS. Connect S3 bucket to website.
- Verify that get requests to the domain name display the file.
- Start adding nested pages and other special Hugo functions.
