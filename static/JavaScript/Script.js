// Array mit den Dateinamen der Designbilder
var designImages = [];
for (var i = 1; i <= 30; i++) {
  designImages.push("design" + i + ".jpg");
}
//print(designImages);

                  
var currentImageIndex = 0;
console.log(currentImageIndex)

// Funktion zum Ändern des Designbilds
function changeImage(direction) {
  if (direction === "prev") {
    if (currentImageIndex > 0) {
      currentImageIndex--;
      console.log(currentImageIndex)
    } else {
      currentImageIndex = designImages.length - 1;
      console.log(currentImageIndex)
    }
  } else if (direction === "next") {
    if (currentImageIndex < designImages.length - 1) {
      currentImageIndex++;
      console.log(currentImageIndex)
    } else {
      currentImageIndex = 0;
      console.log(currentImageIndex)
    }
  }

  var currentImage = document.getElementById("current-image");
  var newImageSource = "/static/images/" + designImages[currentImageIndex];
  currentImage.src = newImageSource;
  document.getElementById("myIndex").value = currentImageIndex;
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

function validateForm() {
  var inputFields = document.getElementsByTagName("input");
  var textareaField = document.getElementById("message");
  var selectedField;

  // Check if any input field is empty
  for (var i = 0; i < inputFields.length; i++) {
    if (inputFields[i].value === "") {
      selectedField = inputFields[i];
      break;
    }
  }

  // Check if the textarea field is empty
  if (textareaField.value === "") {
    selectedField = textareaField;
  }

  // Display validation result
  if (selectedField) {
    alert("Please fill in all fields.");
    selectedField.focus();
    return false;
  } else {
    return true;
  }
}
