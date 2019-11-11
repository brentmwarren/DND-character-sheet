
const parseErrors = (err) => {
  for (const field in err) {
    $(`*[name="${field}"]`).css('border', '2px solid #b22222');
    $('#err-feedback').append(`
      <div class="error-msg">
        ${field}: ${err[field][0].message}
      </div>`);
  }
};

const updateStatus = function() {
  if ($(this).val() != $(this).data('server-value')) {
    $('#status').text('UNSAVED CHANGES');
  } else {
    $('#status').text('No unsaved changes.');
  }
};

const updateServerData = (updated) => {
  for (const field in updated) {
    $(`input[name="${field}"]`).attr('data-server-value', `${updated[field]}`);
  }
};

const removeErrorStyling = () => {
  $('#err-feedback').empty();
  $('input').css('border', '2px solid #cccccc');
};

const submitForm = async (e) => {
  e.preventDefault();
  removeErrorStyling();
  const inputs = document.querySelectorAll('input');
  const characterInfo = {};
  let csrf_token;

  for (const input of inputs) {
    if (input.name === 'csrfmiddlewaretoken') {
      csrf_token = input.value;
    } else {
      characterInfo[input.name] = input.value;
    }
  }
  characterInfo['notes'] = $('.text-area-notes').val();

  const pk = window.location.pathname.split('/')[2];
  const response = await fetch(
    `/characters/${pk}/edit/`,
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrf_token,
      },
      body: JSON.stringify(characterInfo),
    }
  );

  if (response.status === 200) {
    $('#status').text('No unsaved changes.');
    console.log('you did it!');
    const updated = await response.json();
    updateServerData(updated);
  } else if (response.status == 400) {
    const errors = await response.json();
    parseErrors(errors);
  } else {
    console.log('boooo....server side');
  }
}

const main = () => {
  const saveButton = document.getElementById('save-button');
  saveButton.onclick = submitForm;
  $('.text-area').on('change keyup paste', updateStatus);
}

window.onload = main;
