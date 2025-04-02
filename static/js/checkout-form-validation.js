// This function is used to enable the Next Step button on the checkout page, only when all the customer details have been filled out.

$(document).ready(function () {
    // Reference the "Next Step" button
    var nextStepButton = $('#next-step');
    // reference the "alert-box" paragraph
    var alertBox = $('#alert-box')

    // Function to check whether all required fields are filled
    function checkFormCompletion() {
        let isValid = true;

        $('.form-group input[required], .form-group textarea[required]').each(function () {
            // If a required field is empty, set isValid to false
            if ($(this).val().trim() === '') {
                isValid = false;
            }
        });

        if (isValid) {
            alertBox.addClass("text-success").removeClass("text-danger")
            alertBox.text("Details saved.")
        }
        else {
            alertBox.addClass("text-danger").removeClass("text-success")
            alertBox.text("Please fill out all fields above to continue.")
        }

        // Enable the button if all fields are valid; otherwise, disable it
        nextStepButton.prop('disabled', !isValid);
    }

    // Check form completion on input changes
    $('.form-group input[required], .form-group textarea[required]').on('input', function () {
        checkFormCompletion();
    });

    // Initial check when the page loads
    checkFormCompletion();

    // Handle click on the Next Step button
    nextStepButton.click(function (e) {
        e.preventDefault();

        if (!nextStepButton.prop('disabled')) {
            var formData = new FormData();
            $('.form-group input[name], .form-group textarea[name]').each(function () {
                formData.append($(this).attr('name'), $(this).val());
            });
            // Add the CSRF token to the form data
            formData.append('csrfmiddlewaretoken', csrfToken);

            $.ajax({
                type: 'POST',
                url: checkoutUrl,
                contentType: false,
                processData: false,
                data: formData,
                success: function (response) {
                    alert('Details submitted successfully! Proceeding to the next step.');
                },
                error: function (xhr, status, error) {
                    alert('Error while submitting your details. Please try again.');
                }
            });
        }
    });
});