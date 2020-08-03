$('.graf-picker').change(function () {
    let numChart = $(this).attr('one-num');
    let start = appVue.chart[numChart].startDate;
    let end = appVue.chart[numChart].stopDate;
    if ((start != '') && (end != '') && (new Date(start) < new Date(end))) {
        appVue.chart[numChart].grafChart.xAxis[0].setExtremes(new Date(start).getTime(), new Date(end).getTime());
    }
});

function createOneColorLineHorizontal(numChart, typeLine) { //передаем массивы предупреждений, стопов, аварий
    let oneArray = {
        id: typeLine + 'PlotLine',
        value: appVue.chart[numChart][typeLine + 'Set'],
        color: color[typeLine],
        dashStyle: 'shortdash',
        width: 2,
        label: {
            text: typeLine[0].toUpperCase() + typeLine.slice(1),
        }
    };
    return oneArray;
}

$('.matcon').click(function () {
    let numChart = $(this).attr('one-num');
    let typeLine = $(this).attr('one-type');
    let val = appVue.chart[numChart][typeLine + 'Check'];
    let grafLine = appVue.chart[numChart].arrColorHorizontalLine;
    if (val == 'check_box') {

        appVue.chart[numChart].arrColorHorizontalLine.push(createOneColorLineHorizontal(numChart, typeLine));

        let indexElement = '';
        for (let i = 0; i <= grafLine.length - 1; i++) {
            if (appVue.chart[numChart].arrColorHorizontalLine[i].id == typeLine + 'PlotLine') {
                indexElement = i;
                break;
            }
        }

        if (indexElement != '') {
            appVue.chart[numChart].grafChart.yAxis[0].addPlotLine(grafLine[indexElement]);
        };

    } else {
        appVue.chart[numChart].grafChart.yAxis[0].removePlotLine(typeLine + 'PlotLine');
    }
});

$('.set-values').change(function () {
    if ($(this).val() != '') {

        let numChart = $(this).attr('one-num');
        let typeLine = $(this).attr('one-type');
        let grafLine = appVue.chart[numChart].arrColorHorizontalLine;
        let changeVal = appVue.chart[numChart][typeLine + 'Set'];
        let check = appVue.chart[numChart][typeLine + 'Check'];

        //перемещение горизонтальной линии  
        if (check == 'check_box') {
            appVue.chart[numChart].grafChart.yAxis[0].removePlotLine(typeLine + 'PlotLine');
            appVue.chart[numChart].arrColorHorizontalLine.push(createOneColorLineHorizontal(numChart, typeLine));

            let indexElement = '';
            for (let i = 0; i <= grafLine.length - 1; i++) {
                if (appVue.chart[numChart].arrColorHorizontalLine[i].id == typeLine + 'PlotLine') {
                    indexElement = i;
                    break;
                }
            }

            if (indexElement != '') {
                appVue.chart[numChart].grafChart.yAxis[0].addPlotLine(grafLine[indexElement]);
            }
        }


        //перемещение цветов по графику   
        let grafLineL = appVue.chart[numChart].arrColorGrafLine;
        let indexElementL;

        for (let i = 0; i <= grafLineL.length - 1; i++) {
            if (appVue.chart[numChart].arrColorGrafLine[i].name == typeLine) {
                indexElementL = i;
                break;
            }
        };


        if (!isNaN(indexElementL)) {
            appVue.chart[numChart].arrColorGrafLine[indexElementL].value = changeVal;
            appVue.chart[numChart].grafChart.series[0].zones[indexElementL] = appVue.chart[numChart].arrColorGrafLine[indexElementL];
            appVue.chart[numChart].grafChart.series[0].redraw();
        }
    }
});

