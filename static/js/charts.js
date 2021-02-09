var ctx = document.getElementById("chart1");
var chart = new Chart(ctx, {
    type: 'pie',
    data: {
        datasets: [{
            data: ['716862', '614025'],
            backgroundColor: ['#e35549', '#fec14c']
        }],
        labels: ['Detail Audit', "Basic Audit"],
    },
    options: {
        legend: {
            display: true
        },

    },
});

var ctx1 = document.getElementById("chart2");
var chart = new Chart(ctx1, {
    type: 'bar',
    data: {
        datasets: [{
            data: ['716862', '614025', '457910', '15555'],
            backgroundColor: ['#2B91FE', '#F14950', '#206DBF', '#FA8418']
        }],
        labels: ['Detail Audit', "Basic Audit", "Title", "Title"],
    },
    options: {
        legend: {
            display: false
        },

    },
});