class carVersion:
    conn = None

    def init(self, conn, item):
        self.conn = conn
        if 'id' not in item and 'name' in item:
            self.exists(conn.cursor(), item)
        if 'id' in item and 'images' in item:
            self.updateImage(conn.cursor(), item)
        if 'id' in item and 'param_config' in item:
            self.updateConfig(conn.cursor(), item)

    def insert(self, cursor, item):
        insert_sql = """insert into car_version(`brand_id`,`brand_model_id`,`name`,`classify`,`style_year`,`spider_url`) VALUES(%s,%s,%s,%s,%s,%s) """
        cursor.execute(insert_sql,
                       (item['brand_id'], item['brand_model_id'], item['name'], item['classify'], item['style_year'],
                        item['spider_url']))
        item['id'] = cursor.lastrowid
        self.conn.commit()

    def exists(self, cursor, item):
        cursor.execute(
            """SELECT id FROM car_version WHERE `name` = '%s' and `brand_id` = %s and `brand_model_id` = %s""" % (
                item['name'], item['brand_id'], item['brand_model_id']))
        id = cursor.fetchone()
        if id is None:
            self.insert(cursor, item)
        else:
            item['id'] = id['id']
            self.updateClassify(cursor, item)

    def updateImage(self, cursor, item):
        sql = """UPDATE car_version SET `images`=%s where id=%s"""
        cursor.execute(sql, (item['images'], item['id']))
        self.conn.commit()
    def updateConfig(self, cursor, item):
        sql = """UPDATE car_version SET `param_config`=%s where id=%s"""
        cursor.execute(sql, (item['param_config'], item['id']))
        self.conn.commit()

    def updateClassify(self, cursor, item):
        sql = """UPDATE car_version SET `classify`=%s,`spider_url`=%s where id=%s"""
        cursor.execute(sql, (item['classify'], item['spider_url'], item['id']))
        self.conn.commit()
