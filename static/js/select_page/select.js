layui.use('element', function(){
    var element = layui.element;

    //…
});             //element组件
//弹窗
function layuse() {
    layui.use('layer', function () { //独立版的layer无需执行这一句
        var $ = layui.jquery, layer = layui.layer; //独立版的layer无需执行这一句
        var list = {
            'btn0': '001号病人药品扫描错误，请及时处理',
            'btn1': '002号病人药品扫描错误，请及时处理',
            'btn2': '003号病人药品扫描错误，请及时处理',
        };
        for (var i = 0; i < 3; i++) {
            var oBtn = document.getElementById("btn" + i.toString());
            var oSearch = document.getElementById("search");
            // oSearch.onclick = function () {

                // layer.alert('001号病人，正常', {
                //     icon: 6,
                //     skin: 'layer-ext-moon' //该皮肤由layer.seaning.com友情扩展。关于皮肤的扩展规则，去这里查阅
                // })结束
                // layer.prompt({title: '输入手机号，并确认', formType: 1}, function(pass, index){
                //     layer.close(index);
                //     layer.prompt({title: '请输入手机验证码，并确认', formType: 1}, function(text, index){
                //         layer.close(index);
                //         layer.msg('验证完毕！您的手机号：'+ pass +'<br>您的验证码：'+text);
                //     });
                // });结束
            // };
            oBtn.onclick = function () {
                console.log(this.id);
                // layer.open({
                //     skin: 'demo-class'
                // });
                // layer.open({
                //     type: 1,
                //     skin: 'layui-layer-rim', //加上边框
                //     area: ['300px', '200px'], //宽高
                //     content: list[this.id]
                // });弹窗结束
                layer.alert('001号病人药品扫描错误 !', {
                    icon: 5,
                    skin: 'layer-ext-moon' //该皮肤由layer.seaning.com友情扩展。关于皮肤的扩展规则，去这里查阅
                })
            }
        }
    });//弹窗结束
}
$(document).ready(function(){
  window.msgjson={};
  msgget();
  setTimeout(msgprint,1000);
  setTimeout(layuse,1200);
});
function msgprint(){
    var htmlcount="";
    msgli=window.msgjson;
    for(var i=0;i<msgli["bednum"].length;i++){
        htmlcount +="<tr>\n" +
            "<td>" + msgli["bednum"][i] + "</td>\n" +
            "<td>" + msgli["name"][i] + "</td>\n" +
            "<td>" + msgli["sex"][i] + "</td>\n" +
            "<td>" + msgli["age"][i] + "</td>\n" +
            "<td>" + msgli["family"][i] + "</td>\n" +
            "<td>" + msgli["tel"][i] + "</td>\n" +
            "<td><button class='layui-btn layui-btn-primary layui-btn-sm' id='search'>"+
        "<i class='layui-icon'>&#xe615;</i>"+
        "</button>"+
        "</td>\n" +
            "</tr>\n";

    }
    $("#tbody1").html(htmlcount);
}
function msgget(){
    $.ajax({
        url:"http://www.pythonhj.top/msg_get",
        type:"post",
        dataType:"json",
        async:"true",
        data:{},
        headers:{
            // "Access-Control-Allow-Origin":"*"
        },
        success:function(data){
            window.msgjson=data;
        }

    })
}
//搜索
window.onload=function(){
    var oTab=document.getElementById("tab");
    var oBtn=document.getElementById('btn');
    var oTxt=document.getElementById('txt');
    oTxt.onclick=function() {
        if (oTxt.value === "") {
            for (var i = 0; i < oTab.tBodies[0].rows.length; i++) {
                oTab.tBodies[0].rows[i].style.background = "";
                // console.log("空了");
                // alert(oTxt.value === "");
            }
        }
    }
    oBtn.onclick=function () {
        var i = 0;
        for (i = 0; i < oTab.tBodies[0].rows.length; i++) {
         if(oTab.tBodies[0].rows[i].cells[0].innerHTML==oTxt.value||oTab.tBodies[0].rows[i].cells[1].innerHTML==oTxt.value){
             oTab.tBodies[0].rows[i].style.background="yellow";

         }
         else{
             oTab.tBodies[0].rows[i].style.background="";
         }
        }


    }
}
layui.use(['laypage', 'layer'], function() {
    var laypage = layui.laypage
        , layer = layui.layer;

    //总页数低于页码总数
    laypage.render({
        elem: 'demo0'
        , count: 50 //数据总数
    });
})



