from flask import Response, request
from database.models import Movie, User, Item
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from mongoengine.errors import DoesNotExist
from resources.errors import ItemNotFoundError
# You need to implement following REST endpoints 

# GET /api/items/ - fetch all items - DONE
# GET /api/items/<item_id> - fetch item by its ID - TODO
# POST /api/items/<item_id>/add - add quantity to an item - TODO
# POST /api/items/<item_id>/substract - substract quantity from an item - TODO

# data for POST request must be in request body e.g.
# for POST /api/items/<item_id>/substract
# body can look like this:

# {
#    "amount": 13
# }

# you pass in the body how many items you would like to subtract and you do it on the server side 
# item id doesn't have to be included in the body as you can find it in the path of the request
#               HERE |
#                    V
# /api/items/<item_id>/substract  

# POST /api/items/ - create new item - DONE
# DELETE /api/items/<item_id> - delete item - TODO
# UPDATE /api/items/<Item_id> - update an item e.g. product name - TODO

class WarehouseItemsApi(Resource):

    @jwt_required
    def get(self):
        items = Item.objects().to_json()
        return Response(items, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        body = request.get_json()
        item = Item(**body)
        item.save()
        id = item.id
        return {'id': str(id)}, 200
 

class WarehouseItemApi(Resource):

    @jwt_required
    def get(self, id):
        pass

    @jwt_required
    def increase_qunatity(self):
        pass

    @jwt_required
    def decrease_quantity(self):
        pass


    #example of update
    @jwt_required
    def put(self, id):
        user_id = get_jwt_identity()
        item = Item.objects.get(id=id, added_by=user_id)
        body = request.get_json()
        Item.objects.get(id=id).update(**body)
        return '', 200

    #example of delete
    #you have to add exception handling there
    # if item is not found return 404
    # this solution is too simple
    # it will work only if a given item exists in the database
    @jwt_required
    def delete(self, id):
        try:
            item = Item.objects.get(id=id)
            item.delete()
            return '', 200
        except DoesNotExist:
            raise ItemNotFoundError
        except Exception:
            raise InternalServerError
    #example of get for single object
    def get(self, id):
        items = Item.objects.get(id=id).to_json()
        return Response(items, mimetype="application/json", status=200)
