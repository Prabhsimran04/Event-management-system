jQuery(document).ready(function($) {
    "use strict";
  
    //Contact
    // $('form.contactForm').submit(function() {
    //   var f = $(this).find('.form-group'),
    //     ferror = false,
    //     emailExp = /^[^\s()<>@,;:\/]+@\w[\w\.-]+\.[a-z]{2,}$/i;
  
    //   f.children('input').each(function() { // run all inputs
  
    //     var i = $(this); // current input
    //     var rule = i.attr('data-rule');
  
    //     if (rule !== undefined) {
    //       var ierror = false; // error flag for current input
    //       var pos = rule.indexOf(':', 0);
    //       if (pos >= 0) {
    //         var exp = rule.substr(pos + 1, rule.length);
    //         rule = rule.substr(0, pos);
    //       } else {
    //         rule = rule.substr(pos + 1, rule.length);
    //       }
  
    //       switch (rule) {
    //         case 'required':
    //           if (i.val() === '') {
    //             ferror = ierror = true;
    //           }
    //           break;
  
    //         case 'minlen':
    //           if (i.val().length < parseInt(exp)) {
    //             ferror = ierror = true;
    //           }
    //           break;
  
    //         case 'email':
    //           if (!emailExp.test(i.val())) {
    //             ferror = ierror = true;
    //           }
    //           break;
  
    //         case 'checked':
    //           if (! i.is(':checked')) {
    //             ferror = ierror = true;
    //           }
    //           break;
  
    //         case 'regexp':
    //           exp = new RegExp(exp);
    //           if (!exp.test(i.val())) {
    //             ferror = ierror = true;
    //           }
    //           break;
    //       }
    //       i.next('.validation').html((ierror ? (i.attr('data-msg') !== undefined ? i.attr('data-msg') : 'wrong Input') : '')).show('blind');
    //     }
    //   });
    //   f.children('textarea').each(function() { // run all inputs
  
    //     var i = $(this); // current input
    //     var rule = i.attr('data-rule');
  
    //     if (rule !== undefined) {
    //       var ierror = false; // error flag for current input
    //       var pos = rule.indexOf(':', 0);
    //       if (pos >= 0) {
    //         var exp = rule.substr(pos + 1, rule.length);
    //         rule = rule.substr(0, pos);
    //       } else {
    //         rule = rule.substr(pos + 1, rule.length);
    //       }
  
    //       switch (rule) {
    //         case 'required':
    //           if (i.val() === '') {
    //             ferror = ierror = true;
    //           }
    //           break;
  
    //         case 'minlen':
    //           if (i.val().length < parseInt(exp)) {
    //             ferror = ierror = true;
    //           }
    //           break;
    //       }
    //       i.next('.validation').html((ierror ? (i.attr('data-msg') != undefined ? i.attr('data-msg') : 'wrong Input') : '')).show('blind');
    //     }
    //   });
    //   if (ferror) return false;
    //   else var str = $(this).serialize();
    //   var action = $(this).attr('action');
    //   if( ! action ) {
    //     action = 'contactform/contactform.php';
    //   }
    //   $.ajax({
    //     type: "POST",
    //     url: action,
    //     data: str,
    //     success: function(msg) {
    //       // alert(msg);
    //       if (msg == 'OK') {
    //         $("#sendmessage").addClass("show");
    //         $("#errormessage").removeClass("show");
    //         $('.contactForm').find("input, textarea").val("");
    //       } else {
    //         $("#sendmessage").removeClass("show");
    //         $("#errormessage").addClass("show");
    //         $('#errormessage').html(msg);
    //       }
  
    //     }
    //   });
    //   return false;
    // });
    const hostEventForm = document.getElementById('host_event_form');
    hostEventForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission
    
        // Collecting the values from the form
        let data = {
            name: document.querySelector('[name=name]').value,
            info: document.querySelector('[name=info]').value,
            venue: document.querySelector('[name=venue]').value,
            date: document.querySelector('[name=date]').value,
            grade1_price: parseFloat(document.querySelector('[name=grade1_price]').value),
            grade2_price: parseFloat(document.querySelector('[name=grade2_price]').value),
            grade3_price: parseFloat(document.querySelector('[name=grade3_price]').value),
            description: document.querySelector('[name=description]').value,
            url: document.querySelector('[name=url]').value
        }
    
        // Logging the data to check if everything is correct
        console.log(data);
    
        // Sending the data to the server using Fetch API
        fetch('http://127.0.0.1:8000/api/eventrequest', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data), // Sending the data as JSON
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Event created successfully!');
                window.location.replace('/event'); // Redirecting to the event page or another page after success
            } else {
                alert('Event creation failed: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while submitting the form. Please try again.');
        });
    });
    
  
  });
  