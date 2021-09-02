/*
var ctx  = document.querySelector('#line-chart');

var myLineChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels:['1월','2월', '3월','4월','5월','6월','7월','8월','9월','10월','11월','12월'],
      datasets:[
        {        
        label:'2020',
        data:[5,10,20,3,8,12,20,1,5,7,9,12]
        },
        {        
        label:'2021',
        data:[12,20,1,5,7,9,12,5,10,20,3,8]
        }
      ]
    }
});
*/
$(document).ready(function() {
    var cosPoints = []; 
    for (var i=Math.PI; i<=3*Math.PI; i+=0.1){ 
        cosPoints.push([i / Math.PI * 15, Math.cos(i) / 100]);
    }

    var plot1 = $.jqplot('insight-graph', [cosPoints, [[carbon_contribution, Math.cos(carbon_contribution / 15 * Math.PI) / 100]]], {  
        title: '',
        series:[{showMarker:false}],
        axes:{
            xaxis:{
                label:'Carbon Emission'
            },
            yaxis:{
                label:'Rate', textPosition: 'none'
            }
        }
    });
});