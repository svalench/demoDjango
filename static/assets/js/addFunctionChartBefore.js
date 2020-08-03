let color = {
	ok: '#43A047',
	warning: '#FFB300',
	stop: '#ef5350',
	alarm: '#e53935',
	clWork: "#66BB6A",
	clStop: "#BDBDBD",
	clPause: "#FFCA28",
};

//цвета графиков в конкретных зонах 

//функция при передаче в которую массивов с авариями предупреждениями и остановка выплевывает готовый объект с массивами для каждого графика подставляемый в графики 
const createArrayColorLineHorizontal = (valueWarning, valueAlarm, valueStop) => { //передаем массивы предупреждений, стопов, аварий
	
	return [{
			id: 'warningPlotLine',
			value: valueWarning,
			color: color.warning,
			dashStyle: 'shortdash',
			width: 2,
			label: {
				text: 'Warning' //'Внимание'
			}
		},
		{
			id: 'alarmPlotLine',
			value: valueAlarm,
			color: color.alarm,
			dashStyle: 'shortdash',
			width: 2,
			label: {
				text: 'Alarm' //'Авария'
			}
		},
		{
			id: 'stopPlotLine',
			value: valueStop,
			color: color.stop,
			dashStyle: 'shortdash',
			width: 2,
			label: {
				text: 'Stop' //'Остановка'
			}
		},
	];
	
};

const createArrayColorGraf = (valueWarning, valueAlarm, valueStop) => { //передаем  предупреждений, стопов, аварий
	let TotalArr = [];
	TotalArr = [{
			name: 'warning',
			value: valueWarning,
			color: color.ok
		},
		{
			name: 'alarm',
			value: valueAlarm,
			color: color.warning
		},
		{
			name: 'stop',
			value: valueStop,
			color: color.stop
		},
		{
			color: color.stop
		}
	];

	return TotalArr;
};

const SetMinMaxDatepicker = (arrayData, numberChart) => {
	if (arrayData.length>0){
	let temp1 = new Date(arrayData[0].x).setHours(new Date().getHours() + 3);
	appVue.chart[numberChart].minDate = new Date(temp1).toISOString().substring(0, 16);
	appVue.chart[numberChart].startDate = appVue.chart[numberChart].minDate;
	let temp2 = new Date(arrayData.last().x).setHours(new Date().getHours() + 3);
	appVue.chart[numberChart].maxDate = new Date(temp2).toISOString().substring(0, 16);
	appVue.chart[numberChart].stopDate = appVue.chart[numberChart].maxDate;
}
};

appVue.chart.forEach(function (item, i) {
	// appVue.arrColorHorizontalLine
	item.arrColorHorizontalLine = createArrayColorLineHorizontal(item.warningSet, item.alarmSet, item.stopSet);
	item.arrColorGrafLine = createArrayColorGraf(item.warningSet, item.alarmSet, item.stopSet);
	SetMinMaxDatepicker(item.arrDataChart, i);
});