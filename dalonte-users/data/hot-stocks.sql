DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER NOT NULL PRIMARY KEY,
    first TEXT NOT NULL,
    last TEXT NOT NULL,
    avatar TEXT NOT NULL,
    email TEXT NOT NULL,
    username TEXT NOT NULL,
    referrer_id INTEGER REFERENCES users("id") ON DELETE CASCADE
)

INSERT INTO users VALUES
    (1, 'Winnie', 'Pooh', '17000.jpeg', 'wpooh@gmail.com', 'wpooh', null),
    (2, 'Cheshire', 'Cat', '17001.jpeg', 'ccat@gmail.com', 'ccat', null),
    (3, 'Tinky', 'Winky', '17002.jpeg', 'twinky@gmail.com', 'twinky', null),
