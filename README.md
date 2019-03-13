# lambda_py_scrap
AWS Lambda web scrapper package with Headless Chrome and Selenium for Python.


lambda_py_scrap allows to automate actions to webpages from AWS Lambda service. This lambda package is a part of the bigger app created
for signing-up users for gym classes and interacting with them via sms.


## Working

To scrape webpage AWS Lambda function needs a browser working in headless mode and selenium to interact with it. Definitely the major part of work has been done by 21Buttons team creating their PyChromless. The next stage has been accomplished by Roberto Rocha and described in this blog post. The last remaining part was just to fit lambda to my requirements.

To make working lambda function for above purposes, please visit pages from credits. There is no need to rewrite well written codes.

The main reason lambda wasn't working in my purpose was incompatibility of headless-chromium and chrome driver.


## Requirements for current package version:

* Cygwin (for Windows users)
* Python 3.7
* Chromedriver 2.37
* Headless Chromium v1.0.0-39

and for lambda function from requirements.txt:
```
boto3==1.9.106  # interact with S3
botocore==1.12.107  # same as above
selenium==3.14.1
chromedriver-install==0.2
```
## How to start?
1. Clone repository:
```
git clone https://github.com/mihalw28/lambda_py_scrap.git
```
2. Navigate into lambda_py_scrap, add lib and bin folders to avoid some errors during building a zip package (MS Windows only) 
```
$ cd lambda_py_scrap
$ mkdir bin lib
```
3. Next steps are the same like in Roberto's solution

## Credits:

* [Jairo](https://github.com/jairovadillo), Pere and [Ricard](https://github.com/ricardfp) - [21Buttons](https://github.com/21Buttons/pychromeless) and their great PyChromless.
* [Roberto Rocha](https://robertorocha.info/setting-up-a-selenium-web-scraper-on-aws-lambda-with-python/) and his interpretation of PyChromless from 21Buttons.
