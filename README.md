# LMS BOT

This is auto bot for Learning Management System called e-class system.

This is based on the environment of Chuncheon National University of Education.  
so this may not be suitable for other universities' systems.

## Requirements

You have to have it in this directory `Chrome driver` which version is same to chrome you installed.  
Chrome driver is downloadable at [this site](https://chromedriver.chromium.org/downloads).

### System Requirements
Requires Python3 and selenium.  
You can install selenium using the command below.
```
pip3 install selenium
```

## Usage

1. Before you use this bot, you have to fill the `userInfo.json`.  
If you are CNUE student, your lms id is 20200101 and your password is 12345678, you have to write down the following in `userInfo.json`.
```json
{
  "id" : "20200101",
  "password" : "12345678",
  "lms_url" : "http://eclass.cnue.ac.kr"
}
```

2. run `main.py`