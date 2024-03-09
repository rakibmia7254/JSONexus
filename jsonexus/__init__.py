import json
import os
import uuid

class JSONexus:
    def __init__(self, db_name):
        self.db_name = db_name
        if not os.path.exists(db_name):
            with open(db_name, 'w') as f:
                json.dump({}, f)

    def _read_db(self):
        with open(self.db_name, 'r') as f:
            return json.load(f)

    def _write_db(self, db):
        with open(self.db_name, 'w') as f:
            json.dump(db, f, indent=4)

    def insert(self, collection_name, data):
        db = self._read_db()
        if collection_name not in db:
            db[collection_name] = []
        data['_id'] = str(uuid.uuid4())  # Add a UUID for each record
        db[collection_name].append(data)
        self._write_db(db)
    
    def insert_many(self, collection_name, data):
        db = self._read_db()
        if collection_name not in db:
            db[collection_name] = []
        for item in data:
            item['_id'] = str(uuid.uuid4())
        db[collection_name].extend(data)
        self._write_db(db)

    def create_collection(self, collection_name):
        db = self._read_db()
        if collection_name not in db:
            db[collection_name] = []
            self._write_db(db)
            return {"status": "success", "name": collection_name}
        else:
            return {"status": "failed", "message": "Collection already exists"}

    def get_all(self):
        db = self._read_db()
        return db
    
    def get_collection(self, collection_name):
        db = self._read_db()
        return db[collection_name]
    
    def get_collections(self):
        db = self._read_db()
        return list(db.keys())
    
    def drop_collection(self, collection_name):
        db = self._read_db()
        if collection_name in db:
            del db[collection_name]
            self._write_db(db)
            return {"status": "success", "name": collection_name}
        else:
            return {"status": "failed", "message": "Collection not found"}

    def find(self, collection_name, query):
        db = self._read_db()
        for key, value in query.items():
            found_data = []
            if "_op" in value.keys():
                if value["_op"] == "$gt":
                    if isinstance(value["_value"], int) or isinstance(value["_value"], float):
                        for i in db[collection_name]:
                            if i[key] > value["_value"]:
                                found_data.append(i)
                    else:
                        pass
                
                elif value["_op"] == "$gte":
                    if isinstance(value["_value"], int) or isinstance(value["_value"], float):
                        for i in db[collection_name]:
                            if i[key] >= value["_value"]:
                                found_data.append(i)
                    else:
                        pass
                    
                elif value["_op"] == "$lt":
                    if isinstance(value["_value"], int) or isinstance(value["_value"], float):
                        for i in db[collection_name]:
                            if i[key] < value["_value"]:
                                found_data.append(i)
                    else:
                        pass
                    
                elif value["_op"] == "$lte":
                    if isinstance(value["_value"], int) or isinstance(value["_value"], float):
                        for i in db[collection_name]:
                            if i[key] <= value["_value"]:
                                found_data.append(i)
                    else:
                        pass

                elif value["_op"] == "$eq":
                    for i in db[collection_name]:
                        if i[key] == value["_value"]:
                            found_data.append(i)
                elif value["_op"] == "$ne":
                    for i in db[collection_name]:
                        if i[key] != value["_value"]:
                            found_data.append(i)
                else:
                    return {'error': 'invalid operator'}

        return {'result': found_data}
    
    def count(self, collection_name):
        db = self._read_db()
        return len(db[collection_name])
    
    def get_document(self, collection_name, document_id):
        db = self._read_db()
        for item in db[collection_name]:
            if item['_id'] == document_id:
                return item
        return None
    
    def match(self,collection_name, query):
        db = self._read_db()
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
            return {"status": "success", "matched_items": matched_items}
        else:
            return {"status": "failed", "matched_items": []}

    def update(self, collection_name, query, update_fields):
        db = self._read_db()
        for key, value in query.items():
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
        
    def delete(self, collection_name, query):
        db = self._read_db()
        deleted_items = []
        for item in db[collection_name]:
            delete_item = True
            for key, value in query.items():
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
                    else:
                        pass
            if delete_item:
                deleted_items.append(item)
        for item in deleted_items:
            db[collection_name].remove(item)
        self._write_db(db)
        return {"status": "success"}


