$(document).ready(
    function main(){
        getuser();
    }
);


function getuser(){
        $.ajax({
            url: '/user_get',
            type: 'get',
            dataType: 'json',
            async: 'true',
            data: {
                // name: $('#username').val(),
                // password: $('#password').val()
                // code:  $('#code').val(),
                // captcha:  $('#captcha').val()  // 输入的图形验证码的值
                // remember:  remember
                name:"222",
            },
            headers: {
                // "X-XSRFTOKEN":get_cookie("_xsrf")
            },

            success: function(data){
                console.log(data);
                $("#user_bt").text(data);//设置user_bt标签的文本内容为data
            }
        });
    // function(){
    //     // window.setTimeout(username_get,200);
    //     console.log("111");
    //
    // }
}

function print(object){
    console.log(object);
}