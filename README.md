# lambda_py_scrap
AWS Lambda web scrapper package with Headless Chrome and Selenium for Python


lambda_py_scrap allows to automate actions to webpages from AWS Lambda service. This lambda package is a part of the bigger app created
for signing up users for gym classes and interacting with them via sms.


## Working

To scrape webpage AWS Lambda function needs a browser working in headless mode and selenium to interact with it. Definitely the major part
of work was done by 21Buttons team creating their PyChromless. The next stage was accomplished by Roberto Rocha which has been described in
this blog post. The last remaining part was just fits lambda to my requirements.

To make working lambda function for above purposes, please visit pages from credits. There is no need to rewrite well written codes.

The main issue wasn't working in my purpose was incompability of headless-chromium and chrome driver.


## Requirements for current package version:

* Cygwin (for Windows users)
* Python 3.7
* Chromedriver 2.37
* Headless Chromium v1.0.0-39

and for lambda function from requirements.txt:
```
boto3==1.9.106
botocore==1.12.107
selenium==3.14.1
chromedriver-install==0.2
```


## Credits:

* [Jairo](https://github.com/jairovadillo), Pere and [Ricard](https://github.com/ricardfp) - [21Buttons](https://github.com/21Buttons/pychromeless) and their great PyChromless.
* [Roberto Rocha](https://github.com/robroc) and his interpretation of PyChromless from 21Buttons. 
(If you are interested in datavis and storytelling, please take a look at Roterto's website.)
