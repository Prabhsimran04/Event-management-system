
$(document).ready(function(){
  $(".gallery-carousel").owlCarousel({
    items: 3, // Number of items to display
    loop: true,
    margin: 10,
    nav: true,
    dots: true,
    responsive: {
      0: {
        items: 1
      },
      600: {
        items: 2
      },
      1000: {
        items: 3
      }
    }
  });

  // Initialize Venobox
  $('.venobox').venobox(); 

  $('#ticket-form').on('submit', function(e) {
    e.preventDefault(); // Stop default form submission
  
    const formData = {
      event_id: $('input[name="event_id"]').val(),
      your_name: $('input[name="your-name"]').val(),
      your_email: $('input[name="your-email"]').val(),
      ticket_type: $('#ticket-type').val(),
      csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
    };
  
    $.ajax({
      url: 'http://127.0.0.1:8000/book-ticket',
      type: 'POST',
      data: formData,
      success: function(response) {
        console.log('Success:', response);
        alert('Ticket booked successfully!');
        location.reload();
      },
      error: function(xhr, status, error) {
        if (xhr.status === 401 && xhr.responseJSON?.redirect_url) {
          // Redirect anonymous users to register
          window.location.href = xhr.responseJSON.redirect_url;
        } else {
          console.error('Error:', error);
          alert('There was a problem booking your ticket.');
        }
      }
    });
  });

  const cancelButtons = document.querySelectorAll(".cancel-booking-btn");

cancelButtons.forEach(button => {
  button.addEventListener("click", function () {
    // const eventId = this.dataset.eventId;

    if (confirm("Are you sure you want to cancel this booking?")) {
      fetch("http://127.0.0.1:8000/cancel-booking/", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          "X-CSRFToken": getCookie("csrftoken")
        },
        body: `event_id=${eventId}`
      })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          alert("Booking cancelled successfully.");
          location.reload(); // Reload to reflect change
        } else {
          alert("Failed to cancel booking: " + data.error);
        }
      })
      .catch(error => {
        console.error("Error:", error);
        alert("Something went wrong.");
      });
    }
  });
});

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
});

