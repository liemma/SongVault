$(document).ready(function() {
    $("#add-song-form").submit(function(event) {
        event.preventDefault(); // Prevent default form submission

        // Hide previous success message and errors
        $("#success-message").addClass("d-none").hide();
        $("small.text-danger").addClass("d-none").text("");

        let selectedSimilarSongs = $("#similar_songs").val() || [];

        // Prepare form data
        let formData = {
            title: $("#title").val().trim(),
            artist: $("#artist").val().trim(),
            writers: $("#writers").val().trim(),
            album: $("#album").val().trim(),
            year: $("#year").val().trim(),
            summary: $("#summary").val().trim(),
            genre: $("#genre").val().trim(),
            duration: $("#duration").val().trim(),
            song_cover: $("#song_cover").val().trim(),
            lyrics_link: $("#lyrics_link").val().trim(),
            music_video: $("#music_video").val().trim(),
            similar_song_ids: selectedSimilarSongs
        };

        console.log("Sending AJAX request with data:", formData); // Debugging output

        // Send AJAX request
        $.ajax({
            url: "add_song_ajax",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(formData),
            success: function(response) {
                console.log("AJAX Response:", response); // Debugging output

                if (response.success) {
                    // Update "See it here" button link
                    $("#view-link").attr("href", "/view/" + response.id);

                    // Show success message with fade effect
                    $("#success-message").removeClass("d-none").fadeIn();

                    // Clear input fields
                    $("#add-song-form")[0].reset();

                    // Focus on title input for new song entry
                    $("#title").focus();
                } else {
                    console.warn("❌ Failed to add song. Showing errors...");
                    $.each(response.errors, function(field, errorMessage) {
                        $("#error-" + field).text(errorMessage).removeClass("d-none");
                    });
                }
            },
            error: function(xhr, status, error) {
                console.error("❌ AJAX Error:", error);
            }
        });
    });
});