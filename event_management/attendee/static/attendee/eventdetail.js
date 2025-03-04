<script>
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
  });
</script>