## Vastubhandar (e-commerce platform)
_________________________________________________________________________________________________
* ###### **Setup :-**
  clone the repo using Http -
  ```
  git clone https://github.com/nakushwah/c-commerce_demo.git
  ```
  
* ###### **Requirments :-**
    ```
     See the requirments.txt file and run the command 
     pip3 install -r requirments.txt
    ```
    ```      
        * Django==3.2.8
        * celery==5.2.0
        * redis==4.0.0
        * Docker
        * RabbitMq  
    ```
* ###### configuration :- 
  install celery
  ```
      pip install celery
  ```
   For install redis-server  follow the link 
  ```
      https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-20-04 
   ```
  
  install RabbitMQ-server
  ```
     sudo apt install rabbitmq-server
  ```
  Install Stripe CLi on Linux without a package manager
  ```
  * step-1 : Download the latest linux tar.gz file from
  * step-2 : https://github.com/stripe/stripe-cli/releases/latest
  * step-3 : Unzip the file: tar -xvf stripe_X.X.X_linux_x86_64.tar.gz 
  * step-4 : Move ./stripe to your execution path.
  
  for other OS based syetem Follow the link : https://stripe.com/docs/stripe-cli
  ```
  
  

* ###### **Start the Project :-**
  For running the project we have to use three terminal tab because we are using Celery , Django , Stripe_cli
  before starting Django's server start the Celery and Stripe cli in diff terminal tab 
  
  **_Start celery worker_** 
  * ```
     celery -A VastuBhandar worker -l info
    ```
  _**start Stripe cli listen  command**_
  * ```
       stripe listen --forward-to localhost:8000/payments/my_webhook_view/
    ```
  **_Start the Django's Server_**
  * ```
      ./manage.py runserver
    ```



















