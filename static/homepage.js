function displaySongs(selectedSongs) {
    // Empty old data
    $("#popular-songs").empty();

    // Create a Bootstrap row container
    let row = $("<div>").addClass("row g-4"); // `g-4` adds spacing between columns

    // Insert the songs
    $.each(selectedSongs, function (i, datum) {
        let col = $("<div>").addClass("col-md-4 d-flex justify-content-center"); // Each song in a column

        let card = $("<div>").addClass("card text-center shadow-sm p-3").css("width", "100%");

        // Clickable song cover image inside an anchor tag
        let songLink = $("<a>")
            .attr("href", "/view/" + encodeURIComponent(datum["id"]))
            .addClass("d-block");

        let songImage = $("<img>")
            .attr("src", datum["song_cover"]) // Extract song cover from data
            .attr("alt", datum["title"])
            .attr("alt", datum["artist"])
            .addClass("card-img-top img-fluid rounded") // Bootstrap classes
            .css({ "max-height": "200px", "width": "100%", "cursor": "pointer", "object-fit": "cover" });

        songLink.append(songImage);

        let cardBody = $("<div>").addClass("card-body");
        let songTitle = $("<h5>").addClass("card-title").text(datum["title"]);

        let songWriters = $("<p>")
            .addClass("card-text text-muted")
            .text("Written by: " + datum["writers"].join(", ")); // Join writers if multiple

        // Append elements to structure
        cardBody.append(songTitle, songWriters);
        card.append(songLink, cardBody);
        col.append(card);
        row.append(col);
    });

    // Append the row container to the main div
    $("#popular-songs").append(row);
}

$(document).ready(function () {
    let startIndex = 3; // Change this to modify which songs are displayed

    let selectedSongs = Object.values(data).slice(startIndex, startIndex + 3);

    displaySongs(selectedSongs);
});
