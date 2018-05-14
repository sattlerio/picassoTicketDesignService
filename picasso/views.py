from flask import jsonify, request, Blueprint, Response, current_app as app
from picasso.models import *
from picasso.guardianClient import GuardianClient
import uuid
import types

pluto = Blueprint('pluto', __name__)


@pluto.route('/ping', methods=['GET'])
def test():
    return "pong"


