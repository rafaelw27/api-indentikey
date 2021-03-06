from flask_restplus import Namespace, fields


class UsersDto:
    api = Namespace('users', description='user related operations')
    user = api.model('users', {
        'email': fields.String(required=True, description='user email address'),
        'public_id': fields.String(description='user Identifier')
    })

class RolesDto:
    api = Namespace('roles', description='roles related operations')
    role = api.model('roles', {
        'id': fields.Integer(required=False, description='role id'),
        'name': fields.String(required=True, description='role name'),
        'is_deleted': fields.Integer(required=False, description='delete status'),
        'created_at': fields.DateTime(required=False, description=' when was created'),
        'updated_at': fields.DateTime(required=False, description='when was updated'),
    })

class PersonsDto:
    api = Namespace('persons', description='persons related operations')
    role = api.model('persons', {
        'id': fields.Integer(required=False, description='person id'),
        'firstname': fields.String(required=True, description='person firstname'),
        'lastname': fields.String(required=True, description='person lastname'),
        'email': fields.String(required=True, description='person email'),
        'password': fields.String(required=True, description='person password'),
        'was_validated': fields.Integer(required=False, description='validation status'),
        'is_deleted': fields.Integer(required=False, description='delete status'),
        'created_at': fields.DateTime(required=False, description=' when was created'),
        'updated_at': fields.DateTime(required=False, description='when was updated'),
    })

class PersonsDataDto:
    api = Namespace('persons-data', description='persons data related operations')
    role = api.model('persons-data', {
        'id': fields.Integer(required=False, description='person id'),
        'persons_id': fields.Integer(required=False, description='persons id'),
        'qr_code': fields.String(required=True, description='person qr_code'),
        'fingerprint': fields.String(required=True, description='person fingerprint'),
        'face_model': fields.String(required=True, description='person face_model'),
        'voice_profile': fields.String(required=True, description='person voice_profile'),
        'is_deleted': fields.Integer(required=False, description='delete status'),
        'created_at': fields.DateTime(required=False, description=' when was created'),
        'updated_at': fields.DateTime(required=False, description='when was updated'),
    })

class ResourceAccessDto:
    api = Namespace('resource-access', description='resource-access data related operations')
    role = api.model('resource-access', {
        'id': fields.Integer(required=False, description='person id'),
        'resource_id': fields.Integer(required=False, description='resource-access id'),
        'persons_id': fields.Integer(required=False, description='resource-access id'),
        'roles_id': fields.Integer(required=False, description='persons role in resource id'),
        'is_active': fields.Integer(required=False, description='is active status'),
        'from_date': fields.DateTime(required=False, description='from date'),
        'to_date': fields.DateTime(required=False, description='to date'),
        'is_deleted': fields.Integer(required=False, description='delete status'),
        'created_at': fields.DateTime(required=False, description=' when was created'),
        'updated_at': fields.DateTime(required=False, description='when was updated'),
    })

class ResourcesDto:
    api = Namespace('resources', description='resources data related operations')
    role = api.model('resources', {
        'id': fields.Integer(required=False, description='resources id'),
        'persons_id': fields.Integer(required=False, description='owner id'),
        'min_threshold': fields.Integer(required=False, description='minimun threshold'),
        'code': fields.String(required=True, description='resources specific code'),
        'name': fields.String(required=True, description='resources name'),
        'main_resource_id': fields.Integer(required=False, description='resources main resource id'),
        'is_deleted': fields.Integer(required=False, description='delete status'),
        'created_at': fields.DateTime(required=False, description=' when was created'),
        'updated_at': fields.DateTime(required=False, description='when was updated'),
    })

class ResourceSettingsDto:
    api = Namespace('resource-settings', description='resource-settings data related operations')
    role = api.model('resource-settings', {
        'id': fields.Integer(required=False, description='resource-settings id'),
        'threshold': fields.Integer(required=False, description='resource-settings threshold'),
        'verification_methods_id': fields.Integer(required=False, description='verification methods id'),
        'resources_id': fields.Integer(required=False, description='resources id'),
        'is_deleted': fields.Integer(required=False, description='delete status'),
        'created_at': fields.DateTime(required=False, description=' when was created'),
        'updated_at': fields.DateTime(required=False, description='when was updated'),
    })

class VerificationMethodsDto:
    api = Namespace('verification-methods', description='verification-methods data related operations')
    role = api.model('verification-methods', {
        'id': fields.Integer(required=False, description='verification-methods id'),
        'name': fields.String(required=True, description='verification-methods name'),
        'is_deleted': fields.Integer(required=False, description='delete status'),
        'created_at': fields.DateTime(required=False, description=' when was created'),
        'updated_at': fields.DateTime(required=False, description='when was updated'),
    })


class VerifyDto:
    api = Namespace('verify', description='verification related operations')

class RegisterDto:
    api = Namespace('register', description='registration related operations')