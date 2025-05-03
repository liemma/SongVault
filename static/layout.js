

$(document).ready(function(){
    //when the page loads, display all the name  
    $("#searchForm").on("submit", function(event) {
      event.preventDefault();
      let searchInput = $('#searchInput');
      let query = searchInput.val().trim();
      
      if (query.length > 0) {
        window.location.href = `/search/${encodeURIComponent(query)}`;
      } else {
        searchInput.val(''); // Clear the input field
        searchInput.focus(); // Keep focus in the search bar
        
      }
    });                  


})