//добавление графиков
$('.addGraph').click(function () {
    let nameChart = $(this).text(); //название вставляемого графика
    let numInsertChart; //порядковый номер графика который будет добавлен
    for (let i = 0; i <= appVue.chart.length - 1; i++) {
        if (nameChart == appVue.chart[i].name) {
            numInsertChart = i;
            break;
        }
    }

    let numDiv = $(this).parent().attr('number-chart'); //порядковый номер div на странице в который будет добавлен график
    let shortWaySeries = appVue.chart[numDiv].grafChart.series; //короткий путь до объекта series в объекте графика
    let isInsert = false; //Нарисован ли уже вставляемый график?

    //Определяем нужно ли вставлять график
    for (let i = 0; i <= shortWaySeries.length - 1; i++) {
        if (shortWaySeries[i].name == nameChart) {
            isInsert = true;
            break;
        }
    }

    if (!isInsert) {
        //#######_____вставляем график
        //перекрашиваем бордер кнопки в желтый
        $(this).css("border-color", "#ffc107");
        let isInsertYAxis = true; //нужно ли вставлять новую ось?
        let yAxisIdInsert = appVue.chart[numInsertChart].unit; //id yAxis которая будет у вставляемого графика
        let shortWayYAxis = appVue.chart[numDiv].grafChart.options.yAxis; //короткий путь до всех yAxis

        for (let i = 0; i <= shortWayYAxis.length - 1; i++) {
            if (shortWayYAxis[i].id == yAxisIdInsert) {
                isInsertYAxis = false;
                break;
            }
        }

        //добавляем недостающую ось
        if (isInsertYAxis) {
            appVue.chart[numDiv].grafChart.addAxis({ // Secondary yAxis
                id: yAxisIdInsert,
                title: {
                    text: appVue.chart[numInsertChart].yAxisName,
                },
                lineWidth: 1,
                opposite: true,
                crosshair: true,
                labels: {
                    format: '{value} ' + appVue.chart[numInsertChart].unit,
                },
            });
        }

        //добавляем данные
        appVue.chart[numDiv].grafChart.addSeries({
            // dataSorting: {enabled: true},
            data: appVue.chart[numInsertChart].arrDataChart,
            name: appVue.chart[numInsertChart].name,
            turboThreshold: false,
            tooltip: {
                // valueDecimals: 2
            },
            yAxis: yAxisIdInsert
        });
    } else {
        //###____иначе удаляем график

        //перекрашиваем нажатую кнопку
        $(this).css("border-color", "#007BFF");

        let findInd;
        for (let i = 0; i <= shortWaySeries.length - 1; i++) {
            if (nameChart == shortWaySeries[i].name) {
                findInd = i;
                break;
            }
        }
        shortWaySeries[findInd].remove();
    }

    // appVue.chart[0].grafChart.addSeries({data:appVue.chart[1].arrDataChart,name:appVue.chart[1].name,turboThreshold:false})
    // appVue.chart[0].grafChart.series[1].remove()
});

$('.clearGraph').click(function () {
    let numDiv = $(this).parent().attr('number-chart');
    let ChartsInDiv = appVue.chart[numDiv].grafChart.series;
    let shortWayYAxis = appVue.chart[numDiv].grafChart.yAxis; //короткий путь до всех yAxis

    // if (ChartsInDiv.length > 2) {

    let but = $("div[number-chart=" + numDiv + "]").children();
    for (let i = 0; i <= but.length - 1; i++) {
        $(but[i]).css("border-color", "#007BFF");
    }

    for (let i = ChartsInDiv.length - 2; i >= 1; i--) {
        ChartsInDiv[i].remove(false);
    }
    for (let i = shortWayYAxis.length - 1; i >= 2; i--) {
        // shortWayYAxis[i].remove();
        appVue.chart[numDiv].grafChart.yAxis[i].remove();
    }
    appVue.chart[numDiv].grafChart.redraw();
    if (appVue.chart[numDiv].grafChart.options.yAxis.length > 1) {
        appVue.chart[numDiv].grafChart.options.yAxis = appVue.chart[numDiv].grafChart.options.yAxis.shift();
    }
    // }
});

function removeOneYAxis(idAxis) {}

function addNewPoint() {
    appVue.chart.forEach(function (item, i) {
        // console.log(i);
        let addObj = {
            x: item.arrDataChart.last().x + 5000,
            y: getRandomInt(75)
        };
        if (i == 0) {
            // console.log("| "+new Date(item.arrDataChart.last().x)+" | "+new Date(addObj.x));

            item.current = addObj.y;
            item.grafChart.get('id' + item.name).addPoint(addObj, true, false);
            item.arrDataChart.push(addObj);
        }
    });
}

// var ttt = setInterval(addNewPoint,10000);