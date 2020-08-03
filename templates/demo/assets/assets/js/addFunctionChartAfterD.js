$(function () {
    appVue.chartD.forEach(function (item, i) {
        item.grafChart = Highcharts.chart('graphD' + i, {
            chart: {
                backgroundColor: 'transparent',
                zoomType: 'x',
                type: 'xrange',
                panning: true,
                animation: false,
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
                minRange: 60000,
                tickAmount: 10
            },
            yAxis: {
                opposite: false,
                title: {
                    text: ''
                },
                categories: [''],
                reversed: true,
                gridLineColor: '#ffffff',
                labels: {
                    style: {
                        font: '16px Arial, sans-serif'
                    }
                }
            },
            boost: {
                // enabled: false,
                useGPUTranslations: true,
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
                itemDistance: 50
            },
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
            subtitle: {
                text: 'Приближение осуществляется выделением области и навигатором внизу графика'
            },
            time: {
                useUTC: false
            },
            colors: [color.clWork, color.alarm, color.clStop, color.clPause],
            plotOptions: {
                xrange: {
                    borderRadius: 0,
                    borderWidth: 0,
                    grouping: false,
                    colorByPoint: false
                }
            },
            series: item.strData,
        });
    });
});

$("select").change(function () {
    let numb = $(this).parent().parent().attr('one-num');
    let a = $(this).attr('name');
    let v = $('select[name="' + a + '"]').val();
    if (v != 'no') {
        let min = +$("select[name='" + a + "'] option[value='" + v + "']").attr("min") - 1000000;
        let max = +$("select[name='" + a + "'] option[value='" + v + "']").attr("max") + 1000000;
        // console.log(numb +" " +a +" "+ min + ' ' + max);
        appVue.chartD[numb].grafChart.xAxis[0].setExtremes(min, max);
        appVue.chartD[numb].grafChart.showResetZoom();
    }
})