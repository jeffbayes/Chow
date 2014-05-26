/*
$( document ).ready(function() {
    console.log( "ready!" );
});

$.ajax({
           type: 'GET',
           url: "https://api.locu.com/v1_0/venue/search/?name=Tasty%20Thai&locality=Eugene&api_key=fab61d3c1bc8ead95a1c95d80a45ffc291539ba0",
           processData: true,
           data: {},
           dataType: "json",
           xhrFields: {
          withCredentials: true
        },
           success: function (data) {
               processData(data);
           }
});

 
function processData(data){
 console.log(data);
}
*/
$(document).ready( function () {
  //construct data table object with options
  var restTable = $('#restaurant_table').DataTable( {
    paging: false,
    scrollY: 400,
    searching: false,
    "ordering": false
  });

  //there is no data in the table
  if ($('#restaurant_table tr').length === 2) {
    //hide the dataTable
    $('#restaurant_table').hide();
    restTable.columns().visible(false);
    //animate the search bar
    $( "input[name=searchRestaurant]" ).focus(function() {
    $( "input[name=searchCity]").css({
      '-webkit-animation-name': 'expandSearchBar',
      '-webkit-animation-duration': '1s',
      '-webkit-animation-timing-function': 'åcubic-bezier(0.000, 0.795, 0.000, 1.000)',
      
      //TODO - add vendor prefixes

      'width': '350px'
      });
    });
  } else {
    $( "input[name=searchRestaurant]" ).css({
      'width': '350px'
    });
    $( "input[name=searchCity]" ).css({
      'width': '350px'
    });
  }

  //register click event for table rows.
  $('#restaurant_table tbody').on( 'click', 'tr', function () {
    console.log( $(this).html() );
    var cellText = ($('#restaurant_table td').html());
    window.location.href = "Caspian";
  });


  $('#menu_table').DataTable( {
    paging: false,
    scrollY: 400,
    searching: false,
    "ordering": false
  });

    $('.star').raty({
      path: STATIC_URL+'/img/',
      click: function(score, evt) {
        parentNode = $(this).parent(); 
        parentHtml = parentNode.html();
        $(parentHtml).each(function(index, value) {
          $(value).each(function(i, j) {
            var className = $(j).attr('class');
            /*! STORE RATING HERE !*/
            if (className == 'title') {
              console.log($(j).html());
              console.log("Score: " + score);
            }
          });
        });
      }
    });
});



function searchText() {
  var searchValue = document.getElementById('search').value;
  console.log(searchValue);
  var string;
}

function httpGet(theUrl) {
    var xmlHttp = null;

    xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false );
    xmlHttp.send();
    return xmlHttp.responseText;
}
