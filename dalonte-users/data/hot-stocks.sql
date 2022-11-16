DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS trucks;
DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS truck_menu_items;
DROP TABLE IF EXISTS menu_items;

CREATE TABLE users (
  id INTEGER NOT NULL UNIQUE,
  first TEXT NOT NULL,
  last TEXT NOT NULL,
  avatar TEXT NOT NULL,
  email TEXT NOT NULL,
  username TEXT NOT NULL
);

CREATE TABLE trucks (
  id INTEGER NOT NULL UNIQUE,
  name TEXT NOT NULL,
  website TEXT NOT NULL,
  category TEXT NOT NULL,
  vegetarian_friendly BOOLEAN NOT NULL,
  owner_id INTEGER NOT NULL REFERENCES users(id)
);

CREATE TABLE reviews (
  id INTEGER NOT NULL UNIQUE,
  title TEXT NOT NULL,
  content TEXT NOT NULL,
  reviewer_id INTEGER REFERENCES users("id"),
  rating INTEGER NOT NULL,
  truck_id INTEGER NOT NULL REFERENCES trucks("id")
);

CREATE TABLE truck_menu_items (
  truck_id INTEGER NOT NULL REFERENCES trucks("id"),
  menu_item_id INTEGER NOT NULL REFERENCES menu_items("id"),
  price INTEGER NOT NULL
);

CREATE TABLE menu_items (
    id INTEGER NOT NULL UNIQUE,
    name TEXT NOT NULL,
    calories INTEGER NOT NULL
);

INSERT INTO users VALUES
    (1, 'Winnie', 'Pooh', '17000.jpeg', 'wpooh@gmail.com', 'wpooh', null),
    (2, 'Cheshire', 'Cat', '17001.jpeg', 'ccat@gmail.com', 'ccat', null),
    (3, 'Tinky', 'Winky', '17002.jpeg', 'twinky@gmail.com', 'twinky', null),
;

INSERT INTO trucks VALUES
    (1, 'Best Truck', 'besttruck.com', 'French', true, null),
    (2, 'Worst Truck', 'worsttruck.com', 'French', false, null),
;
