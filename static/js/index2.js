layui.use('element', function(){
    var element = layui.element;

    //…
});
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
            var oIcon = document.getElementById("icon_button");
            oBtn.onclick = function () {

                console.log(this.id);
                // layer.open({
                //     skin: 'demo-class'
                // });
                layer.alert('001号药品扫描错误，请及时处理')
            }


        }
    });//弹窗结束
}
layuse();
//搜素
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
    };
    oBtn.onclick=function () {
        // console.log("rows=" + oTab.rows.length +
        //     "\ncells=" + oTab.rows[0].cells.length);
        for (var i = 0; i < oTab.rows.length; i=i+2) {
            for (var j = 0; j < oTab.rows[i].cells.length; j = j + 1){
                var searchoText = oTab.rows[i].cells[j].innerHTML.search(oTxt.value);
                if(searchoText !== -1){
                    oTab.tBodies[0].rows[i].cells[j].style.background="#ff5722";
                }
                else{
                    oTab.tBodies[0].rows[i].cells[j].style.background="";
                }
            }

        }


    }
    $("#icon_button").click(function () {
        // 显示弹出层遮罩
        $("#layer-mask").show();
        // 显示弹出层窗体
        $("#layer-pop").show();
        // 弹出层关闭按钮绑定事件
        $("#layer-close").click(function () {
            // 弹出层关闭
            $("#layer-mask").hide();
            $("#layer-pop").hide();
        });
    });
}
    //开关
    //Demo
    layui.use('form', function(){
        var form = layui.form;

        //监听提交
        form.on('submit(formDemo)', function(data){
            layer.msg(JSON.stringify(data.field));
            return false;
        });
    });





