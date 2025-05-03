$(document).ready(function() {
    $("#save-button").click(function(event) {
        event.preventDefault();  // Prevent default form submission

        let selectedSimilarSongs = $("#similar_songs").val() || [];
        let song_id = song.id

        let formData = {
            id: song_id,
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

        $.ajax({
            url: "/edit_song_ajax",  // ✅ Fix incorrect URL
            type: "POST",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify(formData),
            success: function(response) {
                if (response.success) {
                    window.location.href = "/view/" + response.id;  // ✅ Redirect immediately
                } else {
                    alert("Error: " + JSON.stringify(response.errors));
                }
            },
            error: function(xhr, status, error) {
                console.error("❌ AJAX Error:", error);
                alert("Server error while saving the song.");
            }
        });
    });


    $("#discard-button").click(function(event) {
        event.preventDefault();

        let confirmDiscard = confirm("Are you sure you want to discard changes? Your edits will not be saved.");
        if (confirmDiscard) {
            window.location.href = "/view/" + song.id;  // ✅ Redirect to view page without saving
        }

    });
});