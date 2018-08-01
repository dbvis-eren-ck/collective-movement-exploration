import os
import os.path as op
import atexit

from flask import Flask, render_template, url_for, redirect, request
from flask_security import Security, SQLAlchemyUserDatastore
from flask_admin import helpers as admin_helpers

# from view.admin_view import MyAdminView
from view.center_view import MyCenterView
# from view.file_view import MyFileAdminView
# from view.dataset_view import MyDatasetView
# from view.network_view import MyNetworkView

from model.network_model import Network
from model.user_role_model import *

from helpers.restless import *

# Create Flask application
app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

path = op.join(op.dirname(__file__), 'files')


# Flask views
@app.route('/')
def index():
    return render_template('/index.html')


@app.route('/contact')
def contact():
    return render_template('/contact.html')


# Custom Rest API
@app.route('/api/dataset', methods=['GET'])
def get_dataset():
    return api_get_dataset()


@app.route('/api/dataset/<int:id>', methods=['GET'])
def get_dataset_id(id):
    return api_get_dataset(id)


@app.route('/api/dataset/user/<int:user_id>', methods=['GET'])
def get_dataset_user_id(user_id):
    return api_get_dataset_user(user_id)


@app.route('/api/dataset/<int:id>/<feature>', methods=['GET'])
def get_feature(id, feature):
    return api_get_feature(id, feature)


@app.route('/api/dataset/<int:id>/vc', methods=['GET'])
def get_vc_feature(id):
    return api_get_vc(id)


@app.route('/api/movement_only/<int:id>', methods=['GET'])
def get_movment_only(id):
    return api_get_movment_only(id)


@app.route('/api/percentile/<int:id>', methods=['GET'])
def get_percentile(id):
    return api_get_percentile(id)


@app.route('/api/metadata/<int:id>', methods=['GET'])
def get_metadata(id):
    return api_get_metadata(id)


@app.route('/api/dataset/networks/<int:id>', methods=['GET'])
def get_dataset_networks(id):
    return api_get_dataset_networks(id)


@app.route('/api/dataset/network/<int:dataset_id>/<int:network_id>', methods=['GET'])
def get_dataset_network_data(dataset_id, network_id):
    return api_get_network_data(dataset_id, network_id)


@app.route('/api/dataset/network/hierarchy/<int:dataset_id>/<int:network_id>', methods=['GET'])
def get_dataset_network_hierarchy_data(dataset_id, network_id):
    return api_get_network_hierarchy_data(dataset_id, network_id) \
 \
           @ app.route('/api/dataset/visual_parameter/<int:dataset_id>', methods=['POST'])


def get_dataset_suggested_parameters(dataset_id):
    # Get JSON object passed with Ajax request
    tracked_data = request.json
    return api_get_dataset_suggested_parameters(dataset_id, tracked_data)


# Create view
# admin = Admin(
#     app,
#     name='Collective Movement Exploration',
#     index_view=MyHomeView(name='Info'),
#     base_template='my_master.html',
#     template_mode='bootstrap3'
# )
#
# # Add model views
# admin.add_view(MyFileAdminView(path, '/files/', name='Upload'))
# admin.add_view(MyDatasetView(Dataset, db.session, name='Explore'))
# admin.add_view(MyNetworkView(Network, db.session))
# admin.add_view(MyAdminView(Role, db.session))
# admin.add_view(MyAdminView(User, db.session))


# define a context processor for merging flask-view's template context into the
# flask-security views.
# @security.context_processor
# def security_context_processor():
#     return dict(
#         admin_base_template=admin.base_template,
#         admin_view=admin.index_view,
#         h=admin_helpers,
#         get_url=url_for
#     )


# Class based views
app.add_url_rule('/center/', view_func=MyCenterView.as_view('center_view'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


# defining function to run on shutdown
def close_running_threads():
    db.session.remove()


# Register the function to be called on exit
atexit.register(close_running_threads)

if __name__ == '__main__':
    # Build a sample db on the fly, if one does not exist yet.
    app_dir = os.path.realpath(os.path.dirname(__file__))
    database_path = os.path.join(app_dir, app.config['DATABASE_FILE'])
    # Start app
    app.run(threaded=True, debug=True)
