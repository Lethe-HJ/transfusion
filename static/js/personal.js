//JavaScript代码区域
layui.use('element', function(){
    var element = layui.element;

});

// 基于准备好的dom，初始化echarts实例
var myChart = echarts.init(document.getElementById('main'));

// 指定图表的配置项和数据
var option = {
    color: ['#3398DB'],
    tooltip : {
        trigger: 'axis',
        axisPointer : {            // 坐标轴指示器，坐标轴触发有效
            type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    title : {
        text: '一周内体温变化条形图',
        subtext: '数据来自XX医院',
        x: 'center',
        align: 'right'
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis : [
        {
            type : 'category',
            data : ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            axisTick: {
                alignWithLabel: true
            }
        }
    ],
    yAxis : [
        {  min:35,
            max:40,
            axisLabel:{
                formatter: function (value) {
                    var texts = [];
                    if(value==35){
                        texts.push('35');
                    }
                    else if (value <=36) {
                        texts.push('36');
                    }
                    else if (value<= 37) {
                        texts.push('37');
                    }
                    else if(value<= 38){
                        texts.push('38');
                    }
                    else if(value<= 39){
                        texts.push('39');
                    }
                    else{
                        texts.push('40');
                    }
                    return texts + " °C";

                }
            }
        }
    ],
    series : [
        {
            name:'直接访问',
            type:'line',
            barWidth: '60%',
            data:[38.2, 37.8, 37, 36.9, 37.5, 37, 37.9]
        }
        // {
        //     name:'平均温度',
        //     type:'line',
        //     yAxisIndex: 1,
        //     data:[35, 32, 40, 39, 39, 37,37]
        // }
    ]
};

// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);
//JavaScript代码区域


// 基于准备好的dom，初始化echarts实例
var myChart = echarts.init(document.getElementById('chart'));

// 指定图表的配置项和数据
var option = {
    color: ['#3398DB'],
    tooltip : {
        trigger: 'axis',
        axisPointer : {            // 坐标轴指示器，坐标轴触发有效
            type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    title : {
        text: '一周内血糖变化条形图',
        subtext: '数据来自XX医院',
        x: 'center',
        align: 'right'
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis : [
        {
            type : 'category',
            data : ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            axisTick: {
                alignWithLabel: true
            }
        }
    ],
    yAxis : [
        {  min:3.9,
            max:8.9,
            axisLabel:{
                formatter: function (value) {
                    var texts = [];
                    if(value==3.9){
                        texts.push('3.9');
                    }
                    else if (value <=4.9) {
                        texts.push('4.9');
                    }
                    else if (value<= 5.9) {
                        texts.push('5.9');
                    }
                    else if(value<= 6.9){
                        texts.push('6.9');
                    }
                    else if(value<= 7.9){
                        texts.push('7.9');
                    }
                    else{
                        texts.push('8.9');
                    }
                    return texts + " mmol/L";

                }
            }
        }
    ],
    series : [
        {
            name:'直接访问',
            type:'bar',
            barWidth: '60%',
            data:[4.7, 6.8, 6.9, 7.1, 7.5, 6.5, 6.9]
        }
        // {
        //     name:'平均温度',
        //     type:'line',
        //     yAxisIndex: 1,
        //     data:[35, 32, 40, 39, 39, 37,37]
        // }
    ]
};

// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);
