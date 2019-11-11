const calculateModifier = (stat) => {
  let modifier = Math.floor(0.5*(stat - 10));
  if (stat === '') {
    return '--';
  } else if (modifier >= 0) {
    return `+${modifier}`;
  } else {
    return `${modifier}`;
  }
};

const updateModifier = (input) => {
  const modifier = calculateModifier(input.value);
  $(input).siblings('.modifier').text(modifier);
}

// ---- FORM FEEDBACK ---- //
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
    removeErrorStyling();
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

  const csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
  const inputs = document.querySelectorAll('.text-area');
  const characterInfo = {};
  for (const input of inputs) {
    characterInfo[input.name] = input.value;
  }

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
    $('#status').text('Sorry something\'s gone wrong...');
  }
}

const main = () => {
  const stats = document.querySelectorAll('.text-area-stat');
  for (const input of stats) {
    updateModifier(input);
  }

  const saveButton = document.getElementById('save-button');
  saveButton.onclick = submitForm;
  $('.text-area').on('keyup paste', updateStatus);
  $('.text-area-stat').on('keyup', (e) => updateModifier(e.target));
}

window.onload = main;
