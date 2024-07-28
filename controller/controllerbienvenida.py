from flask import render_template, make_response
from flask_restful import Resource
from models.user  import User


class ControllerBienvenida(Resource):

    def get(self):
        items = User.query.all()
        return make_response(render_template("bienvenida.html", items=items))