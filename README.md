# Manufacturing-Execution-System

## base.html
* 為基底網頁，個網頁以此為基礎樣板

## .html
* 其餘.html檔為各功能頁面，均繼承base.html的內容再加上各自需要的部分

## views.py
* 核心程式所在，資料的處理都在這裡進行
* 負責將參數回傳給base.html，進行網頁顯示

## urls.py
* 負責管理網址路徑
