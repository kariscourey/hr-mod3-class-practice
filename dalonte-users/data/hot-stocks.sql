DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL NOT NULL PRIMARY KEY,
    first TEXT NOT NULL,
    last TEXT NOT NULL,
    avatar TEXT NOT NULL,
    email TEXT NOT NULL,
    username TEXT NOT NULL,
    referrer_id INTEGER REFERENCES users("id") ON DELETE CASCADE
)

CREATE TABLE trucks (
    id SERIAL NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    website TEXT NOT NULL,
    category TEXT NOT NULL check(category='American' or category='Asian' or category='French' or category='Mediterranean'),
    vegetarian_friendly BOOLEAN NOT NULL,
    owner_id INTEGER REFERENCES users("id") ON DELETE CASCADE
)

INSERT INTO users VALUES
    (1, 'Winnie', 'Pooh', '17000.jpeg', 'wpooh@gmail.com', 'wpooh', null),
    (2, 'Cheshire', 'Cat', '17001.jpeg', 'ccat@gmail.com', 'ccat', null),
    (3, 'Tinky', 'Winky', '17002.jpeg', 'twinky@gmail.com', 'twinky', null),
;

INSERT INTO trucks VALUES
    (1, 'Best Truck', 'besttruck.com', 'French', true, null),
    (2, 'Worst Truck', 'worsttruck.com', 'French', false, null),
;
