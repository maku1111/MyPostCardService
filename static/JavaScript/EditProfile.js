// Google tags for google analytics
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());

gtag('config', 'G-8SW1RGVWR2');

// function to validate if password and confirmed password are the same
function validateForm() {
  var newPassword = document.getElementById('newPassword').value;
  var confirmPassword = document.getElementById('confirmPassword').value;

  if (newPassword !== confirmPassword) {
    alert('Passwords do not match.');
    return false; // formular will not be sent
  }

  return true; // formular will be sent
}
