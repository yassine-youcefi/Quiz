
const link = window.location.href;
const quizDiv = document.getElementById('quiz-div');
let data

// _________/   for the get quiz request   \_________
let myHeaders = new Headers();
myHeaders.append('Content-Type', 'application/json');

let requestOptions = {
    method: 'GET',
    headers: myHeaders,
    redirect: 'follow'
  };
  fetch(link + 'data/', requestOptions)
  .then(response => response.json())
  .then(result => {
    let data = result.questions;
    // console.log('data = ',data);
    data.forEach(element => {

      for(const [question, answers] of Object.entries(element)){
        console.log(question);
        console.log(answers);
        quizDiv.innerHTML += `
        <hr>
        <div class="mb-2">
            <p style = "margin-left:20px ;">${question}</p>
        </div>
        `
        answers.forEach(answer => {
          quizDiv.innerHTML += `
          <div class="form-check">
            <input class="answer-input" type="radio" name="${question}" id="${question}-${answer}" value="${answer}">
            <label class="answer-lable" for="${question}">
              ${answer}
            </label>
          </div>
          `
        })
      }
    })
  })
  .catch(error => console.log('error', error));  
 

// _________/   for the post quiz request   \_________
const quizDetailsForm = document.getElementById('quiz-details-form');
const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

const submitButton = () => {
  const elements = [...document.getElementsByClassName('answer-input')];
  let data = {}
  data['csrfmiddlewaretoken'] = csrfToken;

  elements.forEach(element => {
    if (element.checked) {
      data[element.name] = element.value;
    } else {
      if (!data[element.name]) {
        data[element.name] = '';
      }
    }
  })

  // let myHeaders = new Headers();
  // myHeaders.append('Content-Type', 'application/x-www-form-urlencoded');
  // console.log('data --- ',data);
  // console.log('submit ',csrfToken );

  // let requestOptions = {
  //   method: 'POST',
  //   headers: myHeaders,
  //   body: JSON.stringify(data),
  //   redirect: 'follow'
  // };
  // fetch(link + 'results/', requestOptions)
  // .then(response => response.json())
  // .then(result => {
  //   console.log('result = ', result);
  //   if (result.success) {
  //     alert('Thank you for your time!')
  //   } else {
  //     alert('Please answer all the questions')
  //   }
  // })
  // .catch(error => console.log('error', error));

  $.ajax({
    url: link + 'results/',
    type: 'POST',
    data: data,
    success: function(result) {
      console.log('result = ', result);
      if (result.success) {
        alert('Thank you for your time!')
      } else {
        alert('Please answer all the questions')
      }
    },
    error: function(error) {
      console.log('error', error);
    }
  });
}

quizDetailsForm.addEventListener('submit', (e) => {

    e.preventDefault();
    submitButton();

})