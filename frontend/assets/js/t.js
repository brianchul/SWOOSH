const request = require('request'); // 載入request模組

request({
    url: 'http://104.196.179.255:5000/timeline/',
    json: true
}, (error, response, body) => {
    var result = JSON.stringify(body, undefined, 2);
    console.log("123" + result); // body是回傳的json物件，使用JSON.stringify()轉為json字串
    //result.
    });