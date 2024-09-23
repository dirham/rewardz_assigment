# Book rental 
is a book rental app that using openlibarary api to search a book and simulate book rentals and calculate the fee automatically for extended rent.

### Up and run using Docker
You need Docker and docker compose installed before run the command below:

- Clone this project `git@github.com:dirham/rewardz_assigment.git`
- Go to rewardz_assigment `cd rewardz_assigment`
- run `docker compose up -d`
- now the applications is running on port 8000
- create super user with: `docker exec -it book_rentalz sh -c "python manage.py createsuperuser"`


You now can access the service on this <a href="http://localhost:8000">link</a> or visit admin page <a href="http://localhost:8000">here</a>

You also could create student account through this <a href="http://localhost:8000/register/">link</a>. Currently all registerd student will be active and could be used for login

### Things not to expect on this project:
This project is far from perfect,this the thing we expect to be added later:
- Separated the settigns (base.py, dev.py and prod.py)
- Unit test
- Caching response from the openlibrary api using redis or memcache to reduce api call
- Update the UI and UX
