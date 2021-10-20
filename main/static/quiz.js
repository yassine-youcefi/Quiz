
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
        // console.log(question);
        // console.log(answers);
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

const scoreDiv = document.getElementById('score-div');
const resulsDiv = document.getElementById('results-div');

  $.ajax({
    url: link + 'results/',
    type: 'POST',
    data: data,
    success: function(result) {

      const results = result.results;
      quizDetailsForm.classList.add('not-visible');
      console.log('quizDetailsForm.classList = ', quizDetailsForm.classList);
      console.log('results = ', result);


      scoreDiv.innerHTML = `<div>${result.passed ?  ' Congratulatons!  ' : 'Failed ... '} your results is ${result.score.toFixed(2)}% </div>`

      // _________/   for the results page   \_________
      results.forEach(element => {
        const responseDiv = document.createElement('div');
        for (const [question, answer] of Object.entries(element)) {
          responseDiv.innerHTML += question
          const cls = ['contaier', 'p-3', 'text-light', 'h3']
          responseDiv.classList.add(...cls);

          if (element == 'awnser not found') {
            responseDiv.innerHTML += 'awnser not found'
            responseDiv.classList.add('bg-danger');
          }
          else {
            console.log('elements = ', element[question]);

            const answer = element[question]['answered']; 
            const correct_answers = element[question]['correct_answer'];
            
            
            if (answer == correct_answers) {
              
              responseDiv.classList.add('bg-success');
              responseDiv.innerHTML += ` your answer is : ${answer}`
        } else {
              responseDiv.classList.add('bg-danger');
              responseDiv.innerHTML += ` the correct answer is : ${correct_answers}`
              responseDiv.innerHTML += ` answered : ${answer}`
          }



        }
      }
      const body = document.getElementById('form-div');
      // console.log('body = ',body)
      resulsDiv.append(responseDiv);


    })
      
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