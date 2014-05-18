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
  $( "#search" ).addClass('transitionAnim');

  //construct data table object with options
  $('#restaurant_table').DataTable( {
    paging: false,
    scrollY: 400,
    searching: false,
    "ordering": false
  });
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

// var dishLabel = document.getElementsByClassName('dish-name');
// console.log(dishLabel);

function searchText() {
  var searchValue = document.getElementById('search').value;
  console.log(searchValue);
  var string;
  // var responseText = httpGet("https://api.foursquare.com/v2/venues/40a55d80f964a52020f31ee3?client_id=KR5QNGVNULHKBZ1K5JBLAQ1WU4BAZEJQXDFMJ5QD35L4INCP&client_secret=1GB2PJNNLNIVEQQ0FZTI02XZQDLAUHAREO5XXDAXTE1SHXBF&v=20130815");
}

function httpGet(theUrl) {
    var xmlHttp = null;

    xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false );
   // xmlHttp.withCredentials = true;
    xmlHttp.send();
    return xmlHttp.responseText;
}
