// SIGN UP FORM

const form = document.querySelector('form');

const validate = () => {
  let formIsValid = true;
  $('.invalid-feedback').remove();
  $('.signup-input').removeClass('is-invalid');

  $('.signup-input').each((index, element) => {
    if (element.value === '' || element.value === undefined) {
      formIsValid = false;
      $(element).addClass('is-invalid');
      if (element.name === 'password2') {
          $(element).parent('div').append(`
              <div class="invalid-feedback">
                  Please confirm your password.
              </div>
          `);
      } else {
        $(element).parent('div').append(`
          <div class="invalid-feedback">
            Please enter your ${element.name}.
          </div>
        `);
      }
    } else if (element.type === 'password' && element.value.length < 4) {
      formIsValid = false;
      $(element).addClass('is-invalid');
      $(element).parent('div').append(`
        <div class="invalid-feedback">
          Password must be at least 4 characters.
        </div>
      `);
    } else if (element.type === 'email' && !RegExp('[^@]+@([^@]\.)+([^@]+)').test(element.value)) {
      formIsValid = false;
      $(element).addClass('is-invalid');
      $(element).parent('div').append(`
        <div class="invalid-feedback">
          Please enter a valid email address.
        </div>
      `);
    } else if (form.id === 'signup') {
      if ($(`#password`).val() !== $(`#password2`).val()) {
        formIsValid = false;
        if (element.type === "password") {
          $(element).addClass('is-invalid');
          $(element).parent('div').append(`
            <div class="invalid-feedback">
              Passwords do not match.
            </div>
          `);
        }
      }
    }
  });
  return formIsValid;
};

const parseErrors = (err) => {
  for (const field in err) {
    $(`*[name="${field}"]`).addClass('is-invalid');
    $(`*[name="${field}"]`).after(`<p class="invalid-feedback">${err[field]}</p>`);
  }
};

const submitSignUpForm = async (e) => {
  e.preventDefault();

  const inputs = document.querySelectorAll('input');
  const csrf_token = inputs[0].value;
  console.log(csrf_token);

  const userInfo = {};
  for (const input of inputs) {
    if (input.name !== 'csrfmiddlewaretoken') {
      userInfo[input.name] = input.value;
    }
  }
  const isValid = validate();
  console.log(isValid);
  if (isValid) {
    const response = await fetch(
      '/signup/',
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrf_token,
        },
        body: JSON.stringify(userInfo),
      }
    );

    if (response.status == 200) {
      console.log('success');
      window.location.replace(`/characters/`);
    } else if (response.status == 400) {
      console.log('400! client side');
      const errors = await response.json();
      parseErrors(errors);
    } else {
      console.log('oops, server side');
    }
  }
};

const main = () => {
  $('button').on('click', submitSignUpForm);
  $('input').on('keyup', function() {
    $(this).removeClass('is-invalid');
    $(this).siblings('.invalid-feedback').remove();
  });
};

window.onload = main;
