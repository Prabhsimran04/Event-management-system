var ctx = document.getElementById('linechart');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [{
            label: 'Number of Bookings',
            data: booking_data,
            backgroundColor: [
                'rgba(85,85,85,1)',
                
            ],
            borderColor: [
                'rgb(72, 54, 235)',
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
        labels: chartData.labels,
        datasets: [{
            label: 'Attendees',
            data: chartData.data,
            backgroundColor: [
                'rgba(41,155,99,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(120,46,139,1)',
            
            ],
            borderColor: [
                'rgba(41,155,99,1)',
                'rgb(72, 54, 235)',
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

