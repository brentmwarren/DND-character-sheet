
const submitForm = async (e) => {
  e.preventDefault()
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
    console.log('you did it!');
  } else if (response.status == 400) {
    const errors = await response.json()
    console.log(errors);
  } else {
    console.log('boooo....server side');
  }
}

const main = () => {
  const saveButton = document.getElementById('save-button');
  saveButton.onclick = submitForm;
}

window.onload = main;
