(function($) {
    "use strict";

    // Mobile Nav toggle
    $('.menu-toggle > a').on('click', function(e) {
        e.preventDefault();
        $('#responsive-nav').toggleClass('active');
    });

    // Fix cart dropdown from closing
    $('.cart-dropdown').on('click', function(e) {
        e.stopPropagation();
    });

    /////////////////////////////////////////

    // Products Slick
    $('.products-slick').each(function() {
        var $this = $(this),
            $nav = $this.attr('data-nav');

        $this.slick({
            slidesToShow: 4,
            slidesToScroll: 1,
            autoplay: true,
            autoplaySpeed: 2000, // Adjust autoplay speed as needed
            infinite: true,
            speed: 300,
            dots: true, // Show dots for slide indicator
            arrows: true,
            appendArrows: $nav ? $nav : false,
            responsive: [{
                    breakpoint: 991,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1,
                    }
                },
                {
                    breakpoint: 480,
                    settings: {
                        slidesToShow: 1,
                        slidesToScroll: 1,
                    }
                },
            ]
        });
    });

    // Product Main img Slick
    $('#product-main-img').slick({
        infinite: true,
        speed: 300,
        dots: false,
        arrows: true,
        fade: true,
        asNavFor: '#product-imgs',
    });

    // Product imgs Slick
    $('#product-imgs').slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        arrows: true,
        centerMode: true,
        focusOnSelect: true,
        centerPadding: 0,
        vertical: true,
        asNavFor: '#product-main-img',
        responsive: [{
            breakpoint: 991,
            settings: {
                vertical: false,
                arrows: false,
                dots: true,
            }
        }, ]
    });

    // Product img zoom
    var zoomMainProduct = document.getElementById('product-main-img');
    if (zoomMainProduct) {
        $('#product-main-img .product-preview').zoom();
    }

    /////////////////////////////////////////

    // Initialize currentSlide variable
let currentSlide = 0;

// Get all slide elements
const slides = document.querySelectorAll('.slide');

// Total number of slides
const totalSlides = slides.length;

// Function to show a specific slide by index
function showSlide(index) {
    // Get the previous active slide
    const prevSlide = document.querySelector('.slide.active');
    
    // Get the next slide
    const nextSlide = slides[index];

    // Add split-animation class to the previous slide
    prevSlide.classList.add('split-animation');

    // Apply a slight delay before removing the active class to allow animation to start
    setTimeout(() => {
        prevSlide.classList.remove('active');
        nextSlide.classList.add('active');
    }, 500); // Adjust delay time as needed

    // Reset opacity to ensure smooth transition
    prevSlide.style.opacity = 1;
    nextSlide.style.opacity = 1;

    // Update slide indicators
    updateIndicators(index);
}

// Function to update slide indicators
function updateIndicators(index) {
    const indicatorDots = document.querySelectorAll('.indicator-dot');
    indicatorDots.forEach((dot, i) => {
        if (i === index) {
            dot.classList.add('active');
        } else {
            dot.classList.remove('active');
        }
    });
}

// Function to handle next slide
function nextSlide() {
    // Calculate the index of the next slide
    currentSlide = (currentSlide + 1) % totalSlides;
    // Show the next slide
    showSlide(currentSlide);
}

// Function to handle previous slide
function prevSlide() {
    // Calculate the index of the previous slide
    currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
    // Show the previous slide
    showSlide(currentSlide);
}

// Get references to next and previous buttons
const nextButton = document.getElementById('nextBtn');
const prevButton = document.getElementById('prevBtn');

// Add event listeners for next and previous buttons
nextButton.addEventListener('click', nextSlide);
prevButton.addEventListener('click', prevSlide);

// Generate slide indicators
const slideIndicator = document.getElementById('slideIndicator');
for (let i = 0; i < totalSlides; i++) {
    const indicatorDot = document.createElement('span');
    indicatorDot.classList.add('indicator-dot');
    indicatorDot.addEventListener('click', () => {
        currentSlide = i;
        showSlide(currentSlide);
    });
    slideIndicator.appendChild(indicatorDot);
}

// Show the first slide initially
showSlide(currentSlide);

})(jQuery);
