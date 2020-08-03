Array.prototype.last = function () {
  return this[this.length - 1];
};

//формирование рандомной строки
function makeKey(length) {
  var result = '';
  var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  var charactersLength = characters.length;
  for (var i = 0; i < length; i++) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
  }
  return result;
}

function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

function getRandomArr(period, countPoint, maxV) {
  let time = new Date().getTime(),
    ch = [],
    val;
  for (let i = 0; i <= countPoint; i++) {
    val = Math.floor(Math.random() * maxV);
    ch.push({
      x: time,
      y: val
    });
    time = +time + period;
  }
  return ch.sort((a, b) => {
    return a.x - b.x
  });
}

let count = 1000,
  period = 1000;

const addObjectToVue = (maxV) => {

  let createdObject = {
    // idGraph:"graph",
    key: makeKey(8),
    name: makeKey(15),
    unit: makeKey(2),
    yAxisName: makeKey(6),
    current: getRandomInt(56),
    max: getRandomInt(56),
    min: getRandomInt(56),
    stopSet: getRandomInt(56),
    alarmSet: getRandomInt(56),
    warningSet: getRandomInt(56),
    stopCheck: 'check_box',
    alarmCheck: 'check_box',
    warningCheck: 'check_box',
    startDate: '',
    stopDate: '',
    minDate: '',
    maxDate: '',
    arrDataChart: getRandomArr(period, count, maxV),
    arrColorHorizontalLine: [],
    arrColorGrafLine: [],
    grafChart: '',
  };
  return createdObject;
};

var appVue = new Vue({
  el: '#vueAppJs',
  data: dataPoint,
});

appVue.chart.forEach((item,i)=>{
  item.key= makeKey(8);
  item.current = 0;
  item.max = 0;
  item.min = 0;
  item.stopCheck = 'check_box';
  item.alarmCheck = 'check_box';
  item.warningCheck = 'check_box';
  item.startDate = '';
  item.stopDate = '';
  item.minDate = '';
  item.maxDate = '';
  item.arrColorHorizontalLine= [];
  item.arrColorGrafLine= [];
  item.grafChart= '';
})

appVue.chartD.forEach((item,i)=>{
  item.key= makeKey(8);
  item.grafChart= '';
})