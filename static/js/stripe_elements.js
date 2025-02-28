var cardElement = NaN;
var stripePublicKey = NaN;
var clientSecret = NaN;
var stripe = NaN;
var payButton = NaN;
var successfulPayment = false;

document.addEventListener("DOMContentLoaded", function () {
  stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
  clientSecret = $("#id_client_secret").text().slice(1, -1);
  // Use your Stripe publishable key
  stripe = Stripe(stripePublicKey);
  // Create an instance of the card Element and mount it to the container
  var elements = stripe.elements();
  var style = {
    base: {
      color: "#32325d",
      fontSize: "16px",
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
          // Create and append message-container div to header
          // only if it doesn't exist
          $("header").append($("<div>", { class: "message-container" }));
        }
        if ($(".message").length === 0) {
          // Create and append message div to message-container
          // only if it doesn't exist
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
$("#payment-form").on("submit", async function (e) {
  e.preventDefault();
  payButton = $("#pay-button");
  payButton.html("Processing...");
  // Change the displayed text and disable the button
  // once it has been clicked.
  cardElement.update({ disabled: true });

  try {
    const { error } = await stripe.confirmCardPayment(clientSecret, {
      payment_method: {
        card: cardElement,
      },
    });

    if (error) {
      // Display error.message in your UI
      console.log(error.message);
      $(".message-container").show().delay(3000).fadeOut();
      payButton
        .html("Pay")
        .attr("disabled", true)
        .delay(3000)
        .attr("disabled", false);
      cardElement.update({ disabled: true });
    } else {
      // The payment has been processed!
      // Trigger form submission
      payButton.replaceWith(
        `<a href="${$("#payment-form").attr(
          "action"
        )}" class="checkout-page-button" id="pay-button">Continuing to checkout</a>`
      );

      let dotCount = 1;
      const payButtonLink = $("#pay-button");

      const intervalId = setInterval(() => {
        if (dotCount <= 3) {
          payButtonLink.html(`Continuing to checkout${".".repeat(dotCount)}`);
          dotCount++;
          console.log(`dotCount is ${dotCount}`);
        } else {
          console.log("clearing intervalId");
          clearInterval(intervalId);
          document.location = $("#pay-button").attr("href");
          console.log("Payment completed successfully!");
        }
      }, 500); // Adjust the interval duration as needed
    }
  } catch (err) {
    console.error(err);
    $(".message-container").show().delay(3000).fadeOut();
    payButton.html("Pay").attr("disabled", false);
    cardElement.update({ disabled: false });
  }
});

// Stripe.setPublishableKey(stripe_public_key);
