import boto3

import aws_helpers.common


_CLIENT = boto3.client('iam')
_SU_CLIENT = boto3.Session(profile_name='su').client('iam')


@aws_helpers.common.dangerous
def create_policy_version(arn, path_to_document):
    with open(path_to_document) as f:
        document = f.read()
    return _SU_CLIENT.create_policy_version(
        PolicyArn=arn, PolicyDocument=document, SetAsDefault=True
    )


@aws_helpers.common.dangerous
def delete_policy_version(arn, version_id):
    return _SU_CLIENT.delete_policy_version(
        PolicyArn=arn, VersionId=version_id
    )


def update_policy(new_policy_document_path, policy_arn):
    old_version_id = _get_default_version_id(policy_arn)
    create_policy_response = create_policy_version(policy_arn, new_policy_document_path)
    delete_policy_response = delete_policy_version(policy_arn, old_version_id)
    return {
        'create_policy_response': create_policy_response,
        'delete_policy_response': delete_policy_response
    }


def list_users():
    response = _SU_CLIENT.list_users()
    return _get_unless_truncated(response, 'Users')


def list_groups():
    response = _SU_CLIENT.list_groups()
    return _get_unless_truncated(response, 'Groups')


def list_group_names():
    return {group_data['GroupName'] for group_data in list_groups()}


def list_roles():
    response = _CLIENT.list_roles()
    return _get_unless_truncated(response, 'Roles')


def list_role_names():
    return {role_data['RoleName'] for role_data in list_roles()}


def list_attached_group_policies(group_name):
    response = _SU_CLIENT.list_attached_group_policies(GroupName=group_name)
    return _get_unless_truncated(response, 'AttachedPolicies')


def get_all_policy_statements_for_group(group_name):
    policies = list_attached_group_policies(group_name)
    return [get_policy_statement(policy['PolicyArn']) for policy in policies]


def get_policy_document(policy_arn):
    default_version_id = _get_default_version_id(policy_arn)
    document_data = _CLIENT.get_policy_version(PolicyArn=policy_arn, VersionId=default_version_id)
    return document_data['PolicyVersion']['Document']


def _get_default_version_id(policy_arn):
    policy_data = _CLIENT.get_policy(PolicyArn=policy_arn)
    return policy_data['Policy']['DefaultVersionId']


def get_policy_statement(policy_arn):
    return get_policy_document(policy_arn)['Statement']


def _get_unless_truncated(response, field):
    if response['IsTruncated']:
        raise RuntimeError('response was truncated')

    return response[field]
