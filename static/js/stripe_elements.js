var cardElement = NaN;
var stripePublicKey = NaN;
var clientSecret = NaN;
var stripe = NaN;
var paytButton = NaN;

document.addEventListener("DOMContentLoaded", function () {
  stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
  clientSecret = $("#id_client_secret").text().slice(1, -1);
  // Use your Stripe publishable key
  stripe = Stripe(stripePublicKey);
  // Create an instance of the card Element and mount it to the container
  var elements = stripe.elements();
  var style = {
    base: {
      fontSize: "16px",
      color: "#32325d",
    },
  };
  cardElement = elements.create("card", { style });
  cardElement.mount("#card-element");

  // Handle realtime validation errors on the card element
  cardElement.addEventListener(
    "change",
    function (event) {
      if (event.error) {
        // Show the error message

        if ($(".message-container").length === 0) {
          // Create and append message-container div to header only if it doesn't exist
          $("header").append($("<div>", { class: "message-container" }));
        }
        if ($(".message").length === 0) {
          // Create and append message div to message-container only if it doesn't exist
          $(".message-container").append(
            $("<div>", { class: "message", text: event.error.message })
          );
        } else {
          // Update existing message div with new message text
          $(".message").text(event.error.message);
        }
        // Show the message container, wait 3000ms, then fade out
        $(".message-container").show().delay(3000).fadeOut();
      }
    },
    false
  );
});

// Handle form submission
$("#payment-form").on("submit", function (e) {
  e.preventDefault();
  paytButton = $('#pay-button')
  paytButton.html('Processing...').prop('disabled', true);
  // Change the displayed text and disable the button once it has been clicked.
  cardElement.update({ disabled: true });
  // Handle form submission using Stripe.js
  var form = document.getElementById("payment-form");
  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const { error } = await stripe.confirmCardPayment(clientSecret, {
      payment_method: {
        card: cardElement,
      },
    });

    if (error) {
      // Display error.message in your UI
      console.log(error.message);
      paytButton.html('Pay').attr('disabled', true);
      cardElement.update({ disabled: false });
    } else {
      // The payment has been processed!
      window.URL.redirect("/success")
      form.submit();
    }
  });
});

// Stripe.setPublishableKey(stripe_public_key);
