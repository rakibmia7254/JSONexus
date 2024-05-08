import os
import uuid
import orjson

class JSONexus:
    def __init__(self, db_name):
        self.db_name = db_name
        if not os.path.exists(db_name):
            with open(db_name, 'wb') as f:
                f.write(orjson.dumps({}))
        with open(db_name, 'rb') as db:
            self.db = orjson.loads(db.read())

    def _read_db(self):
        with open(self.db_name, 'rb') as f:
            return orjson.loads(f.read())

    def _write_db(self, db):
        with open(self.db_name, 'wb') as f:
            f.write(orjson.dumps(db, option=orjson.OPT_INDENT_2))

    def insert(self, collection_name, data):
        db = self.db
        if collection_name not in db:
            db[collection_name] = []
        data['_id'] = str(uuid.uuid4())  # Add a UUID for each record
        db[collection_name].append(data)
        self._write_db(db)
        return {'status': 'success', "data": data}
    
    def insert_no_duplicate(self, collection_name, data):
        db = self.db
        if collection_name not in db:
            db[collection_name] = []
        for item in db[collection_name]:
            del item['_id']
            if item == data:
                return {"status": "duplicate exists", "data": item}
        data['_id'] = str(uuid.uuid4())  # Add a UUID for each record
        db[collection_name].append(data)
        self._write_db(db)
        return {'status':'success', "data": data}
    
    def insert_many(self, collection_name, data):
        db = self.db
        if collection_name not in db:
            db[collection_name] = []
        for item in data:
            item['_id'] = str(uuid.uuid4())
        db[collection_name].extend(data)
        self._write_db(db)
        return {'status':'success'}

    def create_collection(self, collection_name):
        db = self.db
        if collection_name not in db:
            db[collection_name] = []
            self._write_db(db)
            return {"status": "success", "name": collection_name}
        else:
            return {"status": "failed", "message": "Collection already exists"}

    def get_all(self):
        db = self.db
        return db
    
    def get_collection(self, collection_name):
        db = self.db
        return db[collection_name]
    
    def get_collections(self):
        db = self.db
        return list(db.keys())
    
    def drop_collection(self, collection_name):
        db = self.db
        if collection_name in db:
            del db[collection_name]
            self._write_db(db)
            return {"status": "success", "name": collection_name}
        else:
            return {"status": "failed", "message": "Collection not found"}

    def find(self, collection_name, query):
        db = self.db
        found_data = []
        for key, value in query.items():
            if isinstance(value, str) or isinstance(value, int):
                for i in db[collection_name]:
                    if key in list(i.keys()):
                        if i[key]==value:
                            found_data.append(i)
                return {'result': found_data}
            
            if "_op" in value.keys():
                if value["_op"] == "$gt":
                    if isinstance(value["_value"], int) or isinstance(value["_value"], float):
                        for i in db[collection_name]:
                            if key in list(i.keys()):
                                if i[key] > value["_value"]:
                                    found_data.append(i)
                elif value["_op"] == "$gte":
                    if isinstance(value["_value"], int) or isinstance(value["_value"], float):
                        for i in db[collection_name]:
                            if key in list(i.keys()):
                                if i[key] >= value["_value"]:
                                    found_data.append(i)
                elif value["_op"] == "$lt":
                    if isinstance(value["_value"], int) or isinstance(value["_value"], float):
                        for i in db[collection_name]:
                            if key in list(i.keys()):
                                if i[key] < value["_value"]:
                                    found_data.append(i)
                elif value["_op"] == "$lte":
                    if isinstance(value["_value"], int) or isinstance(value["_value"], float):
                        for i in db[collection_name]:
                            if key in list(i.keys()):
                                if i[key] <= value["_value"]:
                                    found_data.append(i)
                elif value["_op"] == "$eq":
                    for i in db[collection_name]:
                        if key in list(i.keys()):
                            if i[key] == value["_value"]:
                                found_data.append(i)
                elif value["_op"] == "$ne":
                    for i in db[collection_name]:
                        if key in list(i.keys()):
                            if i[key] != value["_value"]:
                                found_data.append(i)
                else:
                    return {'error': 'invalid operator'}

        return {'result': found_data}
    
    def find_one(self, collection_name, query):
        db = self.db
        for key, value in query.items():
            if isinstance(value, str) or isinstance(value, int):
                for i in db[collection_name]:
                    if key in list(i.keys()):
                        if i[key]==value:
                            return i
            if "_op" in value.keys():
                if value["_op"] == "$gt":
                    if isinstance(value["_value"], int) or isinstance(value["_value"], float):
                        for i in db[collection_name]:
                            if key in list(i.keys()):
                                if i[key] > value["_value"]:
                                    return i
                elif value["_op"] == "$gte":
                    if isinstance(value["_value"], int) or isinstance(value["_value"], float):
                        for i in db[collection_name]:
                            if key in list(i.keys()):
                                if i[key] >= value["_value"]:
                                    return i
                elif value["_op"] == "$lt":
                    if isinstance(value["_value"], int) or isinstance(value["_value"], float):
                        for i in db[collection_name]:
                            if key in list(i.keys()):
                                if i[key] < value["_value"]:
                                    return i
                elif value["_op"] == "$lte":
                    if isinstance(value["_value"], int) or isinstance(value["_value"], float):
                        for i in db[collection_name]:
                            if key in list(i.keys()):
                                if i[key] <= value["_value"]:
                                    return i
                elif value["_op"] == "$eq":
                    for i in db[collection_name]:
                        if key in list(i.keys()):
                            if i[key] == value["_value"]:
                                return i
                elif value["_op"] == "$ne":
                    for i in db[collection_name]:
                        if key in list(i.keys()):
                            if i[key] != value["_value"]:
                                return i
                else:
                    return {'error': 'invalid operator'}
        return []

    def count(self, collection_name):
        db = self.db
        return len(db[collection_name])

    
    def get_document(self, collection_name, document_id):
        db = self.db
        for item in db[collection_name]:
            if item['_id'] == document_id:
                return item
        return None
    
    def match(self,collection_name, query):
        db = self.db
        matched_items = []
        for item in db[collection_name]:
            match_item = True
            for key, value in query.items():
                if key in item:
                    if item[key] != value:
                        match_item = False
                        break
                else:
                    match_item = False
                    break
            if match_item:
                matched_items.append(item)
        if matched_items != []:
            return {"status": "success", "result": matched_items}
        else:
            return {"status": "failed", "result": []}

    def update(self, collection_name, query, update_fields):
        db = self.db
        for key, value in query.items():
            if isinstance(value, str) or isinstance(value, int):
                for item in db[collection_name]:
                    item_value = item.get(key)
                    if item_value == value:
                        for update_key, update_value in update_fields.items():
                            item[update_key] = update_value
                            return {"status": "success"}

            if "_op" in value.keys():
                operator = value["_op"]
                comparison_value = value["_value"]
                for item in db[collection_name]:
                    item_value = item.get(key)
                    if isinstance(item_value, (int, float)) and isinstance(comparison_value, (int, float)):
                        if operator == "$eq" and item_value == comparison_value:
                            for update_key, update_value in update_fields.items():
                                item[update_key] = update_value
                        elif operator == "$ne" and item_value != comparison_value:
                            for update_key, update_value in update_fields.items():
                                item[update_key] = update_value
                        elif operator == "$gt" and item_value > comparison_value:
                            for update_key, update_value in update_fields.items():
                                item[update_key] = update_value
                        elif operator == "$gte" and item_value >= comparison_value:
                            for update_key, update_value in update_fields.items():
                                item[update_key] = update_value
                        elif operator == "$lt" and item_value < comparison_value:
                            for update_key, update_value in update_fields.items():
                                item[update_key] = update_value
                        elif operator == "$lte" and item_value <= comparison_value:
                            for update_key, update_value in update_fields.items():
                                item[update_key] = update_value
                    elif isinstance(item_value, str) and isinstance(comparison_value, str):
                        if operator == "$eq" and item_value == comparison_value:
                            for update_key, update_value in update_fields.items():
                                item[update_key] = update_value
                        elif operator == "$ne" and item_value != comparison_value:
                            for update_key, update_value in update_fields.items():
                                item[update_key] = update_value
                    else:
                        {"error": "invalid value type"}
        self._write_db(db)
        return {"status": "success"}
    
    def updateby_id(self, collection_name, document_id, update_fields):
        db = self.db
        for item in db[collection_name]:
            if item['_id'] == document_id:
                for update_key, update_value in update_fields.items():
                    item[update_key] = update_value
        self._write_db(db)
        return {"status": "success"}
    
    def delete(self, collection_name, query):
        db = self.db
        deleted_items = []
        for item in db[collection_name]:
            delete_item = True
            for key, value in query.items():
                if isinstance(value, str) or isinstance(value, int):
                    if item[key] != value:
                        delete_item = False
                        break
                if "_op" in value.keys():
                    operator = value["_op"]
                    comparison_value = value["_value"]
                    item_value = item.get(key)
                    if isinstance(item_value, (int, float)) and isinstance(comparison_value, (int, float)):
                        if operator == "$eq" and item_value != comparison_value:
                            delete_item = False
                            break
                        elif operator == "$ne" and item_value == comparison_value:
                            delete_item = False
                            break
                        elif operator == "$gt" and item_value <= comparison_value:
                            delete_item = False
                            break
                        elif operator == "$gte" and item_value < comparison_value:
                            delete_item = False
                            break
                        elif operator == "$lt" and item_value >= comparison_value:
                            delete_item = False
                            break
                        elif operator == "$lte" and item_value > comparison_value:
                            delete_item = False
                            break
                    elif isinstance(item_value, str) and isinstance(comparison_value, str):
                        if operator == "$eq" and item_value != comparison_value:
                            delete_item = False
                            break
                        elif operator == "$ne" and item_value == comparison_value:
                            delete_item = False
                            break
            if delete_item:
                deleted_items.append(item)
        for item in deleted_items:
            db[collection_name].remove(item)
        self._write_db(db)
        return {"status": "success"}
    
    def deleteby_id(self, collection_name, document_id):
        db = self.db
        for item in db[collection_name]:
            if item['_id'] == document_id:
                db[collection_name].remove(item)
        self._write_db(db)
        return {"status": "success"}
