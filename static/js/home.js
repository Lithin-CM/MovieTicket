function togglePostTaggedItemsDiv() {
    var postTaggedItemsDisplay = document.getElementById("postTaggedItemsDisplay");
    var postTaggedItems = document.getElementById("postTaggedItems");
    postTaggedItemsDisplay.classList.toggle("show");
    postTaggedItems.classList.toggle("show");
}

// carousel starting 
var slideIndex = 0;
showSlides();

function showSlides() {
    var slides = document.getElementsByClassName("carousel-slide");
    for (var i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) { slideIndex = 1 }
    slides[slideIndex - 1].style.display = "block";
    setTimeout(showSlides, 4000); // Change image every 2 seconds
}

function nextSlide() {
    var slides = document.getElementsByClassName("carousel-slide");
    slideIndex++;
    if (slideIndex > slides.length) { slideIndex = 1 }
    showSlides();
}

function prevSlide() {
    var slides = document.getElementsByClassName("carousel-slide");
    slideIndex--;
    if (slideIndex < 1) { slideIndex = slides.length }
    showSlides();
}

// carousel ending