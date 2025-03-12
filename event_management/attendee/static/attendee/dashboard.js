var ctx = document.getElementById('linechart');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [{
            label: 'Earnings in Rs.',
            data: [2050,1900,2100,1800,2800,2000,2500,2600,2450,1950,2300,2900],
            backgroundColor: [
                'rgba(85,85,85,1)',
                
            ],
            borderColor: [
                'rgba(41, 155, 99)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true
    }
});

var ctx = document.getElementById('doughnut').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['Academic', 'Non-academic', 'Administration', 'Others'],
        datasets: [{
            label: 'Employees',
            data: [42,12,8,6],
            backgroundColor: [
                'rgba(41,155,99,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(120,46,139,1)',
            
            ],
            borderColor: [
                'rgba(41,155,99,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(120,46,139,1)',
            ],
            borderWidth: 1
        }]
    },
    options: {
       responsive: true
    }
});

