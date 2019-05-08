
$(document).ready(function(){
    $("#submit_bt").click(function(){
        console.log($("#username").val());
        console.log($("#password").val());
        CheckNull();
    });

});



//判断是否敲击了Enter键
$(document).keyup(function(event){
    if(event.keyCode === 13){
        $("#submit_bt").trigger("click");
    }
});


function CheckNull(){
    var username = $("#username");
    var password = $("#password");
    if(username.val() == ""){
        layer.msg('用户名为空');
        username.focus();
    }
    else if(password.val() == ""){
        layer.msg('密码为空');
        password.focus();
    }
    else{
        $.ajax({
            type: "POST",
            url:"/login_submit",
            dataType: "json",
            data: {
                "username" : username.val(),
                "password" : password.val()
            },
            success: function(rtdata){
                console.log(rtdata);
                layer.msg(rtdata.msg);
                setTimeout(url_jump(rtdata.status),500);
                function url_jump(status){
                    console.log(status);
                    if(status === 200) {
                        console.log("页面跳转");
                        window.location = '../../templates/select.html';
                    }
                  }
            }
        });
    }
}