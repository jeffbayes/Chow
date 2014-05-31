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

    //put placeholder text in search bars
    $( "input[name=searchQuery]" ).attr("placeholder", "Which Restaurant?");
    $( "input[name=searchCity]" ).attr("placeholder", "Which City?");
    //animate the search bar
    $( "input[name=searchQuery]" ).focus(function() {
    $( "input[name=searchCity]").css({
      '-webkit-animation-name': 'expandSearchBar',
      '-webkit-animation-duration': '1s',
      '-webkit-animation-timing-function': 'åcubic-bezier(0.000, 0.795, 0.000, 1.000)',
      
      //TODO - add vendor prefixes

      'width': '350px'
      });
    });
  } else {
    $( "input[name=searchQuery]" ).css({
      'width': '350px'
    });
    $( "input[name=searchCity]" ).css({
      'width': '350px'
    });
  }

  $("input[value='dishSearch']" ).click(function() {
    $("input[name='searchQuery']").attr("placeholder", "Which Dish?");
  });
  $("input[value='restaurantSearch']" ).click(function() {
    $("input[name='searchQuery']").attr("placeholder", "Which Restaurant?");
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
