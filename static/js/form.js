

$(document).ready(function() {
     // Attach a submit event handler to the form with id 'myForm'
    $("#myForm").submit(function(event) {
        // Prevent the default form submission behavior (page reload)
        event.preventDefault();
        // Create a JavaScript object containing the form data
        var formData = {
            "message": $("#message").val() // Get the value of the input field with id 'message'
        };
 // Perform an AJAX request
        $.ajax({
            type: "POST", // HTTP method to use for the request
            url: "/submit_form", // URL to send the request to
            data: JSON.stringify(formData), // Convert formData object to a JSON string
            contentType: "application/json; charset=utf-8",// Set the content type to JSON
            dataType: "json",// Expect a JSON response from the server
            success: function(data) {
                // On success, update the div with id 'response' with the received response message //this represents sendback.response on backend
                $("#response").text(data.response);
            },
            error: function(errMsg) {
                // On error, log the error message to the console
                console.error("Error:", errMsg);
            }
        });
    });
});