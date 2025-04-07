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

      
      let data = {
          event_name: document.querySelector('[name=event_name]').value,
          event_place: document.querySelector('[name=event_place]').value,
          attendees: document.querySelector('[name=attendees]').value,
          price: document.querySelector('[name=price]').value,
          date: document.querySelector('[name=date]').value,
          discription: document.querySelector('[name=discription]').value,
          
      }

      // console.log(JSON.stringify(data))
      console.log(data)

      // fetch('http://127.0.0.1:8000/api/register', {
      //     method: 'POST',
      //     body: JSON.stringify(data),
      // })
      // .then(response => response.json())
      // .then(data => {
      //     if (data.success) {
      //         alert('Registration successful! You can now log in.');
      //         window.location.replace('/event');
      //         // Optionally redirect to login page or clear the form
      //     } else {
      //         alert('Registration failed: ' + data.message);
      //     }
      // })
      // .catch(error => {
      //     console.error('Error:', error);
      // });

      console.log("akldjflksajdf")
  });
  
  });
  