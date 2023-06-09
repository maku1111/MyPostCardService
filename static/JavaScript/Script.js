// Array mit den Dateinamen der Designbilder
var designImages = ["design1.jpg", "design2.jpg", "design3.jpg", "design4.jpg", "design5.jpg", "design6.jpg",
                    "design7.jpg", "design8.jpg", "design9.jpg", "design10.jpg", "design11.jpg", "design12.jpg",
                    "design13.jpg", "design14.jpg", "design15.jpg", "design16.jpg", "design17.jpg", "design18.jpg",
                    "design19.jpg", "design20.jpg", "design21.jpg", "design22.jpg", "design23.jpg", "design24.jpg",
                    "design25.jpg", "design26.jpg", "design27.jpg", "design28.jpg", "design29.jpg", "design30.jpg"               
                  ];
                  
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
