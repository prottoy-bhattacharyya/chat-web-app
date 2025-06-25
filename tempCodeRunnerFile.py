cursor.execute("select full_name from users where id = %s", (receiver_id,))
            receiver_full_name = cursor.fetchone()[0]
