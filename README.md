# ExpertSystemForDiabetes
This is an prototype for Expert System for Diabetes which uses a Neural Network to predict medicine class for Diabetes


This aim of the project is giving prescription to patients effected with diabetes. It uses neural network to predict class of the medicine which is grouped/divided 
on basis of sugar level ranges. It contains a pretty simple prescription form which takes the sugar levels,the current medicine taken and diabetic experience(Since
how many years the patient is effected with diabetes). The System analysis all of this and feed it to the neural network to predict the medicine class.
It is just a prototype. It can be enchanced much by adding additional information to the prescription form and datasets to give accurate result which then can be 
useful in real time.

Dataset:
The Dataset used is developed under supervision of doctor and by getting accustomed by the frequent patterns that the doctors follows it has been created.
It is a 5-features dataset and a target-class which is called medicine class, with 910 rows examples to train and test neural network.

Neural Network:
Neural Network has developed using keras with upto 97% of accuracy. The optimizer used of Adam and activation functions are ReLu and softmax.

Framework:
It was developed in django Framework which uses python. Hence the project is supported by django authentications and inbuild admin panel from django.

STEPS TO RUN PROJECT (ESD):

1. Create a Virtual django Environment and place the project directory in that folder with virtual django env.

2. Open the terminal/cmd and enter the command
          
          python manage.py runserver
   (if any error occurs saying that a particular package has not been install. Install it as it is listed in the installed apps object located in the settings.py
      file of django project).
      
3. Open your browser and type localhost:<portnumber>.

4. Register to the system and login to get to the prescription form and enter the details which will generate a prescription form.

5. Explore the application.

Thank You..
