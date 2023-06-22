
//Google tags for goolge analytics
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());

gtag('config', 'G-8SW1RGVWR2');

// function to validate if password and confirmed password are the same
function validateForm() {
    var password = document.getElementById('password').value;
    var password_conf = document.getElementById('password_conf').value;

    if (password !== password_conf) {
      alert('Passwords do not match.');
      return false; // formular will not be sent
    }

    return true; // formular will be sent
  }

  // function to validate if all imput fields are filled
  function validateIfFilled() {
    var firstName = document.getElementById("firstName").value;
    var lastName = document.getElementById("lastName").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var passwordConf = document.getElementById("password_conf").value;

    // alert if one or more fields are not filled
    if (firstName === '' || lastName === '' || email === '' || password === '' || passwordConf === '') {
      alert('Please fill in all fields.');
      return false;
    }
  }
