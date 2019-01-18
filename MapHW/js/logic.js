
  // Create the tile layer that will be the background of our map
  var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"http://mapbox.com\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.light",
    accessToken: API_KEY
  });

  var darkmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.dark",
    accessToken: API_KEY
  });

  
// Create a baseMaps object to hold the lightmap layer
var baseMaps = {
  "Light Map": lightmap,
  "Dark Map": darkmap
};

// Create the map object with options
var map = L.map("map-id", {
  center: [40.73, -74.0059],
  zoom: 3,
  layers: [darkmap]
});
   // // Create a layer control, pass in the baseMaps and overlayMaps. Add the layer control to the map
   L.control.layers(baseMaps, null, {
    collapsed: false
  }).addTo(map);

  // Add my GeoJSON


function cityZip (feature,layer) {
    layer.bindPopup("<h1 class='infoHeader'> info window</h1><p class='infoHeader'>"
    +feature.properties.postalCode +
    +feature.properties.PO_NAME + "</p>");

  };

  L.geoJson(zipcode_json,{
    onEachFeature: cityZip
  }).addTo(map);