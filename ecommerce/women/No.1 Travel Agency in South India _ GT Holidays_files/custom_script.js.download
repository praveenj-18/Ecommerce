jQuery(function ($) {
  //console.log("render");
  var myVar = setInterval(function () {
    if ($("#map_canvas").length > 0) {
      var script = document.createElement("script");
      script.src =
        "https://maps.googleapis.com/maps/api/js?sensor=false&callback=initialize&key=AIzaSyAbiWD8crgFpYN8GEeaL6Qjg0lTpFJgmuk";
      script.async = true;
      document.body.appendChild(script);
      clearInterval(myVar);
    }
    if (jQuery("#menu-item-13896 .menu-dropdown").length > 0) {
      var selector = jQuery("#menu-item-13896 .menu-dropdown");
      selector.addClass("flexMenu");
      var all = selector.find("li");
      all.sort();
      var ind = Math.ceil(all.length / 7);
      selector.empty();
      for (i = 1; i <= ind; i++) {
        selector.append("<div></div>");
      }
      console.log("reverse");
      all.map((i, e) => {
        var indv = Math.ceil(i / 7);
        jQuery(
          "#menu-item-13896 .menu-dropdown div:nth-child(" + indv + ") "
        ).append(e);
      });
      clearInterval(myVar);
    }
    $(".menu-item").each(function () {
      var h = $(this).hasClass("current-menu-item");
      if (h) {
        $(this).parents("li").addClass("current-menu-ancestor");
      }
    });
    if (jQuery("#menu-item-13966 .menu-dropdown").length > 0) {
      var selector = jQuery("#menu-item-13966 .menu-dropdown");
      selector.addClass("flexMenu");
      var all = selector.find("li");
      all.sort();
      var ind = Math.ceil(all.length / 7);
      selector.empty();
      for (i = 1; i <= ind; i++) {
        selector.append("<div></div>");
      }
      console.log("reverse");
      all.map((i, e) => {
        var indv = Math.ceil(i / 7);
        jQuery(
          "#menu-item-13966 .menu-dropdown div:nth-child(" + indv + ") "
        ).append(e);
      });
      clearInterval(myVar);
    }
  }, 200);
  // Asynchronously Load the map API
});
function initialize() {
  console.log("init");
  var map;
  var bounds = new google.maps.LatLngBounds();
  var mapOptions = {
    // mapTypeId: 'hybrid'
    // mapTypeId: 'satellite'
    mapTypeId: "roadmap",
    // mapTypeId: 'terrain'
  };

  // Display a map on the page
  map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);
  map.setTilt(45);

  // Multiple Markers

  // var cm = jQuery("#idtech").text().split(',');
  // var lh = new Array();
  // var pp = new Array();
  // var cc = cm.map((a, b) => {
  //     if (b % 3 !== 0) {
  //         a = parseFloat(a);
  //         lh.push(a)
  //     } else { lh.push(a) }

  //     if ((b + 1) % 3 == 0) {
  //         lh = [];

  //         pp.push(lh);
  //     }

  // });

  markers = jQuery("#idtech").data("location");
  // Info Window Content
  var infoWindowContent = [
    [jQuery(".d1").html()],
    [jQuery(".d2").html()],

    [jQuery(".d3").html()],

    [jQuery(".d4").html()],

    [jQuery(".d5").html()],

    [jQuery(".d6").html()],

    [jQuery(".d7").html()],
  ];

  // Display multiple markers on a map
  var infoWindow = new google.maps.InfoWindow(),
    marker,
    i;

  // Loop through our array of markers & place each one on the map
  for (i = 0; i < markers.length; i++) {
    var position = new google.maps.LatLng(markers[i][1], markers[i][2]);
    bounds.extend(position);
    marker = new google.maps.Marker({
      position: position,
      map: map,
      title: markers[i][0],
    });

    // Allow each marker to have an info window
    google.maps.event.addListener(
      marker,
      "click",
      (function (marker, i) {
        return function () {
          infoWindow.setContent(infoWindowContent[i][0]);
          infoWindow.open(map, marker);
        };
      })(marker, i)
    );

    // Automatically center the map fitting all markers on the screen
    map.fitBounds(bounds);
  }

  // Override our map zoom level once our fitBounds function runs (Make sure it only runs once)
  var boundsListener = google.maps.event.addListener(
    map,
    "bounds_changed",
    function (event) {
      this.setZoom(7);
      google.maps.event.removeListener(boundsListener);
    }
  );
}

document.addEventListener("DOMContentLoaded", function () {
  const scroll = new LocomotiveScroll({
    el: document.querySelector("[data-scroll-container]"),
    smooth: true,
    // Add other options as needed
  });
});

jQuery(document).ready(function ($) {
  $(".readMoreDiv").each(function () {
    $(this).on("click", function () {
      // Toggle visibility of 'readMoreShow' and 'readMoreHide' within the same tour
      var tourContainer = $(this).closest(".flex-div-container");
      tourContainer.find(".readMoreShow").toggle();
      tourContainer.find(".readMoreHide").toggle();
      // Toggle text between '+ 7 more' and 'Show less'
      var newText =
        readMoreDiv.text() === "+ 7 more" ? "Show less" : "+ 7 more";
      readMoreDiv.text(newText);
    });
  });
});
jQuery(document).ready(function ($) {
  $(".owl-testimonialGT").owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    dots: true,
    responsive: {
      0: {
        items: 1,
      },
      600: {
        items: 1,
      },
      1000: {
        items: 2,
      },
    },
  });
});

jQuery(document).ready(function ($) {
  // Attach a change event listener to the checkboxes
  $(".filter-checkbox").change(function () {
    // Get the filters selected
    var selectedFilters = $(".filter-checkbox:checked")
      .map(function () {
        return $(this).data("filter");
      })
      .get();

    // Show or hide items based on selected filters
    $(".filterable-item").each(function () {
      var itemFilters = $(this).data("filters").split(" ");
      var showItem = selectedFilters.every(function (filter) {
        return itemFilters.includes(filter);
      });

      $(this).toggle(showItem);
    });
  });
});
jQuery(document).ready(function ($) {
  $(".tour-Page-Slider").owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    dots: false,
    responsive: {
      0: {
        items: 1,
      },
      600: {
        items: 1,
      },
      1000: {
        items: 1,
      },
    },
  });
});
