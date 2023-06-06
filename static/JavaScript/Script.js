// Array mit den Dateinamen der Designbilder
var designImages = ["design1.jpg", "design2.jpg", "design3.jpg"];
var currentImageIndex = 0;

// Funktion zum Ändern des Designbilds
function changeImage(direction) {
  if (direction === "prev") {
    if (currentImageIndex > 0) {
      currentImageIndex--;
    } else {
      currentImageIndex = designImages.length - 1;
    }
  } else if (direction === "next") {
    if (currentImageIndex < designImages.length - 1) {
      currentImageIndex++;
    } else {
      currentImageIndex = 0;
    }
  }

  var currentImage = document.getElementById("current-image");
  var newImageSource = "/static/images/" + designImages[currentImageIndex];
  currentImage.src = newImageSource;
}

// Event-Listener für den "Previous" Button
var prevButton = document.querySelector(".prev-button");
prevButton.addEventListener("click", function() {
  changeImage("prev");
});

// Event-Listener für den "Next" Button
var nextButton = document.querySelector(".next-button");
nextButton.addEventListener("click", function() {
  changeImage("next");
});

