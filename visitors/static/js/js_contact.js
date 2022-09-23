function getPosition() {
    if (!navigator.geolocation) {
        alert("HTML5 Geolocation is not supported in your browser.");
        return;
    }
    navigator.geolocation.getCurrentPosition(showLocation , handleLocationError);
} 

function showLocation(position) {
    let date = new Date(position.timestamp);
    document.getElementById("location").innerHTML = date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds()+ "latitude:" + position.coords.latitude + "longitude:" + position.coords.longitude
    + "accuracy:" + position.coords.accuracy;
}

function handleLocationError(error) {
    switch (error.code) {
        case 0:
            alert(`There was an error while retrieving your location: ${error.message}`);
            break;
        case 1:
            alert("The user didn't allow this page to retrieve a location.");
            break;
        case 2:
            alert(`The browser was unable to determine your location: ${error.message}`);
            break;
        case 3:
            alert("The browser timed out before retrieving the location.");
            break;
    }
}