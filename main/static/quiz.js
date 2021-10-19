
const link = window.location.href;

var myHeaders = new Headers();

var requestOptions = {
    method: 'GET',
    headers: myHeaders,
    redirect: 'follow'
  };


  fetch(link + 'data/', requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));  
