
The purpose of the project is to create pretty websites that anyone can update by updates a markdown file in a Git repo.

This allows teams to collaborate. Anyone can view the result in website.
![Lady Eboshi](https://vignette.wikia.nocookie.net/studio-ghibli/images/9/9f/Eboshi.png/revision/latest?cb=20181025001610)


## Why you need this
Organizations need to make decisions and communicate with team members, customers, vendors, and contractors.

## Approach
Eboshi builds beautiful websites from markdown pages hosted in Git repos.
Eboshi does this by using running Hugo in AWS Lambda each time a Git repo is updated.
It generates a static website, which is hosted on S3 and distributed with AWS CloudFront, so that your site is HTTPS, crazy fast, and nearly free.

Users who wish to edit documents can edit markdown files directly through the Github or Gitlab console. They can also propose changes to one or multiple documents by placing a Git pull request. Pull requests can be commented on, creating a discussion.

## Benefits over Google Docs
Google Docs is ugly. Eboshi is beautiful.
Google Docs do not allow proposing changes. Eboshi has a simple, powerful system for proposing changes.
Google Docs does not allow a viewer to see what is changing across a project or company. A log of all change is simple and viewable in Eboshi.
Google's method for tracking changes is clunky. Eboshi's method is elegant.

## Benefits over Confluence
Confluence is ugly. Eboshi is beautiful.
Confluence isn't viewable to members outside of Confluence. Eboshi websites are viewable on the web.
Confluence has a draft mode, but does not allow requesting reviews of a draft. Drafts cannot be commented on. When a draft is published, there is no record of who made the change and who approved the change.
Eboshi has simple, powerful system for proposing changes and requesting approvals.
Confluence's view of changes is clunky. Eboshi's method for tracking changes is elegant.

## Lower costs than Google Docs
Google Docs charges $6 per user per month. Eboshi is nearly free.
Google Docs are slow to load. Eboshi pages load nearly instantly.


## Lower costs than Confluence and SquareSpace
Confluence is $5 per user per month. SquareSpace, which you'd need to host external facing documents, cost $18 per month.
Confluence is slow to load. SquareSpace is sluggish. Eboshi pages load nearly instantly.

# Project plan

- [x] Create an AWS account.
  - Estimate: 15 min
  - Actual: 2:00 hours
- [x] Deploy a Hello World Lambda function using AWS Chalice.
  - Estimate: 15 min
  - Actual: 2 hours
- [x] Create a Github repo that holds the actual website.
  - Estimate: 5 min
  - Actual: 5 min
- [ ] Subscribe the lambda function to the Github repo.
  - Estimate: 25 min
- [ ] Verify that the lambda function executes when pushes are made to the Github repo.
  - Estimate: 5 min
- [ ] Update the lambda function to git-clone the repo into local storage.
  - Estimate: 20 min
- [ ] Add Hugo binary to the lambda function.
    Estimate: 40 min
    - [ ] Download Hugo locally
      - Estimate: 5 min
    - [ ] Add to Lambda function. No layers.
      - Estimate: 5 min
    - [ ] Run in the lambda function using BASH, verifying that it can be executed at all.
      - Estimate: 20 min.
    - [ ] Print a walk of the directory, verifying that files were created
      - Estimate: 10 min.
- [ ] Create two S3 buckets - one for dev and one for prod.
  - Estimate - 10 minutes
- [ ] Change Hugo to in the Lambda function to push to S3 instead of leaving the files locally.
  - Estimate - 30 minutes
- [ ] Change the markdown source repo. Verify that updating the repo triggers the lambda function.
  - Estimate: 5 min.
- [ ] Purchase a domain name.
  - Estimate: 10 min.
- [ ] Move static hosting to HTTPS S3.
  - [ ] Add CloudFront
     - 20 min
  - [ ] Generate ACM. Add HTTPS.
     - 20 min
  - [ ] Connect S3 bucket to website.
     - 20 min
  - [ ] Verify that get requests to the domain name display the file.
     - 10 min
  - Estimate - 2 hour
  - Estimate: 45 min.
- Start adding nested pages and other special Hugo functions.
  - Set new goals.
