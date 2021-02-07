
    // Graphs
    var Chart = require("https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.min.js");
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
      type: 'polarArea',
      data: {
        labels: [
          'Groceries',
          'Restaurant',
          'Clothing',
          'Transit',
          'Debt',
          'Video games',
          'Utilities'
        ],
        datasets: [{
          data: [
            140,
            300,
            1056,
            34,
            5,
            87,
            246
          ]
        }]
      }
});