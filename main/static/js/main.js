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
  $('#table_id').DataTable( {
    paging: false,
    scrollY: 400,
    searching: false
  });
  //register click event for table rows.
  $('#table_id tbody').on( 'click', 'tr', function () {
    alert( $(this).html() );
  });
});

function searchText() {
  var searchValue = document.getElementById('search').value;
  console.log(searchValue);
  var string;
  var responseText = httpGet("https://api.foursquare.com/v2/venues/40a55d80f964a52020f31ee3?client_id=KR5QNGVNULHKBZ1K5JBLAQ1WU4BAZEJQXDFMJ5QD35L4INCP&client_secret=1GB2PJNNLNIVEQQ0FZTI02XZQDLAUHAREO5XXDAXTE1SHXBF&v=20130815");
}

function httpGet(theUrl) {
    var xmlHttp = null;

    xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false );
   // xmlHttp.withCredentials = true;
    xmlHttp.send();
    return xmlHttp.responseText;
}
