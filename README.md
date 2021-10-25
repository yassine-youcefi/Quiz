# Quiz
Quiz management application for  BRENCO code challenge 


# 1- Web interface :
- The web application has authentication with two roles (admin,students)

 ![](main/static/signup.gif)

### Admin :
Can create, update and delete quizzes, and also be able to create questions and answers ro each quiz, each admin can control his own quizzes.

- Note : I applied some modifications concerning the specifications, when the answers have a boolean field which represents is the answer is correct or not , and the system will be calcul the user results and save it later   

 ![](main/static/admin.gif)

### Students :
The student after having connected to his session, he will be able to choose one of the quizzes, then click to start, after having applied his own answers the results will be displayed.

- Note:
the students must respect the tempt of the exam, if not the exam will be kept in the state or the time and finish

 ![](main/static/students.gif)

### Next : add the result page and custom answers.

--- 
---

# 2- CRUD APIs :

