from lib.property import Property

class PropertyRepository():
    
    def __init__(self,connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM properties")
        properties_list = []
        for row in rows:
            item = Property(
                row['id'],row['name'],row['description'],row['price'],row['user_id'])
            properties_list.append(item)
        return properties_list    

    def create(self,property):
        rows = self._connection.execute(
                "INSERT INTO properties (name,description,price,user_id) VALUES (%s, %s,%s,%s) RETURNING id",[
                    property.name,property.description,property.price,property.user_id])
        row = rows[0]
        property.id = row['id']
        return property
    
    def find(self,property_id):
        rows = self._connection.execute(
                "SELECT * FROM properties WHERE id = %s", [property_id])
        row = rows[0]
        return Property(
                row['id'],row['name'],row['description'],row['price'],row['user_id'])

    def price_formatter(self, property):
        property_price = property.price
        formatted_price =  f'{property_price:.2f}'
        return f"£{formatted_price} per night"
        

    def find_property_user_id(self,user_id):
            rows = self._connection.execute(
                "SELECT * FROM properties WHERE user_id = %s", [user_id]
            )
            properties_list = []
            if rows == []:
                return []
            for row in rows:
                item = Property(
                    row['id'],row['name'],row['description'],row['price'],row['user_id'])
                properties_list.append(item)
            return properties_list





