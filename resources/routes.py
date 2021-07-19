from .movie import MoviesApi, MovieApi
from .auth import SignupApi, LoginApi
from .warehouse_item import WarehouseItemApi, WarehouseItemsApi
from .reset_password import ForgotPassword, ResetPassword

def initialize_routes(api):
    api.add_resource(MoviesApi, '/api/movies')
    api.add_resource(MovieApi, '/api/movies/<id>')

    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')

    api.add_resource(WarehouseItemsApi, '/api/items')
    api.add_resource(WarehouseItemApi, '/api/items/<id>')

    api.add_resource(ForgotPassword, '/api/auth/forgot')
    api.add_resource(ResetPassword, '/api/auth/reset')

    def get(self, id):
        movies = Movie.objects.get(id=id).to_json()
        return Response(movies, mimetype="application/json", status=200)

