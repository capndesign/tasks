let csrf = document.querySelector('meta[name=csrftoken]').content
  , form = document.querySelector(".Form--task-add");

form.onsubmit = e => {
  e.preventDefault()

  fetch('/task/add', {
    method: 'post',
    credentials: 'same-origin',
    headers: {
      'X-CSRFToken': csrf,
      'X-Requested-With': 'XMLHttpRequest'
    },
    body: new FormData(form)
  })
    .then(response => {
      console.log(response)
    })
}