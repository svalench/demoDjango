// function syncExtremes(e) {
//     var thisChart = this.chart;

//     if (e.trigger !== 'syncExtremes') { // Prevent feedback loop
//         Highcharts.each(Highcharts.charts, function (chart) {
//             if (chart !== thisChart) {
//                 if (chart.xAxis[0].setExtremes) { // It is null while updating
//                     chart.xAxis[0].setExtremes(
//                         e.min,
//                         e.max,
//                         undefined,
//                         false,
//                         { trigger: 'syncExtremes' }
//                     );
//                 }
//             }
//         });
//     }
// }


Highcharts.setOptions({
    lang: {
        loading: 'Загрузка...',
        months: ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
        weekdays: ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'],
        shortMonths: ['Янв', 'Фев', 'Март', 'Апр', 'Май', 'Июнь', 'Июль', 'Авг', 'Сент', 'Окт', 'Нояб', 'Дек'],
        rangeSelectorFrom: "С",
        rangeSelectorTo: "По",
        rangeSelectorZoom: "Период",
        resetZoom: '  СБРОСИТЬ ЗУМ  '
    }
});


$(function () {
    appVue.chart.forEach(function (item, i) {
        item.grafChart = Highcharts.stockChart('graph' + i, {
            chart: {
                backgroundColor: 'transparent',
                zoomType: 'x',
                type: 'spline',
                events: {
                    render: function (event) {
                        item.min = +event.target.series[0].dataMin;
                        item.max = +event.target.series[0].dataMax;
                        // appVue.chart[i].min = +event.target.series[0].dataMin.toFixed(2);
                        // appVue.chart[i].max = +event.target.series[0].dataMax.toFixed(2);
                    },
                    
    
//             load: function () {

//                 // set up the updating of the chart each second
//                 var series = this.series[0];
//                 setInterval(function () {
//                     var x = (new Date()).getTime(), // current time
//                         y = Math.round(Math.random() * 100);
//                     series.addPoint([x, y], true, true);
//                 }, 3000);
//             }
        
                }
            },
            title: {
                margin: 0,
                text: item.name,

            },
            credits: {
                enabled: false
            },
            xAxis: {
                type: 'datetime',
                crosshair: true,
                // minRange: 30000,
                minRange: 100,
                // events: {
                //     setExtremes: syncExtremes
                // },
            },
            boost: {
                // enabled: false,
                // useGPUTranslations: true,
                // seriesThreshold:4,
                // usePreallocated:true
            },
            tooltip: {
                shared: true,
                crosshairs: true,
                // split: true
            },
            legend: {
                enabled: true,
            },
            subtitle: {
                text: 'Приближение осуществляется выделением области и навигатором внизу графика'
            },
            time: {
                useUTC: false
            },
            // responsive: {
            //     rules: [{
            //             condition: {
            //             minWidth: 400
            //             },         
            //                 }]
            //             },

            rangeSelector: {
                buttons: [{
                        count: 1,
                        type: 'minute',
                        text: '1м'
                    }, {
                        count: 2,
                        type: 'minute',
                        text: '2м'
                    },
                    {
                        count: 3,
                        type: 'minute',
                        text: '3м'
                    },
                    {
                        count: 5,
                        type: 'minute',
                        text: '5м'
                    },
                    {
                        count: 1,
                        type: 'day',
                        text: '1д'
                    }, {
                        type: 'all',
                        text: 'Всё'
                    }
                ],
                inputEnabled: false,
                selected: 2,

                buttonSpacing: 30,
                buttonTheme: { // styles for the buttons  
                    width: 45,
                    style: {
                        color: '#000000',
                    },
                    states: {
                        hover: {
                            fill: '#42A5F5',
                            style: {
                                color: 'white'
                            }
                        },
                        select: {
                            fill: '#29B6F6',
                            style: {
                                color: 'white'
                            }
                        }
                    }
                },
            },
            yAxis: [{
                // lineColor: '#FF0000',
                crosshair: true,
                id: item.unit,
                lineWidth: 1,
                labels: {
                    format: '{value} ' + item.unit,
                    // style: {
                    // color: Highcharts.getOptions().colors[1]
                    // }
                },
                title: {
                    text: item.yAxisName,
                    // style: {
                    // color: Highcharts.getOptions().colors[1]
                    // }
                },
                opposite: false,
                plotLines: item.arrColorHorizontalLine
            }],

            series: [{
                // dataSorting: {enabled: true},
                // turboTreshold: 999999,
                id: 'id'+item.name,
                turboThreshold: false,
                data: item.arrDataChart,
                name: item.name,
                tooltip: {
                    // valueDecimals: 2
                },
                zones: item.arrColorGrafLine,
                fillOpacity: 0.1,
                yAxis:item.unit,
                showInLegend: false,
            }, ]
        });
    });
});