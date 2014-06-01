$(document).ready( function () {

  /*-----INDEX.HTML JAVASCRIPT-----*/
  /*-------------------------------*/
  //construct DataTable object with options
  var restTable = $('#restaurant_table').DataTable( {
    paging: false,
    scrollY: 400,
    searching: false,
    "ordering": false
  });

  //change placeholder text based on which search type is selected.
  $("input[value='dishSearch']" ).click(function() {
    alert ('clicked');
    $("input[name='searchQuery']").attr("placeholder", "Which Dish?");
  });
  $("input[value='restaurantSearch']" ).click(function() {
    $("input[name='searchQuery']").attr("placeholder", "Which Restaurant?");
  });

  /*---RESTAURANT.HTML JAVASCRIPT---*/
  /*-------------------------------*/
  $('#menu_table').DataTable( {
    paging: false,
    scrollY: 600,
    searching: false,
    "ordering": false,
    "oLanguage": {
        "sEmptyTable":     "Sorry, this restaurant does not have menu data!"
    }
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