
const link = window.location.href;
let myHeaders = new Headers();

const quizDiv = document.getElementById('quiz-div');
let data

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
 