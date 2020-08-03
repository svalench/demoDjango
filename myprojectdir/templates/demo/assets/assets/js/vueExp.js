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
  data: {
    chart: [
      //     {
      //     idGraph:"graph",
      //     key:makeKey(8),
      //     name:'Метров залито',
      //     unit:'м',
      //     yAxisName:'Уровень',
      //     current: 12,
      //     max: 35,
      //     min:15,
      //     stopSet:50,
      //     alarmSet:25,
      //     warningSet:12,
      //     stopCheck:'check_box',
      //     alarmCheck:'check_box',
      //     warningCheck:'check_box',  
      //     startDate:'',
      //     stopDate:'',
      //     minDate:'',
      //     maxDate:'',
      //     arrDataChart:ch1,
      //     arrColorHorizontalLine:[],
      //     arrColorGrafLine:[],
      //     grafChart:'',
      // }
      addObjectToVue(60),
      addObjectToVue(20),
      addObjectToVue(30),

    ],
    chartD: [{
      name: makeKey(15),
      key: makeKey(8),
      strData: [{
          name: 'РАБОТАЕТ',

          data: [{
              // id:0,
              // name:'коментарий 1',
              x: Date.UTC(2014, 11, 2, 3, 3, 3),
              x2: Date.UTC(2014, 11, 5, 3, 3, 3),
              y: 0,

            },
            {
              // id:'1',
              // name:'rjvvtynfhbq 2',
              x: Date.UTC(2014, 11, 9, 3, 3, 3),
              x2: Date.UTC(2014, 11, 23, 3, 3, 3),
              y: 0,

            },
          ]
        },
        {
          name: 'АВАРИЯ',
          //pointPadding: 0,
          //groupPadding: 0,

          data: [{
            x: Date.UTC(2014, 10, 21, 3, 3, 3, 3),
            x2: Date.UTC(2014, 11, 2, 3, 3, 3, 3),
            y: 0
          }],
        },
        {
          name: 'ОСТАНОВЛЕН',
          //pointPadding: 0,
          //groupPadding: 0,

          data: [{
            x: Date.UTC(2014, 11, 5, 3, 3, 3, 3),
            x2: Date.UTC(2014, 11, 8, 3, 3, 3, 3),
            y: 0,
          }],

        },
        {
          name: 'ПРОСТОЙ',
          //pointPadding: 0,
          //groupPadding: 0,

          data: [{
            x: Date.UTC(2014, 11, 8, 3, 3, 3),
            x2: Date.UTC(2014, 11, 9, 3, 3, 3),
            y: 0,

          }],
        }
      ]
    }],
    grafChart: '',
  }
});