from queries.pool import pool

class UserQueries:
    def get_all_users(self):
        with pool.connection () as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT id, first, last, avatar, email, username
                    FROM users
                    ORDER BY last, first
                    """
                )
                results = []
                for row in db.fetchall():
                    record = {}
                    for i, column in enumerate(db.description):
                        record[column.name] = row[i]
                    results.append(record)
                return results

    def get_user(self, id):
        with pool.connection () as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT id, first, last, avatar, email, username
                    FROM users
                    WHERE id = %s
                    """,
                    [id],
                )
                record = None
                row = db.fetchone()
                if row is not None:
                    record = {}
                    truck_fields = [
                        'truck_id',
                        'name',
                        'website',
                        'category',
                        'vegetarian_friendly'
                    ]
                for i, column in enumerate(db.description):
                    if column.name in truck_fields:
                        record[column.name] = row[i]
                return record



class TruckQueries:
    def get_truck(self, truck_id):
        with pool.connection () as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT u.id as user_id, u.first, u.last, u.avatar, u.email, u.username,
                    t.id as truck_id, t.name, t.website, t.category, t.vegetarian_friendly
                    FROM users u
                    JOIN trucks t ON(u.id = t.owner_id)
                    WHERE t.id = %s
                    """,
                    [truck_id],
                )

                truck = None
                row = db.fetchone()
                if row is not None:
                    truck = {}
                    for i, column in enumerate(db.description):
                        truck[column.name] =  row[i]
                truck['id'] = truck['truck_id']

                owner = {}
                owner_fields =
