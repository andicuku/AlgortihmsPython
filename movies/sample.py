from .db import Session
from .models import Person, Movie, Category, User


def populate_db():
    session = Session()

    comedy = Category(name="Comedy")
    adventure = Category(name="Adventure")
    animation = Category(name="Animation")
    drama = Category(name="Drama")
    horror = Category(name="Horror")
    action = Category(name="Action")
    western = Category(name="Western")
    scifi = Category(name="Science Fiction")

    session.add_all(
        [comedy, adventure, animation, drama, horror, action, western, scifi]
    )

    # directors
    pj = Person(first_name="Peter", last_name="Jackson")
    ss = Person(first_name="Steven", last_name="Spielberg")
    cn = Person(first_name="Christofer", last_name="Nolan")
    ffc = Person(first_name="Francis", last_name="Ford-Coppola")

    # producers
    jl = Person(first_name="John", last_name="Lennon")
    pm = Person(first_name="Paul", last_name="McCartney")
    gh = Person(first_name="George", last_name="Harrison")
    rs = Person(first_name="Ringo", last_name="Starr")

    # actors
    brad = Person(first_name="Brad", last_name="Pitt")
    tom = Person(first_name="Tom", last_name="Hardy")
    al = Person(first_name="Al", last_name="Paccino")
    george = Person(first_name="George", last_name="Clooney")
    john = Person(first_name="Johny", last_name="Depp")
    angelina = Person(first_name="Angeline", last_name="Jolie")
    marlon = Person(first_name="Marlon", last_name="Brando")
    robert = Person(first_name="Robert", last_name="De Niro")

    session.add_all(
        [
            pj,
            ss,
            cn,
            ffc,
            jl,
            pm,
            gh,
            rs,
            brad,
            tom,
            al,
            george,
            john,
            angelina,
            marlon,
            robert,
        ]
    )

    movies = [
        Movie(
            title="Soul",
            description="Soul the movie",
            year=2020,
            budget=20_000_000,
            bo_returns=100_000_000,
            director=pj,
            producer=jl,
            rating=8.1,
            category=animation,
            actors=[brad, tom, al],
        ),
        Movie(
            title="The Dark Knight",
            description="Batman movie",
            year=2010,
            rating=7.5,
            budget=100_000_000,
            bo_returns=500_000_000,
            director=cn,
            producer=rs,
            category=action,
            actors=[george, john, angelina],
        ),
        Movie(
            title="The Theory of Everything",
            description="Theory of all things",
            year=2017,
            rating=6.5,
            budget=5_000_000,
            bo_returns=35_000_000,
            director=ss,
            producer=pm,
            category=drama,
            actors=[angelina, tom, brad],
        ),
        Movie(
            title="Avengers",
            description="superheroes",
            year=2018,
            rating=9.2,
            budget=500_000_000,
            bo_returns=2_000_000_000,
            director=cn,
            producer=gh,
            category=action,
            actors=[tom, brad, angelina, al],
        ),
        Movie(
            title="The Godfather",
            description="Mafia",
            year=1970,
            rating=9.9,
            budget=1_000_000,
            bo_returns=800_000_000,
            director=ffc,
            producer=jl,
            category=drama,
            actors=[marlon, al, robert, tom],
        ),
    ]

    session.add_all(movies)

    users = [
        User(username="gledi"),
        User(username="juli"),
        User(username="kevin"),
        User(username="andi"),
        User(username="johana"),
        User(username="arjola"),
        User(username="lutmira"),
        User(username="izaura"),
    ]

    session.add_all(users)

    session.commit()
