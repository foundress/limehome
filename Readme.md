Here is my execution of test task for your company.

## Prerequisites

### Pull sources 
Run 

```git clone https://github.com/foundress/limehome.git```

### Download chromedriver
1. Make sure you have Chrome browser installed
2. Find its version in __Settings__ -> __About Chrome__
3. Open https://chromedriver.chromium.org/downloads and download __chromerdriver__ with the same version as your Chrome browser. 
4. Save Chrome driver in the directory where you have pulled sources, name it as ```chromedriver```


### Install packages

Run

```pip install -r requirements-test.txt```

## Running tests  

Run 
  
```CALCULATOR_URL="http://juliemr.github.io/protractor-demo/" pytest.exe limehome/test_calculator.py```
